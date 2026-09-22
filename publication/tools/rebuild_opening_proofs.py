#!/usr/bin/env python3
"""Rebuild selected opening proofs without changing their prose.

The Chapter 01 source is the author-supplied corrected PDF. Its text layer is
read by visual line order because its content-stream order is not reading order.
For later rebuilds, omit --chapter-01-pdf to use the verified Markdown source.
Set EB_GARAMOND_12_TTF_DIR to a directory containing the Regular and Italic
EBGaramond12 TrueType files before running this script.
"""
from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

import fitz
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from pypdf import PdfReader, PdfWriter
from pypdf.generic import DecodedStreamObject, NameObject

ROOT = Path(__file__).resolve().parents[2]
PDF_DIR = ROOT / 'publication' / 'chapters'


def clean(text: str) -> str:
    return re.sub(r'\s+', ' ', text.replace('\u2003', ' ').replace('\u00ad', '').replace('\xa0', ' ')).strip()


def extract_author_pdf(path: Path):
    result = []
    doc = fitz.open(path)
    for number, page in enumerate(doc):
        lines = []
        for block in page.get_text('dict')['blocks']:
            for line in block.get('lines', []):
                spans = line['spans']
                raw = ''.join(s['text'] for s in spans)
                value = clean(raw)
                if not value:
                    continue
                italic = bool(spans) and all('Italic' in s['font'] for s in spans)
                lines.append((line['bbox'][1], line['bbox'][0], value, italic, raw.startswith('\u2003')))
        lines.sort(key=lambda x: (round(x[0], 1), x[1]))
        # The supplied proof has section restarts, so its mirrored inset does
        # not follow the PDF page index throughout. Derive it from each page.
        left = min(x for _, x, value, _, _ in lines if x < 100 and value not in {'⸻', '* * *'})
        if number == 0:
            assert lines[0][2] == 'MAGIC TRICK'
            result.append(('title', lines.pop(0)[2], False))
        for y, x, value, italic, em_indent in lines:
            if value in {'⸻', '* * *'}:
                result.append(('scene', '* * *', False))
                continue
            # First visible line on a page is a new paragraph in this approved
            # proof. Other paragraphs are marked by a 0.22-inch first indent.
            starts = x >= left + 12 or em_indent
            if not result or result[-1][0] != 'body' or starts or y < 60:
                result.append(('body', value, italic))
            else:
                kind, previous, was_italic = result[-1]
                # A line can contain an italic span inside ordinary narration;
                # preserve its words in the visible transcription.
                result[-1] = (kind, previous + ' ' + value, was_italic and italic)
    # Preserve the small number of italic cues in the supplied proof. Markdown
    # markers are source notation and do not form part of its spoken prose.
    italic_phrases = (
        'This is not fucking good.', 'Catch ya on the flipside.',
        'Peace out, ballbag.', "I'll be alright",
        "You've gone and fucked this one up.", 'Consecutive.',
        'concurrent',
    )
    for index, (kind, value, italic) in enumerate(result):
        if kind != 'body': continue
        for phrase in italic_phrases:
            if phrase in value:
                value = value.replace(phrase, '*' + phrase + '*')
        result[index] = (kind, value, italic)
    return result


def parse_markdown(path: Path):
    source = path.read_text(encoding='utf-8')
    items = []
    for chunk in re.split(r'\n\s*\n', source):
        s = chunk.strip()
        if not s:
            continue
        if s.startswith('# '):
            items.append(('title', clean(s[2:]), False))
        elif s == '---':
            if items and items[-1][0] == 'title':
                continue
            items.append(('scene', '* * *', False))
        else:
            italic = s.startswith('*') and s.endswith('*') and s.count('*') == 2
            if italic: s = s[1:-1]
            items.append(('body', clean(s), italic))
    return items


def markdown_from_pdf(items):
    parts = []
    for kind, value, italic in items:
        if kind == 'title': parts.append('# ' + value)
        elif kind == 'scene': parts.append('---')
        elif italic and not (value.startswith('*') and value.endswith('*')):
            parts.append('*' + value + '*')
        else: parts.append(value)
    return '\n\n'.join(parts) + '\n'


def layout(items, destination: Path):
    # EB Garamond 12 optical cut; the installed full fonts are provided at run
    # time. No synthetic bold, and no fallback to EB Garamond 08 is permitted.
    font_dir = Path(__import__('os').environ['EB_GARAMOND_12_TTF_DIR'])
    pdfmetrics.registerFont(TTFont('EBG12', str(font_dir / 'EBGaramond12-Regular.ttf')))
    pdfmetrics.registerFont(TTFont('EBG12Italic', str(font_dir / 'EBGaramond12-Italic.ttf')))
    pdfmetrics.registerFontFamily('EBG12', normal='EBG12', italic='EBG12Italic',
                                  bold='EBG12', boldItalic='EBG12Italic')
    normal = ParagraphStyle('normal', fontName='EBG12', fontSize=11.5,
                            leading=13.35, alignment=TA_JUSTIFY, splitLongWords=0,
                            allowWidows=0, allowOrphans=0, spaceAfter=0)
    title = ParagraphStyle('title', parent=normal, fontSize=15.5, leading=19,
                           alignment=TA_CENTER)
    marker = ParagraphStyle('scene', parent=normal, fontSize=10.5,
                            alignment=TA_CENTER, leading=14)
    destination.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(destination), pagesize=(432, 648), pageCompression=1)
    c.setFont('EBG12', 11.5)
    page = 0
    y = 0
    for index, (kind, value, italic) in enumerate(items):
        if page == 0:
            page = 1
            y = 648 - 54
        left = 66 if page % 2 else 52
        right = 52 if page % 2 else 66
        width = 432 - left - right
        if kind == 'title':
            p = Paragraph(html.escape(value), title)
            _, height = p.wrap(width, 648)
            p.drawOn(c, left, y - height)
            y -= height + 18
            continue
        if kind == 'scene':
            p = Paragraph('* * *', marker)
            before, after = 13, 13
            if y - before - 14 - after - 28 < 46:
                c.showPage(); page += 1; y = 648 - 54
            y -= before
            p.wrap(width, 200)
            p.drawOn(c, left, y - 14)
            y -= 14 + after
            continue
        # Titles and scene markers suppress the following first-line indent.
        no_indent = index and items[index - 1][0] in ('title', 'scene')
        style = ParagraphStyle('p', parent=normal, firstLineIndent=0 if no_indent else 15.8,
                               fontName='EBG12Italic' if italic else 'EBG12')
        safe = html.escape(value)
        safe = re.sub(r'\*([^*]+)\*', r'<i>\1</i>', safe)
        p = Paragraph(safe, style)
        _, height = p.wrap(width, 10000)
        # A multi-line paragraph ending with one or two words is reflowed by
        # narrowing only this paragraph, leaving its words and type size intact.
        def last_word_count(para):
            last = para.blPara.lines[-1]
            if hasattr(last, 'words'):
                return len(''.join(fragment.text for fragment in last.words).split())
            return len(last[1])

        if len(getattr(p.blPara, 'lines', [])) > 1 and last_word_count(p) < 3:
            for narrower in range(0, 30, 2):
                candidate = Paragraph(safe, style)
                candidate.wrap(width - narrower, 10000)
                if last_word_count(candidate) >= 3:
                    p = candidate; width_for_p = width - narrower
                    _, height = p.wrap(width_for_p, 10000)
                    break
            else:
                # Controlled paragraph flow: move the final three words as a
                # unit if modest reflow cannot resolve the runt.
                match = re.match(r'(?s)^(.*?)(\S+\s+\S+\s+\S+)$', safe)
                if match:
                    forced = match.group(1).rstrip() + '<br/>' + match.group(2)
                    p = Paragraph(forced, style)
                    _, height = p.wrap(width, 10000)
                width_for_p = width
        else: width_for_p = width
        if y - height < 47:
            c.showPage(); page += 1; y = 648 - 54
            left = 66 if page % 2 else 52
        # Paragraphs are kept together for this opening sequence to prevent
        # orphan lines. The longest approved paragraph fits a 6 x 9 page.
        p.drawOn(c, left, y - height)
        y -= height
    c.save()
    # ReportLab inserts an unused Helvetica text-state command on each page.
    # Remove it and the resource so the print proof contains EB Garamond only.
    reader, writer = PdfReader(str(destination)), PdfWriter()
    for original_page in reader.pages:
        writer.add_page(original_page)
        page_obj = writer.pages[-1]
        stream = page_obj.get_contents().get_data()
        stream, count = re.subn(rb'BT /F1 12 Tf 14\.4 TL ET\s*', b'', stream)
        if count != 1:
            raise RuntimeError('Expected unused Helvetica setup was not found')
        new_stream = DecodedStreamObject()
        new_stream.set_data(stream)
        page_obj[NameObject('/Contents')] = writer._add_object(new_stream)
        fonts = page_obj['/Resources']['/Font']
        fonts.pop(NameObject('/F1'), None)
    with destination.open('wb') as handle:
        writer.write(handle)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--chapter-01-pdf', type=Path,
                    help='author-supplied corrected proof used for faithful source extraction')
    ap.add_argument('--write-source', action='store_true')
    args = ap.parse_args()
    one = (extract_author_pdf(args.chapter_01_pdf) if args.chapter_01_pdf
           else parse_markdown(ROOT / 'chapters' / '01_MagicTrick.md'))
    if args.write_source:
        if not args.chapter_01_pdf:
            ap.error('--write-source requires --chapter-01-pdf')
        (ROOT / 'chapters' / '01_MagicTrick.md').write_text(markdown_from_pdf(one), encoding='utf-8')
    layout(one, PDF_DIR / '01_MAGIC_TRICK.pdf')
    four = parse_markdown(ROOT / 'chapters' / '04_StartingMonday.md')
    layout(four, PDF_DIR / '04_STARTING_MONDAY.pdf')


if __name__ == '__main__': main()

#!/usr/bin/env python3
from __future__ import annotations
import csv, re, shutil, subprocess, tempfile
from pathlib import Path
from docx import Document
from PIL import Image
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'publication' / 'chapters'
QA = ROOT / 'publication' / 'qa'
CSV = ROOT / 'publication' / 'publication-formatting-manifest.csv'
MD = ROOT / 'publication' / 'publication-formatting-manifest.md'
APPROVED = ROOT / 'publication' / 'qa' / 'VISUAL_QA_APPROVED.txt'


def run(cmd):
    return subprocess.run(cmd, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)


def norm(s: str) -> str:
    s = s.replace('\u00ad', '').replace('•', ' ')
    s = re.sub(r'(?<!\*)\*\s*\*\s*\*(?!\*)', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


def docx_visible(path: Path) -> str:
    d = Document(path)
    return '\n'.join(p.text for p in d.paragraphs if p.text.strip() != '* * *')


def pdf_visible(path: Path) -> str:
    with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as f:
        tmp = Path(f.name)
    try:
        run(['pdftotext', str(path), str(tmp)])
        return tmp.read_text('utf-8', errors='replace')
    finally:
        tmp.unlink(missing_ok=True)


def normalize_trim(pdf: Path):
    reader = PdfReader(str(pdf))
    writer = PdfWriter()
    box = RectangleObject([0, 0, 432, 648])
    for page in reader.pages:
        page.mediabox = box
        page.cropbox = box
        writer.add_page(page)
    tmp = pdf.with_suffix('.normalized.pdf')
    with tmp.open('wb') as f:
        writer.write(f)
    tmp.replace(pdf)


def raster_check(pdf: Path, key: str):
    qd = QA / key
    if qd.exists():
        shutil.rmtree(qd)
    qd.mkdir(parents=True)
    run(['pdftoppm', '-png', '-r', '144', str(pdf), str(qd / 'page')])
    pages = sorted(qd.glob('page-*.png'))
    issues = []
    for i, p in enumerate(pages, 1):
        im = Image.open(p).convert('L')
        if im.size != (864, 1296):
            issues.append(f'p{i}:unexpected_size={im.size}')
        bbox = im.point(lambda x: 255 if x < 245 else 0).getbbox()
        if bbox is None:
            issues.append(f'p{i}:blank_page')
        else:
            x0, y0, x1, y1 = bbox
            if x0 < 12 or y0 < 12 or x1 > im.width - 12 or y1 > im.height - 12:
                issues.append(f'p{i}:content_near_trim_edge bbox={bbox}')
    return pages, issues


def md_escape(s):
    return str(s).replace('|', ' / ')


def main():
    rows = list(csv.DictReader(CSV.open(encoding='utf-8')))
    total_pages = 0
    for r in rows:
        if not r.get('pdf_output'):
            continue
        pdf = ROOT / r['pdf_output']
        docx = ROOT / r['docx_output']
        normalize_trim(pdf)
        pages, issues = raster_check(pdf, pdf.stem)
        total_pages += len(pages)
        r['page_count'] = str(len(pages))
        r['pdf_text_compare'] = 'PASS' if norm(docx_visible(docx)) == norm(pdf_visible(pdf)) else 'FAIL'
        fonts = run(['pdffonts', str(pdf)]).stdout
        font_ok = bool(re.search(r'EB.?Garamond', fonts, re.I))
        r['render_preflight'] = ('PASS' if not issues else 'REVIEW') + ('; font=PASS' if font_ok else '; font=REVIEW')
        r['concern'] = '; '.join(issues) + (('; ' if issues else '') + 'source contains additional H1 GENERAL POPULATION; structural status remains for author review' if r['order'] == '03' else '')
        r['visual_qa'] = 'PASS_100_PERCENT' if APPROVED.exists() else 'PENDING_HUMAN_100_PERCENT'
        r['sync_status'] = 'branch-generated-verified' if APPROVED.exists() else 'branch-generated'

    fields = rows[0].keys()
    with CSV.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(rows)

    base = run(['git', 'merge-base', 'HEAD', 'origin/main']).stdout.strip()
    generated = sum(1 for r in rows if r.get('pdf_output'))
    lines = [
        '# Publication Formatting Manifest', '',
        f'- Governing manuscript base commit: `{base}`',
        f'- Generated chapters: {generated}',
        f'- Generated pages: {total_pages}',
        '- Trim: exact 6 × 9 inches (432 × 648 pt PDF MediaBox/CropBox)',
        '- Individual chapter folios: none',
        f'- Human 100% visual QA: **{"PASS" if APPROVED.exists() else "pending"}**',
        '- Source conflict: consolidated THE ONION WILL NOT WAIT FOR YOU / Stockpot text required by the 2026-09-15 publication instruction is not present as an exact authoritative source in the repository or retrievable account-library file, so the two older standalone files are intentionally not emitted.', '',
        '| Order | Title | Source | Pages | DOCX text | PDF text | Raster preflight | Visual QA | Concern |',
        '|---:|---|---|---:|---|---|---|---|---|'
    ]
    for r in rows:
        lines.append(f'| {r["order"]} | {md_escape(r["title"])} | `{r["source_path"]}` | {r["page_count"]} | {r["docx_text_compare"]} | {r["pdf_text_compare"]} | {r["render_preflight"]} | {r["visual_qa"]} | {md_escape(r["concern"])} |')
    MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')

if __name__ == '__main__':
    main()

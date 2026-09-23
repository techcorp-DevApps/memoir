#!/usr/bin/env python3
"""Typeset the approved Chapter 02 source without printing its metadata.

Fixed margins and type size; paragraph-wide line balancing; no hyphenation,
synthetic fonts, or whole-paragraph page forcing.
"""
from pathlib import Path
from functools import lru_cache
import argparse, html, json, os, re
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from pypdf import PdfReader, PdfWriter
from pypdf.generic import DecodedStreamObject, NameObject

ROOT = Path(__file__).resolve().parents[2]
SIZE, LEADING, WIDTH, INDENT = 11.5, 13.35, 314., 15.8

def read_source(path):
    source = path.read_text(encoding='utf-8')
    if source.startswith('---\n'):
        source = source.split('\n---\n', 1)[1].lstrip()
    lines = source.splitlines()
    assert lines[0] == '# FOUR FLIGHTS'
    body = '\n'.join(lines[1:]).strip()
    paragraphs = [re.sub(r'\s+', ' ', p).strip() for p in re.split(r'\n\s*\n', body)]
    # Controlled paragraph flow at existing sentence boundaries. Words and
    # punctuation remain exact; these avoid forced, oversized word spacing.
    starts = ('Drunk driving charges. ',
              'I’d been in plenty of bare-knuckle fights by then. ',
              'Favours were currency there. ')
    result=[]
    for p in paragraphs:
        match=next((s for s in starts if p.startswith(s)),None)
        result.extend([match.rstrip(),p[len(match):]] if match else [p])
    return result

def balance(text, indent):
    words = text.split()
    widths = [pdfmetrics.stringWidth(w, 'EBG12', SIZE) for w in words]
    space = pdfmetrics.stringWidth(' ', 'EBG12', SIZE)
    n = len(words)
    @lru_cache(None)
    def solve(i):
        available = WIDTH - (indent if i == 0 else 0)
        best = None
        total = 0.
        for j in range(i+1, n+1):
            total += widths[j-1] + (space if j > i+1 else 0)
            chars=sum(len(w) for w in words[i:j])+(j-i-1)
            tracking=min(0.,(available-total)/max(chars-1,1))
            if tracking < -.06:
                break
            final = j == n
            if final and i and j-i < 3:
                continue
            gaps = j-i-1
            if final:
                cost = 2 * ((available-total)/available)**2
                rest = (0., [])
            else:
                if not gaps:
                    continue
                ratio = ((available-total)/gaps + space) / space
                cost = max(0,ratio-1)**3 + 30*max(0, ratio-2.5)**3 + .4 + abs(tracking)*40
                rest = solve(j)
                if rest is None:
                    continue
            score = cost + rest[0]
            if best is None or score < best[0]:
                best = (score, [(i,j,total,available,tracking)] + rest[1])
        return best
    result = solve(0)
    if result is None:
        raise ValueError('Cannot balance paragraph: '+text)
    out=[]
    for k,(i,j,total,available,tracking) in enumerate(result[1]):
        final = j == n
        extra = max(0.,(available-total)/(j-i-1)) if not final else 0.
        out.append(dict(text=' '.join(words[i:j]),indent=indent if k==0 else 0.,
                        extra=extra,tracking=tracking,word_space=space+extra,final=final,
                        pos=k,total=len(result[1]),height=LEADING))
    return out

def build(source, output, report):
    fonts = Path(os.environ['EB_GARAMOND_12_TTF_DIR'])
    pdfmetrics.registerFont(TTFont('EBG12', str(fonts/'EBGaramond12-Regular.ttf')))
    paras = read_source(source)
    records = [dict(kind='title',height=37)]
    first=True
    for idx,p in enumerate(paras):
        if p in ('* * *', '---'):
            records.append(dict(kind='scene',height=40));first=True
            continue
        for line in balance(p, 0 if first else INDENT):
            # Spoken paragraphs retain natural word spacing. This prevents
            # short exchanges being stretched to fill a justified measure.
            if p.startswith(('“','"')):
                line['extra']=0.
                line['word_space']=pdfmetrics.stringWidth(' ','EBG12',SIZE)
            line.update(kind='body',paragraph=idx)
            records.append(line)
        first=False
    # Optimise the whole chapter's page breaks, so a run of short dialogue
    # paragraphs cannot push a near-empty page into the middle of the proof.
    @lru_cache(None)
    def paginate(start):
        if start==len(records):return (0.,[])
        used=0.;best=None
        for cut in range(start+1,len(records)+1):
            used+=records[cut-1]['height']
            if used>548.01:break
            if cut<len(records):
                a,b=records[cut-1],records[cut]
                if a['kind']!='body' or b['kind']!='body':continue
                if a['paragraph']==b['paragraph']:
                    visible=sum(1 for q in records[start:cut] if q.get('paragraph')==a['paragraph'])
                    if visible<2 or b['total']-b['pos']<2:continue
                rest=paginate(cut)
                if rest is None:continue
                # Complete single-line utterances are not split-paragraph
                # widows. Prefer another break when comparable, but do not
                # leave half a page blank to move an entire conversation.
                penalty=2000*((a['total']==1)+(b['total']==1))
                cost=10000+(548-used)**2+penalty+rest[0]
            else:
                rest=(0.,[]);cost=10000
            if best is None or cost<best[0]:best=(cost,[cut]+rest[1])
        return best
    result=paginate(0)
    if result is None:raise ValueError('No widow/orphan-safe pagination')
    pages=[];start=0
    for end in result[1]:pages.append(records[start:end]);start=end
    c=canvas.Canvas(str(output),pagesize=(432,648),pageCompression=1)
    c.setTitle('FOUR FLIGHTS');c.setAuthor('C J Vale')
    for number,page in enumerate(pages,1):
        left=66 if number%2 else 52
        y=594.
        for r in page:
            if r['kind']=='title':
                c.setFont('EBG12',15.5);c.drawCentredString(left+WIDTH/2,y-15.5,'FOUR FLIGHTS')
            elif r['kind']=='scene':
                c.setFont('EBG12',10.5);c.drawCentredString(left+WIDTH/2,y-24,'* * *')
            else:
                t=c.beginText(left+r['indent'],y-SIZE)
                t.setFont('EBG12',SIZE);t.setWordSpace(r['extra']);t.setCharSpace(r['tracking']);t.textOut(r['text']);c.drawText(t)
            r['page']=number;r['top']=y
            y-=r['height']
        c.showPage()
    c.save()
    reader=PdfReader(output);writer=PdfWriter()
    for page in reader.pages:
        writer.add_page(page);p=writer.pages[-1]
        stream=re.sub(rb'BT /F1 12 Tf 14\.4 TL ET\s*',b'',p.get_contents().get_data())
        obj=DecodedStreamObject();obj.set_data(stream)
        p[NameObject('/Contents')]=writer._add_object(obj)
        p['/Resources']['/Font'].pop(NameObject('/F1'),None)
    writer.add_metadata({'/Title':'FOUR FLIGHTS','/Author':'C J Vale'})
    with output.open('wb') as f:writer.write(f)
    report.write_text(json.dumps(dict(pages=len(pages),records=records),ensure_ascii=False,indent=2))
    print('Pages:',len(pages))
    print('Max word space:',max(r.get('word_space',0) for r in records))

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--report',type=Path,required=True)
    args=ap.parse_args()
    build(ROOT/'chapters/02_FourFlights.md',args.output,args.report)

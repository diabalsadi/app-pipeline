# link_sheets.py <PREFIX> <spreadsheet id> <grid.json> <nr.json> ranges|links
# ranges: fixes named ranges and writes links_<spreadsheet id>.json (ID -> URL of its row).
# links:  after "ranges" is clean for EVERY workbook of the product, links each ID in each cell,
#         to its row in this workbook or in any other workbook of the product.
import glob, json, re, sys
PREFIX, SID, GRID, NR, MODE = sys.argv[1:6]
d = json.load(open(GRID))
nr = json.load(open(NR)).get('namedRanges', [])
TOK = re.compile(re.escape(PREFIX) + r'-[A-Z0-9]+(?:-[A-Z0-9]+)+')
LINK = {'rgbColor': {'red': 0.06666667, 'green': 0.33333334, 'blue': 0.8}}
URL = 'https://docs.google.com/spreadsheets/d/{}/edit#rangeid={}'
rid = {x['name'].replace('_', '-'): x['namedRangeId'] for x in nr if x['name'].startswith(PREFIX + '_')}
grid, width = {}, {}
for s in d['sheets']:
    sh = s['properties']['sheetId']; rows = []
    for blk in s['data']:
        for row in blk.get('rowData', []):
            rows.append([c.get('userEnteredValue', {}).get('stringValue', '') for c in row.get('values', [])])
    grid[sh] = (s['properties']['title'], rows)
    width[sh] = max([len(r) for r in rows] + [1])
if MODE == 'ranges':
    fix, own = [], set()
    for sh, (t, rows) in grid.items():
        for i, r in enumerate(rows):
            if i == 0 or not r or not TOK.fullmatch(r[0].strip()): continue
            i_d = r[0].strip(); own.add(i_d)
            rng = {'sheetId': sh, 'startRowIndex': i, 'endRowIndex': i + 1, 'startColumnIndex': 0, 'endColumnIndex': width[sh]}
            if i_d not in rid:
                fix.append({'addNamedRange': {'namedRange': {'namedRangeId': i_d.replace('-', ''), 'name': i_d.replace('-', '_'), 'range': rng}}})
                print('NO RANGE', t, 'row', i + 1, i_d)
            else:
                x = next(n for n in nr if n['namedRangeId'] == rid[i_d])
                if x['range'].get('sheetId', 0) != sh or x['range'].get('startRowIndex', 0) != i:
                    fix.append({'updateNamedRange': {'namedRange': {'namedRangeId': rid[i_d], 'name': x['name'], 'range': rng}, 'fields': 'range'}})
                    print('WRONG ROW', i_d, '->', t, 'row', i + 1)
    json.dump(fix, open(f'range_reqs_{SID}.json', 'w'))
    if fix: print(len(fix), f'range fixes -> range_reqs_{SID}.json. Apply, re-read named ranges, run ranges again.'); sys.exit(0)
    json.dump({i: URL.format(SID, rid[i]) for i in own if i in rid}, open(f'links_{SID}.json', 'w'))
    print('ranges clean;', len(own), f'IDs -> links_{SID}.json'); sys.exit(0)
allurl = {}
for f in glob.glob('links_*.json'):
    for i, u in json.load(open(f)).items():
        if i in allurl and allurl[i] != u: print('DUPLICATE ID', i)
        allurl[i] = u
def target(i):
    u = allurl.get(i)
    if not u: return None
    return '#rangeid=' + u.split('#rangeid=')[1] if u.startswith(URL.format(SID, '')) else u
known = {target(i) for i in allurl}
reqs, broken = [], []
for s in d['sheets']:
    sh = s['properties']['sheetId']
    for blk in s['data']:
        base = blk.get('startRow', 0)
        for ri, row in enumerate(blk.get('rowData', [])):
            for ci, c in enumerate(row.get('values', [])):
                v = c.get('userEnteredValue', {}).get('stringValue')
                if not v or (ci == 0 and TOK.fullmatch(v.strip())): continue
                n = len(v); per = [{} for _ in range(n)]
                runs = c.get('textFormatRuns', [])
                for k, r in enumerate(runs):
                    st = r.get('startIndex', 0); en = runs[k + 1].get('startIndex', n) if k + 1 < len(runs) else n
                    for p in range(st, min(en, n)): per[p] = dict(r.get('format', {}))
                dirty = bool(c.get('hyperlink'))
                for p in range(n):
                    u = per[p].get('link', {}).get('uri', '')
                    if u and u not in known and (not u.startswith('http') or '#rangeid=' in u): per[p] = {}; dirty = True
                for m in TOK.finditer(v):
                    uri = target(m.group(0))
                    if not uri:
                        broken.append((s['properties']['title'], base + ri + 1, ci + 1, m.group(0))); continue
                    if all(per[p].get('link', {}).get('uri') == uri for p in range(m.start(), m.end())): continue
                    for p in range(m.start(), m.end()):
                        per[p] = {'foregroundColorStyle': LINK, 'link': {'uri': uri}, 'underline': True}
                    dirty = True
                if not dirty: continue
                out, prev = [], None
                for p in range(n):
                    k = json.dumps(per[p], sort_keys=True)
                    if k != prev: out.append({'startIndex': p, 'format': per[p]}); prev = k
                if out: out[0].pop('startIndex')
                reqs.append({'updateCells': {'range': {'sheetId': sh, 'startRowIndex': base + ri, 'endRowIndex': base + ri + 1, 'startColumnIndex': ci, 'endColumnIndex': ci + 1}, 'rows': [{'values': [{'userEnteredValue': {'stringValue': v}, 'textFormatRuns': out}]}], 'fields': 'userEnteredValue,textFormatRuns'}})
json.dump(reqs, open(f'link_reqs_{SID}.json', 'w'))
for b in broken: print('BROKEN REFERENCE', *b)
print(len(reqs), f'cells to link -> link_reqs_{SID}.json')

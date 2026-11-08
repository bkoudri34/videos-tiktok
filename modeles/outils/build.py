"""Builder: python3 build.py <config.py> split|html|stills|mix|render
Voice-over: put the Speko WAV of the whole script (lines separated by blank lines) in $WORK/<NAME>/full.wav first.
config defines NAME, TITLE, CSS, BODY, LINES=[(voice, [(display_html, weight_or_None), ...]), ...]
"""
import sys, os, re, json, subprocess, importlib.util, pathlib, html
SP = pathlib.Path(__file__).parent
MOD = SP.parent  # modeles/
cfgp = pathlib.Path(sys.argv[1]); stage = sys.argv[2]
spec = importlib.util.spec_from_file_location('cfg', cfgp); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
W = pathlib.Path(os.environ.get('WORK', '/tmp/videos-work')) / C.NAME; W.mkdir(parents=True, exist_ok=True)
N = len(C.LINES)
GAP = getattr(C, 'GAP', 0.32)
VOFF = 0.05


def sh(cmd, **kw):
    return subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True, **kw)


def dur(f):
    return float(sh(f'ffprobe -v error -show_entries format=duration -of csv=p=0 "{f}"').stdout)


def silences(f, db=-38, d=0.12):
    out = subprocess.run(f'ffmpeg -i "{f}" -af silencedetect=n={db}dB:d={d} -f null -', shell=True, capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', out)]
    en = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', out)]
    return list(zip(st, en + [dur(f)] * (len(st) - len(en))))


def split():
    full = W / 'full.wav'; T = dur(full)
    sil = silences(full)
    lead = sil[0][1] if sil and sil[0][0] < 0.02 else 0.0
    tail = sil[-1][0] if sil and sil[-1][1] >= T - 0.02 else T
    inner = [s for s in sil if s[0] > lead + 0.05 and s[1] < tail - 0.05]
    print('silences', [(round(a, 2), round(b, 2)) for a, b in inner], 'lead', lead, 'tail', tail)
    if hasattr(C, 'SPLITS'):
        bounds = [x for ab in C.SPLITS for x in ab]
    else:
        cuts = sorted(sorted(inner, key=lambda s: s[1] - s[0], reverse=True)[:N - 1])
        bounds = [lead] + [x for c in cuts for x in c] + [tail]
    segs = []
    lens = [len(v) for v, _ in C.LINES]
    for i in range(N):
        a, b = bounds[2 * i], bounds[2 * i + 1]
        a = max(0, a - 0.03); b = min(T, b + 0.06)
        o = W / f'seg{i}.wav'
        sh(f'ffmpeg -y -v error -i "{full}" -ss {a:.3f} -to {b:.3f} -af "afade=t=in:d=0.01,areverse,afade=t=in:d=0.04,areverse" -ar 48000 -ac 1 "{o}"')
        segs.append(round(dur(o), 3))
    rate = [s / l for s, l in zip(segs, lens)]; m = sum(rate) / len(rate)
    print('segments', segs, 'ratio', [round(r / m, 2) for r in rate])
    bad = [i for i, r in enumerate(rate) if r / m < 0.6 or r / m > 1.6]
    chunks = []
    for i in range(N):
        f = W / f'seg{i}.wav'; T = segs[i]
        sl = [(a, b) for a, b in silences(f, -38, 0.08) if a > 0.02 and b < T - 0.02]
        edges = [0.03] + [x for ab in sl for x in ab] + [T - 0.06]
        chunks.append([(round(edges[2 * k], 3), round(edges[2 * k + 1], 3)) for k in range(len(edges) // 2)])
    print('chunks', chunks)
    json.dump({'segs': segs, 'bad': bad, 'chunks': chunks}, open(W / 'segs.json', 'w'))
    if bad: print('SUSPICIOUS', bad)


def timeline():
    J = json.load(open(W / 'segs.json')); segs = J['segs']; CH = J['chunks']
    S = [0.0]
    for i in range(N - 1):
        S.append(round(S[-1] + VOFF + max(segs[i], getattr(C, 'MINLEN', 1.3)) + GAP, 3))
    END = round(S[-1] + VOFF + segs[-1] + getattr(C, 'TAIL', 0.95), 3)
    G = []
    for i, (v, groups) in enumerate(C.LINES):
        # each segment has ~0.03 s lead and ~0.06 s tail around speech
        ch = CH[i]; spd = sum(b - a for a, b in ch)
        def at(x):  # speech-time x -> segment time, skipping pauses
            for a, b in ch:
                if x <= b - a + 1e-6: return a + x
                x -= b - a
            return ch[-1][1]
        ws = [len(re.sub('<[^>]+>', '', w if w2 is None else w2)) + 3 for w, w2 in groups]
        tot = sum(ws); acc = 0; row = []
        for (w, _), k in zip(groups, ws):
            row.append([round(S[i] + VOFF + at(spd * acc / tot) - 0.04, 3), None, w]); acc += k
        if hasattr(C, 'GSTART'):
            for j, gs in enumerate(C.GSTART[i]):
                row[j][0] = round(S[i] + VOFF + 0.03 + (gs - C.SPLITS[i][0]) - 0.03, 3)
        for j in range(len(row)):
            row[j][1] = row[j + 1][0] if j + 1 < len(row) else round(S[i] + VOFF + segs[i] + 0.2, 3)
        G.append(row)
    return S, G, END


def mkhtml():
    S, G, END = timeline()
    eng = open(SP / 'engine.js').read()
    base = open(SP / getattr(C, 'BASE', 'base.css')).read()
    pre = getattr(C, 'JS', '')
    doc = f'''<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<title>{C.TITLE}</title>
<style>
{C.ROOT}
{base}
{C.CSS}
</style></head><body>
<div id="stage">
 <div id="cam">
  <div id="bgtex" class="abs"></div>
{C.BODY}
  <div id="sub" class="abs"></div>
 </div>
 <div id="flash"></div><div id="grain"></div><div id="vig"></div>
</div>
<script>
// Timeline computed from the real voice-over (Speko, speed 1.08): scene starts S, subtitle groups G[scene] = [start, end, text]
const S={json.dumps(S)}, END={END};
const G={json.dumps(G, ensure_ascii=False)};
{pre}
{eng}</script></body></html>
'''
    (MOD / f'{C.NAME}.html').write_text(doc)
    json.dump({'S': S, 'END': END, 'G': G}, open(W / 'tl.json', 'w'), ensure_ascii=False)
    # sfx events
    ev = []
    for m in re.finditer(r'data-g="(\d+)\.(\d+)"[^>]*?(?:data-fx="(\w+)")?', C.BODY):
        i, j, fx = int(m.group(1)), int(m.group(2)), m.group(3) or 'pop'
        tag = C.BODY[m.start():C.BODY.find('>', m.start())]
        fxm = re.search(r'data-fx="(\w+)"', tag); fx = fxm.group(1) if fxm else 'pop'
        slow = 'data-slow' in tag
        t = G[i][min(j, len(G[i]) - 1)][0]
        if i == 0: continue
        ev.append((round(t, 3), 'slow' if slow else fx))
    sf = open(SP / getattr(C, 'SFX', 'sfx_template.py')).read()
    sf = sf.replace('__NAME__', C.NAME).replace('__DUR__', str(END)).replace('__S__', json.dumps(S)).replace('__EV__', json.dumps(ev)).replace('__SEED__', str(sum(map(ord, C.NAME))))
    (MOD / f'sfx_{C.NAME}.py').write_text(sf)
    print('S', S, 'END', END)


def mix():
    S, G, END = timeline()
    sh(f'cd "{MOD}" && python3 sfx_{C.NAME}.py "{W}/sfx.wav"')
    ins = ' '.join(f'-i "{W}/seg{i}.wav"' for i in range(N))
    fl = ';'.join(f'[{i}:a]adelay={int((S[i] + VOFF) * 1000)}|{int((S[i] + VOFF) * 1000)},aformat=channel_layouts=stereo,volume=1.4[v{i}]' for i in range(N))
    fl += f';[{N}:a]volume=0.45[sx];' + ''.join(f'[v{i}]' for i in range(N)) + f'[sx]amix=inputs={N + 1}:normalize=0:duration=longest,atrim=0:{END},alimiter=limit=0.85:level=disabled:attack=3:release=60[o]'
    sh(f'ffmpeg -y -v error {ins} -i "{W}/sfx.wav" -filter_complex "{fl}" -map "[o]" -ar 48000 -ac 2 "{W}/mix.wav"')
    out = subprocess.run(f'ffmpeg -i "{W}/mix.wav" -af volumedetect -f null -', shell=True, capture_output=True, text=True).stderr
    print('mix', re.findall(r'max_volume: (\S+ dB)', out), re.findall(r'mean_volume: (\S+ dB)', out))


def stills(ts=None):
    S, G, END = timeline()
    if ts is None:
        ts = []
        for i in range(N):
            for row in G[i]: ts.append(round(row[0] + 0.25, 2))
        ts += [round(END - 0.2, 2), 0.0]
    d = W / 'stills'; sh(f'rm -rf "{d}"')
    sh(f'cd "{MOD}" && HTMLFILE={C.NAME}.html python3 render.py stills "{d}" ' + ' '.join(map(str, ts)))
    # contact sheet
    sh(f'cd "{d}" && ffmpeg -y -v error -pattern_type glob -i "f_*.png" -vf "scale=270:480,tile=8x{(len(ts) + 7) // 8}:padding=6:color=gray" -frames:v 1 ../sheet.png')
    print('sheet', W / 'sheet.png', len(ts))


def render():
    S, G, END = timeline()
    n = int(round(60 * END)); h = n // 2
    p = subprocess.Popen(f'cd "{MOD}" && HTMLFILE={C.NAME}.html python3 render.py video 60 {END} "{W}/p0.mp4" 0 {h}', shell=True, stdout=subprocess.DEVNULL)
    q = subprocess.Popen(f'cd "{MOD}" && HTMLFILE={C.NAME}.html python3 render.py video 60 {END} "{W}/p1.mp4" {h} {n}', shell=True, stdout=subprocess.DEVNULL)
    assert p.wait() == 0 and q.wait() == 0
    (W / 'list.txt').write_text(f"file '{W}/p0.mp4'\nfile '{W}/p1.mp4'\n")
    sh(f'ffmpeg -y -v error -f concat -safe 0 -i "{W}/list.txt" -i "{W}/mix.wav" -vf "noise=c0s=6:c0f=t+u,format=yuv420p" -c:v libx264 -preset medium -crf 18 -r 60 -c:a aac -b:a 192k -map 0:v -map 1:a -t {END} -movflags +faststart "{W}/final.mp4"')
    print('final', W / 'final.mp4', dur(W / 'final.mp4'))


if stage == 'split': split()
elif stage == 'html': mkhtml()
elif stage == 'stills': stills(None if len(sys.argv) < 4 else [float(x) for x in sys.argv[3:]])
elif stage == 'mix': mix()
elif stage == 'render': render()
elif stage == 'all': mkhtml(); mix(); render()

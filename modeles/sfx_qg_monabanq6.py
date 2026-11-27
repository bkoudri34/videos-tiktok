"""Style C « collage papier » (vidéos QG) : beat libre de droits + bruitages de papier froissé, ciseaux et disque rayé, tout synthétisé ici, calé sur qg_monabanq6.html."""
import numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile

SR = 48000
DUR = 27.578
END = DUR
N = int(SR * DUR)
mix = np.zeros((N, 2))
rng = np.random.default_rng(1210)


import sys

def add(sig, t0, gain=1.0, pan=0.0):
    i = int(t0 * SR)
    if i >= N:
        return
    sig = sig[: N - i] * gain
    l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
    if sig.ndim == 1:
        mix[i:i + len(sig), 0] += sig * l * 1.414
        mix[i:i + len(sig), 1] += sig * r * 1.414
    else:
        mix[i:i + len(sig)] += sig


def bp(x, lo, hi):
    return sosfilt(butter(2, [lo, hi], btype="band", fs=SR, output="sos"), x)


def whoosh(dur=0.7, peak=0.55, lo=(250, 900), hi=(1800, 6000)):
    n = int(dur * SR); t = np.arange(n) / SR
    noise = rng.standard_normal(n)
    a, b = bp(noise, *lo), bp(noise, *hi)
    x = np.clip(t / dur, 0, 1)
    env = np.where(x < peak, (x / peak) ** 2.2, np.exp(-(x - peak) / (1 - peak) * 4.5))
    blend = np.clip((x - 0.15) / 0.6, 0, 1)
    mono = (a * (1 - blend) * 1.3 + b * blend * 0.8) * env
    pan = np.sin((x - 0.5) * np.pi) * 0.8
    return np.stack([mono * np.cos((pan + 1) * np.pi / 4), mono * np.sin((pan + 1) * np.pi / 4)], 1) * 1.4


def boom(dur=1.1, f0=95, f1=42):
    n = int(dur * SR); t = np.arange(n) / SR
    f = f1 + (f0 - f1) * np.exp(-t * 9)
    ph = 2 * np.pi * np.cumsum(f) / SR
    body = np.sin(ph) * np.exp(-t * 3.2)
    click = bp(rng.standard_normal(n), 1500, 6000) * np.exp(-t * 90) * 0.35
    return body + click


def bell(f=1800, dur=1.2, bright=1.0):
    n = int(dur * SR); t = np.arange(n) / SR
    s = (np.sin(2 * np.pi * f * t) * np.exp(-t * 4.5) + 0.5 * bright * np.sin(2 * np.pi * f * 2.76 * t) * np.exp(-t * 7)
         + 0.25 * bright * np.sin(2 * np.pi * f * 5.4 * t) * np.exp(-t * 12))
    return s * (1 - np.exp(-t * 900))


def pop(f0=420, f1=950, dur=0.12):
    n = int(dur * SR); t = np.arange(n) / SR
    f = f0 + (f1 - f0) * (1 - np.exp(-t * 60))
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 32) * (1 - np.exp(-t * 2000))


def click(dur=0.025, lo=2500, hi=9000):
    n = int(dur * SR); t = np.arange(n) / SR
    return bp(rng.standard_normal(n), lo, hi) * np.exp(-t * 260)


def riser(dur=1.0):
    n = int(dur * SR); t = np.arange(n) / SR
    x = t / dur
    noise = bp(rng.standard_normal(n), 900, 5000)
    tone = np.sin(2 * np.pi * np.cumsum(300 + 500 * x ** 2) / SR) * 0.25
    return (noise * 0.6 + tone) * x ** 2.5 * (1 - np.exp(-(1 - x) * 40))


def pad_bed(dur):
    """Soft cinematic bed: sustained minor chords + slow pulse, very low level."""
    n = int(dur * SR); t = np.arange(n) / SR
    chords = [[261.63, 329.63, 392.0], [220.0, 261.63, 329.63], [174.61, 220.0, 261.63], [196.0, 246.94, 293.66]]  # majeur, plus léger (style E)
    out = np.zeros(n)
    seg = 2.4
    for k in range(int(dur / seg) + 1):
        c = chords[k % 4]; i0 = int(k * seg * SR); i1 = min(n, int((k + 1) * seg * SR) + int(0.6 * SR))
        if i0 >= n: break
        tt = np.arange(i1 - i0) / SR
        env = np.minimum(1, tt / 0.5) * np.minimum(1, (tt[-1] - tt + 1e-3) / 0.6)
        for f in c:
            out[i0:i1] += (np.sin(2 * np.pi * f * tt) + 0.3 * np.sin(2 * np.pi * f * 2 * tt + 1)) * env * 0.12
    beat = 60 / 100
    for k in range(int(dur / beat)):
        i0 = int(k * beat * SR); m = min(n - i0, int(0.35 * SR)); tt = np.arange(m) / SR
        out[i0:i0 + m] += np.sin(2 * np.pi * (55 + 40 * np.exp(-tt * 30)) * tt) * np.exp(-tt * 9) * (0.5 if k % 2 == 0 else 0.25)
    out = sosfilt(butter(2, 2500, btype="low", fs=SR, output="sos"), out)
    return np.stack([out, out], 1)


def crinkle(dur=0.22):
    """Papier froissé : salve de micro-craquements filtrés."""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.zeros(n)
    for _ in range(int(dur * 260)):
        i = rng.integers(0, n - 200); m = rng.integers(40, 200)
        x[i:i + m] += rng.standard_normal(m) * np.exp(-np.arange(m) / (m / 4)) * rng.uniform(0.3, 1)
    x = bp(x, 1200, 9000)
    return x * np.exp(-t * 6) / (np.max(np.abs(x)) + 1e-6)


def snip():
    """Ciseaux : deux claquements métalliques rapprochés."""
    a = click(0.03, 2500, 9000) + 0.4 * bell(3400, 0.03, 0.3)[:int(0.03 * SR)]
    out = np.zeros(int(0.16 * SR)); out[:len(a)] += a; out[int(0.09 * SR):int(0.09 * SR) + len(a)] += a * 0.8
    return out


def scratch(dur=0.45):
    """Disque rayé : bruit filtré dont la hauteur fait un aller-retour rapide."""
    n = int(dur * SR); t = np.arange(n) / SR
    f = 600 + 1400 * np.abs(np.sin(t / dur * np.pi * 2.0))
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = (np.sin(ph) * 0.4 + bp(rng.standard_normal(n), 800, 4000) * 0.8) * np.sin(np.pi * t / dur) ** 0.5
    return x


def beat_bed(dur, bpm=100):
    """Petit beat hip-hop léger : kick, claquement, charleston, basse majeure."""
    n = int(dur * SR); out = np.zeros(n); b = 60 / bpm
    bass = [98.0, 98.0, 130.81, 110.0]
    for k in range(int(dur / (b / 2)) + 1):
        t0 = k * b / 2; i0 = int(t0 * SR)
        if i0 >= n: break
        if k % 4 == 0 or k % 8 == 5:
            m = min(n - i0, int(0.3 * SR)); tt = np.arange(m) / SR
            out[i0:i0 + m] += np.sin(2 * np.pi * (50 + 70 * np.exp(-tt * 35)) * tt) * np.exp(-tt * 10) * 0.9
        if k % 4 == 2:
            m = min(n - i0, int(0.18 * SR)); tt = np.arange(m) / SR
            out[i0:i0 + m] += bp(rng.standard_normal(m), 900, 5000) * np.exp(-tt * 22) * 0.55
        m = min(n - i0, int(0.05 * SR)); tt = np.arange(m) / SR
        out[i0:i0 + m] += bp(rng.standard_normal(m), 6000, 12000) * np.exp(-tt * 80) * (0.22 if k % 2 else 0.12)
        if k % 2 == 0:
            f = bass[(k // 8) % 4]; m = min(n - i0, int(b * 0.9 * SR)); tt = np.arange(m) / SR
            out[i0:i0 + m] += (np.sin(2 * np.pi * f * tt) + 0.3 * np.sin(4 * np.pi * f * tt)) * np.exp(-tt * 3) * 0.28
    return np.stack([out, out], 1)

# ---------- timeline (generated from the real voice-over of qg_monabanq6.html) ----------
S = [0.0, 2.828, 6.576, 9.824, 17.723, 20.885, 23.866]
EV = [[2.868, "pop"], [2.868, "right"], [4.873, "pop"], [4.337, "up"], [5.533, "up"], [6.616, "pop"], [7.344, "pop"], [7.842, "pop"], [8.643, "pop"], [7.842, "pop"], [8.643, "stamp"], [9.864, "pop"], [12.22, "stamp"], [12.98, "pop"], [14.357, "up"], [16.248, "stamp"], [17.763, "pop"], [17.763, "pop"], [18.158, "pop"], [18.964, "up"], [20.925, "stamp"], [22.263, "pop"], [23.906, "left"], [25.241, "right"], [25.92, "pop"]]
add(beat_bed(DUR), 0.0, 0.42)                                # beat
add(crinkle(0.3), 0.0, 0.35)                                 # le papier se pose à la 1re image
for c in S[1:]:                                              # changement de plan : coup de ciseaux + papier
    add(snip(), c - 0.12, 0.35); add(crinkle(0.25), c, 0.25)
for k, (t, fx) in enumerate(EV):
    pan = 0.3 if k % 2 else -0.3
    if fx == 'slow':
        add(scratch(0.45), t - 0.1, 0.30); add(boom(1.0, 90, 40), t + 0.3, 0.45)
    elif fx in ('stamp', 'tick'):
        add(boom(0.5, 140, 60), t, 0.22, pan); add(crinkle(0.15), t, 0.30, pan)
    else:
        add(pop(380 + 40 * (k % 5), 900, 0.1), t, 0.16, pan); add(crinkle(0.12), t, 0.22, pan)
add(snip(), END - 0.6, 0.3)

mix *= 0.9

peak = np.max(np.abs(mix))
mix = np.tanh(mix / peak * 1.2) / np.tanh(1.2) * 0.7
fade = np.ones(N); fo = int(0.25 * SR); fade[-fo:] = np.linspace(1, 0, fo)
mix *= fade[:, None]
out = sys.argv[1] if len(sys.argv) > 1 else "sfx.wav"
wavfile.write(out, SR, (mix * 32767).astype(np.int16))
print("sfx ok", round(float(np.max(np.abs(mix))), 3))

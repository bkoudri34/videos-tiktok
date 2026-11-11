"""Sound design layer (whooshes, impacts, ticks, pops) synthesised from scratch, timed to hacoo16.html."""
import numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile

SR = 48000
DUR = 20.385
END = DUR
N = int(SR * DUR)
mix = np.zeros((N, 2))
rng = np.random.default_rng(625)


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
    chords = [[220.0, 261.63, 329.63], [174.61, 220.0, 261.63], [196.0, 246.94, 293.66], [164.81, 207.65, 246.94]]
    out = np.zeros(n)
    seg = 2.4
    for k in range(int(dur / seg) + 1):
        c = chords[k % 4]; i0 = int(k * seg * SR); i1 = min(n, int((k + 1) * seg * SR) + int(0.6 * SR))
        if i0 >= n: break
        tt = np.arange(i1 - i0) / SR
        env = np.minimum(1, tt / 0.5) * np.minimum(1, (tt[-1] - tt + 1e-3) / 0.6)
        for f in c:
            out[i0:i1] += (np.sin(2 * np.pi * f * tt) + 0.3 * np.sin(2 * np.pi * f * 2 * tt + 1)) * env * 0.12
    beat = 60 / 84
    for k in range(int(dur / beat)):
        i0 = int(k * beat * SR); m = min(n - i0, int(0.35 * SR)); tt = np.arange(m) / SR
        out[i0:i0 + m] += np.sin(2 * np.pi * (55 + 40 * np.exp(-tt * 30)) * tt) * np.exp(-tt * 9) * (0.5 if k % 2 == 0 else 0.25)
    out = sosfilt(butter(2, 2500, btype="low", fs=SR, output="sos"), out)
    return np.stack([out, out], 1)

# ---------- timeline (generated from the real voice-over of hacoo16.html) ----------
S = [0.0, 2.81, 6.238, 10.295, 13.105, 15.915]
EV = [[2.868, "tw"], [4.278, "tw"], [2.868, "up"], [2.868, "up"], [4.278, "up"], [5.128, "stamp"], [6.289, "tw"], [6.749, "tw"], [6.289, "up"], [8.199, "type"], [8.199, "pop"], [8.199, "up"], [10.352, "tw"], [10.352, "growY"], [11.532, "slow"], [11.532, "fade"], [13.163, "tw"], [14.263, "tw"], [13.163, "up"], [14.263, "stamp"], [15.972, "tw"], [15.972, "tw"], [17.072, "tw"], [17.662, "up"]]
add(pad_bed(DUR), 0.0, 0.55)                                 # music bed
add(boom(0.9, 110, 50), 0.0, 0.30)                          # hook lands on frame 1
for c in S[1:]:                                              # cut whooshes
    add(whoosh(0.5, 0.6), c - 0.3, 0.42)
for k, (t, fx) in enumerate(EV):                             # elements appearing on the voice
    pan = 0.3 if k % 2 else -0.3
    if fx == 'slow':
        add(riser(1.0), t - 1.0, 0.10)
        add(boom(1.6, 80, 34), t, 0.65); add(bell(1318, 1.6), t + 0.05, 0.14); add(bell(1976, 1.6, 0.6), t + 0.17, 0.12)
    elif fx in ('stamp', 'tick'):
        add(click(0.03, 1500, 7000), t, 0.32, pan); add(bell(1568 + 120 * (k % 4), 0.6, 0.5), t, 0.08, pan)
    else:
        add(bell(1318 + 220 * (k % 4), 0.5, 0.4), t, 0.07, pan); add(click(0.02, 3000, 9000), t, 0.12, pan)
add(whoosh(0.5, 0.6), END - 0.8, 0.4); add(boom(0.9, 110, 50), END - 0.45, 0.3)   # loop back to hook

mix *= 0.9
peak = np.max(np.abs(mix))
mix = np.tanh(mix / peak * 1.2) / np.tanh(1.2) * 0.7
fade = np.ones(N); fo = int(0.25 * SR); fade[-fo:] = np.linspace(1, 0, fo)
mix *= fade[:, None]
out = sys.argv[1] if len(sys.argv) > 1 else "sfx.wav"
wavfile.write(out, SR, (mix * 32767).astype(np.int16))
print("sfx ok", round(float(np.max(np.abs(mix))), 3))

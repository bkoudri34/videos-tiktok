"""Sound design layer (whooshes, impacts, ticks, pops) synthesised from scratch, timed to hellobank3.html."""
import numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile

SR = 48000
DUR = 19.4
N = int(SR * DUR)
mix = np.zeros((N, 2))
rng = np.random.default_rng(30)


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


def ease_out_quint(x):
    return 1 - (1 - np.clip(x, 0, 1)) ** 5


# ---------- timeline (matches hellobank3.html) ----------
import sys
S = [0.0, 3.7, 6.75, 9.15, 11.85, 15.0]
add(boom(0.9, 110, 50), 0.0, 0.35)                         # hook lands on frame 1
add(pop(420, 1000, 0.12), 1.1, 0.25)                       # "80 €" punch
for c in S[1:]:                                             # cut whooshes + punch
    add(whoosh(0.5, 0.6), c - 0.3, 0.45)
add(pop(380, 900, 0.12), S[1] + 0.05, 0.28)                 # notification drops in
add(bell(1568, 1.2, 0.7), S[1] + 0.3, 0.16); add(bell(2349, 1.0, 0.5), S[1] + 0.42, 0.10)
add(click(0.03, 1500, 7000), S[2] + 1.3, 0.32); add(pop(500, 1100, 0.09), S[2] + 1.31, 0.15)   # tick 1
add(click(0.03, 1500, 7000), S[3] + 0.6, 0.32); add(pop(560, 1200, 0.09), S[3] + 0.61, 0.15)   # tick 2
add(pop(360, 850, 0.12), S[3] + 0.7, 0.24, pan=-0.4); add(pop(420, 950, 0.12), S[3] + 1.5, 0.24, pan=0.4)  # option chips
add(riser(1.4), S[4] + 0.6, 0.10)                           # build to slow-mo
add(boom(1.6, 80, 34), S[4] + 2.0, 0.65)                    # 130 reveal (slow-mo moment)
add(bell(1318, 1.6), S[4] + 2.05, 0.14); add(bell(1976, 1.6, 0.6), S[4] + 2.17, 0.12)
add(pop(330, 800, 0.14), S[5] + 0.15, 0.26)                 # CTA chip
add(click(0.03, 1500, 7000), S[5] + 0.55, 0.3)
add(whoosh(0.5, 0.6), 18.6, 0.4); add(boom(0.9, 110, 50), 18.9, 0.3)   # loop back to hook

mix *= 0.9
peak = np.max(np.abs(mix))
mix = np.tanh(mix / peak * 1.2) / np.tanh(1.2) * 0.7
fade = np.ones(N); fo = int(0.25 * SR); fade[-fo:] = np.linspace(1, 0, fo)
mix *= fade[:, None]
out = sys.argv[1] if len(sys.argv) > 1 else "sfx.wav"
wavfile.write(out, SR, (mix * 32767).astype(np.int16))
print("sfx ok", round(float(np.max(np.abs(mix))), 3))

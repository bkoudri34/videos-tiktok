"""Sound design layer (whooshes, impacts, ticks, pops) synthesised from scratch, timed to revolut2.html."""
import numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile

SR = 48000
DUR = 23.0
N = int(SR * DUR)
mix = np.zeros((N, 2))
rng = np.random.default_rng(11)


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


# ---------- timeline (matches video.html) ----------
add(whoosh(0.9, 0.7), 0.0, 0.45)                 # phone rises
add(boom(), 0.42, 0.55)                           # counter starts
# odometer ticks (units column crossings, decelerating)
last = -1
for i in range(int(0.45 * SR), int(2.2 * SR), 48):
    tt = i / SR
    idx = int(40 * ease_out_quint((tt - 0.45) / 1.7))
    if idx != last and (tt - getattr(add, "lt", 0)) > 0.035:
        add(click(0.02, 3000, 9000), tt, 0.10 + 0.08 * (tt - 0.45) / 1.7, pan=0.2)
        add.lt = tt
    last = idx
add(pop(300, 700, 0.14), 1.25, 0.18)              # lock-screen notification
add(pop(380, 900), 1.9, 0.28)                      # money bag
add(bell(1760, 1.4), 2.18, 0.20); add(bell(2640, 1.2, 0.6), 2.2, 0.12); add(boom(0.8, 120, 55), 2.16, 0.35)
for c in (3.0, 8.0, 13.0, 18.0):                  # cut whooshes
    add(whoosh(0.62, 0.55), c - 0.34, 0.6)
add(click(0.03, 1500, 7000), 4.0, 0.35); add(pop(500, 1100, 0.09), 4.02, 0.15)   # tap link
add(whoosh(0.5, 0.3, (400, 1200), (2500, 7000)), 4.0, 0.25)                         # app opens
for a, b in ((4.95, 6.0), (6.35, 7.45)):          # swipes
    add(whoosh(b - a + 0.1, 0.25, (600, 1600), (3000, 8000)), a - 0.05, 0.13)
for a, b, n in ((8.45, 8.8, 4), (8.95, 9.4, 6), (9.55, 10.3, 20)):   # typing
    for k in range(n):
        add(click(0.018, 2000, 8000), a + (b - a) * (k + 1) / n, 0.13 + 0.04 * rng.random(), pan=rng.uniform(-.2, .2))
add(pop(450, 1000), 10.38, 0.2)                    # referral chip
add(click(0.03, 1500, 7000), 10.85, 0.35); add(pop(500, 1100, 0.09), 10.86, 0.15)  # Valider
add(bell(1318, 1.4), 11.08, 0.18); add(bell(1976, 1.4), 11.24, 0.16)                # success chime
for k, a in enumerate((11.65, 12.05, 12.45)):
    add(pop(500 + 120 * k, 1100 + 200 * k), a, 0.22)
for k in range(3):                                  # avatars pop in
    add(pop(350 + 60 * k, 800 + 100 * k, 0.12), 13.85 + 0.15 * k, 0.2, pan=(-.6, .6, 0)[k])
for k in range(3):                                  # pulses arrive
    pa = 14.55 + 0.5 * k
    add(whoosh(0.6, 0.85, (800, 2000), (3000, 8000)), pa, 0.12, pan=(-.6, .6, 0)[k])
    add(bell(1568 + 220 * k, 1.0, 0.7), pa + 0.6, 0.14, pan=(-.6, .6, 0)[k])
add(pop(300, 700, 0.14), 15.3, 0.22); add(pop(330, 760, 0.14), 16.2, 0.22)          # notification cards
add(boom(1.4, 85, 38), 18.02, 0.6)                 # CTA impact
add(pop(380, 900), 18.12, 0.25)                    # link icon
for k in range(11):                                 # letters shimmer
    add(bell(2200 + 90 * k, 0.5, 0.4), 18.3 + 0.055 * k, 0.035, pan=-0.6 + 0.12 * k)
add(pop(330, 800, 0.14), 19.92, 0.26)               # DM bubble
add(riser(0.9), 21.15, 0.08); add(bell(2093, 1.6, 0.5), 22.05, 0.1)                  # final shine

# master: gentle limiting + fades
mix *= 0.9
peak = np.max(np.abs(mix))
mix = np.tanh(mix / peak * 1.2) / np.tanh(1.2) * 0.7
fade = np.ones(N); fo = int(0.6 * SR); fade[-fo:] = np.linspace(1, 0, fo)
mix *= fade[:, None]
import sys
wavfile.write(sys.argv[1] if len(sys.argv)>1 else "sfx.wav", SR, (mix * 32767).astype(np.int16))
print("sfx ok", round(float(np.max(np.abs(mix))), 3))

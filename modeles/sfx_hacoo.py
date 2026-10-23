"""Sound design layer (whooshes, impacts, ticks, pops) synthesised from scratch, timed to video.html."""
import numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile

SR = 48000
DUR = 25.0
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


# ---------- timeline (hacoo.html) ----------
add(whoosh(0.9, 0.7), 0.0, 0.45)
add(boom(), 1.15, 0.5)                                   # "-14 %" lands
for k in range(5): add(pop(300+40*k, 700+60*k, 0.12), 0.15+0.1*k, 0.10, pan=(-.6,.6,-.3,.3,0)[k])
add(bell(1760, 1.2), 1.5, 0.14)
for c in (3.0, 6.0, 10.0, 15.0, 20.0):
    add(whoosh(0.62, 0.55), c - 0.34, 0.6)
add(click(0.03, 1500, 7000), 3.75, 0.35); add(pop(500, 1100, 0.09), 3.76, 0.15)     # tap Profil
add(whoosh(0.4, 0.3, (400, 1200), (2500, 7000)), 3.8, 0.2)
for k in range(3): add(bell(1568+200*k, 0.8, 0.5), 4.4+0.5*k, 0.06)                 # profile highlight
add(whoosh(1.2, 0.6, (300, 900), (1500, 5000)), 6.1, 0.18)                          # zoom to bio
add(click(0.03, 1500, 7000), 8.85, 0.35); add(pop(500, 1100, 0.09), 8.86, 0.15)     # tap Telegram
add(whoosh(0.5, 0.3, (400, 1200), (2500, 7000)), 8.9, 0.25)
for a, b in ((10.6, 11.7), (12.0, 13.0)):
    add(whoosh(b - a + 0.1, 0.25, (600, 1600), (3000, 8000)), a - 0.05, 0.13)
add(click(0.03, 1500, 7000), 13.55, 0.35); add(pop(450, 1000), 13.7, 0.25); add(bell(1976, 1.0, 0.6), 13.75, 0.12)
add(whoosh(1.0, 0.6, (300, 900), (1500, 5000)), 15.2, 0.16)                         # zoom to promo field
for k in range(7): add(click(0.02, 2000, 8000), 16.0 + 0.2 * (k + 1), 0.16, pan=rng.uniform(-.2, .2))
add(click(0.03, 1500, 7000), 17.7, 0.35)
add(bell(1318, 1.4), 17.86, 0.18); add(bell(1976, 1.4), 18.02, 0.16)                # code applied
last = -1
for i in range(int(18.0 * SR), int(18.9 * SR), 48):
    tt = i / SR; v = int((39.90 - 5.59 * ease_out_quint((tt - 18.0) / 0.9)) * 10)
    if v != last and tt - getattr(add, "lt", 0) > 0.04:
        add(click(0.02, 3000, 9000), tt, 0.1); add.lt = tt
    last = v
add(boom(1.4, 85, 38), 20.02, 0.6)
for k in range(3): add(pop(380+60*k, 860+80*k, 0.12), 20.25 + 0.32 * k, 0.22, pan=(-.5, 0, .5)[k])
add(boom(0.9, 110, 50), 20.95, 0.35)
for k in range(7): add(bell(2200 + 110 * k, 0.5, 0.4), 21.0 + 0.06 * k, 0.04, pan=-0.6 + 0.2 * k)
add(pop(330, 800, 0.14), 21.72, 0.24); add(pop(360, 840, 0.14), 22.37, 0.24)
add(riser(0.9), 23.2, 0.08); add(bell(2093, 1.6, 0.5), 24.1, 0.1)

# master: gentle limiting + fades
mix *= 0.9
peak = np.max(np.abs(mix))
mix = np.tanh(mix / peak * 1.2) / np.tanh(1.2) * 0.7
fade = np.ones(N); fo = int(0.6 * SR); fade[-fo:] = np.linspace(1, 0, fo)
mix *= fade[:, None]
wavfile.write("/home/claude/bourso/sfx_hacoo.wav", SR, (mix * 32767).astype(np.int16))
print("sfx ok", round(float(np.max(np.abs(mix))), 3))

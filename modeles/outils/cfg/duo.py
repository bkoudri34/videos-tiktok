"""Briques du style « Duo 3D » (voir STYLE.md, style D) : à importer dans une config cfg/<nom>.py.

La config définit en plus :
- DUO_LINES : une entrée par réplique, {'who': 'M'|'P', 'M': pose, 'P': pose, 'shot': 'wide'|'M'|'P'}
  M = « le malin » (sportif, à droite), P = « le pigeon » (costaud, à gauche).
  Poses : idle, talk, point, shrug, hip, shock, head, cool, think.
- BODY = duo_body(...) + scènes (cartes qui surgissent, ancrées au-dessus d'une tête avec anc('M'|'P', ...)).
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent
THREE = '<script src="https://cdn.jsdelivr.net/npm/three@0.149.0/build/three.min.js"></script>'
BASE = 'base_duo.css'
SFX = 'sfx_luxe_template.py'
ROOT = ':root{--bg:#07080b}'
CAM = 0.35  # légère caméra à l'épaule sur le calque HTML (les cartes), la 3D a sa propre caméra


def duo_js(lines, bg=None):
    cfg = {'lines': lines}
    if bg is not None:
        cfg['bg'] = bg
    return 'const CAM=0.35;const DUO=' + json.dumps(cfg) + ';\n' + (OUT / 'duo3d.js').read_text()


def duo_body(name_m='LE MALIN', name_p='LE PIGEON'):
    return (f'  <div id="three"></div>\n'
            f'  <div class="lbl" id="lblM">{name_m}</div><div class="lbl" id="lblP">{name_p}</div>\n')


def anc(who, inner, scene):
    """Bloc accroché au-dessus de la tête de `who`, visible pendant la scène `scene` (ex. '3' ou '3-4')."""
    return f'<div class="scene" data-s="{scene}" data-in="pop"><div class="anc" data-who="{who}">{inner}</div></div>'

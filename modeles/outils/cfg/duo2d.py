"""Briques du style D2 « Duo dessiné » (voir STYLE.md, style D2) : à importer dans une config cfg/<nom>.py.

Même interface que cfg/duo.py (style D en 3D), sans Three.js ni aucun téléchargement :
- DUO_LINES : une entrée par réplique, {'who': 'M'|'P', 'M': pose, 'P': pose, 'shot': 'wide'|'M'|'P', 'lbl': False facultatif}
  M = « le malin » (fin, casquette, à droite), P = « le pigeon » (rond, t-shirt hachuré, à gauche).
  Poses : idle, talk, point, shrug, hip, shock, head, cool, think.
- JS = duo2d_js(DUO_LINES, p_bun=False) ; p_bun=True ajoute un chignon au pigeon (« la pigeonne »).
- BODY = duo2d_body(...) + scènes ; anc('M'|'P', html, scène) accroche une carte au-dessus de la tête.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent
BASE = 'base_duo2d.css'
SFX = 'sfx_luxe_template.py'
ROOT = ':root{--bg:#faf9f6}'
MINLEN = 0.9
GAP = 0.12
TAIL = 2.6


def duo2d_js(lines, p_bun=False, cap='#e63946'):
    cfg = {'lines': lines, 'bun': p_bun, 'cap': cap}
    return 'const CAM=0.3;const DUO=' + json.dumps(cfg) + ';\n' + (OUT / 'duo2d.js').read_text()


def duo2d_body(name_m='le malin', name_p='le pigeon'):
    return ('  <svg id="duo2d" viewBox="0 0 1080 1920"></svg>\n'
            f'  <div class="lbl" id="lblM">{name_m}</div><div class="lbl" id="lblP">{name_p}</div>\n')


def anc(who, inner, scene):
    """Bloc accroché au-dessus de la tête de `who`, visible pendant la scène `scene` (ex. '3' ou '3-4')."""
    return f'<div class="scene" data-s="{scene}" data-in="pop"><div class="anc" data-who="{who}">{inner}</div></div>'

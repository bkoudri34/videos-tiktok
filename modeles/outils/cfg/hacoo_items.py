"""Illustrations génériques (sans marque) pour les vidéos Hacoo v3."""
ICONS = {
 'Gants': '<path d="M60 170 L60 95 Q60 80 72 80 L72 45 Q72 35 82 35 Q92 35 92 45 L92 75 L92 38 Q92 28 102 28 Q112 28 112 38 L112 75 L112 42 Q112 32 122 32 Q132 32 132 42 L132 85 L140 70 Q148 58 158 66 Q164 72 158 84 L138 130 L138 170 Z" fill="#ffe4dc"/><rect x="58" y="150" width="82" height="22" rx="6" fill="#e04848"/><circle cx="82" cy="42" r="6" fill="#e04848"/>',
 'Bonnet': '<circle cx="100" cy="38" r="20" fill="#fff4f0"/><path d="M45 135 Q45 58 100 58 Q155 58 155 135 Z" fill="#e04848"/><path d="M70 70 L70 132 M100 60 L100 132 M130 70 L130 132" stroke="#b83232" stroke-width="6"/><rect x="38" y="128" width="124" height="34" rx="10" fill="#fff4f0"/>',
 'Plaid': '<rect x="35" y="55" width="130" height="100" rx="18" fill="#f3e2cf"/><path d="M35 85 H165 M35 115 H165 M75 55 V155 M125 55 V155" stroke="#d9a24c" stroke-width="6" opacity=".7"/><path d="M35 145 Q100 175 165 145 L165 155 Q100 185 35 155 Z" fill="#e2c9ab"/>',
 'Doudoune': '<path d="M55 45 L80 32 Q100 44 120 32 L145 45 L162 120 L142 124 L140 170 L60 170 L58 124 L38 120 Z" fill="#cfd9f5"/><path d="M58 70 H142 M58 98 H142 M60 126 H140 M60 152 H140" stroke="#7d93cc" stroke-width="5"/><line x1="100" y1="40" x2="100" y2="170" stroke="#4a5f99" stroke-width="5"/>',
 'Bottines': '<path d="M50 40 H95 V125 Q140 125 160 140 Q168 150 160 160 H50 Z" fill="#c9a27a"/><rect x="50" y="155" width="112" height="14" rx="5" fill="#4a3424"/><path d="M60 60 H90 M60 80 H90 M60 100 H90" stroke="#7a5a3a" stroke-width="5"/>',
 'Écharpe': '<path d="M50 50 Q100 80 150 50 L150 75 Q100 105 50 75 Z" fill="#d9a24c"/><rect x="110" y="70" width="32" height="95" rx="6" fill="#d9a24c"/><path d="M114 165 v12 M122 165 v12 M130 165 v12 M138 165 v12" stroke="#d9a24c" stroke-width="4"/><path d="M60 62 H140" stroke="#7a5016" stroke-width="5" opacity=".5"/>',
}


def icon(name, size=200):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 200 200">{ICONS[name]}</svg>'

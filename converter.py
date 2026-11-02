from pathlib import Path
import re, shutil, sys
src=Path(sys.argv[1]) if len(sys.argv)>1 else None
if not src or not src.is_file():
 print('Uso: python converter.py arquivo_original.html');sys.exit(1)
folder=Path(__file__).resolve().parent
html=src.read_text(encoding='utf-8-sig')
html=re.sub(r'\(function setupPWA\(\) \{.*?\}\)\(\);', '', html, count=1, flags=re.S)
# Remove o antigo manifesto dinâmico e usa ícones estáticos
if '<link rel="manifest"' not in html:
 html=html.replace('</head>','<link rel="manifest" href="./manifest.webmanifest">\n<link rel="icon" type="image/png" href="./icons/icon-192.png">\n<link rel="apple-touch-icon" href="./icons/icon-192.png">\n</head>',1)
(folder/'index.html').write_text(html,encoding='utf-8')
print('OK: index.html criado em',folder)

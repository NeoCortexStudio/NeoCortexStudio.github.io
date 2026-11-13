# Arma las páginas de neocortexstudio.github.io a partir de los textos de abajo (contenido/*.html).
# Uso: python herramientas/generar.py   (desde la carpeta NeoCortexStudio_web)
# Cada página = encabezado + contenido + pie. Los textos van en español e inglés: <div lang="es"> y <div lang="en">.
import os, re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GP = 'https://play.google.com/store/apps/details?id=com.neocortex.simonsi'
AS = 'https://apps.apple.com/app/id6833710828'
APP_STORE_LISTA = False   # cambiar a True cuando Simon Sí ya esté publicado en la App Store
CORREO = 'soporte.neocortexstudio@gmail.com'

PAGINAS = [
    # (archivo, contenido, nav activo, título es, título en, descripción es)
    ('index.html', 'inicio.html', 'inicio', 'NeoCortex Studio', 'NeoCortex Studio', 'Estudio independiente de videojuegos. Creadores de Simon Sí, tu mascota virtual.'),
    ('simonsi/index.html', 'simonsi.html', 'simonsi', 'Simon Sí - Tu Mascota Virtual', 'Simon Sí - Your Virtual Pet', 'Cuida a Simon, un alien que solo dice "Sí": dale de comer, vístelo, decora su casa y juega minijuegos.'),
    ('soporte/index.html', 'soporte.html', 'soporte', 'Soporte - Simon Sí', 'Support - Simon Sí', 'Ayuda y contacto de Simon Sí.'),
    ('privacidad/index.html', 'privacidad.html', 'privacidad', 'Política de privacidad - Simon Sí', 'Privacy policy - Simon Sí', 'Política de privacidad de Simon Sí (Android y iPhone).'),
    ('404.html', '404.html', '', 'Página no encontrada', 'Page not found', 'Esta página no existe.'),
]

def botones_tiendas():
    gp = f'<a class="bt" href="{GP}" target="_blank" rel="noopener">▶ Google Play</a>'
    if APP_STORE_LISTA:
        a = f'<a class="bt oro" href="{AS}" target="_blank" rel="noopener"> App Store</a>'
    else:
        a = '<span class="bt gris"><span lang="es">App Store · Próximamente</span><span lang="en">App Store · Coming soon</span></span>'
    return f'<div class="botones">{gp}{a}</div>'

def pagina(archivo, cont, activo, tes, ten, desc):
    prof = archivo.count('/')
    r = '/' if archivo == '404.html' else '../' * prof   # ruta a la raíz (la 404 se muestra en cualquier dirección: va con ruta absoluta)
    cuerpo = open(os.path.join(RAIZ, 'herramientas', 'contenido', cont), encoding='utf-8').read()
    cuerpo = cuerpo.replace('{{R}}', r).replace('{{TIENDAS}}', botones_tiendas()).replace('{{CORREO}}', CORREO)
    nav = [('inicio', '', 'Inicio', 'Home'), ('simonsi', 'simonsi/', 'Simon Sí', 'Simon Sí'),
           ('soporte', 'soporte/', 'Soporte', 'Support'), ('privacidad', 'privacidad/', 'Privacidad', 'Privacy')]
    navh = ''.join(f'<a href="{r}{u}"{" class=\"on\"" if k == activo else ""}><span lang="es">{es}</span><span lang="en">{en}</span></a>' for k, u, es, en in nav)
    return f'''<!doctype html>
<html lang="es" data-idioma="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title data-es="{tes}" data-en="{ten}">{tes}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0f1230">
<meta property="og:title" content="{tes}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://neocortexstudio.github.io/assets/img/banner_es.png">
<link rel="icon" href="{r}assets/img/favicon_estudio.png">
<link rel="apple-touch-icon" href="{r}assets/img/logo_neocortex_180.png">
<link rel="stylesheet" href="{r}assets/estilo.css">
<script src="{r}assets/idioma.js"></script>
</head>
<body>
<header class="barra"><div class="barra-in">
  <a class="marca" href="{r}"><img class="logo" src="{r}assets/img/logo_neocortex_180.png" alt="">NeoCortex Studio</a>
  <nav class="nav">{navh}</nav>
  <div class="idioma"><button data-l="es">ES</button><button data-l="en">EN</button></div>
</div></header>
<main>
{cuerpo}
</main>
<footer><div class="in">
  <span>© 2026 NeoCortex Studio</span>
  <span><a href="{r}privacidad/"><span lang="es">Privacidad</span><span lang="en">Privacy</span></a> · <a href="{r}soporte/"><span lang="es">Soporte</span><span lang="en">Support</span></a> · <a href="mailto:{CORREO}">{CORREO}</a></span>
</div></footer>
</body>
</html>
'''

for p in PAGINAS:
    ruta = os.path.join(RAIZ, p[0]); os.makedirs(os.path.dirname(ruta), exist_ok=True)
    open(ruta, 'w', encoding='utf-8', newline='\n').write(pagina(*p))
    print('ok', p[0])

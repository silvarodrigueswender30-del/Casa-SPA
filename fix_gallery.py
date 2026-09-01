import glob
for f in ['gallery.html', 'gallery.php']:
    html = open(f, 'rb').read().decode('utf-8')
    if 'scripts.js' not in html:
        html = html.replace('<script src="js/bootstrap.min.js"></script>', '<script src="js/bootstrap.min.js"></script>\n  <script src="js/scripts.js"></script>')
        open(f, 'w', encoding='utf-8').write(html)

import os

links = '''
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="192x192" href="/android-chrome-192x192.png">
<link rel="icon" type="image/png" sizes="512x512" href="/android-chrome-512x512.png">
<link rel="stylesheet" href="css/bootstrap.min.css" />
<link rel="stylesheet" href="css/fontawesome.css" />
<link rel="stylesheet" href="css/flaticon.css" />
<link rel="stylesheet" href="css/pbminfotech-base-icons.css" />
<link rel="stylesheet" href="css/themify-icons.css" />
<link rel="stylesheet" href="css/swiper.min.css" />
<link rel="stylesheet" href="css/magnific-popup.css" />
<link rel="stylesheet" href="css/twentytwenty.css" />
<link rel="stylesheet" href="css/aos.css" />
<link rel="stylesheet" href="css/shortcode.css" />
<link rel="stylesheet" href="css/base.css" />
<link rel="stylesheet" href="css/style.css" />
<link rel="stylesheet" href="css/responsive.css" />
<link rel="stylesheet" href="css/casa-spa-index.css" />
<link rel="stylesheet" href="css/casa-spa.css" />
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" rel="stylesheet" />
'''

with open('gallery.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make sure we don't inject multiple times
if 'bootstrap.min.css' not in html:
    html = html.replace('</head>', links + '\n</head>')
    with open('gallery.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Fixed gallery.html CSS")
else:
    print("gallery.html already has CSS")

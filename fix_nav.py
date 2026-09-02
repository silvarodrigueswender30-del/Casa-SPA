import re

content = open('index.html', encoding='utf-8').read()

# Replace the commented out gallery link
content = re.sub(r'<!--\s*<li class="dropdown">\s*<a href="gallery\.html">Gallery</a>\s*</li>\s*-->', '<li class=""><a href="gallery.html">Galeria</a></li>', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html nav menu")

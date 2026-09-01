import re
html = open('index.html', encoding='utf-8').read()
for s in re.findall(r'<section class="(.*?)"', html):
    print(s)

import re

html = open('gallery.html', encoding='utf-8').read()
match = re.search(r'(<section class="mv-gallery">.*?</section>.*?<script>.*?</script>)', html, re.DOTALL)
if match:
    with open('galeria_content.txt', 'w', encoding='utf-8') as f:
        f.write(match.group(1))
else:
    print('No match')

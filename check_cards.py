import re
html = open('index.html', encoding='utf-8').read()

print("--- staycation-showcase ---")
match = re.search(r'<section class="staycation-showcase.*?>(.*?)</section>', html, re.DOTALL)
if match:
    # count divs with col-
    print("Col classes:", re.findall(r'class="[^"]*col-[^"]*"', match.group(1)))

print("--- marbella-amenities-section ---")
match = re.search(r'<section class="marbella-amenities-section.*?>(.*?)</section>', html, re.DOTALL)
if match:
    print("Articles with col-:", re.findall(r'<article class="[^"]*col-[^"]*"', match.group(1)))

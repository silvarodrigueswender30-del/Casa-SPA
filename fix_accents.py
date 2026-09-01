import glob

replacements = {
    "espao": "espaço",
    "Trs": "Três",
    "reas": "áreas",
    "convivncia": "convivência",
    "voc": "você",
    "refgio": "refúgio",
    "pr": "pôr",
    "Patrimnio": "Patrimônio",
    "Histrico": "Histórico",
    "baa": "baía",
    "d'gua": "d'água",
    "caiara": "caiçara",
    "culinria": "culinária",
    "Dvidas": "Dúvidas",
    "rpido": "rápido",
    "Incio": "Início",
    "Avaliaes": "Avaliações",
    "Histrias": "Histórias",
    "Corumb": "Corumbê",
    "tambm": "também",
    "privatrio": "privativo",
    "pde": "pôde",
    "No": "Não"
}

for f in ['about-us.html', 'about-us.php', 'marbella-farms-resort.html', 'marbella-farms-resort.php', 'marbella-suites.html', 'marbella-suites.php', 'contact-us.html', 'contact-us.php']:
    html = open(f, 'rb').read().decode('utf-8', 'ignore')
    for bad, good in replacements.items():
        html = html.replace(bad, good)
    open(f, 'w', encoding='utf-8').write(html)

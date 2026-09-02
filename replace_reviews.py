import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

reviews = [
    {
        "name": "Edilson Villela Valentim dos Santos filho",
        "role": "Há 2 meses",
        "text": "Nossa estadia na Casa SPA Paraty foi simplesmente incrível! A localização é excelente, muito próxima ao Centro Histórico de Paraty, permitindo fácil acesso aos principais pontos turísticos, restaurantes e atrações da cidade."
    },
    {
        "name": "Camaione Taufner",
        "role": "Há 2 meses",
        "text": "Fiquei hospedado este final de semana com a minha família e foi simplesmente maravilhoso!"
    },
    {
        "name": "MÁRIO BISPO",
        "role": "Há 2 meses",
        "text": "Show... Recomendo, lugar aconchegante e perto de tudo com estrutura completa para desfrutar em família e momentos especiais."
    },
    {
        "name": "Paulo Laguardia",
        "role": "Há 3 semanas",
        "text": "A casa é muito nova e conta com alguns diferenciais. Logo na entrada já o primeiro. Ela tem carregador veicular! Outro diferencial. A casa tem bateria estacionária,o que garante o abastecimento emergencial quando falta luz na região e crescente mais caso fique faltando."
    }
]

def generate_cards(reviews_list):
    cards_html = ""
    for r in reviews_list:
        cards_html += f'''                                                                    <article class="mgr-card">
                                                                        <div class="mgr-quote">“</div>
                                                                        <p>
                                                                            {r["text"]}
                                                                        </p>
                                                                        <div class="mgr-meta">
                                                                            <div>
                                                                                <h6 class="mgr-name">{r["name"]}</h6>
                                                                                <span class="mgr-role">{r["role"]}</span>
                                                                            </div>
                                                                            <div class="mgr-stars">
                                                                                <span></span><span></span><span></span><span></span><span></span>
                                                                            </div>
                                                                        </div>
                                                                    </article>\n'''
    return cards_html

# Block 1
block1_cards = generate_cards(reviews)
# Block 2 (Shuffle or repeat to fill)
block2_cards = generate_cards([reviews[2], reviews[3], reviews[0], reviews[1]])

# Use regex to replace the content inside <div class="mgr-track"> ... </div>
parts = content.split('<!-- ===== BLOCK 1 ===== -->')
if len(parts) == 2:
    block1_parts = parts[1].split('<!-- ===== BLOCK 2 ===== -->')
    if len(block1_parts) == 2:
        # replace in block 1
        b1 = block1_parts[0]
        b1 = re.sub(r'(<div class="mgr-track">)(.*?)(</div>\s*</div>\s*</div>)', r'\1\n' + block1_cards + r'                                                                \3', b1, flags=re.DOTALL)
        
        # replace in block 2
        b2 = block1_parts[1]
        b2 = re.sub(r'(<div class="mgr-track">)(.*?)(</div>\s*</div>\s*</div>)', r'\1\n' + block2_cards + r'                                                                \3', b2, count=1, flags=re.DOTALL)
        
        new_content = parts[0] + '<!-- ===== BLOCK 1 ===== -->' + b1 + '<!-- ===== BLOCK 2 ===== -->' + b2
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Success")
    else:
        print("Block 2 not found")
else:
    print("Block 1 not found")

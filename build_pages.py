import os

html = open('index.html', encoding='utf-8').read()
parts1 = html.split('<!-- page content -->')
top = parts1[0] + '<!-- page content -->\n  <div class="page-content">\n'

parts2 = parts1[1].split('<footer')
bottom = '\n  </div>\n  <footer' + parts2[1]

def build_page(filename, title, content):
    modified_top = top.replace('<title>Casa SPA Paraty</title>', f'<title>{title} | Casa SPA Paraty</title>')
    
    active_nav = '<li class=" active">'
    inactive_nav = '<li class="">'
    modified_top = modified_top.replace(active_nav, inactive_nav)
    
    if "about-us.html" in filename:
        modified_top = modified_top.replace('<a href="about-us.html">A Casa</a>', '<a href="about-us.html" style="color:var(--casa-champagne)">A Casa</a>')
    elif "marbella-farms-resort.html" in filename:
        modified_top = modified_top.replace('<a href="marbella-farms-resort.html">Comodidades</a>', '<a href="marbella-farms-resort.html" style="color:var(--casa-champagne)">Comodidades</a>')
    elif "marbella-suites.html" in filename:
        modified_top = modified_top.replace('<a href="marbella-suites.html">Paraty</a>', '<a href="marbella-suites.html" style="color:var(--casa-champagne)">Paraty</a>')
    elif "contact-us.html" in filename:
        modified_top = modified_top.replace('<a href="contact-us.html">Reservar</a>', '<a href="contact-us.html" style="color:var(--casa-champagne)">Reservar</a>')
    elif "gallery.html" in filename:
        modified_top = modified_top.replace('<a href="gallery.html">Galeria</a>', '<a href="gallery.html" style="color:var(--casa-champagne)">Galeria</a>')

    hero_section = f"""
    <!-- Inner Hero -->
    <div class="pbmit-title-bar-wrapper" style="background-image: url('images/index/r1-exterior.webp'); background-size: cover; background-position: center;">
      <div class="container">
        <div class="pbmit-title-bar-content">
          <div class="pbmit-title-bar-content-inner">
            <div class="pbmit-tbar-title">
              <h1 class="pbmit-tbar-title">{title}</h1>
            </div>
          </div>
        </div>
      </div>
    </div>
    """
    
    final_html = modified_top + hero_section + content + bottom
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    with open(filename.replace('.html', '.php'), 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print(f"Generated {filename}")

content_acasa = """
    <section class="section-md">
      <div class="container">
        <div class="row align-items-center">
          <div class="col-lg-6">
            <img src="images/mf-images/sala-02.webp" alt="Sala da Casa SPA" class="img-fluid rounded shadow" style="margin-bottom: 20px;">
            <img src="images/ms-images/quarto2-01.webp" alt="Quarto Casa SPA" class="img-fluid rounded shadow">
          </div>
          <div class="col-lg-6 mt-4 mt-lg-0">
            <h4 class="pbmit-subtitle">A Casa</h4>
            <h2>Seu espa\u00e7o em Paraty</h2>
            <p>Ambientes pensados para compartilhar os dias com conforto e privacidade. Tr\u00eas quartos, \u00e1reas de conviv\u00eancia e tudo o que voc\u00ea precisa para se sentir em casa, s\u00f3 que longe da rotina.</p>
            <p>Um ref\u00fagio particular entre o verde e o mar, concebido para desacelerar, brindar ao p\u00f4r do sol e viver o momento presente com quem se ama.</p>
            <!-- REVISAR: confirmar hist\u00f3ria/conceito da casa com o propriet\u00e1rio -->
            <br>
            <a class="pbmit-btn pbmit-btn-global" href="https://wa.me/5524998144912" target="_blank">
                <span>Consultar Disponibilidade</span>
            </a>
          </div>
        </div>
      </div>
    </section>
"""

content_comodidades = """
    <section class="section-md" style="background: var(--casa-forest-light);">
      <div class="container">
        <div class="text-center mb-5">
            <h4 class="pbmit-subtitle">Conforto</h4>
            <h2>O que a Casa SPA oferece</h2>
        </div>
        <div class="row">
          <div class="col-md-4 mb-4">
            <div class="p-4 rounded" style="background: var(--casa-forest); border: 1px solid rgba(255,255,255,0.05); height: 100%;">
              <i class="fas fa-bed fa-2x mb-3" style="color: var(--casa-champagne);"></i>
              <h4 style="color: var(--casa-ivory);">3 Quartos Climatizados</h4>
              <p style="color: rgba(255,255,255,0.7); font-size: 14px;">Espa\u00e7os tranquilos e confort\u00e1veis com ar-condicionado para um sono reparador, acomodando at\u00e9 6 h\u00f3spedes confortavelmente.</p>
            </div>
          </div>
          <div class="col-md-4 mb-4">
            <div class="p-4 rounded" style="background: var(--casa-forest); border: 1px solid rgba(255,255,255,0.05); height: 100%;">
              <i class="fas fa-water fa-2x mb-3" style="color: var(--casa-champagne);"></i>
              <h4 style="color: var(--casa-ivory);">SPA / Hidromassagem</h4>
              <p style="color: rgba(255,255,255,0.7); font-size: 14px;">Deck privativo com hidromassagem planejada para relaxar, com vista e atmosfera de ref\u00fagio.</p>
            </div>
          </div>
          <div class="col-md-4 mb-4">
            <div class="p-4 rounded" style="background: var(--casa-forest); border: 1px solid rgba(255,255,255,0.05); height: 100%;">
              <i class="fas fa-utensils fa-2x mb-3" style="color: var(--casa-champagne);"></i>
              <h4 style="color: var(--casa-ivory);">Cozinha Equipada</h4>
              <p style="color: rgba(255,255,255,0.7); font-size: 14px;">Estrutura completa para preparar suas pr\u00f3prias refei\u00e7\u00f5es com liberdade e sem pressa.</p>
            </div>
          </div>
          <div class="col-md-4 mb-4">
            <div class="p-4 rounded" style="background: var(--casa-forest); border: 1px solid rgba(255,255,255,0.05); height: 100%;">
              <i class="fas fa-bath fa-2x mb-3" style="color: var(--casa-champagne);"></i>
              <h4 style="color: var(--casa-ivory);">3 Banheiros</h4>
              <p style="color: rgba(255,255,255,0.7); font-size: 14px;">Conforto e conveni\u00eancia garantidos para todos os h\u00f3spedes com ampla disponibilidade de banheiros.</p>
            </div>
          </div>
          <div class="col-md-4 mb-4">
            <div class="p-4 rounded" style="background: var(--casa-forest); border: 1px solid rgba(255,255,255,0.05); height: 100%;">
              <i class="fas fa-tree fa-2x mb-3" style="color: var(--casa-champagne);"></i>
              <h4 style="color: var(--casa-ivory);">\u00c1rea Externa</h4>
              <p style="color: rgba(255,255,255,0.7); font-size: 14px;">Um amplo espa\u00e7o aberto, cercado de verde e natureza, perfeito para reunir os amigos ou a fam\u00edlia ao ar livre.</p>
            </div>
          </div>
          <div class="col-md-4 mb-4">
            <div class="p-4 rounded" style="background: var(--casa-forest); border: 1px solid rgba(255,255,255,0.05); height: 100%;">
              <i class="fas fa-wifi fa-2x mb-3" style="color: var(--casa-champagne);"></i>
              <h4 style="color: var(--casa-ivory);">Wi-Fi de Alta Velocidade</h4>
              <p style="color: rgba(255,255,255,0.7); font-size: 14px;">Conectividade garantida para quem precisa estar online, mesmo longe da cidade.</p>
            </div>
          </div>
        </div>
        
        <div class="mt-5 text-center">
            <img src="images/ms-images/spa-01.webp" alt="SPA" class="img-fluid rounded shadow mx-2" style="max-height: 250px; width: auto; display: inline-block; object-fit: cover;">
            <img src="images/mf-images/cozinha-03.webp" alt="Cozinha" class="img-fluid rounded shadow mx-2" style="max-height: 250px; width: auto; display: inline-block; object-fit: cover;">
            <img src="images/ms-images/quarto1-01.webp" alt="Quarto" class="img-fluid rounded shadow mx-2" style="max-height: 250px; width: auto; display: inline-block; object-fit: cover;">
        </div>
      </div>
    </section>
"""

content_paraty = """
    <section class="section-md">
      <div class="container">
        <div class="row align-items-center">
          <div class="col-lg-6 order-lg-2">
            <img src="images/ms-images/exterior-01.webp" alt="Jardim e \u00c1rea Externa" class="img-fluid rounded shadow">
          </div>
          <div class="col-lg-6 mt-4 mt-lg-0 order-lg-1">
            <h4 class="pbmit-subtitle">A Regi\u00e3o</h4>
            <h2>Descubra Paraty e Corumb\u00ea</h2>
            <p>Paraty \u00e9 um Patrim\u00f4nio Hist\u00f3rico e Natural que preserva s\u00e9culos de hist\u00f3ria em suas ruas de pedra, em meio a um ecossistema exuberante e vivo.</p>
            <ul class="list-unstyled mt-4" style="color: var(--casa-ivory-soft);">
                <li class="mb-3"><i class="fas fa-map-marker-alt" style="color: var(--casa-champagne); width: 24px;"></i> <strong>Centro Hist\u00f3rico:</strong> Cultura, charme, lojas e casar\u00f5es coloniais a poucos minutos.</li>
                <li class="mb-3"><i class="fas fa-umbrella-beach" style="color: var(--casa-champagne); width: 24px;"></i> <strong>Praias de Corumb\u00ea:</strong> \u00c1guas tranquilas e a brisa leve do mar bem perto de voc\u00ea.</li>
                <li class="mb-3"><i class="fas fa-water" style="color: var(--casa-champagne); width: 24px;"></i> <strong>Cachoeiras:</strong> A Mata Atl\u00e2ntica presenteando com quedas d'\u00e1gua cristalinas.</li>
                <li class="mb-3"><i class="fas fa-ship" style="color: var(--casa-champagne); width: 24px;"></i> <strong>Passeios de Barco:</strong> Explore ilhas paradis\u00edacas e recantos inesquec\u00edveis da ba\u00eda.</li>
                <li class="mb-3"><i class="fas fa-utensils" style="color: var(--casa-champagne); width: 24px;"></i> <strong>Gastronomia Local:</strong> Sabores que misturam a tradi\u00e7\u00e3o cai\u00e7ara com a alta culin\u00e1ria.</li>
            </ul>
            <br>
            <a class="pbmit-btn pbmit-btn-global" href="https://wa.me/5524998144912" target="_blank">
                <span>Planeje sua viagem (WhatsApp)</span>
            </a>
          </div>
        </div>
      </div>
    </section>
"""

content_reservar = """
    <section class="section-md">
      <div class="container">
        <div class="text-center mb-5">
            <h4 class="pbmit-subtitle">Entre em Contato</h4>
            <h2>Fa\u00e7a sua Reserva</h2>
            <p>Fale conosco para consultar disponibilidade, tirar d\u00favidas ou garantir seus dias de descanso na Casa SPA Paraty.</p>
            <!-- REVISAR: confirmar pol\u00edtica de check-in/checkout e cancelamento com o propriet\u00e1rio -->
        </div>
        
        <div class="row">
          <div class="col-md-6 mb-4">
             <div class="p-5 rounded shadow" style="background: var(--casa-forest-light); height: 100%;">
                <h3 style="color: var(--casa-ivory); margin-bottom: 30px;">Canais Diretos</h3>
                
                <div class="d-flex align-items-center mb-4">
                    <div style="background: var(--casa-champagne); border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; margin-right: 15px;">
                        <i class="fab fa-whatsapp fa-lg" style="color: #fff;"></i>
                    </div>
                    <div>
                        <span style="display: block; font-size: 13px; color: var(--casa-champagne); text-transform: uppercase;">Atendimento R\u00e1pido</span>
                        <a href="https://wa.me/5524998144912" target="_blank" style="color: var(--casa-ivory); font-size: 20px; font-weight: bold; text-decoration: none;">+55 24 99814-4912</a>
                    </div>
                </div>

                <div class="d-flex align-items-center mb-4">
                    <div style="background: var(--casa-champagne); border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; margin-right: 15px;">
                        <i class="fas fa-envelope fa-lg" style="color: #fff;"></i>
                    </div>
                    <div>
                        <span style="display: block; font-size: 13px; color: var(--casa-champagne); text-transform: uppercase;">E-mail</span>
                        <a href="mailto:marbellagroup8@gmail.com" style="color: var(--casa-ivory); font-size: 20px; font-weight: bold; text-decoration: none;">marbellagroup8@gmail.com</a>
                    </div>
                </div>
                
                <div class="mt-5">
                    <p style="color: var(--casa-ivory-soft);">Para um retorno mais r\u00e1pido, recomendamos o envio de mensagem via WhatsApp.</p>
                    <a class="pbmit-btn pbmit-btn-global w-100 text-center" href="https://wa.me/5524998144912" target="_blank">
                        <span>Chamar no WhatsApp</span>
                    </a>
                </div>
             </div>
          </div>
          
          <div class="col-md-6 mb-4">
             <div class="rounded shadow overflow-hidden" style="height: 100%; min-height: 400px;">
                <iframe src="https://maps.google.com/maps?q=Corumb\u00ea%2C%20Paraty%20-%20RJ&t=&z=13&ie=UTF8&iwloc=&output=embed" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
             </div>
          </div>
        </div>
      </div>
    </section>
"""

build_page('about-us.html', 'A Casa', content_acasa)
build_page('marbella-farms-resort.html', 'Comodidades', content_comodidades)
build_page('marbella-suites.html', 'Paraty', content_paraty)
build_page('contact-us.html', 'Reservar', content_reservar)

content_galeria = open('galeria_content.txt', encoding='utf-8').read()
build_page('gallery.html', 'Galeria', content_galeria)

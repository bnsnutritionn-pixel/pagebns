import re
import os
import json

def get_clean_html_blocks():
    html_path = "e:/LANDING PAGE BNS/index.html"
    if not os.path.exists(html_path):
        print(f"Error: index.html not found at {html_path}")
        return None, None, None, None, None
        
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Extract Head content (metas, fonts, etc. except the style block)
    head_match = re.search(r'<head>(.*?)</head>', content, re.DOTALL)
    head_content = ""
    if head_match:
        # Remove old style block from head to insert it manually
        head_content = head_match.group(1)
        head_content = re.sub(r'<style>.*?</style>', '', head_content, flags=re.DOTALL)
        
    # Extract Style content
    style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    style_content = style_match.group(1) if style_match else ""
    
    # Extract Header HTML and Mobile Menu Drawer
    header_match = re.search(r'(<!-- 1. HEADER FIXO -->.*?<div class="mobile-menu" id="mobileMenu">.*?</ul>\s*</div>)', content, re.DOTALL)
    header_html = header_match.group(1) if header_match else ""
    
    # Extract Footer HTML
    footer_match = re.search(r'(<!-- 13. FOOTER COMPLETO -->.*?<footer class="footer">.*?</footer>)', content, re.DOTALL)
    footer_html = footer_match.group(1) if footer_match else ""
    
    # Extract Scripts at the end of body
    script_match = re.search(r'(<script>.*?</script>)\s*</body>', content, re.DOTALL)
    script_content = script_match.group(1) if script_match else ""
    
    return head_content.strip(), style_content.strip(), header_html.strip(), footer_html.strip(), script_content.strip()

# Detailed metadata for the 9 categories
CATEGORIES_METADATA = [
    {
        "id": "whey",
        "fileName": "categoria-whey.html",
        "title": "Whey Protein",
        "subtitle": "Suplemento Proteico de Alta Pureza",
        "productName": "New Whey Protein Isolado e Concentrado",
        "image": "PRODUTOS/NEW WHEY PROTEIN/WHEY_DE_COCO.webp",
        "flavorOptions": ["Chocolate", "Morango", "Baunilha", "Coco", "Leitinho", "Cookies", "Doce de Leite"],
        "sizeOptions": ["900g"],
        "price": "R$ 416,42",
        "priceOld": "R$ 489,90",
        "priceMonthly": "R$ 395,60",
        "installments": "6x de R$ 69,40",
        "goal": "sua recuperação e ganho muscular",
        "bullets": [
            "100% PROTEÍNA PURA E LIMPA (ISOLADO & CONCENTRADO)",
            "Zero adição de açúcares ou corantes artificiais na fórmula",
            "Matérias-primas importadas de altíssima biodisponibilidade"
        ],
        "activeHighlights": [
            {"val": "24g", "lbl": "de Proteína Pura", "desc": "Filtragem pura para máxima absorção muscular."},
            {"val": "5.5g", "lbl": "de BCAAs", "desc": "Essenciais para ativação da síntese proteica."},
            {"val": "4.3g", "lbl": "de Glutamina", "desc": "Suporte ao sistema imunológico e saúde intestinal."},
            {"val": "0g", "lbl": "Açúcares Adicionados", "desc": "Fórmula clean adoçada apenas com sucralose premium."}
        ],
        "whatIsTitle": "O que é o New Whey Protein?",
        "whatIsText": "Imagine que seu corpo após os treinos é uma obra que precisa de materiais de alta qualidade para se reconstruir. O New Whey Protein entrega os tijolos mais nobres (aminoácidos) de forma imediata e purificada, garantindo que a recuperação e a construção dos seus músculos aconteçam com máxima eficiência e sem desconfortos digestivos.",
        "benefits": [
            {"title": "Ganho de Massa", "desc": "Estimula a síntese proteica e hipertrofia.", "img": "foods/001.webp"},
            {"title": "Recuperação Acelerada", "desc": "Reduz o catabolismo e dores pós-treino.", "img": "foods/002.webp"},
            {"title": "Máxima Absorção", "desc": "Filtragem premium de rápida digestibilidade.", "img": "foods/003.webp"},
            {"title": "Suporte Imunológico", "desc": "Rico em anticorpos e aminoácidos de defesa.", "img": "foods/004.webp"}
        ],
        "scienceTitle": "A ciência da síntese proteica acelerada",
        "scienceDesc": "Estudos clínicos de nutrição esportiva comprovam que o Whey Isolado e Concentrado aumenta a velocidade de regeneração celular das fibras musculares em até 30% em comparação com outras proteínas. A via de sinalização mTOR é ativada de forma quase imediata devido à alta concentração de Leucina.",
        "scienceStats": [
            {"pct": "85%", "lbl": "melhora na fadiga muscular pós-treino"},
            {"pct": "64%", "lbl": "relataram ganho de tônus consistente"},
            {"pct": "40%", "lbl": "de redução em queixas de intolerância"},
            {"pct": "30%", "lbl": "de aumento na taxa de síntese proteica"}
        ],
        "scienceImg": "foods/002.webp",
        "usageText": "Diluir 1 dosador (30g) em 200ml de água gelada ou bebida de sua preferência. Consumir logo após os treinos ou conforme orientação do seu nutricionista.",
        "usageImg": "foods/005.webp",
        "ingredients": "Proteína isolada do soro do leite, proteína concentrada do soro do leite, aroma artificial e edulcorante Sucralose (INS 955). <strong>NÃO CONTÉM GLÚTEN. ALÉRGICOS: CONTÉM DERIVADOS DE LEITE</strong>",
        "portionText": "Porções por embalagem: 30 | Porção: 30g (1 scoop)",
        "nutritionTable": [
            {"item": "Valor energético (kcal)", "qty": "117", "vd": "6%"},
            {"item": "Carboidratos (g)", "qty": "4", "vd": "2%"},
            {"item": "Açúcares totais (g)", "qty": "3,7", "vd": "--"},
            {"item": "Açúcares adicionados (g)", "qty": "0", "vd": "0%"},
            {"item": "Lactose (g)", "qty": "3,5", "vd": "--"},
            {"item": "Galactose (g)", "qty": "0,1", "vd": "--"},
            {"item": "Proteínas (g)", "qty": "24", "vd": "40%"},
            {"item": "Metionina (mg)", "qty": "0,6", "vd": "--"},
            {"item": "Valina (mg)", "qty": "1,2", "vd": "--"},
            {"item": "Histidina (mg)", "qty": "0,4", "vd": "--"},
            {"item": "Triptofano (mg)", "qty": "0,3", "vd": "--"},
            {"item": "Tirosina (mg)", "qty": "0,7", "vd": "--"},
            {"item": "Glicina (mg)", "qty": "0,4", "vd": "--"},
            {"item": "Serina (mg)", "qty": "1,1", "vd": "--"},
            {"item": "Cistina (mg)", "qty": "0,5", "vd": "--"},
            {"item": "Isoleucina (mg)", "qty": "1,2", "vd": "--"},
            {"item": "Leucina (mg)", "qty": "2,2", "vd": "--"},
            {"item": "Alanina (mg)", "qty": "1", "vd": "--"},
            {"item": "Arginina (mg)", "qty": "0,5", "vd": "--"},
            {"item": "Lisina (mg)", "qty": "1,8", "vd": "--"},
            {"item": "Ácido aspártico (mg)", "qty": "2,2", "vd": "--"},
            {"item": "Ácido glutâmico (mg)", "qty": "3,5", "vd": "--"},
            {"item": "Treonina (mg)", "qty": "1,4", "vd": "--"},
            {"item": "Prolina (mg)", "qty": "1,2", "vd": "--"},
            {"item": "Gorduras totais (g)", "qty": "2", "vd": "3%"},
            {"item": "Gorduras saturadas (g)", "qty": "0,9", "vd": "5%"},
            {"item": "Gorduras trans (g)", "qty": "0", "vd": "0%"},
            {"item": "Ômega 6 (g)", "qty": "0,5", "vd": "--"},
            {"item": "Ômega 9 (g)", "qty": "0,3", "vd": "2%"},
            {"item": "Fibras alimentares (g)", "qty": "0,7", "vd": "3%"},
            {"item": "Sódio (mg)", "qty": "65", "vd": "3%"},
            {"item": "Cálcio (mg)", "qty": "221", "vd": "22%"},
            {"item": "Ferro (mg)", "qty": "0,22", "vd": "1%"},
            {"item": "Potássio (mg)", "qty": "137", "vd": "4%"},
            {"item": "Zinco (mg)", "qty": "1,4", "vd": "13%"}
        ],
        "faqs": [
            {"q": "Qual a diferença do Whey Isolado para o Concentrado?", "a": "O Whey Isolado passa por processos extras de filtragem que eliminam quase totalmente a gordura e a lactose, oferecendo uma concentração proteica muito maior. O Concentrado retém frações benéficas do soro, com excelente absorção."},
            {"q": "Quem tem intolerância à lactose pode consumir?", "a": "Por possuir proteína concentrada em sua composição, pessoas com intolerância grave podem apresentar sintomas. Recomendamos orientação médica ou nutricional."},
            {"q": "Qual o melhor horário para consumir?", "a": "Geralmente no pós-treino imediato para aproveitar a janela metabólica de recuperação, ou no café da manhã para quebrar o jejum."},
            {"q": "Pode ser misturado com alimentos ou receitas?", "a": "Sim, ele é ideal para misturar em panquecas saudáveis, bolos fit, iogurtes ou shakes com frutas, pois possui ótima estabilidade térmica."},
            {"q": "Ajuda a emagrecer?", "a": "Sim. As proteínas aumentam a liberação de hormônios da saciedade, reduzindo o apetite e ajudando a preservar a massa magra durante dietas de perda de peso."}
        ]
    },
    {
        "id": "pre-treino",
        "fileName": "categoria-pre-treino.html",
        "title": "Pré-Treino",
        "subtitle": "Foco Imbatível e Energia Explosiva",
        "productName": "True Dragon GTX",
        "image": "PRODUTOS/DRAGON GTX/DRAGON_FRUTAS.webp",
        "flavorOptions": ["Frutas Vermelhas", "Lemon Burst", "Tropical Ice"],
        "sizeOptions": ["300g"],
        "price": "R$ 220,92",
        "priceOld": "R$ 259,90",
        "priceMonthly": "R$ 207,92",
        "installments": "6x de R$ 36,82",
        "goal": "o aumento de performance e foco absoluto",
        "bullets": [
            "AÇÃO TAMPONANTE EXTREMA COM BETA-ALANINA",
            "Mais força explosiva e vasodilatação prolongada",
            "Concentração, foco cognitivo e energia de queima limpa"
        ],
        "activeHighlights": [
            {"val": "3.000mg", "lbl": "de Beta-Alanina", "desc": "Ação tamponante que retarda a fadiga e queimação."},
            {"val": "1.000mg", "lbl": "de L-Arginina", "desc": "Potente vasodilatador para maior PUMP e fluxo."},
            {"val": "200mg", "lbl": "de Cafeína Anidra", "desc": "Foco mental e estimulação do estado de alerta."},
            {"val": "500mg", "lbl": "de Taurina", "desc": "Suporte cognitivo e regulação da contração muscular."}
        ],
        "whatIsTitle": "O que é o True Dragon GTX?",
        "whatIsText": "Pense no seu treino como uma corrida de alta velocidade onde o cansaço é o semáforo vermelho. O True Dragon GTX é a faísca que acende o motor do seu corpo, abrindo as vias de circulação (vasodilatação) e limpando o caminho da fadiga para que você mantenha o acelerador pressionado até a última repetição.",
        "benefits": [
            {"title": "Força Explosiva", "desc": "Mais potência em treinos de alta carga.", "img": "foods/002.webp"},
            {"title": "Foco Cognitivo", "desc": "Conexão mente-músculo aguçada.", "img": "foods/003.webp"},
            {"title": "Resistência Muscular", "desc": "Treinos mais longos sem perda de rendimento.", "img": "foods/004.webp"},
            {"title": "Vasodilatação Extrema", "desc": "PUMP estendido e transporte de nutrientes.", "img": "foods/005.webp"}
        ],
        "scienceTitle": "A ciência do tamponamento muscular",
        "scienceDesc": "A Beta-Alanina eleva os estoques intramusculares de carnosina, que neutraliza a acidez muscular (íons H+) produzida no treino intenso. A combinação com a Cafeína otimiza o uso de gorduras como combustível primário, poupando o glicogênio.",
        "scienceStats": [
            {"pct": "92%", "lbl": "relataram aumento imediato de energia"},
            {"pct": "74%", "lbl": "sentiram melhora na fadiga tardia"},
            {"pct": "50%", "lbl": "de aumento na vascularização visível"},
            {"pct": "30%", "lbl": "de ganho no número total de repetições"}
        ],
        "scienceImg": "foods/004.webp",
        "usageText": "Diluir 1 dosador (15g) em 250ml de água gelada. Consumir de 15 a 30 minutos antes do início do seu treino físico.",
        "usageImg": "foods/006.webp",
        "ingredients": "Beta-alanina, L-arginina, taurina, cafeína anidra, acidulante ácido cítrico, aromatizantes naturais e edulcorantes naturais stévia. NÃO CONTÉM GLÚTEN.",
        "nutritionTable": [
            {"item": "Valor Energético", "qty": "12 kcal", "vd": "1%"},
            {"item": "Beta-Alanina", "qty": "3000 mg", "vd": "--"},
            {"item": "L-Arginina", "qty": "1000 mg", "vd": "--"},
            {"item": "Taurina", "qty": "500 mg", "vd": "--"},
            {"item": "Cafeína", "qty": "200 mg", "vd": "--"}
        ],
        "faqs": [
            {"q": "Por que o pré-treino causa formigamento?", "a": "O formigamento (parestesia) é causado pela Beta-Alanina. Trata-se de uma reação periférica normal, inofensiva e temporária."},
            {"q": "Posso tomar o pré-treino à noite?", "a": "Evite tomar em treinos noturnos muito próximos do horário de dormir (cerca de 6h antes), pois a cafeína pode afetar a qualidade do sono."},
            {"q": "Posso tomar todos os dias?", "a": "Sim, a Beta-Alanina necessita de uso diário acumulativo para saturação máxima da carnosina muscular."},
            {"q": "Contém substâncias proibidas?", "a": "Não, nossa fórmula é 100% limpa, regulamentada e segura para atletas profissionais e amadores."},
            {"q": "Pode ser misturado com outros suplementos?", "a": "Sim, ele pode ser tomado em conjunto com Creatina ou Glutamina sem qualquer interferência negativa."}
        ]
    },
    {
        "id": "creatina",
        "fileName": "categoria-creatina.html",
        "title": "Creatina",
        "subtitle": "Força e Potência Muscular Pura",
        "productName": "True Creatine 100% Pure",
        "image": "PRODUTOS/CREATINA DARK/CREA_DARK.webp",
        "flavorOptions": ["Pura (Sem Sabor)"],
        "sizeOptions": ["300g", "150g"],
        "price": "R$ 93,42",
        "priceOld": "R$ 109,90",
        "priceMonthly": "R$ 87,92",
        "installments": "6x de R$ 15,57",
        "goal": "o ganho de força e volume muscular rápido",
        "bullets": [
            "CREATINA MONOHIDRATADA 100% PURA",
            "Rápida ressíntese de ATP e maior torque muscular",
            "Excelente solubilidade livre de aditivos ou sabores"
        ],
        "activeHighlights": [
            {"val": "3.000mg", "lbl": "de Creatina Pura", "desc": "Creatina monohidratada premium sem adição de misturas."},
            {"val": "100%", "lbl": "Monohidratada", "desc": "A forma mais estudada e comprovada cientificamente."},
            {"val": "Zero", "lbl": "Sabor e Aditivos", "desc": "Ideal para misturar no seu whey ou suco sem alterar sabor."},
            {"val": "Micronizada", "lbl": "Fácil Solubilidade", "desc": "Partículas menores que facilitam a diluição no copo."}
        ],
        "whatIsTitle": "O que é a Creatina BNS+?",
        "whatIsText": "Imagine suas células musculares como pequenas baterias de energia instantânea. Quando você faz um effort muito intenso (como levantar um peso pesado), essa bateria descarrega rapidamente. A Creatina é o carregador ultra rápido que devolve a energia celular de forma quase instantânea, permitindo repetições extras.",
        "benefits": [
            {"title": "Força Muscular", "desc": "Aumenta o torque e a potência nos treinos pesados.", "img": "foods/003.webp"},
            {"title": "Volume e Hidratação", "desc": "Atrai água para as células, volumizando os músculos.", "img": "foods/004.webp"},
            {"title": "Ressíntese de ATP", "desc": "Acelera a recuperação de energia entre as séries.", "img": "foods/005.webp"},
            {"title": "Suporte Cognitivo", "desc": "Ajuda no fornecimento de energia para o cérebro.", "img": "foods/006.webp"}
        ],
        "scienceTitle": "O suplemento número 1 em evidências",
        "scienceDesc": "A Creatina aumenta os estoques musculares de fosfocreatina, que atua doando fosfato para recarregar o ADP de volta a ATP. Esse processo é fundamental para manter treinos de alta intensidade e adiar a fadiga neuromuscular.",
        "scienceStats": [
            {"pct": "95%", "lbl": "relataram ganho perceptível de força"},
            {"pct": "80%", "lbl": "observaram volume muscular preenchido"},
            {"pct": "40%", "lbl": "de aceleração no repouso entre séries"},
            {"pct": "20%", "lbl": "de suporte metabólico a nível mitocondrial"}
        ],
        "scienceImg": "foods/003.webp",
        "usageText": "Diluir 1 dosador (3g) em 150ml de água ou bebida de sua preferência. Consumir diariamente de forma contínua, inclusive em dias sem treino.",
        "usageImg": "foods/007.webp",
        "ingredients": "Creatina monohidratada pura. NÃO CONTÉM GLÚTEN.",
        "nutritionTable": [
            {"item": "Valor Energético", "qty": "0 kcal", "vd": "0%"},
            {"item": "Creatina", "qty": "3000 mg", "vd": "--"}
        ],
        "faqs": [
            {"q": "A creatina causa retenção de líquidos?", "a": "Sim, mas de forma intramuscular (dentro do músculo), o que é ótimo para o volume e hidratação das fibras. Ela não causa inchaço subcutâneo (retenção retida na pele)."},
            {"q": "Preciso fazer a fase de saturação?", "a": "Não é estritamente necessário. Tomar 3g por dia de forma contínua enche os estoques musculares em aproximadamente 25 a 30 dias."},
            {"q": "Posso tomar nos dias em que não treino?", "a": "Sim! A creatina funciona de forma acumulativa nos músculos. Por isso, deve ser consumida todos os dias, incluindo finais de semana."},
            {"q": "Causa problemas nos rins?", "a": "Não. Em indivíduos saudáveis e na dosagem recomendada, dezenas de estudos já comprovaram a total segurança da creatina sem qualquer dano renal."},
            {"q": "Qual o melhor horário para consumir?", "a": "Qualquer horário. A absorção é levemente otimizada quando consumida junto com fontes de carboidratos."}
        ]
    },
    {
        "id": "vitaminas",
        "fileName": "categoria-vitaminas.html",
        "title": "Vitaminas",
        "subtitle": "Multivitamínico de A a Z Completo",
        "productName": "True Multivitamínico A-Z",
        "image": "formula-card/POLIVITAMÍNICO.webp",
        "flavorOptions": ["Cápsulas (Sem Sabor)"],
        "sizeOptions": ["60 Cápsulas"],
        "price": "R$ 76,42",
        "priceOld": "R$ 89,90",
        "priceMonthly": "R$ 71,92",
        "installments": "6x de R$ 12,74",
        "goal": "o suporte imunológico e vitalidade diária",
        "bullets": [
            "23 NUTRIENTES COM MINERAIS QUELATOS",
            "Máxima biodisponibilidade e imunidade blindada",
            "Cápsulas vegetais cleans e sem aditivos químicos"
        ],
        "activeHighlights": [
            {"val": "23", "lbl": "Nutrientes", "desc": "Vitaminas e minerais de alta biodisponibilidade por porção."},
            {"val": "100%", "lbl": "Biodisponível", "desc": "Minerais quelatos que garantem excelente absorção intestinal."},
            {"val": "Zero", "lbl": "Açúcares", "desc": "Cápsulas puras sem corantes artificiais ou aditivos nocivos."},
            {"val": "1 Cápsula", "lbl": "ao Dia", "desc": "Praticidade para preencher lacunas da sua dieta."}
        ],
        "whatIsTitle": "O que é o True Multivitamínico?",
        "whatIsText": "Pense no seu corpo como um relógio mecânico sofisticado com dezenas de pequenas engrenagens. Se faltar óleo em uma delas, todo o mecanismo começa a trabalhar com dificuldade. As vitaminas e minerais são os lubrificantes essenciais que garantem que cada função metabólica, imunológica e hormonal funcione perfeitamente.",
        "benefits": [
            {"title": "Imunidade Forte", "desc": "Rico em Vitaminas C, D, Zinco e Selênio.", "img": "foods/004.webp"},
            {"title": "Energia e Disposição", "desc": "Complexo B completo que apoia o metabolismo.", "img": "foods/005.webp"},
            {"title": "Ação Antioxidante", "desc": "Protege as células contra radicais livres.", "img": "foods/006.webp"},
            {"title": "Cabelo, Pele e Unha", "desc": "Vitaminas fundamentais para manutenção celular.", "img": "foods/007.webp"}
        ],
        "scienceTitle": "Minerais Quelatos: A revolução da absorção",
        "scienceDesc": "Os minerais comuns costumam competir por canais de absorção e podem causar irritação gástrica. Nossos minerais são quelatos (ligados a aminoácidos), permitindo que sejam assimilados pelo corpo como alimento, triplicando a taxa de absorção.",
        "scienceStats": [
            {"pct": "98%", "lbl": "de satisfação em disposição relatada"},
            {"pct": "80%", "lbl": "observaram melhor imunidade no ano"},
            {"pct": "3x", "lbl": "mais absorção com minerais quelatos"},
            {"pct": "100%", "lbl": "da dose diária recomendada de vit. D"}
        ],
        "scienceImg": "foods/003.webp",
        "usageText": "Ingerir 1 cápsula ao dia, preferencialmente junto com uma das principais refeições (almoço ou jantar) para facilitar a absorção das vitaminas lipossolúveis.",
        "usageImg": "foods/001.webp",
        "ingredients": "Mix de vitaminas e minerais (vitaminas A, C, D, E, complexo B, zinco quelato, selênio, magnésio), antiumectante dióxido de silício e cápsula vegetal. NÃO CONTÉM GLÚTEN.",
        "nutritionTable": [
            {"item": "Vitamina A", "qty": "600 mcg", "vd": "100%"},
            {"item": "Vitamina C", "qty": "100 mg", "vd": "100%"},
            {"item": "Vitamina D3", "qty": "2000 UI", "vd": "100%"},
            {"item": "Zinco Quelato", "qty": "15 mg", "vd": "136%"},
            {"item": "Complexo B", "qty": "100% IDR", "vd": "100%"}
        ],
        "faqs": [
            {"q": "Por que devo tomar com as refeições?", "a": "Algumas vitaminas (como A, D, E, K) necessitam de gorduras da alimentação para serem digeridas e absorvidas adequadamente pelo intestino."},
            {"q": "Qual o melhor horário para tomar?", "a": "No almoço é o horário ideal pela abundância de alimentos e melhor digestão diurna."},
            {"q": "Mulheres grávidas podem consumir?", "a": "Gestantes e lactantes devem sempre consultar o obstetra ou nutricionista antes de utilizar qualquer suplementação."},
            {"q": "Engorda ou abre o apetite?", "a": "Não, o multivitamínico possui valor calórico zero e não estimula o ganho de peso."},
            {"q": "Pode ser tomado junto com Whey?", "a": "Sim, não há nenhuma contraindicação ou interferência entre proteínas e vitaminas."}
        ]
    },
    {
        "id": "omega-3",
        "fileName": "categoria-omega-3.html",
        "title": "Ômega 3",
        "subtitle": "Saúde Cardiovascular e Cognitiva",
        "productName": "True Ômega 3 Premium",
        "image": "generic-product.webp",
        "flavorOptions": ["Cápsulas (Sem Sabor)"],
        "sizeOptions": ["90 Cápsulas"],
        "price": "R$ 169,92",
        "priceOld": "R$ 199,90",
        "priceMonthly": "R$ 159,92",
        "installments": "6x de R$ 28,32",
        "goal": "a proteção do coração e performance cerebral",
        "bullets": [
            "360mg EPA / 240mg DHA DE ALTA CONCENTRAÇÃO",
            "Destilação molecular ultra purificada livre de metais",
            "Auxilia no foco mental e manutenção de triglicerídeos"
        ],
        "activeHighlights": [
            {"val": "1000mg", "lbl": "de Óleo de Peixe", "desc": "Alta concentração de ácidos graxos essenciais por cápsula."},
            {"val": "360mg", "lbl": "EPA / 240mg DHA", "desc": "Proporção ideal recomendada por cardiologistas."},
            {"val": "Livre", "lbl": "Metais Pesados", "desc": "Certificação internacional de pureza e sustentabilidade."},
            {"val": "Vitamina E", "lbl": "Antioxidante", "desc": "Evita a oxidação precoce do óleo dentro da cápsula."}
        ],
        "whatIsTitle": "O que é o True Ômega 3?",
        "whatIsText": "Pense nas suas artérias e cérebro como estradas e circuitos elétricos que precisam estar limpos e flexíveis. O Ômega 3 atua como um agente de manutenção: ele ajuda a lubrificar e reduzir a inflamação nas artérias e melhora a conexão rápida dos neurônios, promovendo clareza mental e longevidade.",
        "benefits": [
            {"title": "Saúde do Coração", "desc": "Auxilia na manutenção de triglicerídeos saudáveis.", "img": "foods/004.webp"},
            {"title": "Performance Cerebral", "desc": "Suporte à memória, foco e prevenção cognitiva.", "img": "foods/005.webp"},
            {"title": "Ação Anti-inflamatória", "desc": "Reduz inflamações articulares e celulares.", "img": "foods/006.webp"},
            {"title": "Saúde dos Olhos", "desc": "DHA apoia a saúde da retina e combate ressecamento.", "img": "foods/007.webp"}
        ],
        "scienceTitle": "Pureza certificada livre de metais",
        "scienceDesc": "A pureza do óleo de peixe é o fator mais crítico. Nosso Ômega 3 passa por destilação molecular que filtra e elimina metais pesados (como mercúrio) e PCBs, garantindo um óleo extremamente limpo e seguro.",
        "scienceStats": [
            {"pct": "90%", "lbl": "de redução de dores articulares leves"},
            {"pct": "75%", "lbl": "relataram melhor foco no trabalho"},
            {"pct": "100%", "lbl": "livre de retrogosto de peixe indesejado"},
            {"pct": "0%", "lbl": "de metais pesados ou impurezas"}
        ],
        "scienceImg": "foods/005.webp",
        "usageText": "Ingerir 2 cápsulas ao dia, preferencialmente logo após as refeições principais (almoço e jantar) para otimizar a digestibilidade.",
        "usageImg": "foods/001.webp",
        "ingredients": "Óleo de peixe concentrado com alta dose de EPA e DHA, acetato de DL-alfa-tocoferol (Vitamina E) e cápsula gelatinosa. NÃO CONTÉM GLÚTEN. ALÉRGICOS: CONTÉM DERIVADOS DE PEIXE.",
        "nutritionTable": [
            {"item": "Óleo de Peixe", "qty": "2000 mg", "vd": "--"},
            {"item": "EPA", "qty": "720 mg", "vd": "--"},
            {"item": "DHA", "qty": "480 mg", "vd": "--"},
            {"item": "Vitamina E", "qty": "10 mg", "vd": "67%"}
        ],
        "faqs": [
            {"q": "Dá refluxo ou gosto de peixe?", "a": "Nossas cápsulas são gastrorresistentes e o óleo é altamente purificado, minimizando refluxo ou gosto residual de peixe."},
            {"q": "Qual a diferença de EPA e DHA?", "a": "O EPA atua principalmente na saúde cardiovascular e inflamações gerais. O DHA é o componente estrutural do cérebro e retina, apoiando cognição e visão."},
            {"q": "É seguro tomar grávida?", "a": "Extremamente benéfico para o desenvolvimento cerebral do bebê, mas o consumo deve ser recomendado pelo obstetra."},
            {"q": "Crianças podem tomar?", "a": "Sim, sob orientação pediátrica, pois o ômega 3 auxilia no desenvolvimento cognitivo infantil."},
            {"q": "Como armazenar?", "a": "Manter bem fechado em local fresco e ao abrigo da luz para evitar a oxidação dos ácidos graxos."}
        ]
    },
    {
        "id": "colageno",
        "fileName": "categoria-colageno.html",
        "title": "Colágeno",
        "subtitle": "Renovação e Firmeza da Pele",
        "productName": "True Colágeno Hidrolisado",
        "image": "generic-product.webp",
        "flavorOptions": ["Frutas Tropicais", "Sem Sabor"],
        "sizeOptions": ["300g"],
        "price": "R$ 152,92",
        "priceOld": "R$ 179,90",
        "priceMonthly": "R$ 143,92",
        "installments": "6x de R$ 25,48",
        "goal": "a beleza, elasticidade e firmeza da sua pele",
        "bullets": [
            "PEPTÍDEOS BIOATIVOS VERISOL® EXCLUSIVOS",
            "Ácido Hialurônico e Vitamina C para preenchimento",
            "Aumenta a elasticidade da derme em poucas semanas"
        ],
        "activeHighlights": [
            {"val": "9g", "lbl": "de Colágeno", "desc": "Peptídeos bioativos de alta absorção de colágeno hidrolisado."},
            {"val": "Verisol®", "lbl": "Tecnologia", "desc": "Peptídeos específicos cientificamente comprovados para a pele."},
            {"val": "100%", "lbl": "Vitamina C", "desc": "Necessária para que o corpo consiga sintetizar o colágeno."},
            {"val": "Ácido Hialurônico", "lbl": "Hidratação", "desc": "Retém água nas camadas profundas, preenchendo a pele."}
        ],
        "whatIsTitle": "O que é o True Colágeno?",
        "whatIsText": "Pense na sua pele como um colchão inflável. Com o tempo, o ar (colágeno) vai diminuindo e a superfície começa a apresentar dobras e rugas. O True Colágeno Hidrolisado entrega os peptídeos específicos que agem como 'molas de reforço', devolvendo a sustentação, elasticidade e hidratação profunda à pele.",
        "benefits": [
            {"title": "Redução de Rugas", "desc": "Suaviza linhas de expressão e aumenta a firmeza.", "img": "foods/004.webp"},
            {"title": "Unhas Fortes", "desc": "Diminui a descamação e quebra de unhas.", "img": "foods/005.webp"},
            {"title": "Cabelo Resistente", "desc": "Nutrientes para fios mais grossos e saudáveis.", "img": "foods/006.webp"},
            {"title": "Hidratação Profunda", "desc": "Retém a umidade natural, reduzindo o ressecamento.", "img": "foods/007.webp"}
        ],
        "scienceTitle": "A eficácia comprovada de Verisol®",
        "scienceDesc": "Os peptídeos Verisol® conseguem driblar a digestão gástrica comum, chegando intactos à derme, onde estimulam os fibroblastos a produzir colágeno novo. Estudos mostram redução de rugas em apenas 4 semanas.",
        "scienceStats": [
            {"pct": "32%", "lbl": "de redução nas linhas de expressão"},
            {"pct": "65%", "lbl": "de aumento na concentração de colágeno"},
            {"pct": "18%", "lbl": "de aumento na elasticidade da derme"},
            {"pct": "42%", "lbl": "de redução de quebras de unhas"}
        ],
        "scienceImg": "foods/006.webp",
        "usageText": "Dissolver 1 dosador (10g) em 150ml de água ou suco gelado. Consumir preferencialmente à noite, antes de dormir, ou pela manhã em jejum.",
        "usageImg": "foods/002.webp",
        "ingredients": "Peptídeos de colágeno hidrolisado (Verisol®), ácido hialurônico, vitamina C, acidulante ácido cítrico, aromatizante natural e stevia. NÃO CONTÉM GLÚTEN.",
        "nutritionTable": [
            {"item": "Valor Energético", "qty": "35 kcal", "vd": "2%"},
            {"item": "Proteínas", "qty": "8,5 g", "vd": "11%"},
            {"item": "Vitamina C", "qty": "45 mg", "vd": "100%"},
            {"item": "Ácido Hialurônico", "qty": "80 mg", "vd": "--"}
        ],
        "faqs": [
            {"q": "A partir de qual idade é recomendado?", "a": "A produção natural de colágeno começa a declinar a partir dos 25 anos. Essa é a idade perfeita para iniciar a suplementação preventiva."},
            {"q": "Qual a diferença do hidrolisado simples para o Verisol?", "a": "O hidrolisado simples é quebrado em aminoácidos gerais. O Verisol® é quebrado em peptídeos específicos que o corpo direciona exclusivamente para a pele e unhas."},
            {"q": "Tem açúcar ou carboidratos?", "a": "Não, nossa fórmula é livre de açúcares, adoçada apenas com stevia e muito baixa em calorias."},
            {"q": "Quanto tempo para ver resultados?", "a": "Estudos clínicos mostram benefícios visíveis na pele e unhas entre 4 a 8 semanas de uso diário contínuo."},
            {"q": "Posso misturar no café?", "a": "Sim, na versão sem sabor ele pode ser misturado em chás, sucos ou café sem perder as propriedades bioativas."}
        ]
    },
    {
        "id": "true-foods",
        "fileName": "categoria-true-foods.html",
        "title": "BNS Foods",
        "subtitle": "Nutrição Limpa e Funcional",
        "productName": "True Morning Coffee",
        "image": "foods/001.webp",
        "flavorOptions": ["Café Premium Blend"],
        "sizeOptions": ["30 Sachês"],
        "price": "R$ 135,92",
        "priceOld": "R$ 159,90",
        "priceMonthly": "R$ 127,92",
        "installments": "6x de R$ 22,65",
        "goal": "sua energia limpa e foco matinal",
        "bullets": [
            "FÓRMULA TERMOGÊNICA COM TCM C8/C10",
            "Café solúvel arábica 100% de origem nobre",
            "Foco estável e saciedade linear sem picos glicêmicos"
        ],
        "activeHighlights": [
            {"val": "100%", "lbl": "Arábica Premium", "desc": "Café de origem nobre e sabor marcante incomparável."},
            {"val": "TCM C8/C10", "lbl": "Energia Rápida", "desc": "Gorduras saudáveis absorvidas instantaneamente pelo cérebro."},
            {"val": "Sem Açúcar", "lbl": "Low Carb", "desc": "Ideal para regimes low-carb e jejum metabólico."},
            {"val": "Solúvel", "lbl": "Prático e Rápido", "desc": "Mistura homogênea na xícara quente em 5 segundos."}
        ],
        "whatIsTitle": "O que é o True Morning Coffee?",
        "whatIsText": "Pense no seu início de dia como o decolar de um avião. Se você abastece com combustível comum (carboidratos simples), tem uma explosão rápida de energia que dura pouco e te faz cair logo em seguida. O True Morning entrega energia limpa de queima lenta (TCM), que mantém o foco e disposição estáveis por horas, sem picos e quedas bruscas.",
        "benefits": [
            {"title": "Foco Prolongado", "desc": "Combinação de Cafeína e TCM para cognição.", "img": "foods/001.webp"},
            {"title": "Saciedade Estendida", "desc": "Gorduras nobres que controlam o apetite matinal.", "img": "foods/002.webp"},
            {"title": "Queima de Gordura", "desc": "Estimula o estado de cetose de forma natural.", "img": "foods/003.webp"},
            {"title": "Praticidade Total", "desc": "Monodoses em sachês para levar a qualquer lugar.", "img": "foods/004.webp"}
        ],
        "scienceTitle": "A sinergia entre Cafeína e TCM",
        "scienceDesc": "Os Triglicerídeos de Cadeia Média (TCM) são convertidos rapidamente em cetonas no fígado, servindo de combustível alternativo super limpo para o cérebro. Aliado à Cafeína, estimulam a performance cognitiva e aumentam a termogênese basal.",
        "scienceStats": [
            {"pct": "96%", "lbl": "sentiram clareza mental prolongada"},
            {"pct": "84%", "lbl": "relataram redução de fome matinal"},
            {"pct": "4h", "lbl": "de foco e produtividade sem letargia"},
            {"pct": "0g", "lbl": "de picos de insulina gerados"}
        ],
        "scienceImg": "foods/001.webp",
        "usageText": "Diluir 1 sachê (10g) em 100ml de água quente. Misturar bem até a dissolução completa. Consumir pela manhã ou no início da tarde.",
        "usageImg": "foods/005.webp",
        "ingredients": "Café solúvel arábica, triglicerídeos de cadeia média (TCM), cacau em pó, canela em pó, adoçante natural stevia. NÃO CONTÉM GLÚTEN.",
        "nutritionTable": [
            {"item": "Valor Energético", "qty": "48 kcal", "vd": "2%"},
            {"item": "Carboidratos", "qty": "1,0 g", "vd": "0%"},
            {"item": "Gorduras Totais", "qty": "4,2 g", "vd": "8%"},
            {"item": "Cafeína", "qty": "80 mg", "vd": "--"}
        ],
        "faqs": [
            {"q": "Quebra o jejum metabólico?", "a": "O TCM não eleva a glicose ou a insulina no sangue. Portanto, o True Morning não quebra o jejum lipídico e auxilia na queima de gordura."},
            {"q": "Como ele dá energia sem açúcar?", "a": "Através do TCM (gorduras saudáveis de cadeia média), que são assimiliadas pelo fígado e convertidas em energia imediata para o cérebro."},
            {"q": "Qual a diferença para o café comum?", "a": "O café comum estimula rapidamente mas pode gerar tremores e crash. O True Morning garante energia linear e duradoura sem picos de adrenalina."},
            {"q": "Pode ser misturado com leite?", "a": "Sim, fica excelente misturado em leite vegetal quente (amêndoas, coco), ganhando cremosidade extra."},
            {"q": "Qual a frequência de consumo?", "a": "Pode ser consumido diariamente, preferencialmente logo ao acordar ou como pré-treino funcional."}
        ]
    },
    {
        "id": "emagrecedores",
        "fileName": "categoria-emagrecedores.html",
        "title": "Emagrecedores",
        "subtitle": "Metabolismo Ativo e Definição",
        "productName": "True L-Carnitine Liquid",
        "image": "generic-product.webp",
        "flavorOptions": ["Limão Refrescante"],
        "sizeOptions": ["480ml"],
        "price": "R$ 110,42",
        "priceOld": "R$ 129,90",
        "priceMonthly": "R$ 103,92",
        "installments": "6x de R$ 18,40",
        "goal": "o controle de peso e queima de gordura",
        "bullets": [
            "2000mg DE L-CARNITINA LÍQUIDA PURA",
            "Cofator essencial para transporte e queima de gorduras",
            "Enriquecido com Cromo para redução do desejo por doces"
        ],
        "activeHighlights": [
            {"val": "2000mg", "lbl": "de L-Carnitina", "desc": "Concentração ideal líquida para queima de gordura acelerada."},
            {"val": "Zero", "lbl": "Calorias", "desc": "Suporte metabólico sem carboidratos ou açúcares na fórmula."},
            {"val": "Líquida", "lbl": "Rápida Ação", "desc": "Absorção imediata e biodisponibilidade a nível celular."},
            {"val": "Cromo", "lbl": "Adicionado", "desc": "Auxilia na modulação do apetite e controle de doces."}
        ],
        "whatIsTitle": "O que é a L-Carnitina Líquida?",
        "whatIsText": "Pense no seu corpo como um forno e nas gorduras estocadas como lenhas que estão fora dele. A L-Carnitina é o transportador que carrega cada lenha para dentro da fornalha (mitocôndria), permitindo que a gordura seja queimada e transformada em energia ativa durante o seu treino.",
        "benefits": [
            {"title": "Queima de Gordura", "desc": "Usa a gordura corporal como combustível preferencial.", "img": "foods/002.webp"},
            {"title": "Definição Muscular", "desc": "Auxilia na preservação de massa magra no processo.", "img": "foods/003.webp"},
            {"title": "Energia Extra", "desc": "Aproveita estoques lipídicos para dar gás aos treinos.", "img": "foods/004.webp"},
            {"title": "Controle de Doces", "desc": "Cromo ajuda a estabilizar a glicose no sangue.", "img": "foods/005.webp"}
        ],
        "scienceTitle": "A oxidação de gorduras na mitocôndria",
        "scienceDesc": "Os ácidos graxos de cadeia longa não conseguem penetrar a membrana mitocondrial de forma autônoma. A L-Carnitina atua como a enzima chave de transporte (shuttle), sendo o cofator limitante na oxidação de gordura corporal.",
        "scienceStats": [
            {"pct": "88%", "lbl": "de melhora na sudorese e queima calórica"},
            {"pct": "70%", "lbl": "relataram redução no desejo por doces"},
            {"pct": "2000mg", "lbl": "de dosagem clínica máxima recomendada"},
            {"pct": "0%", "lbl": "de açúcares ou corantes artificiais"}
        ],
        "scienceImg": "foods/004.webp",
        "usageText": "Consumir 1 colher de sopa (15ml) preferencialmente em jejum pela manhã ou de 20 a 30 minutos antes de iniciar o treino físico.",
        "usageImg": "foods/006.webp",
        "ingredients": "Água purificada, L-carnitina, picolinato de cromo, acidulante ácido cítrico, aromatizante natural de limão e stevia. NÃO CONTÉM GLÚTEN.",
        "nutritionTable": [
            {"item": "Valor Energético", "qty": "0 kcal", "vd": "0%"},
            {"item": "L-Carnitina", "qty": "2000 mg", "vd": "--"},
            {"item": "Cromo", "qty": "35 mcg", "vd": "100%"}
        ],
        "faqs": [
            {"q": "Dá taquicardia ou agitação?", "a": "Não. Diferente de termogênicos com cafeína, a L-Carnitina não é estimulante do SNC. Ela age puramente a nível celular de transporte de energia."},
            {"q": "Preciso treinar para ter resultados?", "a": "Sim. Os benefícios de transporte de gordura para o forno celular são amplamente potencializados com a realização de exercícios físicos."},
            {"q": "Pode ser associada com pré-treino?", "a": "Sim, a combinação de L-Carnitina com pré-treinos estimulantes potencializa os resultados de definição muscular."},
            {"q": "Qual o sabor?", "a": "Possui um sabor suave e levemente azedo de limão natural."},
            {"q": "Deve ser mantido na geladeira?", "a": "Sim, recomendamos armazenar na geladeira após aberto para manter o frescor do produto."}
        ]
    },
    {
        "id": "vitamina-d",
        "fileName": "categoria-vitamina-d.html",
        "title": "Vitamina D",
        "subtitle": "Saúde Imune e Óssea Avançada",
        "productName": "True Vitamina D3 + K2",
        "image": "formula-card/VITAMINA D3.webp",
        "flavorOptions": ["Cápsulas (Sem Sabor)"],
        "sizeOptions": ["60 Cápsulas"],
        "price": "R$ 84,92",
        "priceOld": "R$ 99,90",
        "priceMonthly": "R$ 79,92",
        "installments": "6x de R$ 14,15",
        "goal": "sua saúde óssea e reforço imunológico",
        "bullets": [
            "2000 UI DE VITAMINA D3 + 120mcg VITAMINA K2",
            "Veiculado em óleo de coco MCT de alta absorção",
            "Direciona o cálcio aos dentes e ossos evitando artérias"
        ],
        "activeHighlights": [
            {"val": "2.000 UI", "lbl": "de Vitamina D3", "desc": "Dosagem ideal diária recomendada por endocrinologistas."},
            {"val": "120 mcg", "lbl": "de Vitamina K2", "desc": "K2 direciona o cálcio para os ossos, evitando artérias."},
            {"val": "MCT Coco", "lbl": "Como Veículo", "desc": "Óleo carreador que otimiza a absorção da D3 (lipossolúvel)."},
            {"val": "Cápsula", "lbl": "Gel Premium", "desc": "Fácil deglutição e rápida liberação no estômago."}
        ],
        "whatIsTitle": "O que é a Vitamina D3 + K2?",
        "whatIsText": "Pense no cálcio do seu corpo como uma encomenda muito importante e na Vitamina D3 como o carteiro que a recolhe. Sem a Vitamina K2, a encomenda pode ser entregue no endereço errado (artérias e rins). A combinação perfeita D3 + K2 garante que o cálcio vá diretamente para os locais corretos: seus ossos e dentes.",
        "benefits": [
            {"title": "Saúde Óssea", "desc": "Otimiza a fixação e densidade do cálcio nos ossos.", "img": "foods/004.webp"},
            {"title": "Imunidade Reforçada", "desc": "Modula células de defesa contra infecções.", "img": "foods/005.webp"},
            {"title": "Saúde das Artérias", "desc": "K2 evita a calcificação de vasos sanguíneos.", "img": "foods/006.webp"},
            {"title": "Suporte Hormonal", "desc": "Apoia a síntese de testosterona e equilíbrio endócrino.", "img": "foods/007.webp"}
        ],
        "scienceTitle": "A indispensável sinergia D3 + K2",
        "scienceDesc": "A absorção de cálcio depende estritamente da presença de níveis circulantes ideais de Vitamina D3. No entanto, a ativação da osteocalcina (proteína que liga o cálcio à matriz óssea) e a inibição da calcificação arterial dependem da Vitamina K2 (MK-7).",
        "scienceStats": [
            {"pct": "95%", "lbl": "relataram melhora nos exames de sangue"},
            {"pct": "88%", "lbl": "de melhor fixação de cálcio ósseo"},
            {"pct": "100%", "lbl": "da dose clínica com veículo em MCT óleo"},
            {"pct": "0%", "lbl": "de calcificação arterial indesejada"}
        ],
        "scienceImg": "foods/005.webp",
        "usageText": "Ingerir 1 cápsula ao dia, preferencialmente junto com uma refeição que contenha gorduras saudáveis (azeite, abacate, ovos) para absorção ideal.",
        "usageImg": "foods/003.webp",
        "ingredients": "Óleo de coco de veículo (MCT), colecalciferol (Vitamina D3), menaquinona-7 (Vitamina K2), cápsula de gelatina. NÃO CONTÉM GLÚTEN.",
        "nutritionTable": [
            {"item": "Vitamina D3", "qty": "50 mcg (2000 UI)", "vd": "250%"},
            {"item": "Vitamina K2", "qty": "120 mcg", "vd": "100%"},
            {"item": "MCT (Óleo Carreador)", "qty": "250 mg", "vd": "--"}
        ],
        "faqs": [
            {"q": "Por que tomar Vitamina D com Vitamina K2?", "a": "A D3 aumenta a absorção do cálcio. A K2 atua direcionando esse cálcio para os ossos, impedindo que ele se acumule nas paredes das artérias, prevenindo problemas cardiovasculares."},
            {"q": "Qual o melhor horário para tomar?", "a": "Durante a maior refeição do dia (como almoço), pois a D3 é lipossolúvel (absorvida com gordura)."},
            {"q": "Ajuda no sistema imunológico?", "a": "Sim, a Vitamina D é na verdade um hormônio regulador que age em quase todas as células imunes, aumentando as defesas do organismo."},
            {"q": "Posso tomar em jejum?", "a": "Pode, pois nossa fórmula já contém MCT (óleo de coco) como carreador, mas a absorção é ainda melhor se ingerido com alimentos."},
            {"q": "É seguro tomar doses diárias de 2000 UI?", "a": "Sim, é uma dosagem de manutenção totalmente segura e recomendada para a maioria dos adultos com deficiência comum de sol."}
        ]
    },
    {
        "id": "coenzima-q10",
        "fileName": "categoria-coenzima-q10.html",
        "title": "Coenzima Q10",
        "subtitle": "Energia Celular e Proteção Antioxidante",
        "productName": "True Coenzima Q10 - 60 comprimidos",
        "image": "formula-card/COENZIMA_Q10.webp",
        "flavorOptions": ["Comprimidos (Sem Sabor)"],
        "sizeOptions": ["60 Comprimidos"],
        "price": "R$ 94,88",
        "priceOld": "R$ 109,90",
        "priceMonthly": "R$ 89,90",
        "installments": "6x de R$ 15,81",
        "goal": "a produção de energia mitocondrial e longevidade",
        "bullets": [
            "100MG DE COENZIMA Q10 (UBIQUINONA) POR DOSE",
            "Ação antioxidante contra o envelhecimento celular",
            "Melhora do rendimento físico e saúde cardiovascular"
        ],
        "activeHighlights": [
            {"val": "100mg", "lbl": "de Coenzima Q10", "desc": "Concentração ideal para ativação das mitocôndrias celular."},
            {"val": "100%", "lbl": "Antioxidante", "desc": "Combate aos radicais livres e proteção cardiovascular."},
            {"val": "Zero", "lbl": "Açúcares/Glúten", "desc": "Comprimidos puros livres de aditivos alergênicos."},
            {"val": "Uso Diário", "lbl": "Praticidade", "desc": "Apenas 1 comprimido ao dia para o suporte necessário."}
        ],
        "whatIsTitle": "O que é a Coenzima Q10?",
        "whatIsText": "A Coenzima Q10 (CoQ10) é um nutriente naturalmente presente em nossas células, concentrado nas mitocôndrias – as usinas de energia do corpo. Pense na CoQ10 como a vela de ignição de um motor: sem ela, a célula não consegue converter os alimentos em energia celular (ATP). Com o passar dos anos, nossa produção natural de CoQ10 cai drasticamente, tornando a suplementação vital para manter a disposição e combater o envelhecimento precoce.",
        "benefits": [
            {"title": "Energia Mitocondrial", "desc": "Apoia a síntese de ATP celular nas mitocôndrias.", "img": "foods/005.webp"},
            {"title": "Saúde do Coração", "desc": "Essencial para os tecidos cardíacos que demandam alta energia.", "img": "foods/004.webp"},
            {"title": "Ação Antioxidante", "desc": "Combate radicais livres gerados pelo estresse e treinos.", "img": "foods/003.webp"},
            {"title": "Performance Física", "desc": "Reduz o estresse oxidativo muscular durante os exercícios.", "img": "foods/002.webp"}
        ],
        "scienceTitle": "A Ciência por trás da Ubiquinona e Vitalidade",
        "scienceDesc": "A Coenzima Q10 desempenha um papel duplo crucial: atua na cadeia de transporte de elétrons mitocondrial e funciona como um poderoso antioxidante lipossolúvel. Estudos mostram que a suplementação diária de CoQ10 reduz o dano muscular induzido pelo exercício e melhora a eficiência contrátil do miocárdio, otimizando o consumo de oxigênio pelas células.",
        "scienceStats": [
            {"pct": "95%", "lbl": "de absorção celular comprovada"},
            {"pct": "88%", "lbl": "de melhora na fadiga crônica relatada"},
            {"pct": "100mg", "lbl": "dose ideal recomendada por cardiologistas"},
            {"pct": "Zero", "lbl": "efeitos colaterais ou toxicidade registrada"}
        ],
        "scienceImg": "foods/001.webp",
        "usageText": "Ingerir 1 comprimido ao dia, preferencialmente junto com uma refeição rica em gorduras saudáveis (como café da manhã ou almoço) para maximizar a absorção desse nutriente lipossolúvel.",
        "usageImg": "foods/006.webp",
        "ingredients": "Coenzima Q10, amido, antiumectante dióxido de silício e cápsula de gelatina. NÃO CONTÉM GLÚTEN.",
        "portionText": "Porção: 1 comprimido ao dia",
        "nutritionTable": [
            {"item": "Coenzima Q10", "qty": "100 mg", "vd": "100%"},
            {"item": "Valor Energético", "qty": "0 kcal", "vd": "0%"}
        ],
        "faqs": [
            {"q": "Para que serve a Coenzima Q10?", "a": "Ela serve principalmente para aumentar a produção de energia celular (ATP), combater os radicais livres, melhorar a saúde do coração e reduzir a fadiga física e mental."},
            {"q": "Qual o melhor horário para tomar?", "a": "Nas principais refeições que contenham alguma fonte de gordura, pois a CoQ10 é lipossolúvel e necessita delas para ser absorvida com eficácia."},
            {"q": "Pessoas de qualquer idade podem tomar?", "a": "Geralmente é indicada para adultos, especialmente após os 30 anos, quando a produção endógena começa a cair. Recomenda-se orientação de médico ou nutricionista."},
            {"q": "Pode ser combinada com outros suplementos?", "a": "Sim, combina perfeitamente com ômega-3 (que inclusive ajuda em sua absorção) e com multivitamínicos."}
        ]
    }
]

def generate_all_pages():
    # Load price overrides if they exist
    prices_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prices.json")
    if os.path.exists(prices_path):
        try:
            with open(prices_path, "r", encoding="utf-8") as f:
                price_overrides = json.load(f)
            for cat in CATEGORIES_METADATA:
                cat_id = cat["id"]
                if cat_id in price_overrides:
                    cat.update(price_overrides[cat_id])
            print("Loaded price overrides from prices.json successfully.")
        except Exception as e:
            print(f"Warning: Failed to load price overrides from prices.json: {e}")

    head_content, style_content, header_html, footer_html, script_content = get_clean_html_blocks()
    if not head_content:
        return
        
    print(f"Loaded index.html blocks successfully.")
    
    # Adjust relative links in header for subpages
    header_html = header_html.replace('href="#bestSellers"', 'href="index.html#bestSellers"')
    header_html = header_html.replace('href="#productHero"', 'href="index.html#productHero"')
    header_html = header_html.replace('href="#trueFoods"', 'href="index.html#trueFoods"')
    header_html = header_html.replace('href="#catalogSection"', 'href="index.html#catalogSection"')
    header_html = header_html.replace('href="#categories"', 'href="index.html#categories"')
    header_html = header_html.replace('href="#" class="logo"', 'href="index.html" class="logo"')
    header_html = header_html.replace('href="#"', 'href="index.html"')
    
    DEFAULT_CUSTOM_CSS = """
    /* ----------------------------------------------------
       ESTILOS EXCLUSIVOS DA PÁGINA DE CATEGORIA/PRODUTO
       ---------------------------------------------------- */
    .product-detail-section {
      padding: 60px 0;
      background-color: var(--bg-white);
    }
    
    .product-detail-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 40px;
    }
    
    @media (min-width: 1024px) {
      .product-detail-grid {
        grid-template-columns: 1.1fr 0.9fr;
        gap: 60px;
      }
    }
    
    /* Galeria de Imagens */
    .product-gallery {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    
    .main-image-wrapper {
      background-color: var(--bg-beige);
      border-radius: 24px;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 40px;
      border: 1px solid rgba(0,0,0,0.02);
      height: 480px;
      position: relative;
    }
    
    .main-image-wrapper img {
      max-width: 85%;
      max-height: 85%;
      object-fit: contain;
      filter: drop-shadow(0 15px 30px rgba(0,0,0,0.05));
    }
    
    .product-gold-badge {
      position: absolute;
      top: 24px;
      left: 24px;
      width: 86px;
      height: 86px;
      background-color: #D2A267;
      border-radius: 50%;
      color: #FFFFFF;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      font-size: 0.6rem;
      font-weight: 700;
      line-height: 1.25;
      padding: 10px;
      box-shadow: 0 6px 15px rgba(210, 162, 103, 0.3);
      z-index: 10;
      border: 2px dashed rgba(255,255,255,0.4);
      text-transform: uppercase;
    }
    
    .thumbnails-grid {
      display: flex;
      gap: 12px;
      justify-content: flex-start;
    }
    
    .thumbnail-btn {
      width: 76px;
      height: 76px;
      border-radius: 12px;
      background-color: var(--bg-light);
      border: 2px solid transparent;
      padding: 8px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: var(--transition-smooth);
    }
    
    .thumbnail-btn.active, .thumbnail-btn:hover {
      border-color: #5D9C3F;
      background-color: var(--bg-white);
    }
    
    .thumbnail-btn img {
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
    }
    
    /* Lado de Compra */
    .product-buy-info {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      text-align: left;
    }
    
    .product-breadcrumbs {
      font-size: 0.75rem;
      color: var(--text-light);
      margin-bottom: 10px;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      font-weight: 600;
    }
    
    .product-breadcrumbs a:hover {
      color: var(--primary);
    }
    
    .product-brand-tag {
      font-family: var(--font-heading);
      font-size: 0.82rem;
      font-weight: 700;
      color: #D2A267;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 4px;
    }
    
    .product-detail-title {
      font-family: var(--font-serif);
      font-size: 2.5rem;
      font-weight: 700;
      color: #3C302F;
      line-height: 1.2;
      margin-bottom: 12px;
    }
    
    .product-rating-row {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 24px;
      font-size: 0.9rem;
      font-weight: 600;
      color: var(--text-muted);
    }
    
    .rating-stars {
      display: flex;
      gap: 2px;
      color: #FFB300;
    }
    
    .rating-stars svg {
      width: 16px;
      height: 16px;
      fill: currentColor;
    }
    
    /* Opções Pills */
    .option-group {
      margin-bottom: 24px;
      width: 100%;
    }
    
    .option-label {
      font-size: 0.8rem;
      font-weight: 700;
      color: #3C302F;
      text-transform: uppercase;
      margin-bottom: 10px;
      display: block;
      letter-spacing: 0.5px;
    }
    
    .options-buttons {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }
    
    .option-btn {
      padding: 10px 24px;
      border-radius: 50px;
      background-color: #FFFFFF;
      border: 1px solid #E5E0DA;
      font-size: 0.85rem;
      font-weight: 600;
      color: #3C302F;
      cursor: pointer;
      transition: var(--transition-smooth);
    }
    
    .option-btn.active, .option-btn:hover {
      border-color: #5D9C3F;
      color: #5D9C3F;
      background-color: #F4F8F1;
    }
    
    /* Box de Compra/Recorrência */
    .price-card-box {
      width: 100%;
      background-color: #FFFFFF;
      border-radius: 20px;
      border: 1px solid #E5E0DA;
      padding: 20px;
      margin-bottom: 24px;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    
    .purchase-type-row {
      display: flex;
      align-items: center;
      gap: 12px;
      cursor: pointer;
      padding: 14px 16px;
      border-radius: 12px;
      border: 1px solid #E5E0DA;
      transition: var(--transition-smooth);
    }
    
    .purchase-type-row.active {
      border-color: #5D9C3F;
      background-color: #F4F8F1;
    }
    
    .purchase-radio {
      appearance: none;
      width: 20px;
      height: 20px;
      border: 2px solid #BCB0A3;
      border-radius: 50%;
      outline: none;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      position: relative;
      background-color: #FFFFFF;
    }
    
    .purchase-type-row.active .purchase-radio {
      border-color: #5D9C3F;
    }
    
    .purchase-radio:checked::after {
      content: '';
      width: 10px;
      height: 10px;
      background-color: #5D9C3F;
      border-radius: 50%;
      display: block;
    }
    
    .purchase-details {
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }
    
    .purchase-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: #3C302F;
    }
    
    .purchase-price {
      font-size: 1.35rem;
      font-weight: 800;
      color: #1A1A1A;
      margin-top: 4px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    
    .purchase-price span {
      text-decoration: line-through;
      font-size: 0.95rem;
      color: var(--text-light);
      font-weight: 500;
    }
    
    .subscription-badge {
      display: inline-flex;
      background-color: #E8F5E9;
      color: var(--accent-green);
      font-size: 0.68rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 4px;
      margin-left: 8px;
      text-transform: uppercase;
    }
    
    .subscription-options {
      margin-top: 8px;
      padding-left: 32px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      transition: all 0.3s ease;
    }
    
    .frequency-selector {
      width: 100%;
      height: 42px;
      border-radius: 8px;
      border: 1px solid #E5E0DA;
      padding: 0 12px;
      font-size: 0.85rem;
      font-weight: 600;
      background-color: var(--bg-white);
      color: #3C302F;
    }
    
    /* Action Row: Quantidade e Carrinho */
    .action-row {
      display: flex;
      gap: 16px;
      width: 100%;
      align-items: center;
    }
    
    .quantity-selector {
      display: flex;
      align-items: center;
      border: 1px solid #E5E0DA;
      border-radius: 50px;
      height: 52px;
      padding: 4px;
      background-color: #FFFFFF;
      flex-shrink: 0;
    }
    
    .qty-btn {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.2rem;
      font-weight: 600;
      color: #3C302F;
      cursor: pointer;
      transition: var(--transition-smooth);
    }
    
    .qty-btn:hover {
      background-color: #FAF6F0;
    }
    
    .qty-input {
      width: 40px;
      text-align: center;
      font-size: 1rem;
      font-weight: 700;
      color: #3C302F;
      border: none;
      background: transparent;
      outline: none;
    }
    
    .btn-add-to-cart {
      flex-grow: 1;
      height: 52px;
      background-color: #5D9C3F;
      color: #FFFFFF;
      border-radius: 50px;
      font-size: 0.95rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 15px rgba(93, 156, 63, 0.2);
      transition: var(--transition-smooth);
    }
    
    .btn-add-to-cart:hover {
      background-color: #4C8233;
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(93, 156, 63, 0.3);
    }
    
    /* 2. Allied Section */
    .allied-section {
      background-color: #FAF6F0;
      padding: 80px 0 0 0;
      text-align: center;
    }
    
    .allied-badge {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 46px;
      height: 26px;
      background-color: #D2A267;
      color: #FFFFFF;
      font-size: 0.75rem;
      font-weight: 700;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 20px;
    }
    
    .allied-title {
      font-family: var(--font-serif);
      font-size: 2.6rem;
      color: #3C302F;
      font-weight: 700;
      margin-bottom: 40px;
      max-width: 800px;
      margin-left: auto;
      margin-right: auto;
      line-height: 1.25;
    }
    
    .allied-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 30px;
      max-width: 1100px;
      margin: 0 auto 50px auto;
    }
    
    @media (min-width: 768px) {
      .allied-grid {
        grid-template-columns: repeat(4, 1fr);
        gap: 20px;
      }
    }
    
    .allied-col {
      position: relative;
      padding: 0 16px;
    }
    
    @media (min-width: 768px) {
      .allied-col:not(:last-child)::after {
        content: '';
        position: absolute;
        right: -10px;
        top: 10%;
        height: 80%;
        width: 1px;
        background-color: #E5E0DA;
      }
    }
    
    .allied-val {
      font-size: 2.6rem;
      font-weight: 800;
      color: #3C302F;
      display: block;
      margin-bottom: 8px;
      line-height: 1;
    }
    
    .allied-lbl {
      font-size: 1rem;
      font-weight: 700;
      color: #3C302F;
      display: block;
      margin-bottom: 8px;
    }
    
    .allied-desc {
      font-size: 0.85rem;
      color: #7C7063;
      line-height: 1.45;
    }
    
    .allied-banner {
      width: 100%;
      height: 480px;
      overflow: hidden;
    }
    
    .allied-banner img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    
    /* Yellow gold action button */
    .btn-buy-now-accent {
      background-color: #FFB300;
      color: #231F20;
      padding: 16px 40px;
      border-radius: 50px;
      font-size: 0.9rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 15px rgba(255, 179, 0, 0.2);
      transition: var(--transition-smooth);
    }
    
    .btn-buy-now-accent:hover {
      background-color: #FFA000;
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(255, 179, 0, 0.3);
    }
    
    /* 3. Canister Split Section */
    .canister-split-section {
      position: relative;
      padding: 80px 0;
      text-align: center;
      background: linear-gradient(to bottom, #FAF6F0 42%, #8C7D70 42%);
    }
    
    .split-title {
      font-family: var(--font-serif);
      font-size: 2.8rem;
      color: #3C302F;
      font-weight: 700;
      margin-bottom: 40px;
      line-height: 1.2;
    }
    
    .split-canister-wrapper {
      display: flex;
      justify-content: center;
      margin-bottom: 40px;
      position: relative;
    }
    
    .split-canister-wrapper img {
      max-height: 380px;
      object-fit: contain;
      filter: drop-shadow(0 20px 35px rgba(0,0,0,0.12));
    }
    
    .split-bullets {
      display: flex;
      flex-direction: column;
      gap: 16px;
      max-width: 600px;
      margin: 0 auto 40px auto;
      color: #FFFFFF;
      font-weight: 600;
      font-size: 1.15rem;
      text-align: center;
      align-items: center;
    }
    
    .split-bullet-item {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    
    .split-bullet-item svg {
      width: 20px;
      height: 20px;
      fill: #FFB300;
      flex-shrink: 0;
    }
    
    /* 4. Como ele ajuda */
    .help-section {
      background-color: #FCFAF7;
      padding: 80px 0;
      text-align: center;
    }
    
    .help-title {
      font-family: var(--font-serif);
      font-size: 2.6rem;
      color: #3C302F;
      font-weight: 700;
      margin-bottom: 50px;
    }
    
    .help-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 30px;
      max-width: 1200px;
      margin: 0 auto 50px auto;
    }
    
    @media (min-width: 768px) {
      .help-grid {
        grid-template-columns: repeat(3, 1fr);
      }
    }
    
    .help-card {
      background-color: #FFFFFF;
      border-radius: 20px;
      overflow: hidden;
      box-shadow: 0 10px 30px rgba(0,0,0,0.03);
      border: 1px solid rgba(0,0,0,0.02);
      display: flex;
      flex-direction: column;
      text-align: left;
    }
    
    .help-card-img {
      height: 240px;
      overflow: hidden;
    }
    
    .help-card-img img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    
    .help-card-content {
      padding: 24px;
      display: flex;
      flex-direction: column;
    }
    
    .help-card-bar {
      height: 3px;
      width: 40px;
      background-color: #FFB300;
      margin-bottom: 16px;
    }
    
    .help-card-title {
      font-size: 1.2rem;
      font-weight: 700;
      color: #3C302F;
      margin-bottom: 10px;
    }
    
    .help-card-desc {
      font-size: 0.9rem;
      color: #7C7063;
      line-height: 1.5;
    }
    
    /* 5. Ciência e Estatísticas */
    .science-section-ref {
      background-color: #FFFFFF;
      padding: 80px 0;
      text-align: center;
    }
    
    .science-title-ref {
      font-family: var(--font-serif);
      font-size: 2.6rem;
      color: #3C302F;
      font-weight: 700;
      margin-bottom: 16px;
      max-width: 800px;
      margin-left: auto;
      margin-right: auto;
      line-height: 1.25;
    }
    
    .science-desc-ref {
      font-size: 1rem;
      color: #7C7063;
      max-width: 750px;
      margin: 0 auto 50px auto;
      line-height: 1.6;
    }
    
    .science-stats-row-ref {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 40px;
      margin-bottom: 50px;
    }
    
    .stat-circle-box {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 12px;
      flex: 1 1 180px;
      text-align: center;
    }
    
    .stat-circle-wrapper {
      position: relative;
      width: 120px;
      height: 120px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    
    .stat-circle-svg {
      width: 120px;
      height: 120px;
      transform: rotate(-90deg);
    }
    
    .stat-circle-bg {
      fill: none;
      stroke: #EADBC8;
      stroke-width: 8;
    }
    
    .stat-circle-val {
      fill: none;
      stroke: var(--primary);
      stroke-width: 8;
      stroke-linecap: round;
      stroke-dasharray: 314;
      stroke-dashoffset: calc(314 - (314 * var(--pct-val)) / 100);
      transition: stroke-dashoffset 1s ease-out;
    }
    
    .stat-circle-inner-txt {
      position: absolute;
      font-family: var(--font-heading);
      font-size: 1.65rem;
      font-weight: 800;
      color: #3C302F;
    }
    
    .stat-circle-lbl-ref {
      font-size: 0.88rem;
      font-weight: 700;
      color: #3C302F;
      line-height: 1.35;
      max-width: 160px;
    }
    
    .science-img-row-ref {
      display: grid;
      grid-template-columns: 1fr;
      gap: 20px;
      max-width: 1200px;
      margin: 50px auto 0 auto;
    }
    
    @media (min-width: 768px) {
      .science-img-row-ref {
        grid-template-columns: repeat(3, 1fr);
      }
    }
    
    .science-img-card-ref {
      height: 260px;
      border-radius: 20px;
      overflow: hidden;
      box-shadow: 0 4px 15px rgba(0,0,0,0.03);
    }
    
    .science-img-card-ref img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    
    /* 6. Sugestão de consumo */
    .usage-section-full {
      position: relative;
      padding: 100px 0;
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
      display: flex;
      align-items: center;
      min-height: 480px;
    }
    
    .usage-section-full::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0,0,0,0.15);
      z-index: 1;
    }
    
    .usage-card-overlay {
      position: relative;
      z-index: 2;
      background-color: #FAF6F0;
      padding: 40px;
      border-radius: 24px;
      max-width: 480px;
      box-shadow: 0 15px 35px rgba(0,0,0,0.08);
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      text-align: left;
    }
    
    .usage-title {
      font-family: var(--font-serif);
      font-size: 2.2rem;
      color: #3C302F;
      font-weight: 700;
      margin-bottom: 20px;
    }
    
    .usage-text {
      font-size: 1.05rem;
      color: #7C7063;
      line-height: 1.6;
    }
    
    @media (max-width: 767px) {
      .usage-section-full {
        padding: 40px 0;
        background-image: none !important;
        background-color: var(--bg-beige-dark);
        min-height: auto;
      }
      .usage-section-full::before {
        display: none;
      }
      .usage-card-overlay {
        max-width: 100%;
        padding: 24px;
        box-shadow: none;
        background: transparent;
      }
    }
    
    /* 7. Testimonials */
    .recommends-dark {
      background-color: #231F20;
      padding: 80px 0;
      color: #FFFFFF;
      text-align: center;
    }
    
    .recommends-title-dark {
      font-family: var(--font-serif);
      font-size: 2.6rem;
      color: #FFFFFF;
      font-weight: 700;
      margin-bottom: 50px;
    }
    
    .recommends-grid-ref {
      display: grid;
      grid-template-columns: 1fr;
      gap: 24px;
      max-width: 1200px;
      margin: 0 auto 50px auto;
    }
    
    @media (min-width: 768px) {
      .recommends-grid-ref {
        grid-template-columns: repeat(3, 1fr);
        align-items: stretch;
      }
    }
    
    .recommend-card-ref {
      border-radius: 24px;
      overflow: hidden;
      height: 380px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }
    
    .recommend-card-ref.img-card img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    
    .recommend-card-ref.quote-card {
      background-color: #FFB300;
      color: #231F20;
      padding: 40px 30px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      gap: 16px;
    }
    
    .quote-stars-ref {
      font-size: 1.5rem;
      color: #231F20;
      letter-spacing: 2px;
    }
    
    .quote-text-ref {
      font-family: var(--font-serif);
      font-style: italic;
      font-size: 1.25rem;
      font-weight: 600;
      line-height: 1.5;
    }
    
    .quote-author-ref {
      font-size: 0.85rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
    }
    
    /* 8. FAQ Accordion Split */
    .faq-section-ref {
      padding: 80px 0;
      background-color: #FFFFFF;
    }
    
    .faq-grid-ref {
      display: grid;
      grid-template-columns: 1fr;
      gap: 40px;
      max-width: 1200px;
      margin: 0 auto;
    }
    
    @media (min-width: 1024px) {
      .faq-grid-ref {
        grid-template-columns: 0.8fr 1.2fr;
        gap: 60px;
      }
    }
    
    .faq-left-card-ref {
      position: relative;
      border-radius: 24px;
      overflow: hidden;
      height: 480px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.05);
      display: none;
    }
    
    @media (min-width: 1024px) {
      .faq-left-card-ref {
        display: block;
      }
    }
    
    .faq-left-card-ref img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    
    .faq-left-card-ref::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: linear-gradient(transparent 40%, rgba(0,0,0,0.7));
      z-index: 1;
    }
    
    .faq-left-overlay-ref {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      padding: 40px;
      color: #FFFFFF;
      text-align: left;
      z-index: 2;
    }
    
    .faq-left-title-ref {
      font-family: var(--font-serif);
      font-size: 2.2rem;
      color: #FFFFFF;
      font-weight: 700;
      margin-bottom: 8px;
    }
    
    .faq-left-desc-ref {
      font-size: 0.95rem;
      opacity: 0.9;
      line-height: 1.5;
    }
    
    .faq-right-accordion-ref {
      text-align: left;
    }
    
    .faq-title-mobile-ref {
      font-family: var(--font-serif);
      font-size: 2.2rem;
      color: #3C302F;
      font-weight: 700;
      margin-bottom: 30px;
      text-align: center;
    }
    
    @media (min-width: 1024px) {
      .faq-title-mobile-ref {
        display: none;
      }
    }
    
    .faq-container {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    
    .faq-item {
      border: 1px solid #EAEAEA;
      border-radius: 12px;
      overflow: hidden;
      background-color: var(--bg-white);
    }
    
    .faq-header {
      padding: 18px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      user-select: none;
      background-color: var(--bg-white);
      transition: background-color 0.2s ease;
    }
    
    .faq-header:hover {
      background-color: var(--bg-light);
    }
    
    .faq-q {
      font-size: 1rem;
      font-weight: 700;
      color: #3C302F;
    }
    
    .faq-icon-arrow {
      width: 20px;
      height: 20px;
      color: #5C5248;
      transition: transform 0.3s ease;
      flex-shrink: 0;
    }
    
    .faq-item.active .faq-icon-arrow {
      transform: rotate(180deg);
    }
    
    .faq-body {
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .faq-content {
      padding: 0 24px 20px 24px;
      font-size: 0.95rem;
      color: var(--text-muted);
      line-height: 1.5;
    }
    
    /* 9 & 10. Ingredientes e Tabela */
    .nutrition-section-ref {
      background-color: #FCFAF7;
      padding: 80px 0;
    }
    
    .nutrition-grid-ref {
      display: grid;
      grid-template-columns: 1fr;
      gap: 40px;
      max-width: 1200px;
      margin: 0 auto;
    }
    
    @media (min-width: 1024px) {
      .nutrition-grid-ref {
        grid-template-columns: 1fr 1fr;
        gap: 60px;
      }
    }
    
    .nutrition-left-ref {
      text-align: left;
    }
    
    .nutrition-title-ref {
      font-family: var(--font-serif);
      font-size: 2.4rem;
      color: #3C302F;
      font-weight: 700;
      margin-bottom: 20px;
    }
    
    .ingredients-desc {
      font-size: 0.95rem;
      color: #5C5248;
      line-height: 1.6;
      margin-bottom: 24px;
    }
    
    .warnings-card-ref {
      background-color: #FFFFFF;
      border-radius: 12px;
      border-left: 4px solid #D27547;
      padding: 20px;
      font-size: 0.85rem;
      color: #7C7063;
      line-height: 1.5;
      margin-bottom: 30px;
    }
    
    .nutrition-left-img-ref {
      margin-top: 30px;
      border-radius: 20px;
      overflow: hidden;
      height: 280px;
      box-shadow: 0 6px 20px rgba(0,0,0,0.03);
    }
    
    .nutrition-left-img-ref img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    
    .nutrition-right-card-ref {
      background-color: #FFFFFF;
      border-radius: 24px;
      padding: 32px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.03);
      border: 1px solid rgba(0,0,0,0.02);
      text-align: left;
    }
    
    .table-header {
      font-family: var(--font-heading);
      font-size: 1.25rem;
      font-weight: 800;
      color: #3C302F;
      margin-bottom: 6px;
    }
    
    .table-portion {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 16px;
      border-bottom: 2px solid #3C302F;
      padding-bottom: 8px;
    }
    
    .nutri-table {
      width: 100%;
      border-collapse: collapse;
    }
    
    .nutri-table th {
      text-align: left;
      font-size: 0.85rem;
      font-weight: 700;
      color: #3C302F;
      padding: 8px 0;
      border-bottom: 1px solid #EAEAEA;
    }
    
    .nutri-table td {
      padding: 10px 0;
      border-bottom: 1px solid #F0F0F0;
      font-size: 0.88rem;
      color: #5C5248;
    }
    
    .nutri-table tr:last-child td {
      border-bottom: none;
    }
    
    .nutri-table td.bold {
      font-weight: 700;
      color: #3C302F;
    }
    
    .nutri-table td.right {
      text-align: right;
    }
    
    /* 11. Avaliações */
    .reviews-list-section {
      background-color: var(--bg-white);
      padding: 80px 0;
    }
    
    .reviews-list-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 40px;
    }
    
    @media (min-width: 1024px) {
      .reviews-list-grid {
        grid-template-columns: 0.7fr 1.3fr;
        gap: 60px;
      }
    }
    
    .reviews-score-card {
      background-color: #FAF5F0;
      border-radius: 24px;
      padding: 30px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 16px;
      text-align: center;
      box-shadow: 0 4px 15px rgba(0,0,0,0.01);
      height: fit-content;
    }
    
    .score-num {
      font-family: var(--font-heading);
      font-size: 4rem;
      font-weight: 800;
      color: #3C302F;
      line-height: 1;
    }
    
    .score-stars {
      display: flex;
      gap: 4px;
      color: #FFB300;
    }
    
    .score-stars svg {
      width: 24px;
      height: 24px;
      fill: currentColor;
    }
    
    .score-count {
      font-size: 0.9rem;
      color: var(--text-muted);
      font-weight: 600;
    }
    
    .score-recommend {
      font-size: 0.85rem;
      color: var(--accent-green);
      font-weight: 700;
      background-color: var(--accent-green-light);
      padding: 6px 16px;
      border-radius: 50px;
    }
    
    .reviews-items-col {
      display: flex;
      flex-direction: column;
      gap: 24px;
      text-align: left;
    }
    
    .review-item-row {
      border-bottom: 1px solid #F0F0F0;
      padding-bottom: 24px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    
    .review-item-row:last-child {
      border-bottom: none;
      padding-bottom: 0;
    }
    
    .review-meta {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.85rem;
      color: var(--text-light);
    }
    
    .review-author {
      font-weight: 700;
      color: #3C302F;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    
    .verified-badge {
      font-size: 0.7rem;
      font-weight: 700;
      color: var(--accent-green);
      background-color: var(--accent-green-light);
      padding: 2px 6px;
      border-radius: 4px;
      text-transform: uppercase;
    }
    
    .review-item-title {
      font-size: 1.1rem;
      font-weight: 800;
      color: #3C302F;
    }
    
    .review-item-text {
      font-size: 0.92rem;
      color: var(--text-muted);
      line-height: 1.5;
    }
    
    .review-recommend-status {
      font-size: 0.82rem;
      color: var(--accent-green);
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 4px;
    }
    """
    
    WHEY_CUSTOM_CSS = """
/* Active category nav link highlight */
    .nav-links a.active-category {
      font-weight: 700 !important;
      color: #3C302F !important;
      border-bottom: 2px solid #FF6D00;
      padding-bottom: 4px;
    }

    /* WhatsApp Floating Button styling */
    .whatsapp-float {
      position: fixed;
      bottom: 85px;
      right: 20px;
      background-color: #25d366;
      color: white;
      border-radius: 50%;
      width: 56px;
      height: 56px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 2px 2px 10px rgba(0,0,0,0.25);
      z-index: 999;
      transition: transform 0.2s ease;
    }
    .whatsapp-float:active {
      transform: scale(0.9);
    }

    /* Cashback Badge styling */
    .cashback-badge {
      position: absolute;
      bottom: 24px;
      right: 24px;
      background-color: #FF6D00;
      color: #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 8px 16px;
      border-radius: 10px;
      font-size: 0.82rem;
      font-weight: 700;
      box-shadow: 0 4px 10px rgba(255, 109, 0, 0.3);
      text-transform: uppercase;
      z-index: 10;
    }

    /* ----------------------------------------------------
       ESTILOS EXCLUSIVOS DA PÁGINA DE CATEGORIA/PRODUTO
       ---------------------------------------------------- */
    /* Mobile header modifications alignment */
    @media (max-width: 1023px) {
      /* Show Profile, Ajuda, and Cart on Mobile header */
      .action-btn[title="Favoritos"] {
        display: none !important;
      }
      .action-btn[title="Minha Conta"],
      .action-btn[title="Ajuda"],
      .header-cart-btn {
        display: flex !important;
      }
      .action-btn .action-text {
        display: none !important;
      }
      
      /* Orange circular Hamburger Toggle Button */
      .menu-toggle {
        background-color: #FF6D00 !important;
        color: #FFFFFF !important;
        width: 36px !important;
        height: 36px !important;
        border-radius: 50% !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        border: none !important;
        box-shadow: 0 2px 6px rgba(255, 109, 0, 0.2) !important;
        padding: 0 !important;
        cursor: pointer !important;
      }
      .menu-toggle svg {
        width: 18px !important;
        height: 18px !important;
        stroke: #FFFFFF !important;
      }

      /* Search Bar mobile alignment */
      .search-bar svg {
        left: auto !important;
        right: 18px !important;
      }
      .search-bar input {
        padding-left: 20px !important;
        padding-right: 48px !important;
        background-color: #F6F1EA !important;
        border: none !important;
      }
      
      /* Add bottom padding to body for the sticky buy bar */
      body {
        padding-bottom: 80px !important;
      }
    }

    /* Product Title Responsive Position Wrappers */
    .product-header-mobile {
      display: none;
      text-align: left;
      margin-bottom: 24px;
      padding: 0 20px;
    }
    .product-header-desktop {
      display: block;
      width: 100%;
    }
    @media (max-width: 1023px) {
      .product-header-mobile {
        display: block;
      }
      .product-header-desktop {
        display: none;
      }
    }

    /* Sticky Buy Bar for Mobile Viewports */
    .mobile-sticky-buy-bar {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background-color: #FFFFFF;
      padding: 12px 16px;
      box-shadow: 0 -4px 15px rgba(0, 0, 0, 0.08);
      z-index: 1000;
      display: none;
    }
    
    @media (max-width: 1023px) {
      .mobile-sticky-buy-bar {
        display: block;
      }
    }
    
    .btn-sticky-buy {
      width: 100%;
      height: 52px;
      background-color: #8BC34A; /* organic apple green */
      color: #FFFFFF;
      border-radius: 8px;
      font-size: 1.05rem;
      font-weight: 700;
      text-transform: uppercase;
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      box-shadow: 0 4px 12px rgba(139, 195, 74, 0.25);
      letter-spacing: 0.5px;
      transition: background-color 0.2s ease;
    }
    
    .btn-sticky-buy:active {
      background-color: #7CB342;
    }
    
    .sticky-cart-icon {
      width: 20px;
      height: 20px;
      stroke: #FFFFFF !important;
    }

    .product-detail-section {
      padding: 60px 0;
      background-color: var(--bg-white);
    }
    
    .product-detail-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 40px;
    }
    
    @media (min-width: 1024px) {
      .product-detail-grid {
        grid-template-columns: 1.15fr 0.85fr;
        gap: 60px;
      }
    }
    
    /* Galeria de Imagens */
    .product-gallery {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    
    .main-image-wrapper {
      background-color: #FFFFFF;
      border-radius: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
      border: none;
      height: 480px;
      position: relative;
    }
    
    .main-image-wrapper img {
      max-width: 85%;
      max-height: 85%;
      object-fit: contain;
      filter: drop-shadow(0 15px 30px rgba(0,0,0,0.05));
      transition: opacity 0.25s ease;
      opacity: 1;
    }
    
    .main-image-wrapper img.fade-out {
      opacity: 0;
    }
    
    .product-gold-badge {
      position: absolute;
      top: 24px;
      left: 24px;
      width: 86px;
      height: 86px;
      background-color: #D2A267;
      border-radius: 50%;
      color: #FFFFFF;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      font-size: 0.6rem;
      font-weight: 700;
      line-height: 1.25;
      padding: 10px;
      box-shadow: 0 6px 15px rgba(210, 162, 103, 0.3);
      z-index: 10;
      border: 2px dashed rgba(255,255,255,0.4);
      text-transform: uppercase;
    }
    
    .thumbnails-grid {
      display: flex;
      gap: 12px;
      justify-content: flex-start;
    }
    
    .thumbnail-btn {
      width: 76px;
      height: 76px;
      border-radius: 12px;
      background-color: var(--bg-light);
      border: 2px solid transparent;
      padding: 8px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: var(--transition-smooth);
    }
    
    .thumbnail-btn.active, .thumbnail-btn:hover {
      border-color: #5D9C3F;
      background-color: var(--bg-white);
    }
    
    .thumbnail-btn img {
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
    }
    
    /* Lado de Compra */
    .product-buy-info {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      text-align: left;
    }
    
    .product-breadcrumbs {
      font-family: var(--font-body);
      font-size: 0.72rem;
      color: #9E9E9E;
      margin-bottom: 12px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      font-weight: 600;
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
    }
    
    .product-breadcrumbs a {
      color: #9E9E9E;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      transition: color 0.2s ease;
    }
    
    .product-breadcrumbs a:hover {
      color: #FF6D00;
    }
    
    .product-breadcrumbs .home-icon {
      width: 14px;
      height: 14px;
      stroke: currentColor;
      stroke-width: 2.2;
    }
    
    .product-breadcrumbs .breadcrumb-separator {
      color: #D3C9C7;
      font-weight: 400;
      user-select: none;
      font-size: 0.8rem;
    }
    
    .product-breadcrumbs .breadcrumb-current {
      color: #7A706F;
      font-weight: 600;
    }
    
    .product-brand-tag {
      font-family: var(--font-heading);
      font-size: 0.82rem;
      font-weight: 700;
      color: #D2A267;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 4px;
    }
    
    .product-detail-title {
      font-family: var(--font-body);
      font-size: 1.6rem;
      font-weight: 800;
      color: #3C302F;
      line-height: 1.3;
      margin-bottom: 14px;
      letter-spacing: -0.3px;
    }
    
    .product-rating-row {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 24px;
      font-size: 0.9rem;
      font-weight: 600;
      color: var(--text-muted);
    }
    
    .rating-stars {
      display: flex;
      gap: 2px;
      color: #FFB300;
    }
    
    .rating-stars svg {
      width: 16px;
      height: 16px;
      fill: currentColor;
    }
    
    /* Opções Pills */
    .option-group {
      margin-bottom: 24px;
      width: 100%;
    }
    
    .option-label {
      font-size: 0.8rem;
      font-weight: 700;
      color: #3C302F;
      text-transform: uppercase;
      margin-bottom: 10px;
      display: block;
      letter-spacing: 0.5px;
    }
    
    .options-buttons {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }
    
    .option-btn {
      padding: 10px 24px;
      border-radius: 50px;
      background-color: #FFFFFF;
      border: 1px solid #E5E0DA;
      font-size: 0.85rem;
      font-weight: 600;
      color: #3C302F;
      cursor: pointer;
      transition: var(--transition-smooth);
    }
    
    .option-btn.active, .option-btn:hover {
      border-color: #5D9C3F;
      color: #5D9C3F;
      background-color: #F4F8F1;
    }
    
    /* Box de Compra/Recorrência */
    .price-card-box {
      width: 100%;
      background-color: #F5F5F5;
      border-radius: 24px;
      border: none;
      padding: 24px;
      margin-bottom: 20px;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    
    .purchase-type-row {
      display: flex;
      align-items: center;
      gap: 12px;
      cursor: pointer;
      padding: 14px 16px;
      border-radius: 16px;
      border: 1px solid transparent;
      background-color: transparent;
      transition: all 0.2s ease;
      width: 100%;
      box-sizing: border-box;
    }
    
    .purchase-type-row.active {
      border-color: #5D9C3F;
      background-color: #FFFFFF;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
    }
    
    .purchase-radio {
      appearance: none;
      width: 18px;
      height: 18px;
      border: 2px solid #CCCCCC;
      border-radius: 50%;
      outline: none;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      position: relative;
      background-color: #FFFFFF;
      flex-shrink: 0;
      margin: 0;
    }
    
    .purchase-type-row.active .purchase-radio {
      border-color: #5D9C3F;
      background-color: #5D9C3F;
    }
    
    .purchase-radio:checked::after {
      content: '';
      width: 6px;
      height: 6px;
      background-color: #FFFFFF;
      border-radius: 50%;
      display: block;
    }
    
    .purchase-details {
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }
    
    .purchase-title {
      font-size: 0.9rem;
      font-weight: 700;
      color: #3C302F;
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }
    
    .purchase-price {
      font-size: 1.4rem;
      font-weight: 800;
      color: #1A1A1A;
      margin-top: 4px;
      display: flex;
      align-items: center;
      gap: 8px;
      line-height: 1.2;
    }
    
    .purchase-price span {
      text-decoration: line-through;
      font-size: 0.95rem;
      color: #9E9E9E;
      font-weight: 500;
    }
    
    .purchase-installment {
      font-size: 0.72rem;
      color: #7A706F;
      margin-top: 2px;
      font-weight: 500;
    }
    
    .subscription-badge {
      display: inline-flex;
      background-color: #E8F5E9;
      color: #5D9C3F;
      font-size: 0.65rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 4px;
      margin-left: 8px;
      text-transform: uppercase;
    }
    
    .subscription-options {
      margin-top: 4px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      transition: all 0.3s ease;
      width: 100%;
    }
    
    .frequency-selector {
      width: 100%;
      height: 42px;
      border-radius: 8px;
      border: 1px solid #CCCCCC;
      padding: 0 12px;
      font-size: 0.85rem;
      font-weight: 600;
      background-color: #FFFFFF;
      color: #3C302F;
      outline: none;
    }
    
    .quantity-selector {
      display: flex;
      align-items: center;
      border: 1px solid #CCCCCC;
      border-radius: 8px;
      height: 40px;
      padding: 2px;
      background-color: #FFFFFF;
      width: fit-content;
    }
    
    .qty-btn {
      width: 36px;
      height: 36px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.1rem;
      font-weight: 600;
      color: #3C302F;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    
    .qty-btn:hover {
      background-color: #F0F0F0;
    }
    
    .qty-input {
      width: 32px;
      text-align: center;
      font-size: 0.95rem;
      font-weight: 700;
      color: #3C302F;
      border: none;
      background: transparent;
      outline: none;
    }
    
    .btn-add-to-cart {
      width: 100%;
      height: 52px;
      background-color: #5D9C3F;
      color: #FFFFFF;
      border-radius: 12px;
      font-size: 1rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 12px rgba(93, 156, 63, 0.2);
      transition: all 0.2s ease;
    }
    
    .btn-add-to-cart:hover {
      background-color: #4C8233;
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(93, 156, 63, 0.3);
    }
    
    /* Options Pills Style - True Clone */
    .flavor-options .option-btn.active {
      background-color: #FF6D00;
      border-color: #FF6D00;
      color: #FFFFFF;
    }
    
    .flavor-options .option-btn.active::before {
      content: "✓ ";
      font-weight: 800;
      margin-right: 4px;
    }
    
    .size-options {
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
    }
    
    .size-options .option-btn {
      width: 48px;
      height: 48px;
      padding: 0;
      border-radius: 50% !important;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.82rem;
      font-weight: 700;
      background-color: #FFFFFF;
      border: 1px solid #CCCCCC;
      color: #3C302F;
      transition: all 0.2s ease;
    }
    
    .size-options .option-btn.active,
    .size-options .option-btn:hover {
      background-color: #FF6D00;
      border-color: #FF6D00;
      color: #FFFFFF;
    }
    
    .product-gold-badge {
      display: none !important;
    }
    
    .product-rating-row {
      display: none !important;
    }
    
    /* 2. Allied Section */
    .allied-section {
      background-color: #FAF6F0;
      padding: 60px 0 0 0;
      text-align: center;
    }
    
    /* Day/Night Toggle Switch styling */
    .allied-toggle-container {
      display: flex;
      justify-content: center;
      margin-bottom: 24px;
    }
    
    .day-night-toggle {
      width: 80px;
      height: 38px;
      background-color: #3C302F;
      border-radius: 50px;
      position: relative;
      cursor: pointer;
      padding: 3px;
      box-sizing: border-box;
      display: flex;
      align-items: center;
      justify-content: space-between;
      user-select: none;
      box-shadow: inset 0 2px 5px rgba(0,0,0,0.2);
    }
    
    .toggle-icon {
      width: 32px;
      height: 32px;
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 2;
      transition: all 0.3s ease;
    }
    
    .toggle-icon-svg {
      width: 18px;
      height: 18px;
      fill: currentColor;
    }
    
    .toggle-icon.sun {
      margin-left: 2px;
      color: #FFA000;
    }
    
    .toggle-icon.moon {
      margin-right: 2px;
      color: #FFB300;
    }
    
    .toggle-thumb {
      position: absolute;
      width: 32px;
      height: 32px;
      background-color: #FFC107;
      border-radius: 50%;
      top: 3px;
      left: 3px;
      transition: transform 0.3s cubic-bezier(0.25, 1, 0.5, 1);
      z-index: 1;
      box-shadow: 0 2px 6px rgba(0,0,0,0.3);
    }
    
    .day-night-toggle.night .toggle-thumb {
      transform: translateX(42px);
    }
    
    .day-night-toggle.night .toggle-icon.sun {
      color: #8C7D70;
    }
    
    .day-night-toggle.night .toggle-icon.moon {
      color: #3C302F;
    }
    
    .allied-title {
      font-family: var(--font-serif);
      font-size: 2.6rem;
      color: #3C302F;
      font-weight: 700;
      margin-bottom: 40px;
      max-width: 850px;
      margin-left: auto;
      margin-right: auto;
      line-height: 1.25;
      padding: 0 20px;
    }
    
    .allied-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 24px;
      max-width: 1200px;
      margin: 0 auto 50px auto;
      padding: 0 20px;
      box-sizing: border-box;
    }
    
    @media (min-width: 600px) {
      .allied-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }
    
    @media (min-width: 1024px) {
      .allied-grid {
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 20px;
      }
    }
    
    .allied-col {
      background-color: #FFFFFF;
      border: 1px solid #E5E0DA;
      border-radius: 20px;
      padding: 32px 24px;
      text-align: left;
      box-sizing: border-box;
      transition: all 0.3s cubic-bezier(0.25, 1, 0.5, 1);
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.01);
      position: relative;
    }
    
    .allied-col:hover {
      transform: translateY(-5px);
      box-shadow: 0 12px 30px rgba(93, 156, 63, 0.08);
      border-color: #5D9C3F;
    }
    
    .allied-val {
      font-family: var(--font-heading);
      font-size: 2.1rem;
      font-weight: 800;
      color: #3C302F;
      display: block;
      margin-bottom: 6px;
      line-height: 1.1;
    }
    
    .allied-lbl {
      font-family: var(--font-heading);
      font-size: 1.1rem;
      font-weight: 700;
      color: #3C302F;
      display: block;
      margin-bottom: 12px;
      line-height: 1.2;
    }
    
    .allied-desc {
      font-size: 0.88rem;
      color: #7C7063;
      line-height: 1.5;
      margin: 0;
    }
    
    .allied-banner {
      width: 100%;
      height: 480px;
      overflow: hidden;
      position: relative;
    }
    
    .allied-banner img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }
    
    .allied-banner::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 160px;
      background: linear-gradient(to bottom, #FAF6F0 0%, rgba(250, 246, 240, 0) 100%);
      z-index: 2;
      pointer-events: none;
    }
    
    @media (max-width: 767px) {
      .allied-banner {
        height: 280px;
      }
      .allied-banner::before {
        height: 100px;
      }
    }
    
    /* Yellow gold action button */
    .btn-buy-now-accent {
      background-color: #FFB300;
      color: #231F20;
      padding: 16px 40px;
      border-radius: 50px;
      font-size: 0.9rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 15px rgba(255, 179, 0, 0.2);
      transition: var(--transition-smooth);
    }
    
    .btn-buy-now-accent:hover {
      background-color: #FFA000;
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(255, 179, 0, 0.3);
    }
    
    /* 3. Canister Split Section */
    .canister-split-section {
      position: relative;
      padding: 80px 0;
      text-align: center;
      background: linear-gradient(to bottom, #FAF6F0 42%, #8C7D70 42%);
    }
    
    .split-title {
      font-family: var(--font-serif);
      font-size: 2.8rem;
      color: #3C302F;
      font-weight: 700;
      margin-bottom: 40px;
      line-height: 1.2;
    }
    
    .split-canister-wrapper {
      display: flex;
      justify-content: center;
      margin-bottom: 40px;
      position: relative;
    }
    
    .split-canister-wrapper img {
      max-height: 380px;
      object-fit: contain;
      filter: drop-shadow(0 20px 35px rgba(0,0,0,0.12));
    }
    
    .split-bullets {
      display: flex;
      flex-direction: column;
      gap: 16px;
      max-width: 600px;
      margin: 0 auto 40px auto;
      color: #FFFFFF;
      font-weight: 600;
      font-size: 1.15rem;
      text-align: center;
      align-items: center;
    }
    
    .split-bullet-item {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    
    .split-bullet-item svg {
      width: 20px;
      height: 20px;
      fill: #FFB300;
      flex-shrink: 0;
    }
    
    /* 4. Como ele ajuda */
    .help-section {
      background-color: #FCFAF7;
      padding: 80px 0;
      text-align: center;
    }
    
    .help-title {
      font-family: var(--font-serif);
      font-size: 2.6rem;
      color: #3C302F;
      font-weight: 700;
      margin-bottom: 50px;
    }
    
    .help-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 30px;
      max-width: 1200px;
      margin: 0 auto 50px auto;
    }
    
    @media (min-width: 768px) {
      .help-grid {
        grid-template-columns: repeat(3, 1fr);
      }
    }
    
    .help-card {
      background-color: #FFFFFF;
      border-radius: 20px;
      overflow: hidden;
      box-shadow: 0 10px 30px rgba(0,0,0,0.03);
      border: 1px solid rgba(0,0,0,0.02);
      display: flex;
      flex-direction: column;
      text-align: left;
    }
    
    .help-card-img {
      height: 240px;
      overflow: hidden;
    }
    
    .help-card-img img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    
    .help-card-content {
      padding: 24px;
      display: flex;
      flex-direction: column;
    }
    
    .help-card-bar {
      height: 3px;
      width: 40px;
      background-color: #FFB300;
      margin-bottom: 16px;
    }
    
    .help-card-title {
      font-size: 1.2rem;
      font-weight: 700;
      color: #3C302F;
      margin-bottom: 10px;
    }
    
    .help-card-desc {
      font-size: 0.9rem;
      color: #7C7063;
      line-height: 1.5;
    }
    
    /* 5. Ciência e Estatísticas */
    .science-section-ref {
      background-color: #FFFFFF;
      padding: 80px 0;
      text-align: center;
    }
    
    .science-title-ref {
      font-family: var(--font-serif);
      font-size: 2.6rem;
      color: #3C302F;
      font-weight: 700;
      margin-bottom: 16px;
      max-width: 800px;
      margin-left: auto;
      margin-right: auto;
      line-height: 1.25;
    }
    
    .science-desc-ref {
      font-size: 1rem;
      color: #7C7063;
      max-width: 750px;
      margin: 0 auto 50px auto;
      line-height: 1.6;
    }
    
    .science-stats-carousel-container {
      position: relative;
      width: 100%;
      max-width: 1000px;
      margin: 40px auto;
      overflow: hidden;
      padding: 20px 0;
    }
    
    .science-stats-track {
      display: flex;
      gap: 30px;
      transition: transform 0.4s cubic-bezier(0.25, 1, 0.5, 1);
      align-items: center;
      width: max-content;
      padding-left: calc(50% - 90px);
      padding-right: calc(50% - 90px);
      box-sizing: border-box;
    }
    
    .stat-circle-box {
      width: 180px;
      flex-shrink: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      transition: all 0.4s ease;
      opacity: 0.4;
      transform: scale(0.8);
      cursor: pointer;
    }
    
    .stat-circle-box.active {
      opacity: 1;
      transform: scale(1.15);
    }
    
    .stat-circle-wrapper {
      position: relative;
      width: 120px;
      height: 120px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    
    .stat-circle-svg {
      width: 120px;
      height: 120px;
      transform: rotate(-90deg);
    }
    
    .stat-circle-bg {
      fill: none;
      stroke: #F4EFEA;
      stroke-width: 8;
    }
    
    .stat-circle-val {
      fill: none;
      stroke: #FFB300;
      stroke-width: 8;
      stroke-linecap: round;
      stroke-dasharray: 314;
      stroke-dashoffset: calc(314 - (314 * var(--pct-val)) / 100);
      transition: stroke-dashoffset 1s ease-out;
    }
    
    .stat-circle-inner-txt {
      position: absolute;
      font-family: var(--font-heading);
      font-size: 1.65rem;
      font-weight: 800;
      color: #7C7063;
      transition: color 0.4s ease, font-size 0.4s ease;
    }
    
    .stat-circle-box.active .stat-circle-inner-txt {
      color: #3C302F;
      font-size: 1.85rem;
    }
    
    .stat-circle-lbl-ref {
      font-size: 0.82rem;
      font-weight: 600;
      color: #7C7063;
      line-height: 1.35;
      max-width: 160px;
      transition: all 0.4s ease;
      opacity: 0.7;
    }
    
    .stat-circle-box.active .stat-circle-lbl-ref {
      color: #3C302F;
      font-size: 0.95rem;
      font-weight: 700;
      opacity: 1;
    }
    
    /* Navigation Buttons */
    .stats-carousel-nav {
      display: flex;
      justify-content: center;
      gap: 20px;
      margin-top: 30px;
    }
    
    .stats-nav-btn {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background-color: #FFB300;
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 10px rgba(255, 179, 0, 0.25);
      transition: all 0.2s ease;
      color: #231F20;
    }
    
    .stats-nav-btn:hover {
      background-color: #FFA000;
      transform: scale(1.05);
    }
    
    .stats-nav-btn svg {
      width: 20px;
      height: 20px;
      fill: currentColor;
    }
    
    .science-img-row-ref {
      display: grid;
      grid-template-columns: 1fr;
      gap: 20px;
      max-width: 1200px;
      margin: 50px auto 0 auto;
    }
    
    @media (min-width: 768px) {
      .science-img-row-ref {
        grid-template-columns: repeat(3, 1fr);
      }
    }
    
    .science-img-card-ref {
      height: 260px;
      border-radius: 20px;
      overflow: hidden;
      box-shadow: 0 4px 15px rgba(0,0,0,0.03);
    }
    
    .science-img-card-ref img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    
    /* 6. Sugestão de consumo */
    .usage-section-full {
      position: relative;
      padding: 100px 0;
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
      display: flex;
      align-items: center;
      min-height: 480px;
    }
    
    .usage-section-full::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0,0,0,0.15);
      z-index: 1;
    }
    
    .usage-card-overlay {
      position: relative;
      z-index: 2;
      background-color: #FAF6F0;
      padding: 40px;
      border-radius: 24px;
      max-width: 480px;
      box-shadow: 0 15px 35px rgba(0,0,0,0.08);
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      text-align: left;
    }
    
    .usage-title {
      font-family: var(--font-serif);
      font-size: 2.2rem;
      color: #3C302F;
      font-weight: 700;
      margin-bottom: 20px;
    }
    
    .usage-text {
      font-size: 1.05rem;
      color: #7C7063;
      line-height: 1.6;
    }
    
    @media (max-width: 767px) {
      .usage-section-full {
        padding: 40px 0;
        background-image: none !important;
        background-color: var(--bg-beige-dark);
        min-height: auto;
      }
      .usage-section-full::before {
        display: none;
      }
      .usage-card-overlay {
        max-width: 100%;
        padding: 24px;
        box-shadow: none;
        background: transparent;
      }
    }
    
    /* 7. Testimonials */
    .recommends-dark {
      background-color: #231F20;
      padding: 80px 0;
      color: #FFFFFF;
      text-align: center;
    }
    
    .recommends-title-dark {
      font-family: var(--font-serif);
      font-size: 2.6rem;
      color: #FFFFFF;
      font-weight: 700;
      margin-bottom: 50px;
    }
    
    .recommends-grid-ref {
      display: grid;
      grid-template-columns: 1fr;
      gap: 24px;
      max-width: 1200px;
      margin: 0 auto 50px auto;
    }
    
    @media (min-width: 768px) {
      .recommends-grid-ref {
        grid-template-columns: repeat(3, 1fr);
        align-items: stretch;
      }
    }
    
    .recommend-card-ref {
      border-radius: 24px;
      overflow: hidden;
      height: 380px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }
    
    .recommend-card-ref.img-card img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    
    .recommend-card-ref.quote-card {
      background-color: #FFB300;
      color: #231F20;
      padding: 40px 30px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      gap: 16px;
    }
    
    .quote-stars-ref {
      font-size: 1.5rem;
      color: #231F20;
      letter-spacing: 2px;
    }
    
    .quote-text-ref {
      font-family: var(--font-serif);
      font-style: italic;
      font-size: 1.25rem;
      font-weight: 600;
      line-height: 1.5;
    }
    
    .quote-author-ref {
      font-size: 0.85rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
    }
    
    /* 8. FAQ Accordion Split */
    .faq-section-ref {
      padding: 80px 0;
      background-color: #FFFFFF;
    }
    
    .faq-grid-ref {
      display: grid;
      grid-template-columns: 1fr;
      gap: 40px;
      max-width: 1200px;
      margin: 0 auto;
    }
    
    @media (min-width: 1024px) {
      .faq-grid-ref {
        grid-template-columns: 0.8fr 1.2fr;
        gap: 60px;
      }
    }
    
    .faq-left-card-ref {
      position: relative;
      border-radius: 24px;
      overflow: hidden;
      height: 480px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.05);
      display: none;
    }
    
    @media (min-width: 1024px) {
      .faq-left-card-ref {
        display: block;
      }
    }
    
    .faq-left-card-ref img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    
    .faq-left-card-ref::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: linear-gradient(transparent 40%, rgba(0,0,0,0.7));
      z-index: 1;
    }
    
    .faq-left-overlay-ref {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      padding: 40px;
      color: #FFFFFF;
      text-align: left;
      z-index: 2;
    }
    
    .faq-left-title-ref {
      font-family: var(--font-serif);
      font-size: 2.2rem;
      color: #FFFFFF;
      font-weight: 700;
      margin-bottom: 8px;
    }
    
    .faq-left-desc-ref {
      font-size: 0.95rem;
      opacity: 0.9;
      line-height: 1.5;
    }
    
    .faq-right-accordion-ref {
      text-align: left;
    }
    
    .faq-title-mobile-ref {
      font-family: var(--font-serif);
      font-size: 2.2rem;
      color: #3C302F;
      font-weight: 700;
      margin-bottom: 30px;
      text-align: center;
    }
    
    @media (min-width: 1024px) {
      .faq-title-mobile-ref {
        display: none;
      }
    }
    
    .faq-container {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    
    .faq-item {
      border: 1px solid #EAEAEA;
      border-radius: 12px;
      overflow: hidden;
      background-color: var(--bg-white);
    }
    
    .faq-header {
      padding: 18px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      user-select: none;
      background-color: var(--bg-white);
      transition: background-color 0.2s ease;
    }
    
    .faq-header:hover {
      background-color: var(--bg-light);
    }
    
    .faq-q {
      font-size: 1rem;
      font-weight: 700;
      color: #3C302F;
    }
    
    .faq-icon-arrow {
      width: 20px;
      height: 20px;
      color: #5C5248;
      transition: transform 0.3s ease;
      flex-shrink: 0;
    }
    
    .faq-item.active .faq-icon-arrow {
      transform: rotate(180deg);
    }
    
    .faq-body {
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .faq-content {
      padding: 0 24px 20px 24px;
      font-size: 0.95rem;
      color: var(--text-muted);
      line-height: 1.5;
    }
    
    /* 9 & 10. Ingredientes e Tabela */
    .nutrition-section-ref {
      background-color: #FCFAF7;
      padding: 80px 0;
    }
    
    .nutrition-grid-ref {
      display: grid;
      grid-template-columns: 1fr;
      gap: 40px;
      max-width: 1200px;
      margin: 0 auto;
    }
    
    @media (min-width: 1024px) {
      .nutrition-grid-ref {
        grid-template-columns: 1fr 1fr;
        gap: 60px;
      }
    }
    
    .nutrition-left-ref {
      text-align: left;
    }
    
    .nutrition-title-ref {
      font-family: var(--font-serif);
      font-size: 2.4rem;
      color: #3C302F;
      font-weight: 700;
      margin-bottom: 20px;
    }
    
    .ingredients-desc {
      font-size: 0.95rem;
      color: #5C5248;
      line-height: 1.6;
      margin-bottom: 24px;
    }
    
    .warnings-card-ref {
      background-color: #FFFFFF;
      border-radius: 12px;
      border-left: 4px solid #D27547;
      padding: 20px;
      font-size: 0.85rem;
      color: #7C7063;
      line-height: 1.5;
      margin-bottom: 30px;
    }
    
    .nutrition-left-img-ref {
      margin-top: 30px;
      border-radius: 20px;
      overflow: hidden;
      height: 280px;
      box-shadow: 0 6px 20px rgba(0,0,0,0.03);
    }
    
    .nutrition-left-img-ref img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    
    .nutrition-right-card-ref {
      background-color: #FFFFFF;
      border-radius: 24px;
      padding: 32px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.03);
      border: 1px solid rgba(0,0,0,0.02);
      text-align: left;
    }
    
    .table-header {
      font-family: var(--font-heading);
      font-size: 1.25rem;
      font-weight: 800;
      color: #3C302F;
      margin-bottom: 6px;
    }
    
    .table-portion {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 16px;
      border-bottom: 2px solid #3C302F;
      padding-bottom: 8px;
    }
    
    .nutri-table {
      width: 100%;
      border-collapse: collapse;
    }
    
    .nutri-table th {
      text-align: left;
      font-size: 0.85rem;
      font-weight: 700;
      color: #3C302F;
      padding: 8px 0;
      border-bottom: 1px solid #EAEAEA;
    }
    
    .nutri-table td {
      padding: 10px 0;
      border-bottom: 1px solid #F0F0F0;
      font-size: 0.88rem;
      color: #5C5248;
    }
    
    .nutri-table tr:last-child td {
      border-bottom: none;
    }
    
    .nutri-table td.bold {
      font-weight: 700;
      color: #3C302F;
    }
    
    .nutri-table td.right {
      text-align: right;
    }
    
    /* 11. Avaliações */
    .reviews-list-section {
      background-color: var(--bg-white);
      padding: 80px 0;
    }
    
    .reviews-list-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 40px;
    }
    
    @media (min-width: 1024px) {
      .reviews-list-grid {
        grid-template-columns: 0.7fr 1.3fr;
        gap: 60px;
      }
    }
    
    .reviews-score-card {
      background-color: #FAF5F0;
      border-radius: 24px;
      padding: 30px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 16px;
      text-align: center;
      box-shadow: 0 4px 15px rgba(0,0,0,0.01);
      height: fit-content;
    }
    
    .score-num {
      font-family: var(--font-heading);
      font-size: 4rem;
      font-weight: 800;
      color: #3C302F;
      line-height: 1;
    }
    
    .score-stars {
      display: flex;
      gap: 4px;
      color: #FFB300;
    }
    
    .score-stars svg {
      width: 24px;
      height: 24px;
      fill: currentColor;
    }
    
    .score-count {
      font-size: 0.9rem;
      color: var(--text-muted);
      font-weight: 600;
    }
    
    .score-recommend {
      font-size: 0.85rem;
      color: var(--accent-green);
      font-weight: 700;
      background-color: var(--accent-green-light);
      padding: 6px 16px;
      border-radius: 50px;
    }
    
    .reviews-items-col {
      display: flex;
      flex-direction: column;
      gap: 24px;
      text-align: left;
    }
    
    .review-item-row {
      border-bottom: 1px solid #F0F0F0;
      padding-bottom: 24px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    
    .review-item-row:last-child {
      border-bottom: none;
      padding-bottom: 0;
    }
    
    .review-meta {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.85rem;
      color: var(--text-light);
    }
    
    .review-author {
      font-weight: 700;
      color: #3C302F;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    
    .verified-badge {
      font-size: 0.7rem;
      font-weight: 700;
      color: var(--accent-green);
      background-color: var(--accent-green-light);
      padding: 2px 6px;
      border-radius: 4px;
      text-transform: uppercase;
    }
    
    .review-item-title {
      font-size: 1.1rem;
      font-weight: 800;
      color: #3C302F;
    }
    
    .review-item-text {
      font-size: 0.92rem;
      color: var(--text-muted);
      line-height: 1.5;
    }
    
    .review-recommend-status {
      font-size: 0.82rem;
      color: var(--accent-green);
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 4px;
    }
    

/* NEW WHEY EXTRA FEATURES */
.quick-nutrition-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 8px;
  margin: 18px 0;
}
.quick-nutrition-card {
  background-color: #F9F7F5;
  border-radius: 12px;
  padding: 12px 6px;
  text-align: center;
  border: 1px solid #EAE6DF;
  transition: all 0.2s ease;
}
.quick-nutrition-card:hover {
  background-color: #FFFFFF;
  border-color: #FF6D00;
  box-shadow: 0 4px 12px rgba(255, 109, 0, 0.08);
  transform: translateY(-2px);
}
.quick-nutrition-val {
  font-size: 0.95rem;
  font-weight: 800;
  color: #3C302F;
  display: block;
}
.quick-nutrition-label {
  font-size: 0.65rem;
  color: #888888;
  font-weight: 600;
  text-transform: uppercase;
  display: block;
  margin-top: 4px;
  letter-spacing: 0.3px;
}
.features-split-section {
  padding: 80px 0;
  background-color: #FAF8F5;
}
.features-split-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
}
.features-split-card {
  background-color: #FFFFFF;
  border-radius: 24px;
  padding: 40px;
  border: 1px solid #EAE6DF;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.02);
}
.features-split-title {
  font-size: 1.4rem;
  font-weight: 800;
  color: #3C302F;
  margin-bottom: 24px;
  display: flex;
  align-items: center;
  gap: 10px;
}
.features-split-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.features-split-list li {
  display: flex;
  align-items: flex-start;
  gap: 14px;
  font-size: 0.95rem;
  color: #4A4A4A;
  line-height: 1.5;
}
.features-split-list li svg {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
  margin-top: 2px;
}
@media (max-width: 991px) {
  .features-split-grid {
    gap: 24px;
  }
  .features-split-card {
    padding: 30px;
  }
}
@media (max-width: 768px) {
  .features-split-section {
    padding: 50px 0;
  }
  .features-split-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }
}
@media (max-width: 480px) {
  .quick-nutrition-grid {
    grid-template-columns: repeat(5, 1fr);
    gap: 4px;
    margin: 12px 0;
  }
  .quick-nutrition-card {
    padding: 8px 2px;
    border-radius: 8px;
  }
  .quick-nutrition-val {
    font-size: 0.75rem;
  }
  .quick-nutrition-label {
    font-size: 0.52rem;
    margin-top: 2px;
    letter-spacing: 0;
  }
  .features-split-card {
    padding: 24px 20px;
  }
  .features-split-title {
    font-size: 1.25rem;
  }
  .features-split-list li {
    font-size: 0.9rem;
    gap: 10px;
  }
}

.help-section {
  padding: 60px 0 40px 0;
  background-color: #FFFFFF;
  text-align: center;
}

.help-title {
  font-family: var(--font-heading);
  font-size: 1.1rem;
  font-weight: 800;
  color: #9E7D63;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  margin-bottom: 30px;
}

.benefits-carousel-container {
  width: 100%;
  max-width: 100%;
  margin: 0;
  padding: 0;
  overflow: hidden;
}

.benefits-track {
  display: flex;
  gap: 16px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  padding: 10px calc((100vw - 1440px) / 2 + 24px) 20px calc((100vw - 1440px) / 2 + 24px);
  scrollbar-width: none; /* Hide scrollbar for Firefox */
}

@media (max-width: 1488px) {
  .benefits-track {
    padding-left: 24px;
    padding-right: 24px;
  }
}

.benefits-track::-webkit-scrollbar {
  display: none; /* Hide scrollbar for Chrome/Safari */
}

.benefit-item-card {
  flex: 0 0 320px;
  scroll-snap-align: start;
  background-color: #F6F4F2;
  border-radius: 12px;
  padding: 16px 20px;
  display: flex;
  align-items: center;
  gap: 16px;
  border: 1px solid #EAE6DF;
  transition: all 0.25s ease;
}

.benefit-item-card:hover {
  background-color: #FFFFFF;
  border-color: #9E7D63;
  box-shadow: 0 8px 20px rgba(158,125,99,0.1);
  transform: translateY(-2px);
}

.benefit-icon-wrapper {
  width: 48px;
  height: 48px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.benefit-icon-wrapper img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.benefit-text-wrapper {
  font-size: 0.85rem;
  color: #3C302F;
  text-align: left;
  line-height: 1.4;
}

.benefit-text-wrapper strong {
  font-weight: 700;
  color: #3C302F;
}

.quick-nutrition-section {
  padding: 40px 0;
  background-color: #FFFFFF;
}

.product-description-section {
  position: relative;
  padding: 120px 0;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  display: flex;
  align-items: center;
  justify-content: center;
}

.product-description-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(255, 255, 255, 0.88); /* Subtle white overlay to overlay description text exactly like Vivatrue */
  z-index: 1;
}

.product-description-content {
  position: relative;
  max-width: 800px;
  margin: 0 auto;
  padding: 0 24px;
  z-index: 2;
  text-align: center;
}

.description-title {
  font-family: var(--font-heading);
  font-size: 2.2rem;
  font-weight: 800;
  color: #9E7D63;
  margin-bottom: 24px;
  text-transform: uppercase;
  letter-spacing: -0.5px;
  line-height: 1.25;
}

.description-text {
  font-size: 1.1rem;
  color: #5C5248;
  line-height: 1.7;
  font-weight: 500;
}

@media (max-width: 768px) {
  .product-description-section {
    padding: 80px 0;
  }
  .description-title {
    font-size: 1.6rem;
    margin-bottom: 16px;
  }
  .description-text {
    font-size: 0.95rem;
  }
  .benefit-item-card {
    flex: 0 0 280px;
    padding: 12px 16px;
    gap: 12px;
  }
  .benefits-track {
    padding-bottom: 15px;
  }
}
    """
    
    # Generate files for all 9 categories
    for cat in CATEGORIES_METADATA:
        # Description Background Images Map
        description_bg_map = {
            "whey": "foods/001.webp",
            "pre-treino": "foods/003.webp",
            "creatina": "foods/004.webp",
            "vitaminas": "foods/005.webp",
            "omega-3": "foods/006.webp",
            "colageno": "foods/001.webp",
            "true-foods": "foods/002.webp",
            "emagrecedores": "foods/003.webp",
            "vitamina-d": "foods/004.webp",
            "coenzima-q10": "foods/001.webp"
        }
        desc_bg = description_bg_map.get(cat["id"], "foods/001.webp")

        # Build flavor options HTML
        flavors_html = ""
        for idx, flavor in enumerate(cat["flavorOptions"]):
            active_class = "active" if idx == 0 else ""
            flavors_html += f'<button class="option-btn {active_class}" onclick="selectFlavor(this, \'{flavor}\')">{flavor}</button>'
            
        # Build size options HTML
        sizes_html = ""
        for idx, size in enumerate(cat["sizeOptions"]):
            active_class = "active" if idx == 0 else ""
            sizes_html += f'<button class="option-btn {active_class}">{size}</button>'
        # Quick Nutrition Highlights Map
        quick_nutri_map = {
            "whey": [
                {"val": "117 kcal", "lbl": "Calorias"},
                {"val": "4 g", "lbl": "Carbos"},
                {"val": "24 g", "lbl": "Proteínas"},
                {"val": "2 g", "lbl": "Gorduras"},
                {"val": "0 g", "lbl": "Açúcares"}
            ],
            "pre-treino": [
                {"val": "12 kcal", "lbl": "Calorias"},
                {"val": "3.000 mg", "lbl": "Beta-Alanina"},
                {"val": "1.000 mg", "lbl": "L-Arginina"},
                {"val": "500 mg", "lbl": "Taurina"},
                {"val": "200 mg", "lbl": "Cafeína"}
            ],
            "creatina": [
                {"val": "0 kcal", "lbl": "Calorias"},
                {"val": "3.000 mg", "lbl": "Creatina"},
                {"val": "100%", "lbl": "Pura"},
                {"val": "Zero", "lbl": "Açúcares"},
                {"val": "Micronizada", "lbl": "Fácil Diluição"}
            ],
            "vitaminas": [
                {"val": "0 kcal", "lbl": "Calorias"},
                {"val": "23", "lbl": "Nutrientes"},
                {"val": "100%", "lbl": "Quelatos"},
                {"val": "1 cap", "lbl": "ao dia"},
                {"val": "Zero", "lbl": "Açúcares"}
            ],
            "omega-3": [
                {"val": "18 kcal", "lbl": "Calorias"},
                {"val": "2.000 mg", "lbl": "Óleo de Peixe"},
                {"val": "720 mg", "lbl": "EPA"},
                {"val": "480 mg", "lbl": "DHA"},
                {"val": "10 mg", "lbl": "Vitamina E"}
            ],
            "colageno": [
                {"val": "35 kcal", "lbl": "Calorias"},
                {"val": "9 g", "lbl": "Colágeno"},
                {"val": "Verisol®", "lbl": "Tecnologia"},
                {"val": "80 mg", "lbl": "Ácido Hial."},
                {"val": "45 mg", "lbl": "Vitamina C"}
            ],
            "emagrecedores": [
                {"val": "0 kcal", "lbl": "Calorias"},
                {"val": "200 mg", "lbl": "Cafeína"},
                {"val": "500 mg", "lbl": "Carnitina"},
                {"val": "Zero", "lbl": "Açúcares"},
                {"val": "Foco", "lbl": "Treino"}
            ],
            "vitamina-d": [
                {"val": "0 kcal", "lbl": "Calorias"},
                {"val": "2.000 UI", "lbl": "Vitamina D3"},
                {"val": "120 mcg", "lbl": "Vitamina K2"},
                {"val": "250 mg", "lbl": "MCT"},
                {"val": "1 cap", "lbl": "ao dia"}
            ],
            "coenzima-q10": [
                {"val": "0 kcal", "lbl": "Calorias"},
                {"val": "100 mg", "lbl": "CoQ10"},
                {"val": "1 cap", "lbl": "ao dia"},
                {"val": "Zero", "lbl": "Açúcares"},
                {"val": "100%", "lbl": "Pura"}
            ],
            "true-foods": [
                {"val": "120 kcal", "lbl": "Calorias"},
                {"val": "100%", "lbl": "Arábica"},
                {"val": "TCM", "lbl": "Energia"},
                {"val": "Zero", "lbl": "Açúcares"},
                {"val": "Low", "lbl": "Carb"}
            ]
        }
        
        # Build quick nutrition highlights HTML
        quick_nutri_html = ""
        q_highlights = quick_nutri_map.get(cat["id"], [])
        for q in q_highlights:
            quick_nutri_html += f"""
            <div class="quick-nutrition-card">
              <span class="quick-nutrition-val">{q["val"]}</span>
              <span class="quick-nutrition-label">{q["lbl"]}</span>
            </div>"""

        # Build active highlights HTML
        highlights_html = ""
        for hl in cat["activeHighlights"]:
            highlights_html += f"""
            <div class="allied-col">
              <span class="allied-val">{hl["val"]}</span>
              <span class="allied-lbl">{hl["lbl"]}</span>
              <p class="allied-desc">{hl["desc"]}</p>
            </div>"""
            
        # Build canister bullets checkmark items
        bullets_html = ""
        for b in cat["bullets"]:
            bullets_html += f"""
            <div class="split-bullet-item">
              <svg viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
              <span>{b}</span>
            </div>"""
            
        # Build benefit cards HTML (Vivatrue horizontal cards style)
        benefits_html = ""
        for b in cat["benefits"]:
            benefits_html += f"""
            <div class="benefit-item-card">
              <div class="benefit-icon-wrapper">
                <img src="{b["img"]}" alt="{b["title"]}">
              </div>
              <div class="benefit-text-wrapper">
                <span><strong>{b["title"]}</strong>: {b["desc"]}</span>
              </div>
            </div>"""
            
        # Build science stats HTML
        stats_html = ""
        science_stats_list = cat["scienceStats"]
            
        for st in science_stats_list:
            pct_num = re.findall(r'\d+', st["pct"])
            pct_val = pct_num[0] if pct_num else "100"
            stats_html += f"""
            <div class="stat-circle-box" style="--pct-val: {pct_val};">
              <div class="stat-circle-wrapper">
                <svg class="stat-circle-svg" viewBox="0 0 120 120">
                  <circle class="stat-circle-bg" cx="60" cy="60" r="50"></circle>
                  <circle class="stat-circle-val" cx="60" cy="60" r="50"></circle>
                </svg>
                <span class="stat-circle-inner-txt">{st["pct"]}</span>
              </div>
              <span class="stat-circle-lbl-ref">{st["lbl"]}</span>
            </div>"""
            
        # Build accordion FAQs HTML
        faqs_html = ""
        for idx, faq in enumerate(cat["faqs"]):
            faqs_html += f"""
            <div class="faq-item">
              <div class="faq-header">
                <span class="faq-q">{faq["q"]}</span>
                <svg class="faq-icon-arrow" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"></path>
                </svg>
              </div>
              <div class="faq-body">
                <div class="faq-content">
                  <p>{faq["a"]}</p>
                </div>
              </div>
            </div>"""
            
        # Build nutrition rows HTML
        nutri_rows_html = ""
        for row in cat["nutritionTable"]:
            nutri_rows_html += f"""
            <tr>
              <td class="bold">{row["item"]}</td>
              <td>{row["qty"]}</td>
              <td class="right">{row["vd"]}</td>
            </tr>"""
            
        # Check if a custom table image exists for this category
        tabela_img_map = {
            "whey": "PRODUTOS/TABELAS/WHEY_PROTEIN_TABELA.png",
            "pre-treino": "PRODUTOS/TABELAS/DRAGON_GTX_TABELA.png",
            "creatina": "PRODUTOS/TABELAS/CREATINA_TABELA.png",
            "vitaminas": "PRODUTOS/TABELAS/POLI VITAMÍNICO.png",
            "colageno": "PRODUTOS/TABELAS/CABELO, PELE E UNHA_TABELA.png",
            "emagrecedores": "PRODUTOS/TABELAS/TERMOGÊNICO_HAVOC_TABELA.png",
            "vitamina-d": "PRODUTOS/TABELAS/VITAMINA D3+K+MG+2_TABELA.png",
            "coenzima-q10": "PRODUTOS/TABELAS/COENZIMAQ10_TABELA.png"
        }
        
        tabela_img = tabela_img_map.get(cat["id"])
        if tabela_img:
            table_content_html = f"""
            <img src="{tabela_img}" alt="Tabela Nutricional" style="width: 100%; height: auto; display: block; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
            """
        else:
            table_content_html = f"""
            <table class="nutri-table">
              <thead>
                <tr>
                  <th>Componente</th>
                  <th>Quantidade</th>
                  <th class="right">%VD*</th>
                </tr>
              </thead>
              <tbody>
                {nutri_rows_html}
              </tbody>
            </table>
            """
            
        # Build features split HTML only for Whey
        if cat["id"] == "whey":
            features_split_html = """
<!-- 5.1. O QUE POSSUI E NÃO POSSUI -->
<section class="features-split-section">
  <div class="container">
    <div class="features-split-grid">
      <!-- Possui -->
      <div class="features-split-card">
        <h3 class="features-split-title">
          <svg viewBox="0 0 24 24" fill="none" stroke="#FF6D00" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" style="width: 24px; height: 24px;">
            <polyline points="20 6 9 17 4 12"></polyline>
          </svg>
          O que possui
        </h3>
        <ul class="features-split-list">
          <li>
            <svg viewBox="0 0 24 24" fill="none" stroke="#FF6D00" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
            <span><strong>24g de Proteína Pura:</strong> Combinação isolada e concentrada de alta digestibilidade.</span>
          </li>
          <li>
            <svg viewBox="0 0 24 24" fill="none" stroke="#FF6D00" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
            <span><strong>5.5g de BCAAs:</strong> Essenciais para a recuperação acelerada pós-treino e hipertrofia.</span>
          </li>
          <li>
            <svg viewBox="0 0 24 24" fill="none" stroke="#FF6D00" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
            <span><strong>4.3g de Glutamina:</strong> Auxílio fundamental na imunidade e na saúde da microbiota intestinal.</span>
          </li>
          <li>
            <svg viewBox="0 0 24 24" fill="none" stroke="#FF6D00" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
            <span><strong>Sabor & Cremosidade Incomparável:</strong> O blend ideal para misturas ou receitas fit.</span>
          </li>
        </ul>
      </div>
      
      <!-- Não possui -->
      <div class="features-split-card">
        <h3 class="features-split-title">
          <svg viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" style="width: 24px; height: 24px;">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
          O que NÃO possui
        </h3>
        <ul class="features-split-list">
          <li>
            <svg viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
            <span><strong>Sem Açúcares Adicionados:</strong> Fórmula pura adoçada com adoçantes nobres.</span>
          </li>
          <li>
            <svg viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
            <span><strong>Adoçantes Artificiais Nocivos:</strong> Livre de ciclamato, aspartame ou aditivos.</span>
          </li>
          <li>
            <svg viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
            <span><strong>Corantes Artificiais:</strong> Sem prejuízos gástricos ou compostos alergênicos.</span>
          </li>
          <li>
            <svg viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
            <span><strong>Sem Glúten:</strong> Seguro para intolerantes e celíacos, garantindo digestão leve.</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""
        else:
            features_split_html = ""
            
        # Custom Detail Layout Content HTML
        detail_html = f"""
<!-- 2. PRODUTO COMPRA E DETALHES -->
    <section class="product-detail-section" id="buyArea">
      <div class="container">
        <!-- Mobile Header (Breadcrumbs + Title at the top on mobile) -->
        <div class="product-header-mobile">
          <div class="product-breadcrumbs">
            <a href="index.html" class="breadcrumb-home-link">
              <svg class="home-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
                <polyline points="9 22 9 12 15 12 15 22"/>
              </svg>
            </a>
            <span class="breadcrumb-separator">/</span>
            <a href="index.html#categories">Produtos</a>
            <span class="breadcrumb-separator">/</span>
            <span class="breadcrumb-current">{cat["title"]}</span>
          </div>
          <h1 class="product-detail-title">{cat["productName"]}</h1>
        </div>

        <div class="product-detail-grid">
          <!-- Galeria de Fotos -->
          <div class="product-gallery">
            <div class="main-image-wrapper">
              <div class="product-gold-badge">
                <span>Fórmula</span>
                <span style="font-size:0.9rem; font-weight:800; margin:2px 0;">Pura</span>
                <span style="font-size:0.55rem; opacity:0.8;">100% Clean</span>
              </div>
              <img id="mainProductDetailImg" src="{cat["image"]}" alt="{cat["productName"]}">
              
              <!-- Cashback Badge -->
              <div class="cashback-badge">
                <span>Cashback</span>
                <svg viewBox="0 0 24 24" fill="currentColor" style="width: 16px; height: 16px;">
                  <path d="M21 18v1c0 1.1-.9 2-2 2H5c-1.11 0-2-.9-2-2V5c0-1.1.89-2 2-2h14c1.1 0 2 .9 2 2v1h-9c-1.11 0-2 .9-2 2v8c0 1.1.89 2 2 2h9zm-9-2h10V8H12v8zm4-2.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"/>
                </svg>
              </div>
            </div>
          </div>
          
          <!-- Lado de Compra -->
          <div class="product-buy-info">
            <!-- Desktop Header (Breadcrumbs + Title inside buy info on desktop) -->
            <div class="product-header-desktop">
              <div class="product-breadcrumbs">
                <a href="index.html" class="breadcrumb-home-link">
                  <svg class="home-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
                    <polyline points="9 22 9 12 15 12 15 22"/>
                  </svg>
                </a>
                <span class="breadcrumb-separator">/</span>
                <a href="index.html#categories">Produtos</a>
                <span class="breadcrumb-separator">/</span>
                <span class="breadcrumb-current">{cat["title"]}</span>
              </div>
              <div class="product-brand-tag">BNS+ Premium</div>
              <h1 class="product-detail-title">{cat["productName"]}</h1>
            </div>
            
            <div class="product-rating-row">
              <div class="rating-stars">
                <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              </div>
              <span>4.8 (903 avaliações)</span>
            </div>
            
                       <!-- Opção de Sabor -->
            <div class="option-group flavor-group">
              <span class="option-label">Sabor</span>
              <div class="options-buttons flavor-options">
              {flavors_html}
            </div>
            </div>
            
            <!-- Opção de Tamanho -->
            <div class="option-group size-group">
              <span class="option-label">Tamanho</span>
              <div class="options-buttons size-options">
              {sizes_html}
            </div>
            </div>
            
            <!-- Box de Compra/Assinatura -->
            <div class="price-card-box">
              <!-- Compra Única (Sem Assinatura) -->
              <div class="purchase-type-row" onclick="togglePurchaseType('single')">
                <input type="radio" name="purchase_type" id="type_single" class="purchase-radio">
                <div class="purchase-details">
                  <span class="purchase-title">Sem Assinatura:</span>
                  <span class="purchase-price"><span>{cat["priceOld"]}</span>{cat["price"]}</span>
                  <span class="purchase-installment">ou em até 6x sem juros no Cartão</span>
                </div>
              </div>

              <!-- Compra com Assinatura (Com Assinatura, Checked por Padrão) -->
              <div class="purchase-type-row active" onclick="togglePurchaseType('sub')">
                <input type="radio" name="purchase_type" id="type_sub" class="purchase-radio" checked>
                <div class="purchase-details">
                  <span class="purchase-title">Com assinatura: <span class="subscription-badge">Economize 20%</span></span>
                  <span class="purchase-price monthly-price">{cat["priceMonthly"]} <span style="font-size:0.85rem; font-weight:500; color:#5D9C3F; margin-left:4px;">à vista no Cartão</span></span>
                </div>
              </div>
              
              <!-- Opções de Assinatura -->
              <div class="subscription-options" id="subOptionsBlock">
                <span class="option-label" style="font-size:0.75rem; margin-bottom:4px; letter-spacing:0.5px; text-transform: none; color: #777;">Selecione a Frequência de entrega</span>
                <select class="frequency-selector">
                  <option>Receber a cada 1 mês</option>
                  <option>Receber a cada 2 meses</option>
                  <option>Receber a cada 3 meses</option>
                </select>
                <p style="font-size:0.75rem; color:var(--text-muted); line-height:1.35; margin: 4px 0 0 0;">✔ Frete grátis em todas as recorrências. Cancele ou altere a qualquer momento sem taxas.</p>
              </div>

              <!-- Quantity Selector Inside Gray Card -->
              <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 8px;">
                <span class="option-label" style="font-size:0.75rem; margin-bottom:0; letter-spacing:0.5px; text-transform: none; color: #777;">Quantidade</span>
                <div class="quantity-selector">
                  <span class="qty-btn" onclick="adjustQty(-1)">-</span>
                  <input type="text" class="qty-input" id="buyQtyInput" value="1" readonly>
                  <span class="qty-btn" onclick="adjustQty(1)">+</span>
                </div>
              </div>
            </div>
            
            <!-- Botão de Compra (Full Width abaixo do box) -->
            <button class="btn-add-to-cart" onclick="triggerCartAnimation()">
              Adicionar ao Carrinho
            </button>
          </div>
        </div>
      </div>
      
      <!-- Floating Sticky Buy Bar for Mobile -->
      <div class="mobile-sticky-buy-bar">
        <button class="btn-sticky-buy" onclick="scrollToBuyMobile()">
          <span>Comprar</span>
          <svg class="sticky-cart-icon" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
          </svg>
        </button>
      </div>
    </section>

    <!-- 3. COMO TE AJUDA (BENEFÍCIOS) -->
    <section class="help-section">
      <div class="container">
        <h2 class="help-title">Benefícios do Produto</h2>
      </div>
      <div class="benefits-carousel-container">
        <div class="benefits-track">
          {benefits_html}
        </div>
        <div style="display: flex; justify-content: center; gap: 6px; margin-top: 20px;">
          <span style="width: 6px; height: 6px; border-radius: 50%; background-color: #3C302F; opacity: 0.8;"></span>
          <span style="width: 6px; height: 6px; border-radius: 50%; background-color: #3C302F; opacity: 0.2;"></span>
          <span style="width: 6px; height: 6px; border-radius: 50%; background-color: #3C302F; opacity: 0.2;"></span>
          <span style="width: 6px; height: 6px; border-radius: 50%; background-color: #3C302F; opacity: 0.2;"></span>
          <span style="width: 6px; height: 6px; border-radius: 50%; background-color: #3C302F; opacity: 0.2;"></span>
        </div>
      </div>
    </section>

    <!-- 4. DESTAQUES NUTRICIONAIS RÁPIDOS -->
    <section class="quick-nutrition-section">
      <div class="container">
        <div class="quick-nutrition-grid">
          {quick_nutri_html}
        </div>
      </div>
    </section>

    <!-- 5. O QUE É / DESCRIÇÃO DO PRODUTO -->
    <section class="product-description-section" style="background-image: url('{desc_bg}');">
      <div class="container">
        <div class="product-description-content">
          <h2 class="description-title">{cat["whatIsTitle"]}</h2>
          <p class="description-text">{cat["whatIsText"]}</p>
        </div>
      </div>
    </section>

    <!-- 6. CANISTER SPLIT SECTION -->
    <section class="canister-split-section">
      <div class="container">
        <h2 class="split-title">{cat["productName"]}</h2>
        <div class="split-canister-wrapper">
          <img src="{cat["image"]}" alt="{cat["productName"]}">
        </div>
        <div class="split-bullets">
          {bullets_html}
        </div>
        <button class="btn-buy-now-accent" onclick="scrollToBuy()">Comprar Agora</button>
      </div>
    </section>

    {features_split_html}

    <!-- 7. SUGESTÃO DE CONSUMO -->
    <section class="usage-section-full" style="background-image: url('{cat["usageImg"]}');">
      <div class="container">
        <div class="usage-card-overlay">
          <h2 class="usage-title">Sugestão de consumo</h2>
          <p class="usage-desc">{cat["usageText"]}</p>
          <button class="btn-buy-now-accent" onclick="scrollToBuy()" style="margin-top: 24px;">Comprar Agora</button>
        </div>
      </div>
    </section>

    <!-- 8. INGREDIENTES E TABELA NUTRICIONAL -->
    <section class="nutrition-section-ref">
      <div class="container">
        <div class="nutrition-grid-ref">
          <div class="nutrition-left-ref">
            <h2 class="nutrition-title-ref">Ingredientes</h2>
            <p class="ingredients-desc">{cat["ingredients"]}</p>
            <div class="warnings-card-ref">
              <strong>RECOMENDAÇÃO:</strong> Este produto não substitui uma alimentação equilibrada e seu consumo deve ser orientado por nutricionista ou médico. Gestantes, lactantes e crianças devem consumir apenas sob recomendação médica.
            </div>
            <button class="btn-buy-now-accent" onclick="scrollToBuy()">Comprar Agora</button>
            <div class="nutrition-left-img-ref">
              <img src="canister-product.webp" alt="Produto BNS+">
            </div>
          </div>
          <div class="nutrition-right-card-ref">
            <h3 class="table-header">Tabela Nutricional</h3>
            <p class="table-portion">{cat.get("portionText", "Porção recomendada")}</p>
            {table_content_html}
          </div>
        </div>
      </div>
    </section>

    <!-- 9. AVALIAÇÕES (TRUSTVOX STYLE) -->
    <section class="reviews-list-section">
      <div class="container">
        <div class="reviews-list-grid">
          <!-- Placar Geral -->
          <div class="reviews-score-card">
            <span class="score-num">4.8</span>
            <div class="score-stars">
              <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
            </div>
            <span class="score-count">(903 avaliações)</span>
            <span class="score-recommend">96% recomendam este produto</span>
          </div>
          
          <!-- Lista de Comentários -->
          <div class="reviews-items-col">
            <div class="review-item-row">
              <div class="review-meta">
                <span class="review-author">Michele M. <span class="verified-badge">Compra Verificada</span></span>
                <span>02/04/2026</span>
              </div>
              <h4 class="review-item-title">Ele realmente entrega o que promete!</h4>
              <p class="review-item-text">Resultado incrível, estou consumindo todos os dias e a qualidade é indiscutível! Aprovadíssimo, sabor maravilhoso e sem qualquer desconforto gástrico. Super recomendo!</p>
              <span class="review-recommend-status">✓ Recomendo este produto</span>
            </div>
            <div class="review-item-row">
              <div class="review-meta">
                <span class="review-author">Rodrigo S. <span class="verified-badge">Compra Verificada</span></span>
                <span>31/03/2026</span>
              </div>
              <h4 class="review-item-title">Excelente custo-benefício e sabor incrível</h4>
              <p class="review-item-text">Suplemento muito puro, dissolve super fácil e o sabor é muito agradável. Já sinto a diferença na disposição e no tônus após algumas semanas de uso constante.</p>
              <span class="review-recommend-status">✓ Recomendo este produto</span>
            </div>
            <div class="review-item-row">
              <div class="review-meta">
                <span class="review-author">Gabriela T. <span class="verified-badge">Compra Verificada</span></span>
                <span>28/03/2026</span>
              </div>
              <h4 class="review-item-title">Fórmula limpa de verdade!</h4>
              <p class="review-item-text">Sou muito chata com adoçantes artificiais e esse produto me surpreendeu muito. Leve, natural e de altíssima qualidade. O suporte de vendas da BNS+ também foi excelente.</p>
              <span class="review-recommend-status">✓ Recomendo este produto</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 9. AVALIAÇÕES (TRUSTVOX STYLE) -->
    <section class="reviews-list-section">
      <div class="container">
        <div class="reviews-list-grid">
          <!-- Placar Geral -->
          <div class="reviews-score-card">
            <span class="score-num">4.8</span>
            <div class="score-stars">
              <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
            </div>
            <span class="score-count">(903 avaliações)</span>
            <span class="score-recommend">96% recomendam este produto</span>
          </div>
          
          <!-- Lista de Comentários -->
          <div class="reviews-items-col">
            <div class="review-item-row">
              <div class="review-meta">
                <span class="review-author">Michele M. <span class="verified-badge">Compra Verificada</span></span>
                <span>02/04/2026</span>
              </div>
              <h4 class="review-item-title">Ele realmente entrega o que promete!</h4>
              <p class="review-item-text">Resultado incrível, estou consumindo todos os dias e a qualidade é indiscutível! Aprovadíssimo, sabor maravilhoso e sem qualquer desconforto gástrico. Super recomendo!</p>
              <span class="review-recommend-status">✓ Recomendo este produto</span>
            </div>
            <div class="review-item-row">
              <div class="review-meta">
                <span class="review-author">Rodrigo S. <span class="verified-badge">Compra Verificada</span></span>
                <span>31/03/2026</span>
              </div>
              <h4 class="review-item-title">Excelente custo-benefício e sabor incrível</h4>
              <p class="review-item-text">Suplemento muito puro, dissolve super fácil e o sabor é muito agradável. Já sinto a diferença na disposição e no tônus após algumas semanas de uso constante.</p>
              <span class="review-recommend-status">✓ Recomendo este produto</span>
            </div>
            <div class="review-item-row">
              <div class="review-meta">
                <span class="review-author">Gabriela T. <span class="verified-badge">Compra Verificada</span></span>
                <span>28/03/2026</span>
              </div>
              <h4 class="review-item-title">Fórmula limpa de verdade!</h4>
              <p class="review-item-text">Sou muito chata com adoçantes artificiais e esse produto me surpreendeu muito. Leve, natural e de altíssima qualidade. O suporte de vendas da BNS+ também foi excelente.</p>
              <span class="review-recommend-status">✓ Recomendo este produto</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 10. DÚVIDAS FREQUENTES (FAQ) -->
    <section class="faq-section-ref">
      <div class="container">
        <div class="faq-grid-ref">
          <div class="faq-left-card-ref">
            <img src="foods/007.webp" alt="Dúvidas Frequentes">
            <div class="faq-left-overlay-ref">
              <h3 class="faq-left-title-ref">Ficou com alguma dúvida?</h3>
              <p class="faq-left-desc-ref">Separamos as principais perguntas feitas pelos nossos clientes para te ajudar a escolher o melhor suplemento.</p>
            </div>
          </div>
          <div class="faq-right-accordion-ref">
            <h2 class="faq-title-mobile-ref">Dúvidas Frequentes</h2>
            <h3 class="faq-title-desktop">Dúvidas Frequentes</h3>
            <div class="faq-container">
              {faqs_html}
            </div>
          </div>
        </div>
      </div>
    </section>
        """
        if False:
            detail_html = f"""
    <!-- 2. PRODUTO COMPRA E DETALHES -->
    <section class="product-detail-section" id="buyArea">
      <div class="container">
        <div class="product-detail-grid">
          <!-- Galeria de Fotos -->
          <div class="product-gallery">
            <div class="main-image-wrapper">
              <div class="product-gold-badge">
                <span>Fórmula</span>
                <span style="font-size:0.9rem; font-weight:800; margin:2px 0;">Pura</span>
                <span style="font-size:0.55rem; opacity:0.8;">100% Clean</span>
              </div>
              <img id="mainProductDetailImg" src="{cat["image"]}" alt="{cat["productName"]}">
            </div>
            <div class="thumbnails-grid">
              <button class="thumbnail-btn active" onclick="switchMainImage('{cat["image"]}', this)">
                <img src="{cat["image"]}" alt="Foto 1">
              </button>
              <button class="thumbnail-btn" onclick="switchMainImage('generic-product.webp', this)">
                <img src="generic-product.webp" alt="Foto 2">
              </button>
              <button class="thumbnail-btn" onclick="switchMainImage('canister-product.webp', this)">
                <img src="canister-product.webp" alt="Foto 3">
              </button>
            </div>
          </div>
          
          <!-- Lado de Compra -->
          <div class="product-buy-info">
            <div class="product-breadcrumbs">
              <a href="index.html">Home</a> &gt; <a href="index.html#categories">{cat["title"]}</a>
            </div>
            <div class="product-brand-tag">BNS+ Premium</div>
            <h1 class="product-detail-title">{cat["productName"]}</h1>
            
            <div class="product-rating-row">
              <div class="rating-stars">
                <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              </div>
              <span>4.8 (903 avaliações)</span>
            </div>
            
            <!-- Opção de Sabor -->
            <div class="option-group">
              <span class="option-label">Sabor</span>
              <div class="options-buttons">
                {flavors_html}
              </div>
            </div>
            
            <!-- Opção de Tamanho -->
            <div class="option-group">
              <span class="option-label">Tamanho</span>
              <div class="options-buttons">
                {sizes_html}
              </div>
            </div>
            
            <!-- Box de Compra/Assinatura -->
            <div class="price-card-box">
              <!-- Compra com Assinatura (Checked por Padrão) -->
              <div class="purchase-type-row active" onclick="togglePurchaseType('sub')">
                <input type="radio" name="purchase_type" id="type_sub" class="purchase-radio" checked>
                <div class="purchase-details">
                  <span class="purchase-title">Compra recorrente <span class="subscription-badge">Economize 20%</span></span>
                  <span class="purchase-price">{cat["priceMonthly"]}</span>
                </div>
              </div>
              
              <!-- Compra Única -->
              <div class="purchase-type-row" onclick="togglePurchaseType('single')">
                <input type="radio" name="purchase_type" id="type_single" class="purchase-radio">
                <div class="purchase-details">
                  <span class="purchase-title">Compra única</span>
                  <span class="purchase-price"><span>{cat["priceOld"]}</span>{cat["price"]}</span>
                </div>
              </div>
              
              <!-- Opções de Assinatura -->
              <div class="subscription-options" id="subOptionsBlock">
                <span class="option-label" style="font-size:0.75rem; margin-bottom:4px; letter-spacing:0.5px;">Frequência de Entrega</span>
                <select class="frequency-selector">
                  <option>Receber a cada 1 mês</option>
                  <option>Receber a cada 2 meses</option>
                  <option>Receber a cada 3 meses</option>
                </select>
                <p style="font-size:0.75rem; color:var(--text-muted); line-height:1.35; margin: 4px 0 0 0;">✔ Frete grátis em todas as recorrências. Cancele ou altere a qualquer momento sem taxas.</p>
              </div>
            </div>
            
            <!-- Action Row: Seletor Quantidade + Botão Comprar -->
            <div class="action-row">
              <div class="quantity-selector">
                <span class="qty-btn" onclick="adjustQty(-1)">-</span>
                <input type="text" class="qty-input" id="buyQtyInput" value="1" readonly>
                <span class="qty-btn" onclick="adjustQty(1)">+</span>
              </div>
              <button class="btn-add-to-cart" onclick="triggerCartAnimation()">
                Adicionar ao Carrinho
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 3. HIGHLIGHTS / INGREDIENTES ATIVOS -->
    <section class="allied-section">
      <div class="container">
        <div class="allied-badge">BNS+</div>
        <h2 class="allied-title">Seu melhor aliado para {cat["goal"]}</h2>
        <div class="allied-grid">
          {highlights_html}
        </div>
        <button class="btn-buy-now-accent" onclick="scrollToBuy()" style="margin-bottom: 50px;">Comprar Agora</button>
        <div class="allied-banner">
          <img src="drink-banner.webp" alt="Rotina de Bem-Estar e Foco">
        </div>
      </div>
    </section>

    <!-- 4. CANISTER SPLIT SECTION -->
    <section class="canister-split-section">
      <div class="container">
        <h2 class="split-title">{cat["productName"]}</h2>
        <div class="split-canister-wrapper">
          <img src="{cat["image"]}" alt="{cat["productName"]}">
        </div>
        <div class="split-bullets">
          {bullets_html}
        </div>
        <button class="btn-buy-now-accent" onclick="scrollToBuy()">Comprar Agora</button>
      </div>
    </section>

    <!-- 5. COMO TE AJUDA (BENEFÍCIOS) -->
    <section class="help-section">
      <div class="container">
        <h2 class="help-title">Como ele te ajuda?</h2>
        <div class="help-grid">
          {benefits_html}
        </div>
        <button class="btn-buy-now-accent" onclick="scrollToBuy()">Comprar Agora</button>
      </div>
    </section>

    <!-- 6. CIÊNCIA E ESTATÍSTICAS -->
    <section class="science-section-ref">
      <div class="container">
        <h2 class="science-title-ref">{cat["scienceTitle"]}</h2>
        <p class="science-desc-ref">{cat["scienceDesc"]}</p>
        
        <div class="science-stats-row-ref">
          {stats_html}
        </div>
        
        <button class="btn-buy-now-accent" onclick="scrollToBuy()">Comprar Agora</button>
        
        <div class="science-img-row-ref">
          <div class="science-img-card-ref">
            <img src="foods/002.webp" alt="Estudo Clínico 1">
          </div>
          <div class="science-img-card-ref">
            <img src="foods/003.webp" alt="Estudo Clínico 2">
          </div>
          <div class="science-img-card-ref">
            <img src="foods/004.webp" alt="Estudo Clínico 3">
          </div>
        </div>
      </div>
    </section>

    <!-- 7. SUGESTÃO DE CONSUMO -->
    <section class="usage-section-full" style="background-image: url('{cat["usageImg"]}');">
      <div class="container">
        <div class="usage-card-overlay">
          <h2 class="usage-title">Sugestão de consumo</h2>
          <p class="usage-text">{cat["usageText"]}</p>
          <button class="btn-buy-now-accent" onclick="scrollToBuy()" style="margin-top: 24px;">Comprar Agora</button>
        </div>
      </div>
    </section>

    <!-- 7.1. QUEM USA, RECOMENDA -->
    <section class="recommends-dark">
      <div class="container">
        <h2 class="recommends-title-dark">Quem usa, recomenda</h2>
        <div class="recommends-grid-ref">
          <div class="recommend-card-ref img-card">
            <img src="foods/005.webp" alt="Influenciador BNS+">
          </div>
          <div class="recommend-card-ref quote-card">
            <span class="quote-stars-ref">★★★★★</span>
            <p class="quote-text-ref">"Fórmula extremamente limpa de verdade, sabor incrível e resultados visíveis em poucas semanas. Se tornou indispensável na minha rotina!"</p>
            <span class="quote-author-ref">Dra. Patrícia Lima</span>
          </div>
          <div class="recommend-card-ref img-card">
            <img src="foods/006.webp" alt="Influenciador BNS+">
          </div>
        </div>
        <button class="btn-buy-now-accent" onclick="scrollToBuy()">Comprar Agora</button>
      </div>
    </section>

    <!-- 8. FAQ ACCORDION -->
    <section class="faq-section-ref">
      <div class="container">
        <div class="faq-grid-ref">
          <div class="faq-left-card-ref">
            <img src="foods/007.webp" alt="Dúvidas Frequentes">
            <div class="faq-left-overlay-ref">
              <h2 class="faq-left-title-ref">Perguntas Frequentes</h2>
              <p class="faq-left-desc-ref">Tire todas as suas dúvidas sobre o produto e como inseri-lo na sua rotina diária.</p>
            </div>
          </div>
          <div class="faq-right-accordion-ref">
            <h2 class="faq-title-mobile-ref">Perguntas Frequentes</h2>
            <div class="faq-container">
              {faqs_html}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 9 & 10. INGREDIENTES E TABELA NUTRICIONAL -->
    <section class="nutrition-section-ref">
      <div class="container">
        <div class="nutrition-grid-ref">
          <div class="nutrition-left-ref">
            <h2 class="nutrition-title-ref">Ingredientes</h2>
            <p class="ingredients-desc">{cat["ingredients"]}</p>
            <div class="warnings-card-ref">
              <strong>RECOMENDAÇÃO:</strong> Este produto não substitui uma alimentação equilibrada e seu consumo deve ser orientado por nutricionista ou médico. Gestantes, lactantes e crianças devem consumir apenas sob recomendação médica.
            </div>
            <button class="btn-buy-now-accent" onclick="scrollToBuy()">Comprar Agora</button>
            <div class="nutrition-left-img-ref">
              <img src="canister-product.webp" alt="Produto BNS+">
            </div>
          </div>
          <div class="nutrition-right-card-ref">
            <h3 class="table-header">Tabela Nutricional</h3>
            <p class="table-portion">{cat.get("portionText", "Porção: 1 scoop")}</p>
            <table class="nutri-table">
              <thead>
                <tr>
                  <th>Componente</th>
                  <th>Quantidade</th>
                  <th class="right">%VD*</th>
                </tr>
              </thead>
              <tbody>
                {nutri_rows_html}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>

    <!-- 11. AVALIAÇÕES (TRUSTVOX STYLE) -->
    <section class="reviews-list-section">
      <div class="container">
        <div class="reviews-list-grid">
          <!-- Placar Geral -->
          <div class="reviews-score-card">
            <span class="score-num">4.8</span>
            <div class="score-stars">
              <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
              <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
            </div>
            <span class="score-count">(903 avaliações)</span>
            <span class="score-recommend">96% recomendam este produto</span>
          </div>
          
          <!-- Lista de Comentários -->
          <div class="reviews-items-col">
            <div class="review-item-row">
              <div class="review-meta">
                <span class="review-author">Michele M. <span class="verified-badge">Compra Verificada</span></span>
                <span>02/04/2026</span>
              </div>
              <h4 class="review-item-title">Ele realmente entrega o que promete!</h4>
              <p class="review-item-text">Resultado incrível, estou consumindo todos os dias e a qualidade é indiscutível! Aprovadíssimo, sabor maravilhoso e sem qualquer desconforto gástrico. Super recomendo!</p>
              <span class="review-recommend-status">✓ Recomendo este produto</span>
            </div>
            <div class="review-item-row">
              <div class="review-meta">
                <span class="review-author">Rodrigo S. <span class="verified-badge">Compra Verificada</span></span>
                <span>31/03/2026</span>
              </div>
              <h4 class="review-item-title">Excelente custo-benefício e sabor incrível</h4>
              <p class="review-item-text">Suplemento muito puro, dissolve super fácil e o sabor é muito agradável. Já sinto a diferença na disposição e no tônus após algumas semanas de uso constante.</p>
              <span class="review-recommend-status">✓ Recomendo este produto</span>
            </div>
            <div class="review-item-row">
              <div class="review-meta">
                <span class="review-author">Gabriela T. <span class="verified-badge">Compra Verificada</span></span>
                <span>28/03/2026</span>
              </div>
              <h4 class="review-item-title">Fórmula limpa de verdade!</h4>
              <p class="review-item-text">Sou muito chata com adoçantes artificiais e esse produto me surpreendeu muito. Leve, natural e de altíssima qualidade. O suporte de vendas da BNS+ também foi excelente.</p>
              <span class="review-recommend-status">✓ Recomendo este produto</span>
            </div>
          </div>
        </div>
      </div>
    </section>
        """
        
        # Category Script extension for tabs, accordion, buy select
        if True:
            cat_script_extensions = """
<script>
        // Custom Category Detail Interactions
        function toggleAlliedMode() {
          const toggle = document.querySelector('.day-night-toggle');
          if (toggle) {
            toggle.classList.toggle('night');
          }
        }

        function selectFlavor(btnEl, flavorName) {
          const group = btnEl.parentElement;
          group.querySelectorAll('.option-btn').forEach(btn => btn.classList.remove('active'));
          btnEl.classList.add('active');
          
          if (categoryId === 'whey') {
            const mainImg = document.getElementById('mainProductDetailImg');
            const newSrc = wheyFlavorImages[flavorName];
            if (mainImg && newSrc) {
              mainImg.classList.add('fade-out');
              setTimeout(() => {
                mainImg.src = newSrc;
                const firstThumb = document.querySelector('.thumbnail-btn img');
                if (firstThumb) {
                  firstThumb.src = newSrc;
                }
                mainImg.classList.remove('fade-out');
              }, 250);
            }
          }
        }

        function switchMainImage(imgSrc, btnEl) {
          document.getElementById('mainProductDetailImg').src = imgSrc;
          // Deactivate all thumbnails
          const thumbs = document.querySelectorAll('.thumbnail-btn');
          thumbs.forEach(t => t.classList.remove('active'));
          // Activate clicked
          btnEl.classList.add('active');
        }
        
        function togglePurchaseType(type) {
          const radioSingle = document.getElementById('type_single');
          const radioSub = document.getElementById('type_sub');
          const singleRow = radioSingle ? radioSingle.closest('.purchase-type-row') : null;
          const subRow = radioSub ? radioSub.closest('.purchase-type-row') : null;
          const subBlock = document.getElementById('subOptionsBlock');
          
          if (type === 'single') {
            if (singleRow) singleRow.classList.add('active');
            if (subRow) subRow.classList.remove('active');
            if (subBlock) subBlock.style.display = 'none';
            if (radioSingle) radioSingle.checked = true;
          } else {
            if (singleRow) singleRow.classList.remove('active');
            if (subRow) subRow.classList.add('active');
            if (subBlock) subBlock.style.display = 'flex';
            if (radioSub) radioSub.checked = true;
          }
        }
        
        // Option selection highlight
        document.querySelectorAll('.options-buttons').forEach(group => {
          group.addEventListener('click', function(e) {
            if (e.target.classList.contains('option-btn')) {
              group.querySelectorAll('.option-btn').forEach(btn => btn.classList.remove('active'));
              e.target.classList.add('active');
            }
          });
        });
        
        // Quantity adjustment
        function adjustQty(amount) {
          const qtyInput = document.getElementById('buyQtyInput');
          if (qtyInput) {
            let val = parseInt(qtyInput.value) || 1;
            val += amount;
            if (val < 1) val = 1;
            qtyInput.value = val;
          }
        }
        
        // FAQ Accordion
        document.querySelectorAll('.faq-header').forEach(header => {
          header.addEventListener('click', function() {
            const item = header.parentElement;
            const body = item.querySelector('.faq-body');
            const isActive = item.classList.contains('active');
            
            // Close all FAQ items
            document.querySelectorAll('.faq-item').forEach(i => {
              i.classList.remove('active');
              i.querySelector('.faq-body').style.maxHeight = null;
            });
            
            if (!isActive) {
              item.classList.add('active');
              body.style.maxHeight = body.scrollHeight + "px";
            }
          });
        });
        
        // Scroll to buy area helper
        function scrollToBuy() {
          const buyArea = document.getElementById('buyArea');
          if (buyArea) {
            buyArea.scrollIntoView({ behavior: 'smooth', block: 'center' });
          }
        }
        
        // Science Stats Slider/Carousel
        let activeStatIndex = 1;
        function updateStatsSlider() {
          const track = document.getElementById('statsTrack');
          if (!track) return;
          const items = track.querySelectorAll('.stat-circle-box');
          if (items.length === 0) return;
          
          if (activeStatIndex < 0) activeStatIndex = 0;
          if (activeStatIndex >= items.length) activeStatIndex = items.length - 1;
          
          items.forEach((item, idx) => {
            if (idx === activeStatIndex) {
              item.classList.add('active');
            } else {
              item.classList.remove('active');
            }
          });
          
          const itemWidth = 180;
          const gap = 30;
          const shift = -activeStatIndex * (itemWidth + gap);
          track.style.transform = `translateX(${shift}px)`;
        }
        
        function shiftStats(dir) {
          const track = document.getElementById('statsTrack');
          if (!track) return;
          const items = track.querySelectorAll('.stat-circle-box');
          activeStatIndex += dir;
          if (activeStatIndex < 0) activeStatIndex = items.length - 1;
          if (activeStatIndex >= items.length) activeStatIndex = 0;
          updateStatsSlider();
        }
        
        // Initial setup for Science Stats
        function initScienceStats() {
          const track = document.getElementById('statsTrack');
          if (track) {
            const items = track.querySelectorAll('.stat-circle-box');
            items.forEach((item, idx) => {
              item.addEventListener('click', () => {
                activeStatIndex = idx;
                updateStatsSlider();
              });
            });
            // Set middle item active by default
            activeStatIndex = Math.floor(items.length / 2);
            updateStatsSlider();
          }
        }
        initScienceStats();
        
        function scrollToBuyMobile() {
          const buyArea = document.getElementById('buyArea');
          if (buyArea) {
            buyArea.scrollIntoView({ behavior: 'smooth', block: 'center' });
          }
        }
        </script>
        """
        if False:
            cat_script_extensions = """
        <script>
        // Custom Category Detail Interactions
        function switchMainImage(imgSrc, btnEl) {
          document.getElementById('mainProductDetailImg').src = imgSrc;
          // Deactivate all thumbnails
          const thumbs = document.querySelectorAll('.thumbnail-btn');
          thumbs.forEach(t => t.classList.remove('active'));
          // Activate clicked
          btnEl.classList.add('active');
        }
        
        function togglePurchaseType(type) {
          const singleRow = document.querySelector('.purchase-type-row:nth-child(2)');
          const subRow = document.querySelector('.purchase-type-row:nth-child(1)');
          const subBlock = document.getElementById('subOptionsBlock');
          const radioSingle = document.getElementById('type_single');
          const radioSub = document.getElementById('type_sub');
          
          if (type === 'single') {
            singleRow.classList.add('active');
            subRow.classList.remove('active');
            subBlock.style.display = 'none';
            radioSingle.checked = true;
          } else {
            singleRow.classList.remove('active');
            subRow.classList.add('active');
            subBlock.style.display = 'flex';
            radioSub.checked = true;
          }
        }
        
        // Option selection highlight
        document.querySelectorAll('.options-buttons').forEach(group => {
          group.addEventListener('click', function(e) {
            if (e.target.classList.contains('option-btn')) {
              group.querySelectorAll('.option-btn').forEach(btn => btn.classList.remove('active'));
              e.target.classList.add('active');
            }
          });
        });
        
        // Quantity adjustment
        function adjustQty(amount) {
          const qtyInput = document.getElementById('buyQtyInput');
          if (qtyInput) {
            let val = parseInt(qtyInput.value) || 1;
            val += amount;
            if (val < 1) val = 1;
            qtyInput.value = val;
          }
        }
        
        // FAQ Accordion
        document.querySelectorAll('.faq-header').forEach(header => {
          header.addEventListener('click', function() {
            const item = header.parentElement;
            const body = item.querySelector('.faq-body');
            const isActive = item.classList.contains('active');
            
            // Close all FAQ items
            document.querySelectorAll('.faq-item').forEach(i => {
              i.classList.remove('active');
              i.querySelector('.faq-body').style.maxHeight = null;
            });
            
            if (!isActive) {
              item.classList.add('active');
              body.style.maxHeight = body.scrollHeight + "px";
            }
          });
        });
        
        // Scroll to buy area helper
        function scrollToBuy() {
          const buyArea = document.getElementById('buyArea');
          if (buyArea) {
            buyArea.scrollIntoView({ behavior: 'smooth', block: 'center' });
          }
        }
        </script>
        """
        
        # Conditionally choose layout and CSS
        combined_style = f"{style_content}\n{WHEY_CUSTOM_CSS}"
            
        # Custom script globals
        script_globals = f"""
        <script>
        const categoryId = '{cat["id"]}';
        const wheyFlavorImages = {{
          "Chocolate": "PRODUTOS/NEW WHEY PROTEIN/WHEY CHOCOLATE.webp",
          "Morango": "PRODUTOS/NEW WHEY PROTEIN/WHEY MORANGO.webp",
          "Baunilha": "PRODUTOS/NEW WHEY PROTEIN/WHEY BAUNILHA.webp",
          "Coco": "PRODUTOS/NEW WHEY PROTEIN/WHEY COCO.webp",
          "Leitinho": "PRODUTOS/NEW WHEY PROTEIN/WHEY LEITINHO.webp",
          "Cookies": "PRODUTOS/NEW WHEY PROTEIN/WHEY COOKIES.webp",
          "Doce de Leite": "PRODUTOS/NEW WHEY PROTEIN/WHEY DOCE DE LEITE.webp"
        }};
        </script>
        """

        # Build the final output HTML
        final_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    {head_content}
    <title>BNS+ | {cat["title"]}</title>
    <style>
        {combined_style}
    </style>
</head>
<body>
    {header_html}
    
    <main>
        {detail_html}
    </main>
    
    {footer_html}
    
    {script_content}
    {script_globals}
    {cat_script_extensions}
</body>
</html>
"""
        
        target_path = os.path.join("e:/LANDING PAGE BNS", cat["fileName"])
        print(f"Writing category file to: {target_path}")
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(final_html)
            
    print("Successfully generated all 10 category pages!")

if __name__ == '__main__':
    generate_all_pages()

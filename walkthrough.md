# Entrega da Landing Page Premium - BNS+

A landing page completa e responsiva para a marca de suplementos premium **BNS+** foi criada com sucesso. O arquivo está localizado em [index.html](file:///e:/LANDING%20PAGE%20BNS/index.html).

---

## 🛠️ Tecnologias e Recursos Utilizados
- **HTML5 Semântico**: Estruturação limpa com tags semânticas (`<header>`, `<main>`, `<section>`, `<article>`, `<footer>`).
- **CSS3 Moderno**: Utilização de variáveis globais de CSS, Flexbox, CSS Grid, media queries (Mobile-First) e animações personalizadas.
- **Tipografia**:
  - `Poppins` para cabeçalhos e elements fortes.
  - `Inter` para leitura agradável e corrida.
  - `Playfair Display` para títulos editoriais com apelo elegante (ex: Destaque de Produto Hero).
- **Sem Dependências Externas**: Ícones construídos nativamente via vetores SVG in-line para otimizar velocidade de carregamento e evitar dependências de CDNs terceiros.

---

## 📐 Estrutura de Blocos Desenvolvida (Ordem Estrita)

1. **Header Fixo**:
   - Barra superior promocional com anúncio de frete grátis (personalizado para compras acima de R$ 99).
   - Logomarca principal apontando para o arquivo de imagem personalizado `logo_blue.png` com dimensões e proporções otimizadas via CSS.
   - Barra de pesquisa integrada (com lupa SVG).
   - Ícones de ações atualizados com rótulos de texto no desktop ("Faça seu login ou cadastre-se" ao lado de Usuário, "Precisa de ajuda?" ao lado do ícone de Ajuda adicionado, e contador na Sacola).
   - Sub-menu de navegação contendo o botão de destaque "**Todos os produtos**" em azul à esquerda, links alinhados à referência (`Compre por objetivo`, `Mais Vendidos`, `Lançamentos`, `Destaque da Semana`, `GLP-1 Support`, `Assinatura`), pequenos **separadores de bolinhas cinzas (`•`)** com espaçamento ajustado de `16px`, e ícone de chevron na categoria `Compre por objetivo`.
   - Menu mobile drawer adaptado com a mesma lista de links correspondente.
   - **Comportamento Scrolled / Fixo (Novo)**: Ao rolar a página para baixo, o cabeçalho se contrai de duas linhas para **uma única linha ultra compacta**, alinhada perfeitamente com a referência visual:
     - Reordena dinamicamente os elementos usando Flexbox e `display: contents` no CSS, sem alterar a estrutura do DOM.
     - A ordem dos elementos torna-se: `Logo` | `Todos os produtos` | `Compre por objetivo` (com chevron) | `Assinatura` | `Barra de Busca` (em formato de pílula compacta de fundo bege `#F5F0EB` e ícone de lupa alinhado à direita) | `Ações do Header` (Minha Conta, Ajuda e Sacola de compras).
     - Oculta de forma inteligente os links intermediários (`Mais Vendidos`, `Lançamentos`, `Destaque da Semana`, `GLP-1 Support`) e os pontos separadores.
     - Esconde o botão de Favoritos e o texto dos ícones de login e ajuda em resoluções abaixo de `1200px` para evitar sobreposições, mantendo o cabeçalho 100% responsivo e elegante.

2. **Banner Hero Principal**:
   - Configurado como um **card centralizado e responsivo** dentro da largura do container, utilizando a imagem enviada pelo usuário (`dragon-gtx-banner.png`) como imagem de fundo e contendo bordas arredondadas (`border-radius: 24px`) com `overflow: hidden` e uma máscara WebKit (`-webkit-mask-image`) para forçar o arredondamento perfeito de todos os cantos no navegador, incluindo os dois cantos inferiores.
   - Remoção do estiramento de tela cheia nas laterais, com a seção externa adotando fundo branco limpo, mantendo o foco centralizado no conteúdo.
   - Posicionamento da imagem de fundo (`dragon-gtx-banner.png`) deslocado `220px` para a direita e largura do conteúdo limitada a `520px` no desktop, evitando sobreposição com os produtos da imagem e mantendo o pote próximo à borda direita.
   - Disposição interna dos elementos reestruturada para seguir fielmente a referência: rótulo superior, headline grande, **ticket de brindes com bordas pontilhadas e duas colunas** (`Kit Ritual do Treino` e `Intra-Treino ou Cúrcuma`), botão CTA primário e nota de rodapé informativa.

3. **Carrossel de Categorias**:
   - Scroll horizontal fluido com 9 categorias representadas por círculos pastéis e ícones SVG temáticos (com a categoria "Proteínas Veganas" removida de acordo com a customização).

4. **Seção Best Sellers (Best Sellers)**:
   - Título e link para listagem geral.
   - Grid horizontal scrollável com setas de navegação desktop.
   - Cards com badge de desconto, avaliação de estrelas, preços antigo/novo e botão de carrinho com animação de pulso.

5. **Seção Editorial / Blog Preview**:
   - Grid 2x2 responsiva com as 4 postagens solicitadas (Saúde, Vitaminas, Fitness) e títulos idênticos à referência.

6. **Destaque de Produto Hero ("Cabelo, Pele & Unhas")**:
   - Seção full-width de fundo bege médio com tipografia serifada gigante e benefícios organizados em cards brancos de destaque.

7. **Seção "Quem Usa, Recomenda"**:
   - Carrossel horizontal de influencers com depoimento, foto em estilo retrato com gradiente escuro e botão de compra rápida.

8. **Seção True Foods**:
   - Grid de 4 produtos com fundos pastéis coloridos vibrantes (rosa, marrom, caramelo e azul/verde), preço e botão circular de compra rápida.

9. **Bloco Depoimento Destaque**:
   - Banner de destaque em azul sólido `#015CAB`.
   - Foto grande do produto à esquerda. Aspas gigantes e carrossel interativo em JS com troca automática/manual de depoimentos à direita.

10. **Bloco Depoimento Médico**:
    - Fundo off-white `#F5F0EB` com foco em autoridade.
    - Foto circular de especialista à esquerda e declaração oficial em itálico à direita com setas funcionais de navegação.

11. **Seção "Recomendados Para Você"**:
    - Grid de 4 produtos com descontos e estilo idêntico à seção Best Sellers.

12. **Banner Institucional**:
    - Fundo suave e layout moderno conectando o propósito da marca (insumos limpos e naturais) com uma foto editorial sofisticada.

13. **Footer Completo**:
    - Logo, assinatura de newsletter com botão azul brand, links corporativos e de ajuda estruturados em 4 colunas responsivas, selo SSL seguro, selos de segurança adicionais e ícones de cartões/Pix.

---

## 💫 Interações Funcionais Desenvolvidas (via JavaScript Embutido)
- **Header Dinâmico**: Diminui de tamanho e adiciona sombra leve (`backdrop-filter`) ao rolar a página para baixo.
- **Carrinho Interativo**: Ao clicar em "Conhecer produto", o contador do cabeçalho incrementa dinamicamente com uma animação de salto (scale) e o botão exibe um status temporário de "✓ Adicionado!".
- **Carrosséis Horizontais**: Setas funcionais de navegação horizontal no grid de Best Sellers, Recomendados e Influencers.
- **Sliders de Depoimento**:
  - Depoimentos Destaque (Azul) alternam textos e autores por meio de setas sem recarregar a página.
  - Depoimentos Médicos (Autoridade) contam com navegação funcional para múltiplas citações médicas.
- **Newsletter**: Validação de e-mail e popup interativo confirmando a assinatura.

---

## 🎨 Novo Layout Premium dos Cards de Produto
- Alinhado com a nova referência visual solicitada pelo usuário, todos os 8 cards de produtos (Bloco 4: Best Sellers e Bloco 11: Recomendados Para Você) foram reestruturados e estilizados:
  1. **Badge de Sabor / Benefício (Pílula Overlay)**:
     - Posicionamento absoluto e centralizado na base do wrapper da imagem do produto.
     - Fundo branco limpo com texto em azul da marca (`#015CAB`) em negrito, criando um contraste premium.
     - Textos adaptados para cada produto:
       - *Whey*: "Sabor do Coco de Verdade"
       - *Creatina*: "100% Pura & Importada"
       - *Termogênico*: "Fórmula Fit Clean"
       - *Multivitamínico*: "A-Z Vitaminas e Minerais"
       - *Vitamina D3+K2*: "Saúde Imunológica"
       - *Ômega 3*: "Ultra Purificado"
       - *Colágeno*: "Beleza & Firmeza"
  2. **Alinhamento Inline de Preços e Avaliação (Meta Row)**:
     - Em vez de blocos separados, o preço (De / Por) e a avaliação do produto (estrela gold + número) agora compartilham a mesma linha horizontal logo abaixo do nome do produto.
     - Preço De (antigo) com traço em cinza claro, preço Por (atual) em negrito e preto `#1A1A1A`, e estrela gold com a nota (ex: `★ 4.8`) alinhada à direita.
  3. **Botão de Adicionar ao Carrinho (Visual Clean)**:
     - Removida a borda outline e o ícone de sacola para adotar um estilo minimalista premium.
     - Fundo bege claro sólido (`#F5F0EB`) com texto marrom escuro em negrito (`#4A3E3D`).
     - Efeito hover premium: transiciona suavemente para o azul principal da marca (`#015CAB`) com texto em branco e uma sombra sutil projetada.
  4. **Proporção e Imagem Genérica Temporária**:
     - Ajustada a proporção do wrapper da imagem (`.product-img-wrapper`) para **aspect ratio 4:5** conforme a referência.
     - Definido o ajuste de encaixe da imagem para `object-fit: cover` para cobrir o espaço inteiro da proporção.
     - Configurada a imagem [generic-product.jpg](file:///E:/LANDING PAGE BNS/generic-product.jpg) como imagem genérica em todos os 8 cards de produtos para visualização rápida do layout real.

---

## 🥤 Substituição da Seção de Artigos por Card de Nova Fórmula
- A seção de "Artigos" (Bloco 5) foi totalmente substituída por um card promocional moderno e responsivo que destaca a **Nova Fórmula** do suplemento *True Energyzer & Focus*:
  1. **Recorte de Imagens de Alta Fidelidade**:
     - O pote do produto foi salvo como [canister-product.webp](file:///E:/LANDING PAGE BNS/canister-product.webp).
     - O bloco contendo a bebida no copo foi salvo como [drink-banner.webp](file:///E:/LANDING PAGE BNS/drink-banner.webp).
  2. **Desenvolvimento do Layout (.formula-card)**:
     - Grid responsivo de duas colunas (50%/50% no desktop, empilhando-se verticalmente no mobile).
     - Adotado fundo bege claro (`#F5F0EB`) e bordas bem arredondadas (`28px`), idêntico ao modelo.
     - O lado esquerdo exibe o pote de produto, a tipografia limpa da chamada, descrição resumida e botões. O lado direito exibe a imagem coral completa da bebida.

---

## 🎠 Carrossel Dinâmico de 12 Produtos no Card de Fórmula
- O bloco promocional de fórmula foi transformado em um carrossel interativo e funcional que navega entre 12 produtos da marca contidos na pasta `formula-card/`:
  1. **Troca Dinâmica de Elementos**:
     - Ao clicar nas setas de navegação (`#formulaPrev` e `#formulaNext`), o card atualiza em tempo real as seguintes informações:
       - Imagem do pote do produto (buscada da pasta local `formula-card/`).
       - Título e nome do produto.
       - Descrição com os benefícios e diferenciais específicos de cada fórmula.
       - Imagem promocional de fundo na coluna direita.
  2. **Efeito de Transição Suave (Fade Transition)**:
     - Implementamos a classe CSS `.formula-fade` combinada com o JavaScript para aplicar um efeito suave de esmaecimento e leve deslocamento vertical (`transform: translateY`) a cada transição de slide.

---

## 🌟 Destaque de Produto Hero: Cabelo, Pele & Unhas
- A seção de **Destaque de Produto Hero (Bloco 6)** foi atualizada para promover o produto **Cabelo, Pele & Unhas**:
  1. **Alteração de Mídia**:
     - Substituído o pote anterior pela imagem real do pote do produto [CABELO, PELE E UNHA.webp](file:///E:/LANDING PAGE BNS/formula-card/CABELO,%20PELE%20E%20UNHA.webp).
  2. **Atualização Textual & Benefícios**:
     - Título alterado para "Cabelo, Pele & Unhas" com o subtítulo "Brilho, Força e Elasticidade".
     - Descrição reescrita destacando a sinergia entre a biotina concentrada, colágeno hidrolisado e minerais quelatos.
     - Preço no botão ajustado de forma atrativa para **R$ 89,90**.

---

## ⚓ Rolagem Suave com Offset para Menu Desktop e Mobile
- Para atender à solicitação de que a navegação e rolagens automáticas surtam efeito perfeito também na versão mobile:
  1. **Ajuste de Margem de Rolagem (CSS scroll-margin-top)**:
     - Unificamos a propriedade `scroll-margin-top: 140px` tanto no desktop quanto no mobile para as seções `#bestSellers`, `#productHero`, `#trueFoods`, `#categories`, `#reviews` e `#recommended`.
     - Isso garante que a rolagem nativa deixe um espaçamento adequado no topo, impedindo que a barra de cabeçalho fixa/sticky (que ficou ligeiramente mais alta no mobile com a nova barra de categorias) cubra os títulos das seções.
  2. **Interceptador de Cliques do Menu Drawer (JavaScript)**:
     - Implementado um tratador de eventos em JS para todos os links do menu drawer do mobile (`.mobile-menu-links a`).
     - Quando um link é clicado, o drawer inicia seu fechamento deslizante (que leva 300ms) e é executado um `setTimeout` de 300ms antes de rolar. Isso evita engasgos e reposicionamentos incorretos durante a transição do menu.
     - O cálculo de rolagem é dinâmico: `targetElement.getBoundingClientRect().top + window.scrollY - headerHeight`, garantindo precisão milimétrica em qualquer resolução.

---

## 📱 Banner Hero Exclusivo para Versão Mobile (VERSAO_MOBILE_ALTA.webp - Alta Qualidade)
- Para solucionar definitivamente a questão de resolução do banner mobile:
  1. **Conversão e Otimização**:
     - O arquivo de alta resolução `VERSAO_MOBILE_ALTA.png` (3MB) foi processado e salvo como `VERSAO_MOBILE_ALTA.webp` com largura limitada a `1000px` (proporção mantida), garantindo nitidez impecável em telas Retina de smartphones.
     - O tamanho final do arquivo foi reduzido para apenas **113 KB** (otimização de ~96%).
  2. **Substituição no HTML**:
     - Atualizada a tag de imagem do banner mobile em [index.html](file:///E:/LANDING%20PAGE%20BNS/index.html) para apontar para `VERSAO_MOBILE_ALTA.webp`.

---

## 🥗 Seção True Foods Expandida (7 Cards & Fotos Reais)
- A seção **True Foods (Bloco 8)** foi reestruturada para exibir **7 cards ao todo** (uma adição de 3 novos cards):
  1. **Fotos Reais e Otimizadas**:
     - As 7 imagens fornecidas na pasta `foods/` (de 500KB a 10MB) foram redimensionadas para largura máxima de `800px` e convertidas para WebP.
     - O tamanho total das fotos caiu de ~35MB para apenas **~440KB** somados (redução de 98.7% no peso dos arquivos), otimizando drasticamente a velocidade de carregamento.
  2. **Paleta de Cores Pastéis Ampliada**:
     - Criamos novas classes CSS (`.tf-purple`, `.tf-orange`, `.tf-yellow`) com fundos pastéis harmônicos para os 3 novos produtos.
  3. **Identidade dos Produtos**:
     - **Card 1 (Rosa - tf-pink)**: `foods/001.webp` - Pasta de Amendoim BNS+ (R$ 29,66)
     - **Card 2 (Chocolate - tf-chocolate)**: `foods/002.webp` - Proteína em Barra BNS+ (R$ 12,66)
     - **Card 3 (Caramelo - tf-caramel)**: `foods/003.webp` - Granola Proteica BNS+ (R$ 25,42)
     - **Card 4 (Verde - tf-green)**: `foods/004.webp` - Bebida Proteica Matcha BNS+ (R$ 16,06)
     - **Card 5 (Roxo - tf-purple)**: `foods/005.webp` - Cookies Proteicos BNS+ (R$ 16,91) [NOVO]
     - **Card 6 (Laranja - tf-orange)**: `foods/006.webp` - Creme de Avelã Proteico BNS+ (R$ 33,91) [NOVO]
     - **Card 7 (Amarelo - tf-yellow)**: `foods/007.webp` - Chips de Coco BNS+ (R$ 10,96) [NOVO]
  4. **Preservação de Regras**:
     - Todos os cards novos utilizam o botão `"Conhecer produto"`, sem fluxo de carrinho direto ("adicionar à sacola").
     - Grid 100% responsivo: no desktop os 7 cards dividem-se de forma fluida, e no mobile continuam com o comportamento de scroll horizontal por arrasto/touch.

---

## 🧭 Barra de Categorias Horizontal no Mobile (Estilo Menu Junto)
- Ajustamos a barra de categorias secundária no mobile para ficar idêntica à referência:
  1. **Remoção de Elementos**:
     - Ocultamos completamente o botão azul `"Todos os produtos"` (`.btn-all-products`) no mobile para evitar poluição visual.
     - Removemos todos os círculos/pontos separadores (`.nav-dot`) para manter o menu clean.
  2. **Agrupamento e Espaçamento (CSS)**:
     - Modificamos a classe `.nav-links` no mobile para se comportar como um contêiner flex (`display: flex !important; flex-direction: row !important; gap: 20px`).
     - O critério de rolagem e toque aproxima as opções de navegação (`Mais Vendidos`, `Destaque da Semana`, `Foods`, `Catálogo`), agrupando-as lateralmente de forma compacta como na referência.
     - A tipografia foi atualizada para uma cor escura premium (`var(--text-dark)`) com peso negrito (`600`) para melhor leitura.
     - A navegação secundária permanece scrollável horizontalmente sem quebras de linha em qualquer dispositivo móvel.

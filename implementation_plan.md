# Plano de Implementação - Landing Page Premium BNS+

Este plano detalha o design e a estrutura de código para a criação de uma Landing Page responsiva, moderna e visualmente premium para a marca brasileira de suplementos **BNS+**, baseada no layout do site de referência.

## Visão Geral do Design e Identidade Visual

- **Paleta de Cores**:
  - Destaque: Azul Brand `#015CAB` (Hover: `#004B8C`)
  - Fundos Secundários: Cinza Claro `#F8F8F8`, Bege/Off-white Suave `#FAF6F0`, Off-white Médio `#F5F0EB` (bloco médico)
  - Escuros/Texto: Preto `#1A1A1A`, Cinza Escuro `#4A4A4A`
  - Feedback/Descontos: Verde Clássico de E-commerce `#2E7D32`
- **Tipografia**:
  - `Poppins` (Google Fonts) para títulos e destaques modernos e bold.
  - `Inter` (Google Fonts) para leitura fluida de textos corporativos, tabelas e parágrafos.
- **Efeitos e Interações**:
  - Transição de cor e tamanho do header ao rolar a página (`sticky` header com sombra e desfoque de fundo - glassmorphism).
  - Cards com design estático (sem animação de elevação/zoom no hover) para um visual mais limpo e estável.
  - Efeito de pulso discreto nos botões "Conhecer produto" ao passar o mouse.
  - Layout totalmente responsivo com grid adaptativo para telas grandes, tablets e smartphones (mobile-first).

---

## Proposta de Estrutura de Código

Implementaremos a landing page em um único arquivo HTML contendo todos os estilos CSS no bloco `<style>` e comportamentos interativos (carrosséis, toggle de mobile menu, transição de header) em um bloco `<script>` no final.

### Detalhamento dos 13 Blocos (Ordem Estrita)

1. **HEADER FIXO**:
   - Barra superior com mensagem/aviso dinâmico (ex: frete grátis).
   - Logo `BNS+` (com ícone de sol estilizado em SVG para garantir qualidade vetorial).
   - Campo de busca centralizado com lupa integrada e placeholder "O que você procura?".
   - Ícones de usuário, favoritos e sacola (com contador flutuante).
   - Menu secundário com categorias principais e link de "Promoções" destacado em azul.

2. **BANNER HERO PRINCIPAL**:
   - Seção flex/grid bipartida (50% / 50%).
   - Texto à esquerda: tag azul "OFERTA ESPECIAL", headline bold 15% Off, subheadline de produtos com termos em destaque, botão CTA principal.
   - Imagem à direita: Composição fotográfica simulada com `placehold.co` estilizado com gradiente premium e proporção adequada para whey/vitamina.

3. **CARROSSEL DE CATEGORIAS**:
   - Fileira com `overflow-x: auto` permitindo scroll horizontal suave (especialmente em celulares).
   - Ícones circulares coloridos (com pequenos SVG ou emojis estilizados) e rótulos abaixo.

4. **SEÇÃO BEST SELLERS**:
   - Título e link "Ver todos os produtos >".
   - Grid horizontal scrollável com setas de navegação.
   - Cards com badge de desconto, foto em fundo neutro, avaliação em estrelas, preços (riscado e promocional) e botão de carrinho outline.

5. **SEÇÃO EDITORIAL / BLOG PREVIEW**:
   - Grid 2x2 responsiva com cards contendo imagem em proporção panorâmica, tag azul de categoria e título marcante.

6. **DESTAQUE DE PRODUTO HERO (Full-Width)**:
   - Fundo bege premium. Título "Ferro Liposomal" gigante com tipografia refinada/serifada para contraste editorial, composição de produto centralizada/direita e subtítulo de benefício.

7. **SEÇÃO "QUEM USA, RECOMENDA" (Prova Social)**:
   - Carrossel horizontal com cards de influencers, foto de rosto/lifestyle estilizada, depoimento curto e botão de compra rápida.

8. **SEÇÃO TRUE FOODS / LINHA ESPECIAL**:
   - Linha especial com grid de 4 cards coloridos (Rosa Pastel, Caramelo, Marrom Chocolate, Verde Claro), exibindo nome, foto recortada do produto, preço e botão.

9. **BLOCO DEPOIMENTO DESTAQUE (Full-Width)**:
   - Fundo azul brand `#015CAB`. Lado esquerdo: whey gigante. Lado direito: aspas enormes, depoimento impactante em branco, nome do cliente e estrelas.

10. **BLOCO DEPOIMENTO MÉDICO / AUTORIDADE**:
    - Fundo off-white `#F5F0EB`. Foto circular de jaleco à esquerda. Depoimento em itálico à direita detalhando a segurança e eficácia das fórmulas.

11. **SEÇÃO "RECOMENDADOS PARA VOCÊ"**:
    - Grid de 4 produtos com layout consistente com o bloco 4 (Best Sellers).

12. **BANNER INSTITUCIONAL FULL-WIDTH**:
    - Fundo texturizado suave. Texto de impacto sobre sustentabilidade e pureza à esquerda. Foto de coquetel sofisticado e moderno à direita.

13. **FOOTER COMPLETO**:
    - Logotipo, newsletter com assinatura rápida. 4 colunas organizadas de links, seção de cartões de crédito/PIX e selos de segurança.

---

## Plano de Verificação

### Testes Manuais
- Verificar a responsividade em tamanhos de tela (desktop > 1200px, tablet 768px, mobile < 480px).
- Testar transições de hover em todos os botões e cards de produtos.
- Testar o comportamento "sticky" do header e o scroll suave ao clicar nos links de navegação.
- Validar a acessibilidade básica e estrutura correta de tags (`<header>`, `<main>`, `<section>`, `<footer>`).

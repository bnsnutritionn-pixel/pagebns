import os
import sys
import json
import re
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
import subprocess

# Função auxiliar para carregar variáveis do .env manualmente
def load_env(filepath=".env"):
    env_vars = {}
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    env_vars[key.strip()] = val.strip()
    return env_vars

# Formata o float no padrão de moeda brasileiro R$ XX,XX
def format_price_br(value_float):
    return f"R$ {value_float:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Converte string de preço do XML (ex: "R$ 179,97" ou "179.97") em float
def parse_xml_price(price_str):
    if not price_str:
        return 0.0
    # Remover "R$" e espaços
    clean_str = price_str.replace("R$", "").replace(" ", "").strip()
    # Se o formato usar vírgula para decimal (ex: 179,97)
    if "," in clean_str and "." not in clean_str:
        clean_str = clean_str.replace(",", ".")
    elif "," in clean_str and "." in clean_str:
        # Formato americano com separador de milhar (ex: 1,179.97)
        clean_str = clean_str.replace(",", "")
    try:
        return float(clean_str)
    except ValueError:
        return 0.0

# Atualiza a Landing Page index.html com os preços do XML e links corretos
def update_landing_page_prices(prices_data):
    index_path = "index.html"
    if not os.path.exists(index_path):
        # Se estiver rodando de fora, tenta e:/LANDING PAGE BNS/index.html
        index_path = "e:/LANDING PAGE BNS/index.html"
        
    if not os.path.exists(index_path):
        print("[LandingPage/Erro] index.html não foi encontrado para atualização de preços.")
        return False
        
    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read().replace("\r\n", "\n")
        
    categories_map = {
        "whey": {
            "identifier": "WHEY_DE_COCO.webp",
            "link": "categoria-whey.html"
        },
        "pre-treino": {
            "identifier": "DRAGON_FRUTAS.webp",
            "link": "categoria-pre-treino.html"
        },
        "creatina": {
            "identifier": "CREA_DARK.webp",
            "link": "categoria-creatina.html"
        },
        "coenzima-q10": {
            "identifier": "COENZIMA Q10.webp",
            "link": "categoria-coenzima-q10.html"
        },
        "emagrecedores": {
            "identifier": "HAVOC.webp",
            "link": "categoria-emagrecedores.html"
        }
    }
    
    updated_html = html
    changes_made = 0
    
    for cat_id, config in categories_map.items():
        if cat_id not in prices_data:
            continue
            
        price_info = prices_data[cat_id]
        price_old = price_info.get("priceOld", "")
        price_current = price_info.get("price", "")
        identifier = config["identifier"]
        target_link = config["link"]
        
        # Regex robusta para substituir preços e botão de "Conhecer produto"
        pattern = rf'(<div class="product-card">[^>]*?.*?{identifier}.*?<span class="price-old">)[^<]*(</span>.*?<span class="price-current">)[^<]*(</span>.*?)(<(button|a) class="add-to-cart-btn"[^>]*>\s*Conhecer produto\s*</(button|a)>)'
        
        replacement = rf'\1{price_old}\2{price_current}\3<a href="{target_link}" class="add-to-cart-btn" style="text-decoration: none;">Conhecer produto</a>'
        
        new_html, count = re.subn(pattern, replacement, updated_html, flags=re.DOTALL | re.IGNORECASE)
        if count > 0:
            updated_html = new_html
            changes_made += count
            print(f"[LandingPage] Card [{cat_id}] atualizado: {price_old} | {price_current} -> Link: {target_link}")
            
    if changes_made > 0:
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(updated_html)
        print(f"[LandingPage] {changes_made} cards atualizados em index.html com sucesso!")
        return True
    else:
        print("[LandingPage] Nenhuma alteração pendente em index.html.")
        return False

def main():
    print("=== Sincronizador de Preços via XML (Google Ads / Merchant Center) ===")
    
    # Carregar variáveis do .env
    env = load_env()
    xml_url = env.get(
        "TRAY_XML_URL", 
        "https://www.bnssuplementos.com.br/xml/xml.php?Chave=w9GazVGbn92bnxHMwADN3MTM"
    )
    
    # Mapeamento ID da Categoria BNS+ -> ID do produto (<g:id>) no XML da BNS
    product_mapping = {
        "whey": env.get("TRAY_ID_WHEY", "51-79"),              # New Whey Protein Concentrado - Chocolate
        "pre-treino": env.get("TRAY_ID_PRE_TREINO", "59-97"),    # DRAGON GTX PRE WORKOUT - Frutas Vermelhas
        "creatina": env.get("TRAY_ID_CREATINA", "37"),          # Creatina Micronizada Dark 300g
        "vitaminas": env.get("TRAY_ID_VITAMINAS", "41"),        # Multivitamínico 120 cápsulas
        "omega-3": env.get("TRAY_ID_OMEGA_3", "N/A"),           # Não presente no XML atual (mantém preço padrão)
        "colageno": env.get("TRAY_ID_COLAGENO", "N/A"),         # Não presente no XML atual (mantém preço padrão)
        "true-foods": env.get("TRAY_ID_TRUE_FOODS", "N/A"),     # Não presente no XML atual (mantém preço padrão)
        "emagrecedores": env.get("TRAY_ID_EMAGRECEDORES", "17"),# Termogênico HAVOC 60ca
        "vitamina-d": env.get("TRAY_ID_VITAMINA_D", "103"),     # VITAMINA D3+K+MG+II - 60 COMPRIMIDOS
        "coenzima-q10": env.get("TRAY_ID_COENZIMA_Q10", "87"),  # COENZIMA Q10 - 60 COMPRIMIDOS
    }
    
    print(f"Baixando feed XML de: {xml_url}...")
    req = urllib.request.Request(xml_url, headers={"User-Agent": "Mozilla/5.0"})
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            xml_data = response.read()
    except Exception as e:
        print(f"[ERRO] Falha ao baixar o feed XML: {e}")
        sys.exit(1)
        
    print("Processando arquivo XML...")
    try:
        root = ET.fromstring(xml_data)
    except Exception as e:
        print(f"[ERRO] Falha ao parsear estrutura XML: {e}")
        sys.exit(1)
        
    # Namespaces usados no XML do Google Shopping da Tray
    namespaces = {
        'g': 'http://base.google.com/ns/1.0',
        'c': 'http://base.google.com/cns/1.0'
    }
    
    # Extrair todos os produtos do XML e guardar num dicionário por ID
    xml_products = {}
    items = root.findall('.//item')
    for item in items:
        item_id_el = item.find('g:id', namespaces)
        if item_id_el is not None:
            item_id = item_id_el.text.strip()
            title_el = item.find('title')
            price_el = item.find('g:price', namespaces)
            sale_price_el = item.find('g:sale_price', namespaces)
            
            title = title_el.text.strip() if title_el is not None else ""
            price_str = price_el.text.strip() if price_el is not None else ""
            sale_price_str = sale_price_el.text.strip() if sale_price_el is not None else ""
            
            xml_products[item_id] = {
                "title": title,
                "price": parse_xml_price(price_str),
                "sale_price": parse_xml_price(sale_price_str)
            }
            
    print(f"Total de {len(xml_products)} produtos indexados a partir do XML.")
    
    prices_data = {}
    
    for cat_id, target_id in product_mapping.items():
        if target_id == "N/A" or target_id not in xml_products:
            print(f"  -> Categoria '{cat_id}': ID {target_id} não encontrado no XML. Mantendo preços do template padrão.")
            continue
            
        prod_data = xml_products[target_id]
        price_val = prod_data["price"]
        sale_price_val = prod_data["sale_price"]
        
        # Lógica de determinação do preço atual/promocional
        if sale_price_val > 0 and sale_price_val < price_val:
            price_current = sale_price_val
            price_old = price_val
        else:
            price_current = price_val
            # Se não tiver promoção, simulamos um "Preço Antigo" sugerido (+15%) para manter a identidade visual da LP
            price_old = price_val * 1.15
            
        price_monthly = price_current * 0.95
        
        prices_data[cat_id] = {
            "price": format_price_br(price_current),
            "priceOld": format_price_br(price_old),
            "priceMonthly": format_price_br(price_monthly),
            "installments": f"6x de {format_price_br(price_current / 6)}"
        }
        print(f"  -> Sincronizado [{cat_id}] (ID XML: {target_id}): {prod_data['title']} | Preço Atual={prices_data[cat_id]['price']}, Preço Antigo={prices_data[cat_id]['priceOld']}")

    # Gravar as alterações no prices.json
    if prices_data:
        with open("prices.json", "w", encoding="utf-8") as f:
            json.dump(prices_data, f, indent=4, ensure_ascii=False)
        print("\nArquivo 'prices.json' gerado e salvo com sucesso!")
        
        # Atualizar os preços e links na Landing Page index.html
        print("Atualizando Landing Page (index.html)...")
        update_landing_page_prices(prices_data)
        
        # Disparar compilação automática
        print("Iniciando compilação das páginas de categoria...")
        try:
            result = subprocess.run([sys.executable, "generate_category_pages.py"], capture_output=True, text=True, encoding="utf-8")
            print(result.stdout)
            if result.returncode == 0:
                print("Compilação concluída com sucesso! Todos os arquivos categoria-*.html foram atualizados.")
                
                # Git Auto-push
                print("\nIniciando push automático para o GitHub...")
                try:
                    # 1. Adicionar os arquivos gerados/modificados
                    subprocess.run(["git", "add", "prices.json"], check=True)
                    subprocess.run(["git", "add", "categoria-*.html"], check=True)
                    
                    # Também adicionamos index.html se modificado (alterações de layout anteriores)
                    subprocess.run(["git", "add", "index.html"], check=True)
                    
                    # 2. Verificar se há alterações staged
                    status_res = subprocess.run(["git", "diff", "--cached", "--name-only"], capture_output=True, text=True, check=True)
                    if status_res.stdout.strip():
                        # 3. Commitar as alterações
                        commit_msg = "chore: auto-sync prices and categories via XML"
                        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
                        print("[Git] Alterações commitadas localmente.")
                    else:
                        print("[Git] Nenhuma alteração pendente de commit nos arquivos de preços/categorias.")
                        
                    # 4. Push para o repositório remoto
                    print("[Git] Enviando alterações para o repositório remoto (git push)...")
                    # Adicionamos um timeout de 30 segundos para evitar que trave indefinidamente se houver problemas de credenciais
                    push_res = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True, timeout=30)
                    if push_res.returncode == 0:
                        print("[Git] Push concluído com sucesso!")
                        print(push_res.stdout)
                    else:
                        print(f"[Git/AVISO] Falha ao enviar para o GitHub (talvez necessite de autenticação manual): {push_res.stderr}")
                except subprocess.TimeoutExpired:
                    print("[Git/AVISO] O comando git push expirou o tempo limite de 30 segundos (provavelmente aguardando credenciais interativas).")
                except Exception as e:
                    print(f"[ERRO] Falha durante o processo do Git: {e}")
            else:
                print(f"[ERRO] Falha na compilação: {result.stderr}")
        except Exception as e:
            print(f"[ERRO] Não foi possível rodar o script de compilação: {e}")
    else:
        print("\nNenhum preço foi atualizado. Abortando compilação.")

if __name__ == "__main__":
    main()

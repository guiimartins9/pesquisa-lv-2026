import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo teste.env
load_dotenv('teste.env')

TOKEN = os.getenv('token_acesso_meta')

# Versão atualizada da Graph API
VERSION = 'v19.0' 
BASE_URL = f'https://graph.facebook.com/{VERSION}'

headers = {
    'Authorization': f'Bearer {TOKEN}'
}

def get_ad_accounts():
    """Busca as contas de anúncio vinculadas ao usuário/token"""
    url = f"{BASE_URL}/me/adaccounts"
    params = {'fields': 'id,name,account_status'}
    response = requests.get(url, headers=headers, params=params, timeout=10)
    
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        print("\n❌ Erro ao buscar contas de anúncio:")
        print(response.text)
        return []

def get_active_campaigns(ad_account_id):
    """Busca apenas as campanhas ativas de uma conta"""
    url = f"{BASE_URL}/{ad_account_id}/campaigns"
    params = {
        'fields': 'id,name,status,objective',
        'effective_status': '["ACTIVE"]',
        'limit': '500'
    }
    response = requests.get(url, headers=headers, params=params, timeout=10)
    
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        print(f"    ❌ Erro ao buscar campanhas: {response.text}")
        return []

def get_active_adsets(campaign_id):
    """Busca os conjuntos de anúncios ativos de uma campanha"""
    url = f"{BASE_URL}/{campaign_id}/adsets"
    params = {
        'fields': 'id,name,status,daily_budget,lifetime_budget',
        'effective_status': '["ACTIVE"]',
        'limit': '500'
    }
    response = requests.get(url, headers=headers, params=params, timeout=10)
    
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        print(f"      ❌ Erro ao buscar conjuntos: {response.text}")
        return []

def get_active_ads(adset_id):
    """Busca os anúncios ativos dentro de um conjunto"""
    url = f"{BASE_URL}/{adset_id}/ads"
    params = {
        'fields': 'id,name,status',
        'effective_status': '["ACTIVE"]',
        'limit': '500'
    }
    response = requests.get(url, headers=headers, params=params, timeout=10)
    
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        print(f"        ❌ Erro ao buscar anúncios: {response.text}")
        return []

def format_budget(value):
    """Formata o orçamento retornado pela API (que vem em centavos) para reais"""
    if not value:
        return "N/A"
    return f"R$ {int(value) / 100:.2f}"

def main():
    if not TOKEN:
        print("❌ Token não encontrado no arquivo teste.env")
        print("Certifique-se de que a variável 'token_acesso_meta' está definida.")
        return

    print("--- 🔍 Buscando estrutura ATIVA na Meta Ads ---")
    
    ad_accounts = get_ad_accounts()
    
    if not ad_accounts:
        print("Nenhuma conta de anúncio encontrada ou erro de permissão.")
        return

    for account in ad_accounts:
        # Se você quiser filtrar apenas contas ativas (status 1 = ACTIVE)
        account_name = account.get('name', 'Conta sem nome')
        print(f"\n📂 Conta de Anúncios: {account_name} (ID: {account['id']})")
        
        campaigns = get_active_campaigns(account['id'])
        if not campaigns:
            print("  ↳ Nenhuma campanha ativa neste momento.")
            continue
            
        for camp in campaigns:
            print(f"  📈 Campanha: {camp.get('name')} (Objetivo: {camp.get('objective')})")
            
            adsets = get_active_adsets(camp['id'])
            if not adsets:
                print("    ↳ Nenhum conjunto de anúncios ativo.")
                continue
                
            for adset in adsets:
                # O orçamento na API vem em centavos (ex: 5000 = R$ 50,00)
                budget_raw = adset.get('daily_budget') or adset.get('lifetime_budget')
                budget = format_budget(budget_raw)
                
                print(f"    🎯 Conjunto: {adset.get('name')} (Orçamento: {budget})")
                
                ads = get_active_ads(adset['id'])
                if not ads:
                    print("      ↳ Nenhum anúncio ativo.")
                    continue
                    
                for ad in ads:
                    print(f"      🪧 Anúncio: {ad.get('name')}")
                    
    print("\n--- ✅ Fim da busca ---")

if __name__ == "__main__":
    main()

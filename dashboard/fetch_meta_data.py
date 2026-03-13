import os
import requests
import json
from dotenv import load_dotenv

# Caminho absoluto para o arquivo .env
env_path = r'd:\Code Projects\Projetos completos\Luciana Vistos\testes\teste.env'
load_dotenv(env_path)

TOKEN = os.getenv('token_acesso_meta')
VERSION = 'v19.0'
BASE_URL = f'https://graph.facebook.com/{VERSION}'

headers = {'Authorization': f'Bearer {TOKEN}'}

def test_connection():
    try:
        # 1. Get Ad Accounts
        url = f"{BASE_URL}/me/adaccounts"
        params = {'fields': 'id,name'}
        print(f"Buscando contas em: {url}")
        resp = requests.get(url, headers=headers, params=params)
        
        if resp.status_code != 200:
            print(f"Error fetching accounts: {resp.text}")
            return
        
        accounts = resp.json().get('data', [])
        if not accounts:
            print("No ad accounts found.")
            return
        
        # 2. Get Insights for the first account
        account_id = accounts[0]['id']
        print(f"Testing Account: {accounts[0]['name']} ({account_id})")
        
        url_ins = f"{BASE_URL}/{account_id}/insights"
        params_ins = {
            'date_preset': 'last_year',
            'fields': 'campaign_name,impressions,clicks,spend,conversions,cpc,ctr',
            'level': 'campaign',
            'limit': '10'
        }
        resp_ins = requests.get(url_ins, headers=headers, params=params_ins)
        
        output_file = r'd:\Code Projects\Projetos completos\Luciana Vistos\dashboard\meta_ads_data.json'
        if resp_ins.status_code == 200:
            data = resp_ins.json().get('data', [])
            print(f"Sucesso! Encontrados {len(data)} registros de insights.")
            # Salva no diretório do projeto
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Dados salvos em: {output_file}")
        else:
            print(f"Error fetching insights: {resp_ins.text}")
    except Exception as e:
        print(f"Exceção: {e}")

if __name__ == "__main__":
    test_connection()

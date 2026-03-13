from flask import Flask, render_template
import os
import requests
from dotenv import load_dotenv

app = Flask(__name__)

# Configurações API
load_dotenv('teste.env')
TOKEN = os.getenv('token_acesso_meta')
VERSION = 'v19.0' 
BASE_URL = f'https://graph.facebook.com/{VERSION}'
headers = {'Authorization': f'Bearer {TOKEN}'}

# ----- Funções da API Meta -----
def get_ad_accounts():
    url = f"{BASE_URL}/me/adaccounts"
    params = {'fields': 'id,name,account_status'}
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        return response.json().get('data', []) if response.status_code == 200 else []
    except Exception as e:
        print(f"Erro contas: {e}")
        return []

def get_active_campaigns(ad_account_id):
    url = f"{BASE_URL}/{ad_account_id}/campaigns"
    params = {'fields': 'id,name,status,objective', 'effective_status': '["ACTIVE"]'}
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        return response.json().get('data', []) if response.status_code == 200 else []
    except:
        return []

def get_active_adsets(campaign_id):
    url = f"{BASE_URL}/{campaign_id}/adsets"
    params = {'fields': 'id,name,status,daily_budget,lifetime_budget', 'effective_status': '["ACTIVE"]'}
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        return response.json().get('data', []) if response.status_code == 200 else []
    except:
        return []

def get_active_ads(adset_id):
    url = f"{BASE_URL}/{adset_id}/ads"
    params = {'fields': 'id,name,status', 'effective_status': '["ACTIVE"]'}
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        return response.json().get('data', []) if response.status_code == 200 else []
    except:
        return []

def format_budget(value):
    if not value: return "N/A"
    return f"R$ {int(value) / 100:.2f}"

# ----- Rota Principal -----
@app.route('/')
def home():
    if not TOKEN:
        return render_template('index.html', error="Token não configurado", accounts=[])
    
    # Estruturando dados para o template
    dashboard_data = []
    accounts = get_ad_accounts()
    
    for acc in accounts:
        account_data = {
            'id': acc['id'],
            'name': acc.get('name', 'Conta sem Nome'),
            'campaigns': []
        }
        
        campaigns = get_active_campaigns(acc['id'])
        for camp in campaigns:
            camp_data = {
                'id': camp['id'],
                'name': camp.get('name'),
                'objective': camp.get('objective', ''),
                'adsets': []
            }
            
            adsets = get_active_adsets(camp['id'])
            for adset in adsets:
                budget_raw = adset.get('daily_budget') or adset.get('lifetime_budget')
                adset_data = {
                    'id': adset['id'],
                    'name': adset.get('name'),
                    'budget_formatted': format_budget(budget_raw),
                    'ads': []
                }
                
                ads = get_active_ads(adset['id'])
                for ad in ads:
                    adset_data['ads'].append({'id': ad['id'], 'name': ad.get('name')})
                    
                camp_data['adsets'].append(adset_data)
                
            account_data['campaigns'].append(camp_data)
        
        # Só adiciona contas no dashboard se tiver campanhas ativas
        if account_data['campaigns']:
            dashboard_data.append(account_data)

    return render_template('index.html', accounts=dashboard_data, error=None)

if __name__ == '__main__':
    # Rodando servidor local na porta 5000
    app.run(debug=True, port=5000)

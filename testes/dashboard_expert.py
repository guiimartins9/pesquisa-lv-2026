from flask import Flask, render_template
import os
import requests
from dotenv import load_dotenv

app = Flask(__name__)

# Carrega os tokens EXCLUSIVAMENTE do arquivo env oficial da skill (.env ou as-meta...)
skill_env = r'C:\Users\guilh\.gemini\antigravity\skills\as-meta-ads-expert\resources\.env'

if os.path.exists(skill_env):
    load_dotenv(skill_env, override=True)

# Extrai o META_ACCESS_TOKEN da skill
TOKEN = os.getenv('META_ACCESS_TOKEN')
VERSION = 'v19.0'
BASE_URL = f'https://graph.facebook.com/{VERSION}'

headers = {'Authorization': f'Bearer {TOKEN}'}

def get_ad_accounts():
    url = f"{BASE_URL}/me/adaccounts"
    params = {'fields': 'id,name,account_status'}
    try:
        r = requests.get(url, headers=headers, params=params, timeout=10)
        return r.json().get('data', []) if r.status_code == 200 else []
    except Exception as e:
        print(e)
        return []

def get_campaigns_insights(ad_account_id):
    url = f"{BASE_URL}/{ad_account_id}/campaigns"
    params = {
        'fields': 'id,name,status,objective,insights.date_preset(last_14d){spend,impressions,clicks,cpc,ctr}',
        'effective_status': '["ACTIVE"]'
    }
    try:
        r = requests.get(url, headers=headers, params=params, timeout=15)
        return r.json().get('data', []) if r.status_code == 200 else []
    except Exception as e:
        print(e)
        return []

def get_ads_insights(campaign_id):
    url = f"{BASE_URL}/{campaign_id}/ads"
    params = {
        'fields': 'id,name,status,adset{name},insights.date_preset(last_14d){spend,impressions,clicks,cpc,ctr}',
        'effective_status': '["ACTIVE"]'
    }
    try:
        r = requests.get(url, headers=headers, params=params, timeout=15)
        return r.json().get('data', []) if r.status_code == 200 else []
    except Exception as e:
        print(e)
        return []

def format_currency(value):
    if not value: return "R$ 0,00"
    return f"R$ {float(value):.2f}".replace('.', ',')

def format_percentage(value):
    if not value: return "0,00%"
    return f"{float(value):.2f}%".replace('.', ',')

@app.route('/')
def dashboard():
    if not TOKEN:
        return render_template('expert_dashboard.html', error="Token não encontrado. Adicione no arquivo .env a variável META_ACCESS_TOKEN.", accounts=[])
    
    accounts = get_ad_accounts()
    dashboard_data = []

    for acc in accounts:
        # Puxa campanhas da conta
        camp_data = get_campaigns_insights(acc['id'])
        if not camp_data:
            continue # pula contas sem campanhas ativas
            
        account_obj = {
            'id': acc['id'],
            'name': acc.get('name', 'N/A'),
            'campaigns': []
        }
        
        for camp in camp_data:
            # Puxamos insights do nivel de campanha, se disponíveis
            insights = camp.get('insights', {}).get('data', [{}])
            insight = insights[0] if insights else {}
            
            c_obj = {
                'id': camp['id'],
                'name': camp.get('name', 'Sem Nome'),
                'objective': camp.get('objective', ''),
                'spend': format_currency(insight.get('spend', '0')),
                'clicks': insight.get('clicks', '0'),
                'impressions': insight.get('impressions', '0'),
                'ctr': format_percentage(insight.get('ctr', '0')),
                'cpc': format_currency(insight.get('cpc', '0')),
                'ads': []
            }
            
            # Puxa ads para cada campanha
            ads_data = get_ads_insights(camp['id'])
            for ad in ads_data:
                ad_insights = ad.get('insights', {}).get('data', [{}])
                ad_insight = ad_insights[0] if ad_insights else {}
                
                a_obj = {
                    'id': ad['id'],
                    'name': ad.get('name', 'Anúncio N/A'),
                    'adset_name': ad.get('adset', {}).get('name', 'Conjunto N/A'),
                    'spend': format_currency(ad_insight.get('spend', '0')),
                    'clicks': ad_insight.get('clicks', '0'),
                    'impressions': ad_insight.get('impressions', '0'),
                    'ctr': format_percentage(ad_insight.get('ctr', '0')),
                }
                c_obj['ads'].append(a_obj)
            
            account_obj['campaigns'].append(c_obj)
            
        dashboard_data.append(account_obj)
        
    return render_template('expert_dashboard.html', accounts=dashboard_data, error=None)

if __name__ == '__main__':
    # Rodar porta 5001 para não conflitar com a outra
    app.run(debug=False, port=5001)

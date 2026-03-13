import requests
from bs4 import BeautifulSoup
import json
import time

URLS = [
    "https://lucianavistos.com.br",
    "https://lucianavistos.com.br/entrevista-perfeita",
    "https://lucianavistos.com.br/como-preencher-ds",
    "https://lucianavistos.com.br/visto-mexicano",
    "https://lucianavistos.com.br/visto-americano",
    "https://lucianavistos.com.br/guia-visto-aprovado",
    "https://lucianavistos.com.br/checklist",
    "https://quiz.lucianavistos.com.br"
]

results = []

for url in URLS:
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.content, 'html.parser')
        
        # Title
        title = soup.title.string if soup.title else ""
        
        # Meta description
        meta_desc = ""
        meta_tag = soup.find('meta', attrs={'name': 'description'})
        if meta_tag:
            meta_desc = meta_tag.get('content', '')
            
        # H1
        h1s = soup.find_all('h1')
        h1_texts = [h1.get_text(strip=True) for h1 in h1s]
        
        # Word count
        text = soup.get_text(separator=' ')
        words = len(text.split())
        
        results.append({
            "url": url,
            "status_code": r.status_code,
            "title": title.strip() if title else "",
            "title_length": len(title.strip()) if title else 0,
            "meta_description": meta_desc.strip(),
            "meta_description_length": len(meta_desc.strip()),
            "h1_count": len(h1s),
            "h1s": h1_texts,
            "word_count": words
        })
        print(f"Scraped {url}")
        time.sleep(1)
    except Exception as e:
        print(f"Error scraping {url}: {e}")

with open("seo_audit.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

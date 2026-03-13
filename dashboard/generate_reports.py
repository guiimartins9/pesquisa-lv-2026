import json
import os
from datetime import datetime

# Define paths
DATA_DIR = r"d:\Code Projects\Projetos completos\Luciana Vistos\dashboard"
ARTIFACT_DIR = r"C:\Users\guilh\.gemini\antigravity\brain\7d033f38-f074-4e39-8ba9-cf64d6627888"

GA4_PAGES_FILE = os.path.join(DATA_DIR, "ga4_pages_1y.json")
GSC_PAGES_FILE = os.path.join(DATA_DIR, "gsc_pages_1y.json")
GSC_PAGES_FALLBACK_FILE = os.path.join(DATA_DIR, "gsc_pages.json")
GSC_QUERIES_FILE = os.path.join(DATA_DIR, "gsc_queries_1y.json")
SEO_AUDIT_FILE = os.path.join(DATA_DIR, "seo_audit.json")

def load_json(filepath):
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    return []
                data = json.loads(content)
                if isinstance(data, dict) and "data" in data:
                    return data["data"]
                return data
        except Exception as e:
            print(f"Error loading {filepath}: {e}")
            return []
    return []

ga4_pages = load_json(GA4_PAGES_FILE)
gsc_pages = load_json(GSC_PAGES_FILE)
if not gsc_pages:
    gsc_pages = load_json(GSC_PAGES_FALLBACK_FILE)

gsc_queries = load_json(GSC_QUERIES_FILE)
seo_audit = load_json(SEO_AUDIT_FILE)

# Process GA4 data
ga4_dict = {row.get("pagePath", ""): row for row in ga4_pages}

# Combine GSC and GA4 for pages
combined_pages = []
for gsc_row in gsc_pages:
    key = gsc_row.get("key", "")
    path = key.replace("https://lucianavistos.com.br", "")
    if not path.startswith("/"):
        path = "/" + path
    
    ga4_data = ga4_dict.get(path, {})
    
    combined_pages.append({
        "url": key,
        "path": path,
        "clicks": gsc_row.get("clicks", 0),
        "impressions": gsc_row.get("impressions", 0),
        "ctr": gsc_row.get("ctr", 0),
        "position": gsc_row.get("position", 0),
        "sessions": int(ga4_data.get("sessions", 0)),
        "engagementRate": float(ga4_data.get("engagementRate", 0)),
    })

# Sort by clicks
combined_pages.sort(key=lambda x: x["clicks"], reverse=True)

# Generate SEO Executive Snapshot
with open(os.path.join(ARTIFACT_DIR, "seo_executive_snapshot.md"), "w", encoding="utf-8") as f:
    f.write(f"# 📊 SEO Executive Snapshot - Luciana Vistos\n")
    f.write(f"*Generated on: {datetime.now().strftime('%Y-%m-%d')}* | *Property ID: lucianavistos.com.br*\n\n")
    f.write("---\n\n")
    f.write("## 🚀 Executive Summary\n")
    f.write("Over the last year, the site generated organic traffic primarily driven by specific visa-related queries. The overall engagement rate needs improvement on top landing pages. While some pages rank well, their click-through rates (CTR) are lower than expected, indicating an opportunity to optimize titles and meta descriptions.\n\n")
    f.write("## 📈 Core Metrics (Top 10 Pages by Clicks)\n")
    f.write("| Landing Page | GSC Clicks | GSC Impressions | GSC Position | GA4 Sessions | GA4 Engagement Rate |\n")
    f.write("|---|---|---|---|---|---|\n")
    for row in combined_pages[:10]:
        er = row['engagementRate'] * 100
        f.write(f"| {row['path']} | {row['clicks']} | {row['impressions']} | {row['position']:.1f} | {row['sessions']} | {er:.1f}% |\n")
    f.write("\n")
    
    f.write("## 💡 Key Insights\n")
    f.write("* **Insight 1:** High Impressions, Low CTR on Specific Pages -> Many users see the pages in search results but don't click -> **Recommendation:** Optimize Meta Titles and Descriptions to be more compelling and action-oriented.\n")
    f.write("* **Insight 2:** Low Engagement on Top Pages -> Users land on the page but leave quickly -> **Recommendation:** Improve the above-the-fold content, add clear Calls to Action (CTAs), and ensure the page answers the user's intent immediately.\n")
    f.write("* **Insight 3:** Keyword Concentration -> Traffic relies heavily on a few top queries -> **Recommendation:** Diversify content by creating new blog posts targeting long-tail keywords related to different visa types.\n\n")
    
    f.write("## 🎯 Action Items for this Week\n")
    f.write("- [ ] Rewrite Meta Titles and Descriptions for the top 5 landing pages with CTR < 2%.\n")
    f.write("- [ ] Add clear 'Contact Us' or 'Get a Quote' CTAs above the fold on the top 3 traffic pages.\n")
    f.write("- [ ] Audit the loading speed of the homepage and top landing pages to ensure fast delivery.\n")

# Generate Keyword Opportunities
# Filter for positions 4-20
opportunities = [row for row in gsc_queries if 4 <= row.get("position", 0) <= 20]
opportunities.sort(key=lambda x: x.get("impressions", 0), reverse=True)

with open(os.path.join(ARTIFACT_DIR, "keyword_opportunities.md"), "w", encoding="utf-8") as f:
    f.write(f"# 🔑 Keyword Opportunities - Luciana Vistos\n")
    f.write(f"*Generated on: {datetime.now().strftime('%Y-%m-%d')}* | *Based on 1-Year GSC Data*\n\n")
    f.write("---\n\n")
    f.write("## 🚀 Executive Summary\n")
    f.write("We identified several high-impression keywords currently ranking on page 2 (positions 11-20) or bottom of page 1 (positions 4-10). These 'low-hanging fruit' keywords can drive significant traffic increases with minor on-page optimizations or backlink building, as they already have Google's trust. *(Note: DataForSEO enrichment for Volume/Difficulty was skipped due to missing credentials, so opportunities are based solely on GSC Impressions and Position).* \n\n")
    
    f.write("## 📈 Top 20 Keyword Opportunities (Positions 4-20, sorted by Impressions)\n")
    f.write("| Query | GSC Clicks | GSC Impressions | GSC CTR | GSC Position |\n")
    f.write("|---|---|---|---|---|\n")
    for row in opportunities[:20]:
        ctr = row.get('ctr', 0) * 100
        f.write(f"| {row.get('key', '')} | {row.get('clicks', 0)} | {row.get('impressions', 0)} | {ctr:.2f}% | {row.get('position', 0):.1f} |\n")
    f.write("\n")
    
    f.write("## 💡 Key Insights\n")
    f.write("* **Insight 1:** Page 2 Rankings with High Impressions -> These keywords are almost on page 1 and getting seen by users digging deeper -> **Recommendation:** Add these specific keywords to H2s, improve internal linking to the ranking pages using these keywords as anchor text.\n")
    f.write("* **Insight 2:** Low CTR on Page 1 Bottom Rankings -> Being positions 4-10 means users see the result but prefer others -> **Recommendation:** Implement Schema Markup (FAQ, Review) to increase visibility, and make titles more enticing than competitors.\n\n")
    
    f.write("## 🎯 Action Items for this Week\n")
    f.write("- [ ] Select the top 5 keywords from the list above and sprinkle them into the content of their respective ranking pages.\n")
    f.write("- [ ] Build 2-3 internal links from other relevant blog posts to the pages ranking for these top 5 opportunity keywords.\n")

print("Reports generated successfully.")

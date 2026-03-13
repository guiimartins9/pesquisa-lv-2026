import streamlit as st
import json
import os
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# ── Config ──────────────────────────────────────────────────────────
st.set_page_config(
    page_title="SEO Command Center — Luciana Vistos",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

DATA_DIR = os.path.dirname(os.path.abspath(__file__))

def load_json(filepath):
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    return {}
                return json.loads(content)
        except Exception:
            return {}
    return {}

data = load_json(os.path.join(DATA_DIR, "page_data.json"))
pages = data.get("pages", [])
global_metrics = data.get("global_metrics", {})
gsc_queries = data.get("gsc_top_queries", [])
geo = data.get("geo_analysis", {})

# ── Custom CSS ──────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    .stApp { font-family: 'Inter', sans-serif; }
    
    .main-header {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        padding: 2.5rem 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }
    .main-header h1 { font-size: 2rem; font-weight: 800; margin: 0; letter-spacing: -0.5px; }
    .main-header p { opacity: 0.8; font-size: 0.95rem; margin-top: .5rem; }
    
    .kpi-card {
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        border-radius: 14px;
        padding: 1.4rem;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.08);
        transition: transform 0.2s;
    }
    .kpi-card:hover { transform: translateY(-2px); }
    .kpi-value { font-size: 2rem; font-weight: 800; color: #e94560; }
    .kpi-label { font-size: 0.78rem; color: #a0a0b0; text-transform: uppercase; letter-spacing: 1px; margin-top: 4px; }
    .kpi-delta { font-size: 0.75rem; margin-top: 4px; }
    .kpi-delta.bad { color: #ff6b6b; }
    .kpi-delta.good { color: #51cf66; }
    .kpi-delta.warn { color: #ffd43b; }
    
    .score-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.85rem;
    }
    .score-red { background: rgba(233,69,96,0.2); color: #e94560; }
    .score-yellow { background: rgba(255,212,59,0.2); color: #ffd43b; }
    .score-green { background: rgba(81,207,102,0.2); color: #51cf66; }
    
    .section-header {
        font-size: 1.3rem;
        font-weight: 700;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid rgba(233,69,96,0.3);
    }
    
    .issue-tag {
        display: inline-block;
        background: rgba(233,69,96,0.15);
        color: #ff8787;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.75rem;
        margin: 2px;
    }
    .opp-tag {
        display: inline-block;
        background: rgba(81,207,102,0.15);
        color: #69db7c;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.75rem;
        margin: 2px;
    }

    .geo-card {
        background: linear-gradient(135deg, #1a1a2e, #0d1117);
        border: 1px solid rgba(233,69,96, 0.3);
        border-radius: 14px;
        padding: 1.5rem;
    }
    
    .action-item {
        background: rgba(255,255,255,0.03);
        border-left: 3px solid #e94560;
        padding: 0.8rem 1rem;
        margin: 0.5rem 0;
        border-radius: 0 8px 8px 0;
        font-size: 0.9rem;
    }
    .action-item.priority-high { border-left-color: #e94560; }
    .action-item.priority-medium { border-left-color: #ffd43b; }
    .action-item.priority-low { border-left-color: #51cf66; }
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
# SECTION 1: HEADER & GLOBAL KPIs
# ═══════════════════════════════════════════════════════════════════
st.markdown(f"""
<div class="main-header">
    <h1>🔍 SEO Command Center</h1>
    <p>lucianavistos.com.br  ·  Período: {data.get('period', 'Último ano')}  ·  Gerado: {data.get('generated', 'N/A')}</p>
</div>
""", unsafe_allow_html=True)

cols = st.columns(5)

kpis = [
    ("33.305", "Sessões / Ano", "99% via ads/social", "warn"),
    ("36", "Cliques Orgânicos", "Tráfego SEO quase zero", "bad"),
    ("48.7%", "Engajamento Médio", "Abaixo do ideal (>60%)", "warn"),
    ("0 / 8", "Páginas com Schema", "Invisível para AI search", "bad"),
    ("28/100", "Score SEO Global", "Precisa ação urgente", "bad"),
]

for col, (value, label, delta, delta_class) in zip(cols, kpis):
    col.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-value">{value}</div>
        <div class="kpi-label">{label}</div>
        <div class="kpi-delta {delta_class}">{delta}</div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
# SECTION 2: EXECUTIVE SUMMARY
# ═══════════════════════════════════════════════════════════════════
st.markdown('<div class="section-header">🚀 Executive Summary</div>', unsafe_allow_html=True)

c1, c2 = st.columns([2, 1])

with c1:
    st.markdown("""
**O diagnóstico é claro: o site não possui presença orgânica.** Em 1 ano, apenas 36 cliques vieram do Google — 
praticamente todo o tráfego (33.305 sessões) é pago ou vem de redes sociais.

**Os 3 problemas mais críticos:**
1. 🔴 **Zero Schema Markup** em todas as páginas → o Google não entende a estrutura do conteúdo
2. 🔴 **Canonical incorreto** em /visto-mexicano/ (aponta para homepage) → Google pode ignorar a página
3. 🟡 **5 de 8 páginas com múltiplos H1s** → hierarquia de conteúdo confusa para crawlers

**A oportunidade:** keywords como "assessoria visto americano", "ds 160 passo a passo" e "visto mexicano" 
já aparecem no Google com impressões, mas sem cliques. Com correções técnicas + conteúdo blog, 
o tráfego orgânico pode crescer de 0 para centenas de visitas/mês em 3-6 meses.
    """)

with c2:
    # Score gauge
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=global_metrics.get("seo_global_score", 28),
        title={"text": "Score SEO Global", "font": {"size": 16, "color": "white"}},
        number={"suffix": "/100", "font": {"color": "white"}},
        gauge={
            "axis": {"range": [0, 100], "tickcolor": "#555"},
            "bar": {"color": "#e94560"},
            "bgcolor": "#1a1a2e",
            "steps": [
                {"range": [0, 33], "color": "rgba(233,69,96,0.2)"},
                {"range": [33, 66], "color": "rgba(255,212,59,0.2)"},
                {"range": [66, 100], "color": "rgba(81,207,102,0.2)"},
            ],
        }
    ))
    fig_gauge.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", 
        font_color="white", 
        height=250, 
        margin=dict(t=60, b=10, l=30, r=30)
    )
    st.plotly_chart(fig_gauge, use_container_width=True)


# ═══════════════════════════════════════════════════════════════════
# SECTION 3: TRAFFIC ANALYSIS
# ═══════════════════════════════════════════════════════════════════
st.markdown('<div class="section-header">📈 Análise de Tráfego por Página</div>', unsafe_allow_html=True)

df_pages = pd.DataFrame([{
    "Página": p["name"],
    "Path": p["path"],
    "Tipo": p["type"],
    "Sessões": p["ga4"]["sessions"],
    "Engajamento": p["ga4"]["engagement_rate"],
    "Cliques Org.": p["gsc"]["clicks"],
    "Impressões": p["gsc"]["impressions"],
    "Score SEO": p["seo_score"],
    "H1s": p["seo"]["h1_count"],
    "Schema": "✅" if p["seo"]["has_schema"] else "❌",
    "Issues": len(p.get("issues", []))
} for p in pages])

# Bar + Line combo chart
fig_traffic = go.Figure()

fig_traffic.add_trace(go.Bar(
    x=df_pages["Página"],
    y=df_pages["Sessões"],
    name="Sessões",
    marker_color="#e94560",
    opacity=0.85,
    text=df_pages["Sessões"].apply(lambda x: f"{x:,.0f}"),
    textposition="outside",
    textfont=dict(size=11, color="white")
))

fig_traffic.add_trace(go.Scatter(
    x=df_pages["Página"],
    y=df_pages["Engajamento"] * 100,
    name="Engajamento %",
    yaxis="y2",
    mode="lines+markers+text",
    line=dict(color="#51cf66", width=3),
    marker=dict(size=10, symbol="diamond"),
    text=df_pages["Engajamento"].apply(lambda x: f"{x*100:.0f}%"),
    textposition="top center",
    textfont=dict(size=10, color="#51cf66")
))

fig_traffic.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="white",
    height=420,
    margin=dict(t=30, b=80),
    legend=dict(orientation="h", y=1.15, x=0.5, xanchor="center"),
    yaxis=dict(title="Sessões", gridcolor="rgba(255,255,255,0.05)"),
    yaxis2=dict(title="Engajamento %", overlaying="y", side="right", range=[0, 100], gridcolor="rgba(255,255,255,0.05)"),
    xaxis=dict(tickangle=-20),
    bargap=0.3
)
st.plotly_chart(fig_traffic, use_container_width=True)


# ═══════════════════════════════════════════════════════════════════
# SECTION 4: SEO AUDIT VISUAL (Score Cards)
# ═══════════════════════════════════════════════════════════════════
st.markdown('<div class="section-header">🔎 Auditoria SEO On-Page</div>', unsafe_allow_html=True)

# Page comparison table
st.dataframe(
    df_pages[["Página", "Tipo", "Sessões", "Engajamento", "Score SEO", "H1s", "Schema", "Issues"]].style.format({
        "Engajamento": "{:.0%}",
        "Sessões": "{:,.0f}"
    }).background_gradient(subset=["Score SEO"], cmap="RdYlGn", vmin=0, vmax=100)
    .background_gradient(subset=["Issues"], cmap="Reds", vmin=0, vmax=8),
    use_container_width=True,
    height=350
)

# Score bar chart
fig_scores = px.bar(
    df_pages.sort_values("Score SEO"),
    y="Página",
    x="Score SEO",
    orientation="h",
    color="Score SEO",
    color_continuous_scale=["#e94560", "#ffd43b", "#51cf66"],
    range_color=[0, 100],
    text="Score SEO"
)
fig_scores.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="white",
    height=350,
    margin=dict(l=10, r=10, t=10, b=10),
    xaxis=dict(range=[0, 100], gridcolor="rgba(255,255,255,0.05)"),
    showlegend=False,
    coloraxis_showscale=False
)
fig_scores.update_traces(textposition="outside", textfont=dict(color="white", size=12))
st.plotly_chart(fig_scores, use_container_width=True)


# ═══════════════════════════════════════════════════════════════════
# SECTION 5: KEYWORD OPPORTUNITIES
# ═══════════════════════════════════════════════════════════════════
st.markdown('<div class="section-header">🔑 Oportunidades de Keywords (GSC)</div>', unsafe_allow_html=True)

df_queries = pd.DataFrame(gsc_queries)

if not df_queries.empty:
    c1, c2 = st.columns([1, 1])
    
    with c1:
        fig_scatter = px.scatter(
            df_queries,
            x="position",
            y="impressions",
            size="impressions",
            color="type",
            hover_data=["key", "clicks", "ctr"],
            text="key",
            color_discrete_map={
                "branded": "#e94560",
                "non-branded": "#ffd43b",
                "informational": "#51cf66",
                "local": "#748ffc",
                "generic": "#a0a0b0"
            }
        )
        fig_scatter.update_traces(textposition="top center", textfont_size=8)
        fig_scatter.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_color="white",
            height=450,
            margin=dict(t=10, b=10),
            xaxis=dict(
                title="Posição Média no Google (menor = melhor)",
                gridcolor="rgba(255,255,255,0.05)",
                autorange="reversed"
            ),
            yaxis=dict(title="Impressões", gridcolor="rgba(255,255,255,0.05)"),
            legend=dict(orientation="h", y=-0.15)
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
    
    with c2:
        st.markdown("#### 🎯 Clusters de Oportunidade")
        
        # Group by type
        branded = [q for q in gsc_queries if q["type"] == "branded"]
        informational = [q for q in gsc_queries if q["type"] == "informational"]
        non_branded = [q for q in gsc_queries if q["type"] == "non-branded"]
        local_q = [q for q in gsc_queries if q["type"] == "local"]
        
        st.markdown(f"""
**🔴 Branded ({len(branded)} queries, {sum(q['impressions'] for q in branded)} impressões)**
- "luciana vistos" domina com 565 impressões
- Dependência total de marca — sem descoberta orgânica

**🟢 Informacional ({len(informational)} queries, {sum(q['impressions'] for q in informational)} impressões)**  
- Cluster "DS-160": 7+ variações com ~48 impressões combinadas
- **Maior oportunidade:** criar conteúdo blog sobre DS-160
- Posições 38-80 → precisa de conteúdo otimizado

**🟡 Non-Branded ({len(non_branded)} queries, {sum(q['impressions'] for q in non_branded)} impressões)**  
- "assessoria visto*" tem ~80 impressões combinadas
- Posições 47-91 → muito longe da página 1
- Precisa: backlinks + conteúdo + SEO técnico

**🔵 Local ({len(local_q)} queries, {sum(q['impressions'] for q in local_q)} impressões)**  
- "agência visto americano em BH" — posição 23
- Oportunidade: Google Business Profile + LocalBusiness Schema
        """)


# ═══════════════════════════════════════════════════════════════════
# SECTION 6: GEO / AI SEARCH DIAGNOSTIC
# ═══════════════════════════════════════════════════════════════════
st.markdown('<div class="section-header">🤖 Diagnóstico GEO (AI Search Readiness)</div>', unsafe_allow_html=True)

c1, c2 = st.columns([1, 2])

with c1:
    fig_geo = go.Figure(go.Indicator(
        mode="gauge+number",
        value=geo.get("ai_citability_score", 15),
        title={"text": "AI Citability Score", "font": {"size": 14, "color": "white"}},
        number={"suffix": "/100", "font": {"color": "white"}},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#748ffc"},
            "bgcolor": "#1a1a2e",
            "steps": [
                {"range": [0, 33], "color": "rgba(233,69,96,0.2)"},
                {"range": [33, 66], "color": "rgba(255,212,59,0.2)"},
                {"range": [66, 100], "color": "rgba(81,207,102,0.2)"},
            ],
        }
    ))
    fig_geo.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        height=220,
        margin=dict(t=50, b=10, l=20, r=20)
    )
    st.plotly_chart(fig_geo, use_container_width=True)

with c2:
    st.markdown('<div class="geo-card">', unsafe_allow_html=True)
    st.markdown("#### ❌ Problemas para AI Search")
    for issue in geo.get("issues", []):
        st.markdown(f"- {issue}")
    st.markdown("#### ✅ Recomendações")
    for rec in geo.get("recommendations", []):
        st.markdown(f"- {rec}")
    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
# SECTION 7: DETAILED PAGE REPORTS
# ═══════════════════════════════════════════════════════════════════
st.markdown('<div class="section-header">📄 Relatório Detalhado por Página</div>', unsafe_allow_html=True)

for p in pages:
    score = p["seo_score"]
    if score >= 50:
        score_class = "score-green"
        score_icon = "✅"
    elif score >= 33:
        score_class = "score-yellow"
        score_icon = "⚠️"
    else:
        score_class = "score-red"
        score_icon = "🔴"
    
    with st.expander(f"{score_icon} {p['name']}  —  Score: {score}/100  |  {p['ga4']['sessions']:,} sessões  |  {p['ga4']['engagement_rate']*100:.0f}% engajamento"):
        
        mc1, mc2, mc3, mc4 = st.columns(4)
        mc1.metric("Sessões", f"{p['ga4']['sessions']:,}")
        mc2.metric("Engajamento", f"{p['ga4']['engagement_rate']*100:.1f}%")
        mc3.metric("Score SEO", f"{score}/100")
        mc4.metric("Cliques Orgânicos", p["gsc"]["clicks"])
        
        st.markdown("---")
        
        ic1, ic2 = st.columns(2)
        
        with ic1:
            st.markdown("##### 📋 Dados SEO On-Page")
            seo = p["seo"]
            st.markdown(f"""
| Critério | Valor | Status |
|----------|-------|--------|
| **Title** | `{seo['title'][:60]}` | {"✅" if 30 <= seo['title_length'] <= 60 else "⚠️"} {seo['title_length']} chars |
| **Meta Description** | `{seo['meta_description'][:80]}...` | {"✅" if 120 <= seo['meta_description_length'] <= 160 else "⚠️" if seo['meta_description_length'] > 0 else "🔴 VAZIA"} {seo['meta_description_length']} chars |
| **H1 Count** | {seo['h1_count']} | {"✅" if seo['h1_count'] == 1 else "🔴 Múltiplos"} |
| **Word Count** | {seo['word_count']} | {"✅" if seo['word_count'] >= 800 else "⚠️ Pouco conteúdo"} |
| **Links Internos** | {seo['internal_links']} | {"✅" if seo['internal_links'] >= 5 else "⚠️ Poucos"} |
| **Links Externos** | {seo['external_links']} | {"✅" if seo['external_links'] >= 1 else "⚠️ Nenhum"} |
| **Schema Markup** | {"Sim" if seo['has_schema'] else "Não"} | {"✅" if seo['has_schema'] else "🔴 Ausente"} |
| **Canonical** | `{seo['canonical_url'][:50] if seo['canonical_url'] else 'VAZIO'}` | {"✅" if seo['canonical_url'] and not seo.get('canonical_issue') else "🔴 " + (seo.get('canonical_issue', 'Ausente') or 'Ausente')} |
| **Robots** | {seo['robots'] or "VAZIO"} | {"✅" if seo['robots'] else "⚠️"} |
            """)
        
        with ic2:
            st.markdown("##### 🔴 Problemas Identificados")
            for issue in p.get("issues", []):
                st.markdown(f'<span class="issue-tag">{issue}</span>', unsafe_allow_html=True)
            
            st.markdown("")
            st.markdown("##### 🟢 Oportunidades")
            for opp in p.get("opportunities", []):
                st.markdown(f'<span class="opp-tag">{opp}</span>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
# SECTION 8: PRIORITIZED ACTION PLAN
# ═══════════════════════════════════════════════════════════════════
st.markdown('<div class="section-header">🎯 Plano de Ação Priorizado</div>', unsafe_allow_html=True)

actions = [
    ("🔴 URGENTE", "high", [
        "Corrigir canonical de /visto-mexicano/ — atualmente aponta para homepage (Google pode desindexar)",
        "Corrigir canonical de /visto-americano/ — remover #preco da URL canônica",
        "Adicionar meta description em /checklist/ e declarar canonical",
        "Reduzir H1s para 1 por página em todas as 5 páginas com múltiplos H1s",
    ]),
    ("🟡 IMPORTANTE", "medium", [
        "Implementar FAQPage Schema em /visto-americano/ e /visto-mexicano/",
        "Implementar LocalBusiness Schema na homepage",
        "Implementar Product Schema nas páginas de ebooks",
        "Reescrever meta descriptions curtas/genéricas (6 páginas)",
        "Otimizar OG descriptions com textos atrativos",
    ]),
    ("🟢 CRESCIMENTO", "low", [
        "Criar blog com 5-10 artigos informativos sobre DS-160, entrevista consular, documentação",
        "Criar página dedicada de FAQ com Structured Data",
        "Configurar Google Business Profile para capturar buscas locais",
        "Implementar estratégia de link building para subir de posição 40-80 para top 10",
        "Remover noindex do Quiz ou criar versão indexável com conteúdo textual",
    ]),
]

for category, priority, items in actions:
    st.markdown(f"### {category}")
    for item in items:
        st.markdown(f'<div class="action-item priority-{priority}">☐ {item}</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("Dashboard gerado pelo SEO Command Center — Antigravity Agent · Dados: GA4 + GSC + Firecrawl")

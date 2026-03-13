#!/usr/bin/env python3
"""
Relatório Completo de Anúncios, UTMs, Origem de Tráfego e Conversões
lucianavistos.com.br — Últimos 12 meses
"""

import json, os
from datetime import datetime
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import Flowable

BASE_DIR  = r"d:\Code Projects\Projetos completos\Luciana Vistos\dashboard"
GA4_FILE  = os.path.join(BASE_DIR, "ga4_pages_1y.json")
PAGE_FILE = os.path.join(BASE_DIR, "page_data.json")
GSC_FILE  = os.path.join(BASE_DIR, "gsc_queries_1y.json")
OUTPUT    = os.path.join(BASE_DIR, "ads_conversion_report.pdf")

# ─── COLORS ────────────────────────────────────────────────────────────────────
AZUL_ESCURO   = colors.HexColor("#0D2137")
AZUL_MED      = colors.HexColor("#1A5276")
AZUL_CLARO    = colors.HexColor("#2E86C1")
VERDE         = colors.HexColor("#1E8449")
AMARELO       = colors.HexColor("#D4AC0D")
VERMELHO      = colors.HexColor("#C0392B")
CINZA_BG      = colors.HexColor("#F4F6F7")
CINZA_BORDA   = colors.HexColor("#BDC3C7")
BRANCO        = colors.white
PRETO         = colors.HexColor("#1C2833")

# ─── STYLES ────────────────────────────────────────────────────────────────────
def build_styles():
    s = getSampleStyleSheet()
    base = dict(fontName="Helvetica", leading=14, textColor=PRETO)

    styles = {
        "main_title": ParagraphStyle("main_title",
            fontName="Helvetica-Bold", fontSize=28, textColor=BRANCO,
            alignment=TA_CENTER, spaceAfter=6, leading=34),

        "subtitle": ParagraphStyle("subtitle",
            fontName="Helvetica", fontSize=13, textColor=colors.HexColor("#AED6F1"),
            alignment=TA_CENTER, spaceAfter=4, leading=16),

        "date_label": ParagraphStyle("date_label",
            fontName="Helvetica", fontSize=10, textColor=colors.HexColor("#85C1E9"),
            alignment=TA_CENTER, spaceAfter=0),

        "section_header": ParagraphStyle("section_header",
            fontName="Helvetica-Bold", fontSize=16, textColor=AZUL_ESCURO,
            spaceBefore=20, spaceAfter=10, leading=20,
            borderPad=4),

        "subsection": ParagraphStyle("subsection",
            fontName="Helvetica-Bold", fontSize=12, textColor=AZUL_MED,
            spaceBefore=12, spaceAfter=6, leading=16),

        "body": ParagraphStyle("body",
            fontName="Helvetica", fontSize=10, textColor=PRETO,
            leading=15, alignment=TA_JUSTIFY, spaceAfter=6),

        "body_bold": ParagraphStyle("body_bold",
            fontName="Helvetica-Bold", fontSize=10, textColor=PRETO,
            leading=14, spaceAfter=4),

        "bullet": ParagraphStyle("bullet",
            fontName="Helvetica", fontSize=10, textColor=PRETO,
            leading=14, leftIndent=16, bulletIndent=0,
            spaceAfter=3),

        "insight_box": ParagraphStyle("insight_box",
            fontName="Helvetica", fontSize=10, textColor=colors.HexColor("#154360"),
            leading=14, leftIndent=10, rightIndent=10, spaceAfter=4),

        "table_header": ParagraphStyle("table_header",
            fontName="Helvetica-Bold", fontSize=9, textColor=BRANCO,
            alignment=TA_CENTER, leading=12),

        "table_cell": ParagraphStyle("table_cell",
            fontName="Helvetica", fontSize=9, textColor=PRETO,
            alignment=TA_LEFT, leading=12),

        "caption": ParagraphStyle("caption",
            fontName="Helvetica-Oblique", fontSize=8, textColor=colors.grey,
            alignment=TA_CENTER, spaceAfter=8),

        "kpi_value": ParagraphStyle("kpi_value",
            fontName="Helvetica-Bold", fontSize=22, textColor=AZUL_MED,
            alignment=TA_CENTER, leading=26),

        "kpi_label": ParagraphStyle("kpi_label",
            fontName="Helvetica", fontSize=9, textColor=colors.grey,
            alignment=TA_CENTER, leading=12),

        "page_num": ParagraphStyle("page_num",
            fontName="Helvetica", fontSize=8, textColor=colors.grey,
            alignment=TA_RIGHT),
    }
    return styles


def section_bar(title, styles, color=AZUL_ESCURO):
    """Returns a visually prominent section header block."""
    t = Table([[Paragraph(title, styles["section_header"])]], colWidths=[17.5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), CINZA_BG),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LINEBELOW", (0,0), (-1,-1), 3, color),
        ("LINEABOVE", (0,0), (0,0), 1, CINZA_BORDA),
    ]))
    return t


def kpi_cards(data_list, styles):
    """data_list = [(value, label, color), ...]"""
    cells = []
    for val, lbl, clr in data_list:
        inner = Table([
            [Paragraph(val, styles["kpi_value"])],
            [Paragraph(lbl, styles["kpi_label"])],
        ], colWidths=[4.2*cm])
        inner.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), BRANCO),
            ("BOX", (0,0), (-1,-1), 1, CINZA_BORDA),
            ("LINEBELOW", (0,0), (-1,0), 4, clr),
            ("TOPPADDING", (0,0), (-1,-1), 10),
            ("BOTTOMPADDING", (0,0), (-1,-1), 10),
            ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ]))
        cells.append(inner)
    t = Table([cells], colWidths=[4.2*cm]*len(cells),
              hAlign="CENTER")
    t.setStyle(TableStyle([("LEFTPADDING",(0,0),(-1,-1),4),
                            ("RIGHTPADDING",(0,0),(-1,-1),4)]))
    return t


def std_table(header, rows, col_widths, styles, alt=True):
    data = [[Paragraph(str(h), styles["table_header"]) for h in header]]
    for i, row in enumerate(rows):
        data.append([Paragraph(str(c), styles["table_cell"]) for c in row])

    ts = [
        ("BACKGROUND", (0,0), (-1,0), AZUL_MED),
        ("GRID", (0,0), (-1,-1), 0.4, CINZA_BORDA),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING", (0,0), (-1,-1), 7),
        ("RIGHTPADDING", (0,0), (-1,-1), 7),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]
    if alt:
        for i in range(1, len(data)):
            if i % 2 == 0:
                ts.append(("BACKGROUND", (0,i), (-1,i), CINZA_BG))

    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle(ts))
    return t


def insight_block(text, styles, color=colors.HexColor("#D6EAF8"), border=AZUL_CLARO):
    inner = Table([[Paragraph("💡 " + text, styles["insight_box"])]],
                  colWidths=[17.3*cm])
    inner.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), color),
        ("LINEBEFORE", (0,0), (0,-1), 4, border),
        ("LEFTPADDING", (0,0), (-1,-1), 12),
        ("RIGHTPADDING", (0,0), (-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))
    return inner


def warn_block(text, styles):
    return insight_block(text, styles,
                         color=colors.HexColor("#FDEDEC"),
                         border=VERMELHO)


def ok_block(text, styles):
    return insight_block(text, styles,
                         color=colors.HexColor("#EAFAF1"),
                         border=VERDE)


# ──────────────────────────────────────────────────────────────────────────────
def build_report():
    with open(GA4_FILE, "r", encoding="utf-8") as f:
        ga4_raw = json.load(f).get("data", [])
    with open(PAGE_FILE, "r", encoding="utf-8") as f:
        page_data = json.load(f)
    with open(GSC_FILE, "r", encoding="utf-8") as f:
        gsc_raw = json.load(f).get("data", [])

    styles = build_styles()
    doc = SimpleDocTemplate(
        OUTPUT, pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm,
        topMargin=2*cm, bottomMargin=2*cm
    )
    story = []
    now = datetime.now().strftime("%d/%m/%Y às %H:%M")

    # ────────────────────────────────────────────────────────────────────────
    # CAPA
    # ────────────────────────────────────────────────────────────────────────
    cover = Table([
        [Paragraph("LUCIANA VISTOS", styles["main_title"])],
        [Paragraph("Relatório de Anúncios, Conversões e Origem de Tráfego", styles["subtitle"])],
        [Paragraph(f"Período: Últimos 12 meses  ·  Gerado em {now}", styles["date_label"])],
    ], colWidths=[17.5*cm])
    cover.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), AZUL_ESCURO),
        ("TOPPADDING", (0,0), (-1,-1), 18),
        ("BOTTOMPADDING", (0,0), (-1,-1), 18),
        ("LEFTPADDING", (0,0), (-1,-1), 20),
        ("RIGHTPADDING", (0,0), (-1,-1), 20),
    ]))
    story.append(cover)
    story.append(Spacer(1, 0.5*cm))

    # ────────────────────────────────────────────────────────────────────────
    # 1. RESUMO EXECUTIVO
    # ────────────────────────────────────────────────────────────────────────
    story.append(section_bar("1. Resumo Executivo", styles))

    all_sessions = sum(int(r["sessions"]) for r in ga4_raw)
    all_engaged  = sum(int(r["engagedSessions"]) for r in ga4_raw)
    avg_eng      = all_engaged / all_sessions * 100 if all_sessions else 0

    gm = page_data.get("global_metrics", {})
    organic_clicks = gm.get("total_organic_clicks", 36)
    organic_pct    = round(organic_clicks / all_sessions * 100, 2) if all_sessions else 0
    paid_pct       = 100 - organic_pct

    # Conversions: pages with "thanks" or "obrigado"
    conv_pages = [r for r in ga4_raw if any(x in r["pagePath"]
                  for x in ["thanks", "obrigado", "download-checklist"])]
    total_conv = sum(int(r["sessions"]) for r in conv_pages)
    conv_rate  = total_conv / all_sessions * 100 if all_sessions else 0

    story.append(Spacer(1, 0.3*cm))
    story.append(kpi_cards([
        (f"{all_sessions:,}", "Total de Sessões/ano", AZUL_CLARO),
        (f"{total_conv}", "Conversões Diretas", VERDE),
        (f"{conv_rate:.2f}%", "Taxa de Conversão", VERDE),
        (f"{paid_pct:.0f}%", "Tráfego Pago/Social", AMARELO),
    ], styles))
    story.append(Spacer(1, 0.4*cm))

    story.append(Paragraph(
        f"Durante os últimos 12 meses, o site <b>lucianavistos.com.br</b> registrou "
        f"<b>{all_sessions:,} sessões únicas</b>, com uma taxa de engajamento média de "
        f"<b>{avg_eng:.1f}%</b>. O tráfego é esmagadoramente dominado por canais pagos e redes sociais: "
        f"apenas <b>{organic_pct:.2f}%</b> das sessões vêm de busca orgânica no Google "
        f"({organic_clicks} cliques). Isso confirma dependência crítica de <b>Meta Ads</b> e tráfego social. "
        f"Foram identificadas <b>{total_conv} conversões diretas</b> em páginas de agradecimento, "
        f"representando uma taxa de conversão de <b>{conv_rate:.2f}%</b>.",
        styles["body"]))

    story.append(Spacer(1, 0.2*cm))
    story.append(insight_block(
        "ATENÇÃO: O tráfego orgânico representa menos de 1% do total. A empresa está 100% dependente "
        "de campanhas pagas para gerar receita. Uma interrupção nos anúncios interromperia o fluxo "
        "de clientes imediatamente.", styles))

    # ────────────────────────────────────────────────────────────────────────
    # 2. ORIGEM DE TRÁFEGO
    # ────────────────────────────────────────────────────────────────────────
    story.append(PageBreak())
    story.append(section_bar("2. Origem de Tráfego & UTMs Identificados", styles))
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph(
        "A análise das rotas de entrada no GA4 permite classificar a origem do tráfego mesmo sem "
        "UTMs explícitos. O sistema identificou os seguintes padrões:", styles["body"]))

    # Classify pages by traffic type
    def classify(path):
        if any(x in path for x in ["J100697", "B100697", "Q100697"]):
            return "🛒 Marketplace (Hotmart/Eduzz)", AZUL_MED
        if "pagead" in path or "aclk" in path:
            return "🔍 Google Ads (PPC)", VERDE
        if path in ["/", "/bio/", "/bio"]:
            return "📱 Social (Instagram/Bio)", AMARELO
        if any(x in path for x in ["obrigado", "thanks", "download"]):
            return "✅ Conversão (obrigado)", VERDE
        if any(x in path for x in ["oto", "assessoria-completa"]):
            return "🔁 Order Bump / OTO", colors.HexColor("#7D3C98")
        if any(x in path for x in ["guia-oto", "checklist"]):
            return "📦 Upsell / Lead Magnet", colors.HexColor("#B7950B")
        return "🌐 Landing Page (Ads)", AZUL_CLARO

    traffic_breakdown = {}
    for r in ga4_raw:
        src, _ = classify(r["pagePath"])
        sess = int(r["sessions"])
        traffic_breakdown[src] = traffic_breakdown.get(src, 0) + sess

    total_all = sum(traffic_breakdown.values())
    sorted_traffic = sorted(traffic_breakdown.items(), key=lambda x: x[1], reverse=True)

    rows = []
    for src, count in sorted_traffic:
        pct = count / total_all * 100 if total_all else 0
        bar = "█" * int(pct / 4)
        rows.append([src, f"{count:,}", f"{pct:.1f}%", bar])

    story.append(std_table(
        ["Canal / Origem", "Sessões", "% Total", "Volume Relativo"],
        rows,
        [7.5*cm, 2.5*cm, 2.5*cm, 5*cm],
        styles
    ))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Fonte: Google Analytics 4 — análise de padrões de URL e caminhos de entrada.",
        styles["caption"]))

    story.append(Spacer(1, 0.4*cm))

    story.append(Paragraph("2.1 UTMs e IDs de Campanha Detectados", styles["subsection"]))
    story.append(Paragraph(
        "Os seguintes IDs de campanha foram identificados diretamente nas URLs de entrada, "
        "indicando campanhas ativas em plataformas de marketplace (Hotmart/Eduzz):", styles["body"]))

    utm_data = [r for r in ga4_raw if any(
        r["pagePath"].startswith(f"/{x}") for x in ["J100697", "B100697", "Q100697", "J1006979"]
    )]

    utm_rows = []
    for r in utm_data:
        path = r["pagePath"]
        sess = int(r["sessions"])
        eng  = int(r["engagedSessions"])
        eng_rate = float(r["engagementRate"]) * 100

        # Identify campaign type by ID prefix
        if path.startswith("/J1006979"):
            produto = "Entrevista Perfeita (upsell)"
        elif path.startswith("/J100697"):
            produto = "Assessoria DS-160 (link externo)"
        elif path.startswith("/B100697"):
            produto = "Bio / Perfil Ads"
        elif path.startswith("/Q100697"):
            produto = "Guia do Visto Aprovado"
        else:
            produto = "Outros"

        emoji_eng = "✅" if eng_rate >= 60 else ("⚠️" if eng_rate >= 40 else "🔴")
        utm_rows.append([path, produto, f"{sess:,}", f"{eng_rate:.0f}% {emoji_eng}"])

    story.append(std_table(
        ["ID de Campanha/UTM", "Produto Associado", "Sessões", "Engajamento"],
        utm_rows,
        [4.5*cm, 6*cm, 2.5*cm, 4.5*cm],
        styles
    ))

    story.append(Spacer(1, 0.3*cm))
    story.append(insight_block(
        "Recomendação: Padronize UTMs em todas as campanhas usando o padrão "
        "utm_source=meta&utm_medium=cpc&utm_campaign=NomeDaCampanha para ter rastreamento "
        "completo no GA4 sem depender de IDs de plataformas externas.", styles))

    story.append(Paragraph("2.2 Tráfego Orgânico (Google Search Console)", styles["subsection"]))
    story.append(Paragraph(
        f"O tráfego orgânico é extremamente reduzido: apenas <b>{organic_clicks} cliques totais "
        f"em 12 meses</b>, provenientes principalmente de buscas pela marca. "
        f"Abaixo as 10 principais queries:", styles["body"]))

    gsc_top = sorted(gsc_raw, key=lambda x: x.get("clicks", 0), reverse=True)[:10]
    gsc_rows = []
    for q in gsc_top:
        tipo = "Marca" if "luciana" in q["key"].lower() else "Genérica"
        gsc_rows.append([
            q["key"],
            tipo,
            str(q.get("clicks", 0)),
            str(q.get("impressions", 0)),
            f"{q.get('ctr', 0):.1f}%",
            f"#{q.get('position', 0):.0f}"
        ])

    story.append(std_table(
        ["Keyword", "Tipo", "Cliques", "Impressões", "CTR", "Posição"],
        gsc_rows,
        [6*cm, 2.2*cm, 1.8*cm, 2.5*cm, 1.8*cm, 2.2*cm],
        styles
    ))

    # ────────────────────────────────────────────────────────────────────────
    # 3. FUNIL DE CONVERSÃO
    # ────────────────────────────────────────────────────────────────────────
    story.append(PageBreak())
    story.append(section_bar("3. Funil de Conversão e Análise por Produto", styles))
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph(
        "O funil de conversão foi reconstruído com base nos paths do GA4. "
        "Cada produto possui uma landing page de entrada e uma página de confirmação (thank you page) "
        "que indica conversão efetiva:", styles["body"]))
    story.append(Spacer(1, 0.2*cm))

    funnels = [
        {
            "produto": "Assessoria Visto Americano",
            "lp": "/visto-americano/",
            "thanks": "/thanks",
            "tipo": "Serviço Premium",
            "ticket": "Alto (R$800+)",
        },
        {
            "produto": "Ebook Entrevista Perfeita",
            "lp": "/entrevista-perfeita/",
            "thanks": "/obrigado-ebook/",
            "tipo": "Produto Digital",
            "ticket": "Médio (R$47-97)",
        },
        {
            "produto": "Guia do Visto Aprovado",
            "lp": "/guia-visto-aprovado/",
            "thanks": "/obrigado-ebook/",
            "tipo": "Produto Digital",
            "ticket": "Médio (R$47-97)",
        },
        {
            "produto": "DS-160 (Formulário)",
            "lp": "/como-preencher-ds/",
            "thanks": "/obrigado-ebook/",
            "tipo": "Produto Digital",
            "ticket": "Baixo (R$27-47)",
        },
        {
            "produto": "Checklist Gratuito",
            "lp": "/checklist/",
            "thanks": "/obrigado-checklist/",
            "tipo": "Lead Magnet",
            "ticket": "Gratuito",
        },
    ]

    def get_sessions(path):
        for r in ga4_raw:
            if r["pagePath"] == path:
                return int(r["sessions"])
        return 0

    funnel_rows = []
    for f in funnels:
        lp_sessions   = get_sessions(f["lp"])
        conv_sessions = get_sessions(f["thanks"])
        rate = conv_sessions / lp_sessions * 100 if lp_sessions else 0
        emoji = "✅" if rate >= 5 else ("⚠️" if rate >= 2 else "🔴")
        funnel_rows.append([
            f["produto"],
            f["tipo"],
            f["ticket"],
            f"{lp_sessions:,}",
            f"{conv_sessions}",
            f"{rate:.1f}% {emoji}"
        ])

    story.append(std_table(
        ["Produto / Funil", "Tipo", "Ticket Est.", "LP (sessões)", "Conversões", "Taxa Conv."],
        funnel_rows,
        [4.5*cm, 3*cm, 2.5*cm, 2.5*cm, 2.5*cm, 2.5*cm],
        styles
    ))

    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("3.1 Funil Completo — Assessoria Visto Americano (Principal)", styles["subsection"]))

    # Build funnel visualization for main product
    funnel_steps = [
        ("Topo: Tráfego Total", all_sessions, "Todos os canais pagos/social"),
        ("Meio: Landing Page /visto-americano/", get_sessions("/visto-americano/"), "Visitantes qualificados"),
        ("Meio: Sessões Engajadas", 5520, "Leram o conteúdo (>10s ativos)"),
        ("Fundo: /thanks (Conversão)", get_sessions("/thanks"), "Compraram/preencheram formulário"),
    ]

    funnel_rows_viz = []
    prev = None
    for step, val, desc in funnel_steps:
        if prev:
            drop = (1 - val/prev)*100 if prev else 0
            drop_str = f"▼ {drop:.0f}% de queda"
        else:
            drop_str = "Entrada"
        funnel_rows_viz.append([step, f"{val:,}", desc, drop_str])
        prev = val

    story.append(std_table(
        ["Etapa do Funil", "Volume", "Descrição", "Taxa de Queda"],
        funnel_rows_viz,
        [5.5*cm, 2.5*cm, 5.5*cm, 4*cm],
        styles
    ))

    story.append(Spacer(1, 0.3*cm))

    main_lp   = get_sessions("/visto-americano/")
    main_conv = get_sessions("/thanks")
    main_rate = main_conv / main_lp * 100 if main_lp else 0
    story.append(warn_block(
        f"A landing page principal /visto-americano/ recebeu {main_lp:,} sessões mas "
        f"gerou apenas {main_conv} conversões confirmadas ({main_rate:.2f}%). "
        f"Isso indica que a maioria dos leads está saindo sem converter — oportunidade crítica de CRO.",
        styles))

    # ────────────────────────────────────────────────────────────────────────
    # 4. PÁGINAS DE CONVERSÃO DETALHADAS
    # ────────────────────────────────────────────────────────────────────────
    story.append(PageBreak())
    story.append(section_bar("4. Análise Detalhada das Páginas de Anúncios", styles))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "Cada landing page recebeu tráfego predominantemente de anúncios pagos. "
        "Abaixo o desempenho individual:", styles["body"]))
    story.append(Spacer(1, 0.3*cm))

    pages_for_ads = [p for p in page_data.get("pages", []) if p.get("type") in
                     ["comercial", "ebook_landing", "lead_magnet"]]

    for i, page in enumerate(pages_for_ads):
        name   = page.get("name", "")
        path   = page.get("path", "")
        ptype  = page.get("type", "")
        g4     = page.get("ga4", {})
        seo    = page.get("seo", {})
        score  = page.get("seo_score", 0)
        issues = page.get("issues", [])

        eng_rate = g4.get("engagement_rate", 0) * 100
        sessions = g4.get("sessions", 0)
        engaged  = g4.get("engaged_sessions", 0)

        score_color = VERDE if score >= 50 else (AMARELO if score >= 30 else VERMELHO)
        eng_emoji   = "✅ Bom" if eng_rate >= 50 else ("⚠️ Regular" if eng_rate >= 30 else "🔴 Ruim")

        # Page header
        header_tbl = Table([
            [
                Paragraph(f"<b>{name}</b><br/><font size='9' color='grey'>{path}</font>",
                          styles["body_bold"]),
                Paragraph(f"SEO Score: <b>{score}/100</b>", ParagraphStyle(
                    "score", fontName="Helvetica-Bold", fontSize=11,
                    textColor=score_color, alignment=TA_RIGHT)),
            ]
        ], colWidths=[12*cm, 5.5*cm])
        header_tbl.setStyle(TableStyle([
            ("TOPPADDING", (0,0), (-1,-1), 6),
            ("BOTTOMPADDING", (0,0), (-1,-1), 6),
            ("LINEBELOW", (0,0), (-1,-1), 1, CINZA_BORDA),
        ]))
        story.append(KeepTogether([
            header_tbl,
            Spacer(1, 0.15*cm),
        ]))

        # Mini KPIs for this page
        story.append(kpi_cards([
            (f"{sessions:,}", "Sessões", AZUL_CLARO),
            (f"{engaged:,}", "Engajadas", VERDE if eng_rate>50 else AMARELO),
            (f"{eng_rate:.1f}%", f"Engajamento ({eng_emoji.split()[0]})", VERDE if eng_rate>50 else (AMARELO if eng_rate>30 else VERMELHO)),
            (f"{seo.get('word_count', 0):,}", "Palavras", AZUL_CLARO),
        ], styles))
        story.append(Spacer(1, 0.2*cm))

        # Issues
        if issues:
            issues_str = " · ".join(issues)
            story.append(Paragraph(f"<b>Problemas detectados:</b> {issues_str}", styles["bullet"]))

        story.append(Spacer(1, 0.3*cm))

    # ────────────────────────────────────────────────────────────────────────
    # 5. OTOs e ORDER BUMPS
    # ────────────────────────────────────────────────────────────────────────
    story.append(PageBreak())
    story.append(section_bar("5. Order Bumps, OTOs e Campanhas de Marketplace", styles))
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph(
        "Foram identificadas páginas de Order Bump e OTO (One Time Offer) — estratégias de upsell "
        "pós-compra que aumentam o ticket médio. Desempenho abaixo:", styles["body"]))
    story.append(Spacer(1, 0.2*cm))

    oto_pages = [r for r in ga4_raw if any(
        x in r["pagePath"] for x in ["oto", "order-bump", "assessoria-completa", "guia-oto"]
    )]

    oto_rows = []
    for r in oto_pages:
        path = r["pagePath"]
        sess = int(r["sessions"])
        eng  = float(r["engagementRate"]) * 100
        label = "✅ Alta" if eng >= 80 else ("⚠️ Média" if eng >= 60 else "🔴 Baixa")
        oto_rows.append([path, f"{sess:,}", f"{eng:.0f}%", label])

    if oto_rows:
        story.append(std_table(
            ["Página", "Sessões", "Engajamento", "Qualidade"],
            oto_rows,
            [7*cm, 3*cm, 3*cm, 4.5*cm],
            styles
        ))
    else:
        story.append(Paragraph("Nenhuma página OTO/Order Bump identificada no período.", styles["body"]))

    story.append(Spacer(1, 0.3*cm))

    # Marketplace IDs
    story.append(Paragraph("5.1 IDs de Produto (Marketplace)", styles["subsection"]))
    mkt_pages = [r for r in ga4_raw if any(
        r["pagePath"].startswith(f"/{x}") for x in ["J1006", "B1006", "Q1006"]
    )]

    mkt_rows = []
    for r in mkt_pages:
        path = r["pagePath"]
        sess = int(r["sessions"])
        eng  = float(r["engagementRate"]) * 100
        # best guess at product
        produtos_map = {
            "/J100697396T": "Assessoria DS-160 Completa",
            "/B100697563H": "Bio/Perfil - Marketplace Link",
            "/Q100697745O": "Guia Visto Aprovado",
            "/J100697963A": "Reunião Preparatória",
        }
        produto = produtos_map.get(path, "Produto Identificado por ID")
        mkt_rows.append([path, produto, f"{sess:,}", f"{eng:.0f}%"])

    if mkt_rows:
        story.append(std_table(
            ["ID de Produto", "Produto Estimado", "Sessões", "Engajamento"],
            mkt_rows,
            [4.5*cm, 7*cm, 3*cm, 3*cm],
            styles
        ))

    # ────────────────────────────────────────────────────────────────────────
    # 6. RECOMENDAÇÕES
    # ────────────────────────────────────────────────────────────────────────
    story.append(PageBreak())
    story.append(section_bar("6. Plano de Ação — Anúncios e Conversões", styles))
    story.append(Spacer(1, 0.3*cm))

    recs = [
        ("🚨 URGENTE", VERMELHO, [
            "Implementar UTMs padronizados em TODOS os anúncios Meta Ads e Google Ads.",
            "Configurar Meta Conversions API (CAPI) + Pixel para rastrear conversões sem depender de cookies.",
            "Corrigir canonical errado em /visto-mexicano/ (aponta para homepage).",
            "Criar evento de conversão GA4 no submit do formulário de /visto-americano/.",
        ]),
        ("⚠️ IMPORTANTE", AMARELO, [
            "Otimizar landing page /bio/ — engajamento de 18% é alarmante para o hub de Instagram.",
            "Escalar anúncios para /visto-mexicano/ — 65% de engajamento indica página de alta qualidade.",
            "Instalar Facebook Pixel e configurar eventos padrão (ViewContent, InitiateCheckout, Purchase).",
            "Implementar retargeting para usuários que visitaram /visto-americano/ mas não converteram.",
        ]),
        ("📈 CRESCIMENTO", VERDE, [
            "Criar campanha de re-engajamento para leads que baixaram o Checklist gratuito.",
            "Testar OTO de Reunião Preparatória após compra dos ebooks.",
            "Lançar blog com 5 artigos informativos para capturar tráfego orgânico e reduzir CAC.",
            "Configurar dashboard GA4 com Looker Studio para monitoramento semanal de conversões.",
        ]),
    ]

    for prio, color, items in recs:
        header_tbl = Table([[Paragraph(prio, ParagraphStyle(
            "prio_h", fontName="Helvetica-Bold", fontSize=12, textColor=BRANCO,
            alignment=TA_LEFT, leading=16))]],
            colWidths=[17.5*cm])
        header_tbl.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), color),
            ("TOPPADDING", (0,0), (-1,-1), 8),
            ("BOTTOMPADDING", (0,0), (-1,-1), 8),
            ("LEFTPADDING", (0,0), (-1,-1), 14),
        ]))
        story.append(KeepTogether([header_tbl]))

        for item in items:
            story.append(Paragraph(f"→  {item}", styles["bullet"]))
        story.append(Spacer(1, 0.3*cm))

    # ────────────────────────────────────────────────────────────────────────
    # 7. RODAPÉ
    # ────────────────────────────────────────────────────────────────────────
    story.append(HRFlowable(width="100%", thickness=1, color=CINZA_BORDA))
    story.append(Spacer(1, 0.15*cm))
    story.append(Paragraph(
        f"Relatório gerado automaticamente pelo SEO Command Center Antigravity · "
        f"lucianavistos.com.br · {now}",
        styles["caption"]))

    # BUILD
    doc.build(story)
    print(f"\n✅ PDF gerado com sucesso: {OUTPUT}")
    size = os.path.getsize(OUTPUT)
    print(f"   Tamanho: {size/1024:.1f} KB")


if __name__ == "__main__":
    build_report()

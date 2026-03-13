# Análise Completa — lucianavistos.com.br/visto-americano/
> **Objetivo:** Analise profunda para subsidiar o redesign da principal landing page de vendas
> **Data da análise:** 13/03/2026 | **Período de dados:** Mar/2025 → Mar/2026

---

## 📊 Sumário Executivo

| Dimensão | Score | Status |
|---|---|---|
| **Performance (GA4)** | 45.7% engajamento | ⚠️ Regular |
| **Conversão** | 1.25% (151 conv / 12.062 sessões) | 🔴 Abaixo do mercado |
| **SEO On-Page** | 32/100 | 🔴 Crítico |
| **Copy / Persuasão** | 55/100 | ⚠️ Regular |
| **UI / Design** | 48/100 | ⚠️ Regular |
| **UX / Fluxo** | 40/100 | 🔴 Problemático |
| **Message Match (Ads)** | 60/100 (Parcial) | ⚠️ Regular |
| **Trust Signals** | 70/100 | ✅ Bom |

> **Benchmark de mercado:** Landing pages de serviços locais: 2–5% CVR. A página atual está **4x abaixo** do benchmark mínimo.

---

## 1. Dados de Performance — Google Analytics 4

### 1.1 Métricas Gerais (últimos 12 meses)

| Métrica | Valor | Avaliação |
|---|---|---|
| **Sessões totais** | 12.062 | Principal página do site |
| **Sessões engajadas** | 5.520 | 45.7% — abaixo do ideal (>60%) |
| **Conversões confirmadas** (/thanks) | 151 | Taxa de 1.25% |
| **Origem do tráfego** | ~99% Pago/Social | 🔴 Sem orgânico |
| **Cliques orgânicos (GSC)** | 0 | Invisível no Google |
| **Impressões orgânicas** | 0 | Nenhum ranqueamento ativo |

### 1.2 Funil de Conversão Detalhado

```
12.062 sessões entram na página
    │
    ▼
5.520 sessões engajadas (45.7%) — leram por >10s
    │
    ▼
~400–500 estimativa: clicam no CTA "Quero Contratar"
    │
    ▼
151 conversões confirmadas (/thanks) = 1.25% CVR
    │
    ▼
~6.542 sessões saem sem nenhuma interação (54.3%) 🔴
```

**Diagnóstico:** A partir das 12.062 sessões, mais de **54% saem sem engajar** com o conteúdo. Das que engajam, apenas uma fração converte. Isso aponta para problemas nas **primeiras dobras** (hero section) e na **proposta de valor**.

### 1.3 Comparativo com Outras Páginas do Site

| Página | Sessões | Engajamento | CVR Est. |
|---|---|---|---|
| **/visto-americano/** | 12.062 | 45.7% | 1.25% |
| / (Homepage) | 11.706 | 63.3% | — |
| /visto-mexicano/ | 277 | **65.3%** | — |
| /como-preencher-ds/ | 1.354 | 41.7% | — |
| /guia-visto-aprovado/ | 1.429 | 35.8% | — |

> **Insight:** O /visto-mexicano/ tem estrutura semelhante mas 20pp a mais de engajamento. O /visto-americano/ tem o maior volume mas pior proporção de engajamento — indicativo de que o tráfego está desqualificado ou a página não sustenta a atenção.

---

## 2. Análise de Campanhas Google Ads

> ⚠️ **Dados reais coletados via API Google Ads** — Conta: `CA - LV` (ID: 5217167876) · Moeda: BRL · Fuso: America/Sao_Paulo · Auto-tagging: ✅ Ativo

### 2.1 Estrutura da Conta

| Campanha | ID | Status | Tipo | Bidding |
|---|---|---|---|---|
| **[REDE DE PESQUISA] [TESTE 2]** | 21154812473 | 🟢 ATIVA | Search | Maximize Conversions |
| [VENDAS][EBOOK][Guia][REDE DE PESQUISA] | 22880259265 | ⏸️ PAUSADA | Search | Maximize Conversions |
| [REDE DE PESQUISA] [TESTE 1] | 21108108426 | 🗑️ REMOVIDA | Search | Maximize Conversions |
| Despachante de Vistos | 21096523906 | 🗑️ REMOVIDA | Smart | Target Spend |

**Conclusão:** A conta tem **1 campanha Search ativa** (visto americano) e **1 pausada** (e-book/guia). O foco real de investimento está no Google Search — não apenas no Meta Ads.

---

### 2.2 Performance da Campanha Principal (último ano)

**Campanha: [REDE DE PESQUISA] [TESTE 2]** — Período: Mar/2025–Mar/2026

| Métrica | Valor | Avaliação |
|---|---|---|
| **Investimento total** | R$ 22.674,07 | Sólido |
| **Impressões** | 251.749 | Volume alto |
| **Cliques** | 15.061 | |
| **CTR** | 5.98% | ⚠️ Abaixo do benchmark (6.66%) |
| **CPC médio** | R$ 1,51 | ✅ Eficiente (benchmark: R$5,26) |
| **Conversões** | 3.002 | Alto volume |
| **Custo/Conversão** | R$ 7,55 | ✅ Muito eficiente |
| **All Conversions** | 3.037 | |
| **Search Impression Share** | 9.99% | 🔴 Crítico — perdendo 90% das licitações |

> 🚨 **Search Impression Share de apenas 9.99%** significa que os anúncios aparecem em menos de 1 a cada 10 pesquisas elegíveis. A conta está **severamente sub-investida** em relação ao potencial do mercado.

---

### 2.3 Grupos de Anúncio Ativos

| Ad Group | Status | Cliques | Conversões | Gasto (R$) | CVR |
|---|---|---|---|---|---|
| [EUA] [TESTE 2][Segmentação] | 🟢 ATIVO | 8.675 | 1.747 | R$ 12.857 | **20.1%** |
| [EUA] [TESTE 2][Segmentação][-PC] | ⏸️ PAUSADO | 5.231 | 910 | R$ 6.314 | **17.4%** |
| [MÉXICO] [TESTE 2][Segmentação] | 🟢 ATIVO | 1.155 | 345 | R$ 3.501 | **29.9%** |
| EBOOK — Grupo 1 | 🟢 ATIVO | 738 | 52 | R$ 396 | 7.0% |

> **Insight crítico:** O ad group de México tem CVR de **29.9%** — superior ao de EUA. O produto de visto mexicano está convertendo muito melhor comparativamente. O ad group de PC (desktop) está pausado apesar de ter ótimas métricas (17.4% CVR) — considerar reativar.

---

### 2.4 Keywords — Quality Score e Performance

| Keyword | Match | QS | CTR Previsto | Post-Click QS | Cliques | Conv. | CPC Médio |
|---|---|---|---|---|---|---|---|
| **assessoria visto americano** | Broad | **7** | AVERAGE | AVERAGE | 2.932 | 716 | R$ 1,37 |
| **consultoria visto americano** | Broad | **7** | AVERAGE | AVERAGE | 2.070 | 374 | R$ 1,21 |
| visto eua | Broad | 5 | BELOW_AVG | AVERAGE | 4.227 | 861 | R$ 1,18 |
| renovação visto americano | Broad | 4–5 | BELOW_AVG | AVERAGE | 3.979 | 718 | R$ 1,36 |
| **assessoria visto mexicano** | Phrase | **8** | ABOVE_AVG | AVERAGE | 219 | 93 | R$ 4,79 |
| visto mexicano | Phrase | 3 | BELOW_AVG | BELOW_AVG | 605 | 191 | R$ 3,15 |
| visto americano | Phrase | 5 | BELOW_AVG | AVERAGE | 640 | 104 | R$ 1,57 |
| despachante visto americano | Phrase | 5 | BELOW_AVG | AVERAGE | 272 | 46 | R$ 1,45 |
| visto de turismo | Phrase | 4 | BELOW_AVG | AVERAGE | 31 | 10 | R$ 2,24 |

**Diagnósticos por keyword:**

- 🔴 **"visto eua"** — QS 5 com `search_predicted_ctr: BELOW_AVERAGE` — o anúncio não está sendo relevante para essa busca genérica
- 🟡 **"renovação visto americano"** — QS 4/5, alta intenção de compra, mas CTR previsto baixo. Candidata a RSA dedicado
- 🟢 **"assessoria visto americano"** — QS 7, melhor keyword da conta, mais eficiente
- 🟢 **"assessoria visto mexicano"** — QS 8 ⭐ , melhor QS da conta — bom produto secundário
- 🔴 **"visto mexicano"** — QS 3, `post_click_quality_score: BELOW_AVERAGE` — landing page inadequada para essa keyword

---

### 2.5 Diagnóstico de Quality Score — Landing Page

O `post_click_quality_score: AVERAGE` em quase todas as keywords indica que o Google avalia a **experiência pós-clique como mediana**. Nenhuma keyword tem `post_click_quality_score: ABOVE_AVERAGE`.

| Dimensão | Status | Causa provável |
|---|---|---|
| **post_click_quality_score** | AVERAGE (maioria) | Página lenta, canonical errado, 8 H1s |
| **search_predicted_ctr** | BELOW_AVERAGE (maioria) | Anúncios genéricos, sem match com query |
| **creative_quality_score** | ABOVE_AVERAGE (maioria) | RSAs com boa variedade de headlines ✅ |

> **Impacto direto:** QS baixo = CPC mais alto + posição mais baixa. Melhorar a landing page pode reduzir CPCs em 20–40%.

---

### 2.6 Campanha EBOOK (Pausada)

**Campanha: [VENDAS][EBOOK][Guia][REDE DE PESQUISA]** — Investiu R$ 396 com 738 cliques e apenas 52 conversões (7% CVR).

Keywords incluídas: `assessoria de visto`, `visto americano`, `visto americano valor`, `visto eua`, `formulario visto americano`, `agencia de visto americano`, `agendamento visto americano`, etc.

> **Análise:** Campanha mistura keywords de intenção informacional (formulário, valor) com transacional (agência, assessoria). A landing page do Ebook não era específica para essas keywords — explica o CVR baixo. Correto tê-la pausado.

---

### 2.7 Análise da Landing Page — Google Quality

Com base no `landing_page_view` da API e nos dados de QS:

| Fator | Status | Detalhe |
|---|---|---|
| **Mobile experience** | Não avaliado | Dado não retornado pela API (requer data recente) |
| **Speed score** | Não avaliado | Dado não disponível no período |
| **Canonical URL** | 🔴 Problemático | Aponta para `#preco` — Google pode confundir |
| **H1 múltiplos** | 🔴 8 H1s | Afeta relevância de content match |
| **Keyword no H1** | ⚠️ Parcial | "A única assessoria para Visto Americano" — keyword presente mas no final |
| **Auto-tagging** | ✅ Ativo | GCLID sendo capturado corretamente |

---

### 2.8 Impression Share — Oportunidade de Escala

**Search Impression Share: 9.99%** é o maior alerta da conta. Isso significa:

- 90% das pesquisas por "assessoria visto americano" e similares **não veem o anúncio da Luciana Vistos**
- Concorrentes estão capturando ~9x mais tráfego qualificado
- Causa mais provável: **orçamento diário insuficiente** (campanhas com maximize conversions limitadas por budget)

**Cálculo de potencial:**
- Atualmente: 251.749 impressões com 9.99% IS
- Potencial 100% IS: ~2.520.010 impressões
- Com CTR atual (5.98%): ~150.697 cliques adicionais possíveis
- Com CVR médio (20%): ~30.139 conversões adicionais

> **Recomendação:** Aumentar orçamento ou ajustar bidding para Target CPA (usando o CPA atual de R$7,55 como referência) para capturar mais IS sem elevar o CPC.

---

### 2.9 Keywords Negativas — Análise

A conta tem **100+ keywords negativas** configuradas — boa prática. Estão cobrindo termos como consulado (informacional), formulário DS-160 (DIY), etc.

---

### 2.10 Recomendações Prioritárias — Google Ads

| Prioridade | Ação | Impacto Estimado |
|---|---|---|
| 🔴 CRÍTICO | **Aumentar orçamento** — Impression Share de 9.99% significa que 90% das buscas são perdidas | +200–400% em cliques |
| 🔴 CRÍTICO | **Corrigir landing page** (canonical, H1s, velocidade) — QS melhora = CPC cai -20-40% | Redução de custo |
| 🔴 CRÍTICO | **Reativar Ad Group de PC** — Estava convertendo a 17.4% CVR e foi pausado sem justificativa clara | +910 conv/ano perdidas |
| ⚠️ ALTO | **Criar RSA dedicado para "renovação visto americano"** — QS 4-5, alta intenção | QS +2-3 pontos |
| ⚠️ ALTO | **Separar campanha de México** — Ad group de México tem CVR 29.9%, merece campanha e budget dedicado | ROI melhor |
| 📈 CRESCIMENTO | **Implementar Target CPA** (R$7,55 como alvo) ao invés de Maximize Conversions sem restrição | Controle de escala |
| 📈 CRESCIMENTO | **Adicionar headlines com termos exatos** nas RSAs — "search_predicted_ctr: BELOW_AVERAGE" em 4 keywords | CTR +15-30% |

---

## 3. Análise da Copy — Eficácia Persuasiva

### 3.1 Hero Section (Acima da Dobra)

**Copy atual:**
> *"A única assessoria para Visto Americano que você vai precisar para garantir uma viagem tranquila."*
> *"Já pensou que um simples erro em sua aplicação pode cancelar a tão planejada viagem?"*

**Avaliação:**

| Critério | Score | Problema |
|---|---|---|
| Clareza da proposta | 6/10 | "Única" é claim difícil de provar |
| Especificidade | 4/10 | Sem resultado tangível (ex: aprovado em X dias) |
| Dor mapeada | 7/10 | O medo do erro é real e relevante |
| Benefit-driven | 5/10 | "Viagem tranquila" é vago |
| Urgência | 3/10 | Sem deadline real. Promoção parece outdated (Black November em março) |

**Problemas identificados:**
1. 🔴 **Banner de promoção desatualizado** — "Black November / Use cupom LV150" exibido em março de 2026. Isso **destrói credibilidade** imediatamente.
2. 🔴 **H1 começa com "A única assessoria"** — claim presunçoso sem prova. A copy começa falando da empresa, não do cliente.
3. 🟡 O medo ("cancelar a tão planejada viagem") é válido mas o framing é negativo sem resolver rapidamente.
4. 🔴 **CTA "QUERO CONTRATAR AGORA"** — forte em intenção mas aparece **antes** do visitante entender o produto/preço. Gera dissonância.

**Copy sugerida para o Hero:**

```
HEADLINE: "Seu Visto Americano aprovado — sem burocracia, sem erros, sem estresse."

SUBHEADLINE: +2.500 clientes aprovados. 5 anos. Taxa de sucesso de 98%.

CTA: "Quero começar meu processo"
MICRO-COPY: Atendimento online para todo o Brasil · Resposta em até 1 hora
```

---

### 3.2 Seção: "Para quem é a nossa assessoria?"

**Copy atual:** Cards com ícones para turismo, trabalho e estudos.

**Avaliação:**
- ✅ **Segmentação por perfil** é boa prática — aumenta identificação
- ⚠️ O texto dos cards é genérico ("cuidaremos de toda a burocracia")
- 🔴 **Não há problema específico** de cada perfil mapeado

**Sugestão:** Tornar os problemas específicos por perfil:
- Turismo: *"Família planejando férias nos EUA mas trava na papelada?"*
- Trabalho: *"Evento corporativo se aproximando e você ainda sem visto?"*
- Estudos: *"Sonha em estudar nos EUA mas o processo parece impossível?"*

---

### 3.3 Seção: Comparativo "Outras Assessorias vs Luciana Vistos"

**Avaliação:**

| Critério | Score |
|---|---|
| Diferenciação real | 6/10 |
| Especificidade | 4/10 |
| Credibilidade claims | 5/10 |

- ✅ A tabela comparativa é boa estratégia (posicionamento por contraste)
- 🔴 Os diferenciais são **genéricos e indistinguíveis**: "atendimento humanizado", "ágil", "personalizado" — qualquer concorrente pode dizer o mesmo
- 🔴 **Sem evidências** que comprovem os diferenciais (não há dados ou exemplos concretos)

**Sugestão:** Adicionar provas concretas:
- *"Respondemos em até 2 horas no WhatsApp (das 8h às 20h)"*
- *"98% dos nossos clientes aprovados — veja os dados da nossa pesquisa de satisfação"*
- *"Reunião preparatória com simulação real da entrevista consular"* (isso é genuinamente diferente)

---

### 3.4 Seção: Como Funciona (6 etapas)

**Avaliação:**
- ✅ **Processo claro** — 6 etapas bem definidas
- ✅ **Reduz ansiedade** ao mostrar o passo-a-passo
- ⚠️ Nomes das etapas em CAPS LOCK reduz legibilidade
- 🔴 **Sem tempo estimado** por etapa — visitante não sabe quanto demora o processo
- 🔴 **Muito técnico** — foco em atividades (preencher DS-160, emitir MRV) em vez de benefícios

**Sugestão:** Reformatar como timeline com tempo e benefício:
> *"Etapa 1: Análise do seu perfil (1 dia útil) → Saberemos exatamente o que você precisa"*

---

### 3.5 Seção: Preço

**Copy atual:**
> *"DE ~~797~~ POR APENAS R$ 597 +TAXAS"*

**Avaliação:**

| Critério | Score |
|---|---|
| Clareza do preço | 5/10 |
| Ancoragem | 7/10 |
| Justificativa de valor | 4/10 |
| Tratamento do custo extra (taxas) | 3/10 |

- 🔴 **"+TAXAS" sem explicar** quanto são essas taxas gera desconfiança. O visitante teme um preço oculto.
- ✅ O desconto de R$797 para R$597 é boa ancoragem psicológica
- 🔴 O preço aparece sem um argumento de valor precedente sólido
- 🟡 A frase *"uma assessoria representa menos de 4% do valor total de sua viagem"* é excelente argumento — mas está **enterrada no rodapé** da seção de preço

**Sugestão:** Reestruturar a seção de preço:
```
[Argumento de valor em destaque]:
"Sua viagem aos EUA vai custar R$15.000 ou mais.
Nossa assessoria custa R$597 — menos de 4% do seu investimento total."

[Preço claro]:
1º Visto: R$597
Renovação: R$597
Taxa consular (paga ao consulado americano): US$185 (~R$950) — separada

[Garantia]:
Se seu processo tiver algum erro nosso, refazemos sem custo adicional.
```

---

### 3.6 Seção: Prova Social / Depoimentos

**Avaliação:**
- ✅ **Presença de avaliações Google** — credibilidade alta
- ✅ **Depoimentos específicos e emocionalmente ressonantes**
- ⚠️ Os depoimentos são **screenshots de imagens** (não texto) — o Google não os indexa
- 🔴 **Fotos de clientes ausentes** — depoimentos anônimos têm menos peso
- 🔴 **Pesquisa de satisfação** são imagens com SVG placeholder (não carregam corretamente no Firecrawl — possível problema de lazy loading ou imagens quebradas)
- 🟡 A nota Google (estrelas) deveria aparecer no topo, não no meio da página

**Melhores depoimentos identificados:**
> *"Tínhamos tentado o visto americano sem auxílio de assessoria e foi negado. Com os serviços da Luciana entendemos o quanto é importante contratar uma assessoria…"* — ⭐ Poderoso (conta história de fracasso → sucesso)

---

### 3.7 Seção: Quem é a Luciana

**Avaliação:**
- ✅ Humanização da marca — muito importante para serviço pessoal
- ⚠️ Aparece **muito tarde** na página (penúltima seção) — clientes contratam a Luciana, não uma empresa anônima
- 🔴 A foto e história deveriam estar **no hero ou acima da dobra**
- 🟡 O lema *"Nas minhas mãos, o seu visto é como se fosse o meu"* é genuíno e diferenciador

---

### 3.8 CTAs: Mapeamento Completo

| Local | Texto do CTA | Destino | Problema |
|---|---|---|---|
| Hero | "QUERO CONTRATAR AGORA" | Popup | 🔴 Muito cedo |
| Pós-comparativo | "QUERO CONTRATAR AGORA" | Popup | ✅ Lugar certo |
| Pós-documentos | "QUERO CONTRATAR AGORA" | Popup | ✅ Bom |
| Pós-depoimentos | "QUERO CONTRATAR AGORA" | Popup | ✅ Bom |
| Cards de preço | Link direto WhatsApp | WhatsApp | 🟡 Bom mas inconsistente |
| Rodapé | WhatsApp / Instagram / Email | Canais | ✅ Bom |

**Problemas de CTA:**
1. 🔴 **CTA idêntico em todos os pontos** — nenhuma variação de contexto ou microcopy
2. 🔴 **Popup como destino** — popups de formulário reduzem conversão vs. página dedicada
3. 🟡 **Inconsistência**: alguns CTAs vão para popup, outros direto ao WhatsApp

---

## 4. Análise de UI (Interface do Usuário)

### 4.1 Diagnóstico Visual

| Elemento | Avaliação | Problema |
|---|---|---|
| **Identidade visual** | ✅ Consistente | Logo + paleta definidos |
| **Hero image/vídeo** | ⚠️ Ausente | Sem elemento visual forte na dobra principal |
| **Tipografia** | ⚠️ Regular | CAPS LOCK excessivo deslegibiliza o texto |
| **Hierarquia visual** | 🔴 Fraca | Vários H1s no mesmo nível |
| **Espaçamento** | ⚠️ Regular | Seções muito densas sem respiro |
| **Cores** | ✅ Adequado | Azul/verde transmite confiança |
| **Imagens** | ⚠️ Fraqueza | Imagens de pesquisa de satisfação com SVG placeholder (quebradas) |
| **Mobile** | 🔴 Não testado | CTA deveria ser full-width |

### 4.2 Problemas SEO/Técnicos da UI

| Problema | Impacto |
|---|---|
| **8 tags H1** em uma única página | Google penaliza — hierarquia quebrada |
| **Canonical URL** aponta para `#preco` | Google pode ignorar a indexação |
| Sem **Schema Markup** (LocalBusiness, Service, FAQPage) | Invisível para AI Search |
| **Lazy loading incorreto** nos gráficos de satisfação | Imagens não carregam |
| **Robots.txt**: `index, follow` — ✅ correto | OK |
| **OG type: `article`** | Deveria ser `website` ou `product` |

### 4.3 Estrutura da Página vs. Ideal

#### Estrutura Atual

```
1. Banner de promoção [desatualizado 🔴]
2. Hero + H1 + CTA
3. 4 métricas sociais (5 anos, 2500 clientes, 98%, 99%)
4. Para quem é? (cards)
5. Comparativo vs. concorrentes
6. CTA
7. Como funciona (6 etapas)
8. Seção "Consegue fazer sozinho?"
9. CTA
10. Preços (2 planos)
11. CTA
12. Depoimentos Google
13. Pesquisa de satisfação (imagens quebradas)
14. Mais depoimentos
15. CTA
16. Aviso legal
17. Quem é a Luciana
18. Contatos
```

#### Estrutura Ideal (Baseado em Boas Práticas de Landing Page)

```
1. Hero: Promessa + Prova rápida + CTA (Above the fold)
2. Social proof imediato: nota Google, nº de aprovações
3. Quem sou eu (Luciana) — humanização rápida
4. Para quem é? — segmentação por perfil
5. Por que isso é difícil (problema) — conteúdo do DS-160
6. Como funciona (processo simplificado)
7. Comparativo vs. concorrentes (com provas)
8. Depoimentos detalhados com foto
9. Preços (claro e sem surpresas)
10. FAQ — objections killer
11. CTA final com garantia
12. Contatos
```

---

## 5. Análise de UX (Experiência do Usuário)

### 5.1 Fluxo de Navegação

**Problema principal:** O usuário que chega de um anúncio Meta Ads sendo prometido "assessoria de visto americano" encontra:
1. Banner de promoção desatualizada → **perda de confiança imediata**
2. Hero genérico → **não reforça o anúncio**
3. CTA prematuro antes de entender o produto
4. Processo longo sem contexto de preço
5. Preço aparece na posição #10 da página

**Resultado esperado:** Alta taxa de abandono na primeira dobra.

### 5.2 Message Match (Ad → Landing Page)

| Anúncio (estimado) | Landing Page | Match |
|---|---|---|
| "Assessoria Visto Americano" | H1: "A única assessoria..." | ✅ 60% |
| "98% aprovados" | Aparece no hero como bullet | ✅ 80% |
| CTA do anúncio (ex: "Saiba mais") | CTA imediato de compra | ⚠️ Dissonância |
| Promoção de desconto | LV150 cupom — mas Black November | 🔴 0% |

### 5.3 Objeções Não Tratadas

As seguintes objeções de compra **não são respondidas** na página atual:

| Objeção | Tratamento atual |
|---|---|
| "Quanto custa exatamente?" | Menciona R$597 + taxas mas não explica as taxas |
| "Qual é o prazo?" | Não menciona prazo médio de processo |
| "E se meu visto for negado?" | Apenas aviso legal no final |
| "Vocês têm CNPJ/são legalizados?" | CNPJ no rodapé mas não em destaque |
| "Funciona para minha cidade?" | "Atendemos online em todo o Brasil" — OK mas tímido |
| "Qual a diferença do 1º visto vs. Renovação?" | Listagem nos planos mas sem explicação |
| "Posso pagar parcelado?" | **Não mencionado** |

### 5.4 Mobile UX (Estimado)

Com base na análise da estrutura (Elementor + WordPress):
- 🔴 Banner de promoção toma ~30% da tela mobile
- 🔴 Cards de "para quem é" podem ser muito pequenos em mobile
- ⚠️ CTA pode não ser full-width em todos os dispositivos
- ✅ Viewport declarado corretamente (`width=device-width, initial-scale=1.0`)

---

## 6. Diagnóstico de Confiança (Trust Signals)

### 6.1 Elementos Presentes

| Trust Signal | Presença | Posição | Força |
|---|---|---|---|
| Logo profissional | ✅ | Topo | ✅ Boa |
| Métricas sociais | ✅ | Hero | ✅ Forte (+2500, 98%, 99%) |
| Avaliações Google | ✅ | Meio | ✅ Forte |
| Depoimentos textuais | ✅ | Meio-baixo | ✅ Bom |
| Foto da Luciana | ✅ | Muito baixo | ⚠️ Deveria subir |
| CNPJ | ✅ | Rodapé | ⚠️ Invisível |
| SSL (HTTPS) | ✅ | URL | ✅ OK |
| Aviso legal | ✅ | Rodapé | ✅ Bom (integridade) |
| Foto dos clientes nos depoimentos | ❌ | — | 🔴 Faltando |
| Schema/Structured data | ❌ | — | 🔴 Faltando |
| FAQ | ❌ | — | 🔴 Faltando |
| Garantia/política de devolução | ❌ | — | 🔴 Faltando |
| Número de telefone clicável | ✅ | Rodapé | ⚠️ Deveria estar no hero |

---

## 7. Oportunidades de Melhoria — Priorização

### 🚨 CRÍTICO (impacto imediato na conversão)

1. **Remover o banner de Black November** — uma promoção de novembro exibida em março destrói credibilidade na primeira visita
2. **Esclarecer o preço total** — explicar que "+TAXAS" são taxas do consulado americano (US$185 ≈ R$950), não da assessoria
3. **Testar CTA mais suave no hero** — "Quero saber mais" ou "Fale com uma consultora" antes de "Quero Contratar"
4. **Subir a foto e história da Luciana** para o hero ou logo após — é o principal diferenciador

### ⚠️ ALTO IMPACTO

5. **Adicionar FAQ** com as objeções mais comuns (prazo, garantia, parcelamento)
6. **Adicionar foto aos depoimentos** para aumentar credibilidade
7. **Corrigir imagens da pesquisa de satisfação** (SVG placeholder)
8. **Corrigir canonical URL** (remover `#preco`)
9. **Consolidar os 8 H1s** em 1 único
10. **Ativar Google Ads Search** para keywords de fundo de funil

### 📈 CRESCIMENTO

11. Implementar **Schema Markup** (LocalBusiness + Service + FAQPage)
12. Adicionar **meta pixel** e **conversions API** para rastreamento preciso
13. Criar **landing page dedicada por segmento** (turismo, trabalho, estudos)
14. **A/B test**: Preço logo no primeiro bloco vs. preço após benefícios
15. Adicionar **widget de WhatsApp com gatilho de saída** (exit intent)

---

## 8. Referências para o Redesign

### Estrutura Recomendada para a Nova Página

```
[HERO — dobra 1]
├── Headline: Promessa específica + resultado mensurável
├── Subheadline: Prova social imediata
├── CTA suave (Falar com consultora)
├── Foto da Luciana [ACIMA DA DOBRA]
└── Métricas: +2500 clientes | 98% aprovados | 5 anos

[SEGMENTAÇÃO — dobra 2]
└── Para quem é? — 3 perfis com dor específica

[PROVA SOCIAL — dobra 3]
└── Nota Google com estrelas + trecho de depoimento mais poderoso

[PROBLEMA — dobra 4]
└── "O visto americano é complexo — veja por que 30% são negados"

[SOLUÇÃO — dobra 5]
└── 6 etapas simplificadas com timeline e prazo estimado

[DIFERENCIAL — dobra 6]
└── Tabela vs. concorrentes (com provas concretas)

[PREÇO — dobra 7]
├── Argumento de valor (4% do custo da viagem)
├── Planos claros (1º visto / Renovação)
├── Taxas do consulado explicadas
└── Formas de pagamento

[DEPOIMENTOS — dobra 8]
└── 6 depoimentos com foto + nota Google embed

[FAQ — dobra 9]
└── 8 objeções mais comuns respondidas

[CTA FINAL — dobra 10]
├── Garantia
├── CTA principal (WhatsApp direto)
└── Confiança: CNPJ em destaque

[RODAPÉ]
└── Aviso legal · Links · Créditos
```

### Paleta e tom sugeridos

- **Tom da copy:** Caloroso + confiante. Evitar jargões jurídicos. Falar como a Luciana fala.
- **Paleta visual:** Manter identidade atual (azul + branco) com mais espaço em branco
- **Tipografia:** Reduzir CAPS LOCK. Usar hierarquia real (H1 → H2 → H3)
- **Imagens:** Fotos reais da Luciana e clientes — humanização é o principal diferencial

---

## 9. Dados Técnicos da Página

| Dado | Valor |
|---|---|
| **CMS** | WordPress 6.9.4 |
| **Page Builder** | Elementor 3.30.2 |
| **Idioma** | pt-BR |
| **Canonical** | `https://lucianavistos.com.br/visto-americano/#preco` 🔴 |
| **Robots** | `index, follow` ✅ |
| **OG Type** | `article` ⚠️ (deveria ser `product` ou `website`) |
| **Status HTTP** | 200 ✅ |
| **Schema Markup** | Ausente 🔴 |
| **H1 count** | 8 🔴 |
| **Word count** | 878 palavras |
| **Links internos** | 10 |
| **Links externos** | 7 (WhatsApp, Instagram, email) |
| **Imagens com lazy-load** | Alguns com SVG placeholder quebrado 🔴 |

---

*Análise gerada pelo SEO Command Center Antigravity · lucianavistos.com.br · 13/03/2026*

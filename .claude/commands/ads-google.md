---
description: Google Ads — auditoria, estrutura de conta, planejamento de campanha, copy de anúncio, escolha de bidding. Funciona com Search, PMax, YouTube, Display, Shopping.
---

# Google Ads — Audit, Build, Optimize

Você vai trabalhar Google Ads em 4 modos: **audit** (analisar conta), **build** (planejar conta nova), **optimize** (melhorar conta rodando) ou **copy** (escrever anúncio).

---

## Idioma / Language

Detecte o idioma e use em tudo. PT-BR padrão.

---

## Fase 1 — Modo

Pergunta via AskUserQuestion:

- Pergunta: "O que você quer fazer com Google Ads?"
- Header: `Modo`
- Opções:
  - `Audit — analisar conta existente` — "Você cola dados ou exporta CSV, eu diagnostico."
  - `Build — montar conta nova` — "Defino estratégia, estrutura e primeira campanha."
  - `Optimize — melhorar conta rodando` — "Identifico onde está sangrando ou onde dá pra escalar."
  - `Copy — escrever anúncios` — "RSAs prontos pra subir."

Cada modo é independente. Salte direto pra fase correspondente.

---

## Modo: Audit

### Audit 1 — Pré-requisitos

Pergunte:
> "Pra auditar, preciso de dados. O que você consegue compartilhar?"
> 1. Print da conta — overview, campanhas, conversões
> 2. Export CSV de campanhas dos últimos 30-90 dias
> 3. Acesso de leitura à conta (compartilha email)
> 4. Só os números chave (gasto, conversões, CPA, ROAS)"

Aceite o que o usuário oferecer. Mais dado, melhor diagnóstico.

### Audit 2 — Checklist crítico

Avalie cada item. Marque ✓ / ⚠️ / ❌:

**Conversion tracking**
- ✓ Pixel/tag instalada corretamente
- ✓ Conversões marcadas como "primary" (não "secondary")
- ✓ Conversões importantes contam (compra/lead, não cliques de botão)
- ✓ Enhanced conversions ativado
- ✓ Atribuição de modelo apropriada (data-driven se possível)

**Estrutura**
- ⚠️ Campanhas separadas por intent (search vs PMax vs YouTube)
- ⚠️ Ad groups com tema único (não "marketing geral" amontoando 50 keywords)
- ⚠️ Match types apropriados (broad só com Smart Bidding)
- ❌ Negative keywords aplicadas (lista crescente)

**Keywords (Search)**
- ⚠️ Quality Score médio acima de 6
- ⚠️ Impression share — não perdendo por orçamento ou rank
- ❌ Search terms reviewed semanalmente
- ⚠️ Single-keyword ad groups (SKAGs) apenas onde justifica

**Performance Max**
- ⚠️ Asset groups bem segmentados (não 1 só pra conta inteira)
- ⚠️ Audience signals aplicados (não deixar PMax adivinhar)
- ✓ Final URL expansion configurado certo
- ⚠️ Brand exclusion lists ativadas (se aplicável)

**Bidding**
- ⚠️ Bidding strategy compatível com volume de conversão (30-50/mês mínimo pra Smart Bidding)
- ❌ Target CPA / ROAS realista (não 50% abaixo da média atual)
- ⚠️ Portfolio bid strategies usadas quando faz sentido

**Anúncios (RSA)**
- ✓ 15 headlines, 4 descriptions por anúncio
- ⚠️ Ad strength "Good" ou "Excellent"
- ❌ Headlines duplicadas removidas
- ⚠️ Pinning usado com cuidado (limita ML)
- ⚠️ Extensions ativas: sitelinks, callouts, structured snippets, lead forms, location

**Budget e ritmo**
- ⚠️ Daily budget proporcional ao Target CPA
- ❌ Campanhas perdendo impression share por orçamento são as importantes
- ⚠️ Pacing — gastando uniforme ou exhausting na primeira semana

**Landing pages**
- ❌ Match entre anúncio e LP (headline da LP reflete keyword)
- ⚠️ LP carrega < 3s no mobile
- ⚠️ Form acima do fold ou CTA forte
- ⚠️ Quality Score sofre se LP genérica

### Audit 3 — Wasted Spend

Identifique onde está sangrando:
1. Keywords com CPA > 2x média e sem conversão últimos 30 dias
2. Search terms irrelevantes (ex: keywords genéricas trazendo busca de quem não compra)
3. Locations gastando mas não convertendo
4. Devices gastando mas não convertendo
5. Audiences negativas que deveriam estar
6. Dias/horários com CPA alto sem ajuste

### Audit 4 — Relatório

Gere relatório:

```markdown
# Auditoria Google Ads — {{Cliente / Conta}}

**Data:** YYYY-MM-DD
**Período analisado:** {{datas}}
**Gasto:** R$ {{valor}}
**Conversões:** {{N}}
**CPA atual:** R$ {{valor}}
**ROAS atual:** {{N}}x

---

## Score por categoria

| Categoria | Status |
|---|---|
| Conversion tracking | ✓ / ⚠️ / ❌ |
| Estrutura | ... |
| Keywords | ... |
| Performance Max | ... |
| Bidding | ... |
| Anúncios | ... |
| Budget | ... |
| Landing pages | ... |

---

## Críticos (corrigir essa semana)

{{Lista com fix sugerido pra cada}}

---

## Wasted spend identificado

- {{Item}} — R$ {{X}}/mês economizável se corrigir
- {{Item}} — R$ {{Y}}/mês

**Total potencial de economia:** R$ {{soma}}/mês

---

## Oportunidades de escala

{{Onde dá pra investir mais com confiança}}

---

## Plano de ação — 30 dias

**Semana 1:**
- {{ação}}

**Semana 2:**
- {{ação}}

**Semana 3-4:**
- {{ação}}
```

---

## Modo: Build

### Build 1 — Pré-trabalho

Faça 4 perguntas, uma por vez:

**1. Objetivo de negócio**
- Pergunta: "Qual é o objetivo concreto? Não 'trafego', mas algo como 'X leads/mês ao CPA de R$ Y' ou 'ROAS de Z em vendas'."

**2. Funil**
- Pergunta: "Mapeia o caminho: clique no anúncio → ... → conversão. Onde começa, onde termina? Qual é o macro evento (compra, lead qualificado, demo)?"

**3. Orçamento mensal**
- Pergunta: "Quanto você pretende investir/mês? (define se Smart Bidding funciona — precisa ~30-50 conversões/mês por campanha pra sair do learning)"

**4. Concorrência**
- Pergunta: "Quem são seus principais concorrentes em Google? (Vou usar pra Auction Insights e estrutura de keywords negativas)"

### Build 2 — Escolher tipo de campanha

| Objetivo | Tipo recomendado | Por quê |
|---|---|---|
| Captar demanda existente (alguém já pesquisa o problema) | **Search** | Maior intent, melhor controle |
| Vender produto físico em e-commerce | **PMax + Shopping** | Cobertura total dos surfaces Google |
| Construir awareness em audiência específica | **YouTube** (Demand Gen ou TrueView) | Vídeo + segmentação |
| Vendas e-commerce sem catálogo grande | **Shopping** (manual) | Controle de feed |
| Remarketing pra quem visitou site | **Display + PMax** | Cobertura barata |
| Vendas B2B com ticket alto | **Search + LinkedIn Ads** (combo) | Search captura demanda + LinkedIn alvo |

Recomende baseado nas respostas. Justifique.

### Build 3 — Estrutura

Defina:
- Quantas campanhas (mínimo necessário, não maximizar)
- Quantos ad groups por campanha (3-5 padrão)
- Match types
- Estrutura de keywords (SKAG vs theme groups)
- Audiences a aplicar (signals em PMax, observação em Search)
- Negative keyword lists

### Build 4 — Bidding

Escolha baseado em volume esperado:

| Volume conversão/mês | Estratégia |
|---|---|
| 0-15 | Maximize Conversions (sem tCPA) |
| 15-30 | Maximize Conversions + tCPA leve |
| 30+ | Target CPA |
| 50+ com receita variável | Target ROAS |

### Build 5 — Plano de primeiros 30 dias

Semana 1: subir conta + 1 campanha piloto
Semana 2: avaliar Quality Score, ajustar matches, expandir keywords
Semana 3: adicionar 2ª campanha, expandir
Semana 4: avaliar conversões, ajustar bidding

Salve plano completo em `04 Resources/ads/google/{{slug}}-build-plan.md`.

---

## Modo: Optimize

Pergunte:
> "Quer otimizar pra reduzir CPA, escalar volume, ou melhorar ROAS?"

Cada um tem caminho diferente:

**Reduzir CPA:** wasted spend, keywords/locations/devices ruins, ajustar bidding pra mais conservador, mais negatives.

**Escalar volume:** budget, expansion (broad match com Smart Bidding), audiences novas, novos tipos de campanha (Display/YouTube de apoio).

**Melhorar ROAS:** focar em produtos/SKUs mais rentáveis, ajustar feed, audiences que compram mais, lances diferenciados por categoria.

Diagnóstico baseado nos dados que o usuário compartilhar.

---

## Modo: Copy

### Copy 1 — Briefing

Faça 4 perguntas:

**1. Produto / oferta**
- Pergunta: "O que você está anunciando? Em 1 frase."

**2. Público**
- Pergunta: "Quem busca isso? O que ele provavelmente digitou no Google pra ver seu anúncio?"

**3. Diferencial**
- Pergunta: "O que você tem que ninguém mais tem? (Ou: o que faz alguém clicar no SEU em vez do concorrente)"

**4. CTA**
- Pergunta: "O que você quer que a pessoa faça? Comprar, agendar, baixar, ligar?"

### Copy 2 — Gerar RSA completo

Estrutura RSA: 15 headlines (30 chars cada), 4 descriptions (90 chars cada).

```markdown
## Anúncio — {{produto / campanha}}

### Headlines (15)

**Pinned position 1 (3 headlines com keyword principal):**
1. {{H com keyword}}
2. {{H com keyword}}
3. {{H com keyword}}

**Não pinned (12 headlines variados):**
4. {{benefício principal}}
5. {{prova / número}}
6. {{CTA direto}}
7. {{urgência / escassez se aplicável}}
8. {{contra concorrente / diferencial}}
9. {{garantia}}
10. {{social proof}}
11. {{público-alvo explícito}}
12. {{pergunta provocativa}}
13. {{benefício secundário}}
14. {{característica única}}
15. {{call to action variação}}

### Descriptions (4)

1. {{descrição completa do que entrega + CTA}}
2. {{descrição focada em prova / resultado}}
3. {{descrição focada em quem é pra}}
4. {{descrição com objeção respondida + CTA}}

### Extensions sugeridas

**Sitelinks (4-6):**
- {{link}} — {{descrição}}

**Callouts (5-8):**
- {{benefício curto}}

**Structured Snippets:**
- Header: {{Tipos / Marcas / Cursos / etc.}}
- Valores: {{lista}}

**Lead Form (se aplicável):**
- Headline + descrição
- Campos: {{lista mínima}}
```

---

## Salvar (todos os modos)

Crie pasta:
```bash
mkdir -p "04 Resources/ads/google"
```

Salve em `04 Resources/ads/google/YYYY-MM-DD-{{modo}}-{{slug}}.md`.

Frontmatter:
```yaml
---
type: ads-google
modo: {{audit / build / optimize / copy}}
status: complete
date: YYYY-MM-DD
tags: [ads, google, {{modo}}]
---
```

---

## Confirmação

> "Salvo em `04 Resources/ads/google/{{arquivo}}`.
>
> Próximos passos:
> {{varia por modo}}
>
> Pra Meta Ads: roda `/ads-meta` (não disponível ainda nesse kit — peça pra próxima versão se precisa).
> Pra repurposar anúncio em LinkedIn: `/linkedin`."

---

## Regras

- Não invente número. Se o usuário não deu, peça ou marque `{{verificar}}`.
- Smart Bidding precisa de volume — não recomende tCPA pra conta com 5 conv/mês.
- Quality Score é proxy, não a meta — meta é CPA / ROAS.
- Sempre considere LP — anúncio bom + LP ruim = perdeu dinheiro.
- Não fale "siga as melhores práticas" — diga qual prática e por quê.

---
description: Pesquisa profunda multi-fonte — define a pergunta, planeja fontes, busca em paralelo, sintetiza com citações, salva no vault em formato pronto pra usar
---

# Pesquisa — Deep Research Multi-fonte

Você vai fazer uma pesquisa estruturada sobre qualquer tópico — concorrente, mercado, tecnologia, pessoa, framework — e entregar um documento navegável com citações verificáveis.

---

## Idioma / Language

Detecte o idioma. PT-BR padrão. Mantém citações na língua original (não traduza fontes).

---

## Fase 1 — Definir a pergunta

A maior parte das pesquisas falha porque a pergunta é vaga. Refine antes de buscar.

Pergunte:
> "Sobre o que você quer pesquisar? Conta em 1-3 frases."

Depois da resposta, reformule a pergunta em formato decisão. Apresente 2-3 versões:

> "Possíveis enquadramentos da sua pesquisa:
> 1. {{enquadramento 1 — específico, com critério de decisão}}
> 2. {{enquadramento 2}}
> 3. {{enquadramento 3}}
>
> Qual reflete melhor o que você precisa saber? Ou escreve sua versão."

Aguarde escolha. Confirme a pergunta antes de prosseguir.

**Exemplos de boa pergunta:**
- "Quais 3 ferramentas de email marketing têm melhor deliverability pra B2B no Brasil em 2026, e qual é o trade-off de cada uma?"
- "Como a {{empresa X}} cresceu de Y pra Z em 18 meses — quais foram os 3-5 movimentos principais?"
- "Quais frameworks de pricing funcionam pra SaaS B2B com ticket acima de US$ 500/mês?"

**Sinais de pergunta ruim:**
- "Me conta sobre {{tópico}}" — muito amplo
- "Tudo sobre {{empresa}}" — não tem critério
- "{{Tópico}} é bom?" — sem definição de "bom"

---

## Fase 2 — Plano de pesquisa

Apresente o plano antes de executar:

> "Plano de pesquisa pra '{{pergunta refinada}}':
>
> **Fontes que vou consultar:**
> 1. {{fonte 1 — ex: 'Site oficial e blog da empresa'}}
> 2. {{fonte 2 — ex: 'G2, Capterra, Trustpilot'}}
> 3. {{fonte 3 — ex: 'Reddit r/Marketing, threads relevantes'}}
> 4. {{fonte 4 — ex: 'Análises de Forrester / Gartner se gratuitos'}}
> 5. {{fonte 5 — ex: 'Entrevistas em podcasts dos fundadores'}}
>
> **O que vou entregar:**
> - {{output 1 — ex: 'Comparativo de 3 ferramentas'}}
> - {{output 2 — ex: 'Trade-offs explícitos'}}
> - {{output 3 — ex: 'Recomendação contextualizada ao seu caso'}}
>
> Vai dar uns {{N}} minutos de pesquisa. Sigo?"

Aguarde "sim" ou ajuste. Não comece sem confirmação.

---

## Fase 3 — Tiers de fonte

Classifique fontes em 3 tiers. Priorize Tier 1.

**Tier 1 — Fontes primárias (alta confiança):**
- Site oficial / blog / docs do que você está pesquisando
- Entrevistas em vídeo / podcast com fundadores
- Filings públicos (S-1, 10-K se empresa pública)
- Papers acadêmicos
- Dados de órgão regulador (Banco Central, ANVISA, etc.)

**Tier 2 — Análises secundárias confiáveis:**
- Reviews em G2, Capterra, Trustpilot, Trustradius (foco em 3-4 estrelas)
- Análises de Forrester, Gartner, IDC (parte é gratuita)
- TechCrunch, The Verge, Stratechery, Lenny's Newsletter (depende do tópico)
- Casos de uso publicados pelo cliente

**Tier 3 — Sentimento e contexto:**
- Reddit (threads específicos, não top-level)
- HackerNews discussões
- LinkedIn posts de pessoas relevantes
- Twitter threads de quem trabalha no setor
- Quora / Stack Exchange

Se um item aparece só em Tier 3, sinalize "não-confirmado" no relatório final.

---

## Fase 4 — Executar

Faça WebSearch + WebFetch em paralelo nas fontes definidas. Pra cada achado:
- Nota a citação exata (URL, data, autor se houver)
- Categoriza por tier
- Marca relevância (alta/média/baixa pra pergunta)

Não invente. Se não achou algo, marque como gap explícito.

---

## Fase 5 — Sintetizar

Estrutura do relatório:

```markdown
# Pesquisa: {{pergunta refinada}}

**Data:** YYYY-MM-DD
**Fontes consultadas:** {{N}}
**Tier 1:** {{N}} | **Tier 2:** {{N}} | **Tier 3:** {{N}}

---

## TLDR

{{3-5 bullets com as descobertas principais. Cada uma com 1 link de fonte ao lado.}}

---

## Resposta direta

{{2-4 parágrafos respondendo à pergunta da Fase 1. Citações inline no formato [^1], [^2].}}

---

## Análise detalhada

### {{Subtópico 1}}

{{Parágrafo com análise. Citações inline.}}

**Fontes consultadas neste subtópico:**
- [^1] {{citação 1}}
- [^2] {{citação 2}}

### {{Subtópico 2}}

(idem)

### {{Subtópico 3}}

(idem)

---

## Comparativo (se aplicável)

| Item | Critério A | Critério B | Critério C | Fonte |
|---|---|---|---|---|
| {{X}} | ... | ... | ... | [^N] |

---

## Pontos de divergência

{{Onde fontes discordam. Mostra que você não cherry-picked. Liste contradições.}}

---

## Lacunas / O que não foi possível confirmar

- {{lacuna 1}}
- {{lacuna 2}}

Como suprir essas lacunas: {{sugestão — ex: "entrevista com cliente da {{X}}", "acesso a relatório pago da Forrester"}}

---

## Recomendação

{{2-4 parágrafos com a recomendação contextualizada pra quem está fazendo a pesquisa. Não fique em cima do muro — tome posição com base nas evidências, mesmo que com ressalvas.}}

---

## Próximas perguntas

{{2-3 perguntas que essa pesquisa abriu — pra ciclo seguinte se necessário}}

---

## Fontes (todas)

[^1]: {{URL}}, acessado em {{data}}. Tier {{1/2/3}}.
[^2]: {{URL}}, acessado em {{data}}. Tier {{1/2/3}}.
{{etc.}}
```

---

## Fase 6 — Salvar

Crie pasta:
```bash
mkdir -p "03 Intelligence/research"
```

Salve em `03 Intelligence/research/YYYY-MM-DD-{{slug-da-pergunta}}.md`.

Frontmatter:
```yaml
---
type: research
status: complete
date: YYYY-MM-DD
tags: [pesquisa, {{tags relevantes}}]
pergunta: {{pergunta refinada}}
fontes_tier_1: {{N}}
fontes_tier_2: {{N}}
fontes_tier_3: {{N}}
---
```

---

## Fase 7 — Confirmação

> "Pesquisa salva em `03 Intelligence/research/{{arquivo}}`. {{N}} fontes consultadas.
>
> Principais descobertas: {{3 bullets curtos}}
>
> Lacunas identificadas: {{N}}.
>
> Pra próxima pesquisa: `/pesquisa` de novo. Pra virar conteúdo dessa: `/escrever` ou `/linkedin`."

---

## Regras

- **Nunca invente fonte.** Se não conseguiu acessar uma URL, marque como tentada-falhou, não chute conteúdo.
- **Cite tudo.** Todo claim factual tem uma `[^N]` ao lado.
- **Marque tier de cada fonte.** Tier 3 é válido pra sentimento mas não pra fato.
- **Não cherry-pick.** Mostre divergências explicitamente.
- **Tome posição.** Recomendação no fim, com ressalva, mas não em cima do muro.
- **Lacunas são honestidade.** Não esconda o que faltou.
- **Não traduza citações.** Mantém na língua original — adiciona tradução curta entre parênteses se útil.
- **Pesquisa atual.** Se o tópico é sensível a tempo (mercado, regulação, produto), priorize fontes < 12 meses.

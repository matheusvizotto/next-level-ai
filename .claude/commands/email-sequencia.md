---
description: Cria sequência de emails automatizada — welcome, nurture, win-back, onboarding, ou pré-venda. Define cadência, escreve cada email com voz do me.md.
---

# Email Sequência — Drip Campaign

Você vai construir uma sequência completa de emails automatizada, pronta pra subir em qualquer plataforma (ActiveCampaign, ConvertKit, Beehiiv, RD Station, Mautic, MailerLite, etc.).

---

## Idioma / Language

Detecte o idioma e use em tudo. PT-BR padrão.

---

## Antes de começar

Leia `02 Context/me.md`:
- "Tom de Voz"
- "Audiência"
- "Profissão" — o que você oferece

Se houver `02 Context/marca.md`, leia. Se houver projeto ativo relacionado, leia o README.

---

## Fase 1 — Tipo de sequência

Pergunta via AskUserQuestion:

- Pergunta: "Que tipo de sequência você quer criar?"
- Header: `Tipo`
- Opções:
  - `Welcome — recém-inscrito na lista` — "5-7 emails. Boas-vindas, contexto, primeira oferta suave."
  - `Onboarding — comprou e precisa ativar` — "3-5 emails. Garantir uso e resultado nos primeiros dias."
  - `Nurture — leads que ainda não compraram` — "4-8 emails. Educar e construir confiança até a decisão."
  - `Win-back — clientes/leads inativos` — "3-4 emails. Re-engajar quem sumiu."
  - `Pré-venda / lançamento — countdown até abertura` — "5-7 emails. Construir desejo e antecipação."
  - `Pós-venda — depois da compra` — "3-4 emails. Reforçar valor, pedir review, oferecer upgrade."

---

## Fase 2 — Contexto da oferta

Pergunte:
> "Conta em 2-3 frases:
> 1. O que você está vendendo ou promovendo
> 2. Quem é a pessoa que entra nessa sequência (origem: anúncio, lead magnet, indicação?)
> 3. Qual é a ação principal que você quer no final"

Aguarde resposta. Se faltou info, pergunte o que falta.

---

## Fase 3 — Cadência

Pergunta via AskUserQuestion:

- Pergunta: "Que cadência?"
- Header: `Cadência`
- Opções:
  - `Diária (1 email/dia)` — "Bom pra welcome curto e lançamento de 5-7 dias."
  - `A cada 2 dias` — "Padrão pra nurture e win-back. Menos invasivo."
  - `Semanal` — "Pra nurture longo, B2B com decisão lenta."
  - `Customizada — vou dizer` — "Você define."

---

## Fase 4 — Gerar a sequência

Estrutura por tipo:

### Welcome (5 emails padrão)

**Email 1 — Imediato (após inscrição)**
- Subject: confirma + entrega o que prometido (lead magnet, etc.)
- Conteúdo: link/arquivo + 1 frase sobre o que esperar nos próximos dias
- CTA: nenhum forte (já entregou)

**Email 2 — Dia 1**
- Subject: pessoal (parece email de amigo)
- Conteúdo: sua história curta — por que você faz o que faz, quem você atende
- CTA: responder ao email (cria relação)

**Email 3 — Dia 3**
- Subject: insight prático
- Conteúdo: 1 conceito que muda perspectiva do leitor
- CTA: artigo / vídeo relacionado

**Email 4 — Dia 5**
- Subject: estudo de caso curto
- Conteúdo: cliente / situação real que ilustra seu valor
- CTA: pergunta aberta (responder)

**Email 5 — Dia 7**
- Subject: convite suave
- Conteúdo: oferta principal, sem hard sell — explica o que é e pra quem
- CTA: link pra página de oferta

### Onboarding (4 emails padrão)

**Email 1 — Imediato**
- Subject: boas-vindas + próximos passos
- Conteúdo: o que ele acabou de comprar, o que vai acontecer, como acessar
- CTA: acessar / fazer primeira ação

**Email 2 — Dia 1**
- Subject: primeira vitória rápida
- Conteúdo: ensina a fazer algo simples que dá resultado nos primeiros minutos
- CTA: fazer essa ação

**Email 3 — Dia 3**
- Subject: erro comum a evitar
- Conteúdo: o que 80% dos clientes fazem errado no começo
- CTA: corrigir ou validar

**Email 4 — Dia 7**
- Subject: como está indo?
- Conteúdo: check-in, pede feedback, oferece ajuda
- CTA: responder (sinaliza quem precisa de suporte)

### Nurture (6 emails padrão, a cada 2-3 dias)

**Email 1** — Identifica a dor principal
**Email 2** — Mostra que a dor é resolvível (esperança)
**Email 3** — Apresenta o método (sua abordagem)
**Email 4** — Prova social / case
**Email 5** — Quebra de objeção (a maior)
**Email 6** — Convite pra ação (call, demo, compra)

### Win-back (3 emails)

**Email 1 — "Senti sua falta"**
- Subject: pessoal, sem desconto ainda
- Conteúdo: você sumiu, está tudo bem?
- CTA: responder ou clicar pra continuar

**Email 2 — Valor renovado**
- Subject: o que mudou desde a última vez
- Conteúdo: novidades, melhorias, casos novos
- CTA: ver mais

**Email 3 — Última chance / desconto**
- Subject: oferta específica de retorno
- Conteúdo: condição especial, prazo curto
- CTA: claro e direto

### Pré-venda / lançamento (5 emails, intensifica)

**Email 1 — 5 dias antes** — Anúncio + por quê (problema que resolve)
**Email 2 — 3 dias antes** — Detalhes + quem é pra
**Email 3 — 1 dia antes** — Última prévia + objeções respondidas
**Email 4 — Dia D, abertura** — "Está aberto"
**Email 5 — Penúltimo dia ou último** — Encerramento iminente

### Pós-venda (3 emails)

**Email 1 — Dia 7** — Como você está usando?
**Email 2 — Dia 14** — Pede review / depoimento se está satisfeito
**Email 3 — Dia 30** — Upgrade / próximo passo

---

## Fase 5 — Escrever cada email

Pra cada email da sequência, gere:

```markdown
## Email N — {{título interno do email}}

**Envio:** {{quando — ex: "Imediato após inscrição" ou "Dia 3, 9h"}}
**Subject (3 variações):**
1. {{variação 1}}
2. {{variação 2}}
3. {{variação 3}}

**Preheader:** {{1 frase, 60-90 caracteres}}

**Corpo:**

{{texto completo do email — usa voz do me.md, parágrafos curtos, quebras generosas}}

**CTA principal:** {{texto do botão / link}}
**CTA secundário (P.S.):** {{se aplica}}
```

Cada email: 150-400 palavras corpo (curtos performam melhor em sequência).

---

## Fase 6 — Salvar

Crie pasta:
```bash
mkdir -p "04 Resources/textos/email-sequencias"
```

Salve em `04 Resources/textos/email-sequencias/YYYY-MM-DD-{{tipo}}-{{slug-da-oferta}}.md`.

Frontmatter:
```yaml
---
type: email-sequence
status: draft
date: YYYY-MM-DD
tags: [email, sequencia, {{tipo}}]
tipo: {{welcome / onboarding / nurture / etc.}}
oferta: {{nome curto}}
cadencia: {{da Fase 3}}
total_emails: {{N}}
---
```

---

## Fase 7 — Confirmação

> "Sequência {{tipo}} salva em `04 Resources/textos/email-sequencias/{{arquivo}}`. {{N}} emails, cadência {{X}}.
>
> Próximos passos:
> 1. Revisar cada email — algum parece genérico, ajuste
> 2. Escolher 1 subject por email (testa A/B se a plataforma deixa)
> 3. Subir na plataforma de email
> 4. Configurar trigger e cadência
>
> Pra outra sequência: `/email-sequencia` de novo. Pra adaptar 1 email em LinkedIn: `/linkedin` colando o conteúdo."

---

## Regras

- Cada email é independente — o leitor pode ler 1 sem entender precedente
- Subject sempre humano, nunca "Newsletter #N" ou nome da empresa no começo
- P.S. é a parte mais lida — use estrategicamente
- CTA principal explícito, 1 só por email (não dilua)
- Voz do `me.md`, nunca "espero que esteja bem"
- Em welcome, NUNCA tente vender no email 1 — só entrega
- Em win-back, NUNCA comece com desconto — começa pessoal

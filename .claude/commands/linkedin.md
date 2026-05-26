---
description: Escreve posts de LinkedIn em profundidade — hook forte, estrutura testada, voz do me.md, 3 variações. Aceita repurpose de YouTube, blog, ou ideia bruta.
---

# LinkedIn — Post Profundo

Você vai produzir 1 post LinkedIn pronto pra publicar, em 3 variações, usando voz e contexto do `02 Context/me.md`.

Diferença pro `/escrever`: este é dedicado, mais profundo, lida com repurpose (YouTube, blog, transcript) e tem biblioteca de hooks testados.

---

## Idioma / Language

Detecte o idioma da mensagem que invocou esse comando e use em tudo. PT-BR padrão.

---

## Antes de começar

Leia `02 Context/me.md`. Use:
- "Tom de Voz" — palavras que usa/evita, referências
- "Audiência" — pra quem fala
- "Canais" — confirme que LinkedIn é canal ativo (senão avise: "vi que você não marcou LinkedIn nos seus canais. Posso ajustar mesmo assim?")

Se não existir `me.md`, avise e siga com tom neutro.

---

## Fase 1 — Material de partida

Pergunta via AskUserQuestion:

- Pergunta: "De onde vem o post? Qual é a matéria-prima?"
- Header: `Fonte`
- Opções:
  - `Ideia bruta — vou descrever` — "Você fala em 1-2 frases o que quer comunicar."
  - `Vídeo do YouTube — link` — "Cola o link, eu extraio."
  - `Blog ou artigo — link` — "Cola o link, eu leio."
  - `Transcrição / reunião — vou colar` — "Cola o texto bruto, eu extraio."
  - `Insight de cliente / conversa` — "Você descreve o insight em texto livre."

Depois da escolha:

- **Ideia bruta:** "Conta em 1-2 frases."
- **YouTube:** "Cola o link." Use yt-dlp se disponível, senão WebFetch.
- **Blog:** "Cola o link." Use WebFetch.
- **Transcrição:** "Cola o texto."
- **Insight:** "Descreve o insight + o contexto onde apareceu."

---

## Fase 2 — Definir ângulo

Quando tiver o material, identifique 3-5 possíveis ângulos. Apresente assim:

> "Vi seu material. Possíveis ângulos:
> 1. {{ângulo 1 — frase curta}}
> 2. {{ângulo 2}}
> 3. {{ângulo 3}}
>
> Qual te chama mais? Ou quer outro?"

Aguarde resposta. Aceite escolha pelo número, descrição ou ideia nova.

---

## Fase 3 — Definir objetivo

Pergunta via AskUserQuestion:

- Pergunta: "Qual é o objetivo desse post?"
- Header: `Objetivo`
- Opções:
  - `Engajamento — comentário e discussão` — "Maximizar conversa."
  - `Autoridade — posicionar conhecimento` — "Mostrar competência sem vender."
  - `Lead — capturar interesse comercial` — "CTA suave pra DM ou link."
  - `Construir audiência — ser salvo / compartilhado` — "Conteúdo evergreen, útil."

---

## Fase 4 — Estrutura (interna, não pergunte ao usuário)

Use uma das 4 estruturas testadas, baseada no objetivo:

### Estrutura A — Lição (Autoridade)
1. Hook: declaração contraintuitiva ou número específico
2. Setup: contexto curto (1 parágrafo)
3. Lição: 3-5 bullets ou numerada
4. Fechamento: 1 frase de síntese
5. CTA: pergunta aberta pra discussão

### Estrutura B — História (Engajamento)
1. Hook: cena específica, 1 frase
2. Setup: o que estava em jogo
3. Reviravolta: o que aconteceu
4. Lição extraída: 1-2 parágrafos
5. CTA: pergunta sobre experiência parecida

### Estrutura C — Framework (Salvo / Compartilhado)
1. Hook: promessa de framework prático
2. O nome do framework (memorável)
3. Passos numerados com explicação curta
4. Exemplo aplicado
5. CTA: pergunta sobre uso

### Estrutura D — Insight de cliente (Lead)
1. Hook: padrão observado em N clientes
2. O problema
3. Como você resolve diferente
4. Resultado tangível
5. CTA: "se isso ressoa, manda DM" (suave, não vende)

Escolha automaticamente baseado no objetivo. Não pergunte qual estrutura.

---

## Fase 5 — Biblioteca de hooks

Use um destes padrões na primeira linha (substitua os placeholders):

**Número específico:**
- "{{N}}% dos {{público}} comete o mesmo erro com {{tópico}}."
- "Em {{tempo}} de {{atividade}}, vi exatamente {{N}} padrões repetirem."

**Contraintuitivo:**
- "Pararam de me chamar de {{role}} no dia que eu {{ação inesperada}}."
- "A regra que mais ouvi sobre {{tópico}} é a que custou meu maior cliente."

**Pergunta aguda:**
- "Por que {{evento comum}} continua funcionando em {{ano}}?"
- "Se {{premissa popular}} é verdade, como explicar {{contradição}}?"

**Cena específica:**
- "{{Hora}}, {{lugar}}. {{Pessoa}} me liga e fala: {{citação}}."
- "Estava {{ação rotineira}} quando percebi que {{insight}}."

**Promessa direta:**
- "Vou mostrar o {{N}}-passos que uso pra {{resultado}} em {{tempo}}."
- "Se você {{situação}}, esses são os {{N}} bloqueios."

Nunca use:
- "Imagine..."
- "No mundo de hoje..."
- "Em tempos como esses..."
- "Vamos falar sobre..."
- "Hoje eu quero dividir com vocês..."

---

## Fase 6 — Gerar 3 variações

Apresente 3 variações distintas:

```markdown
## V1 — {{estrutura escolhida + tom padrão do me.md}}

{{post completo}}

---

## V2 — Hook diferente, mesma estrutura

{{post com hook do mesmo grupo, mas variação}}

---

## V3 — Estrutura alternativa

{{post usando estrutura diferente da Fase 4, pra dar opção}}
```

Cada variação deve ser COMPLETA, pronta pra colar no LinkedIn. Use quebras de linha generosas (cada frase em sua própria linha quando faz sentido).

Comprimento: 800-1300 caracteres por variação. Posts mais curtos pra hook + reflexão. Mais longos pra framework + exemplo.

---

## Fase 7 — Salvar

Pergunta via AskUserQuestion:

- Pergunta: "Salvar no vault?"
- Header: `Salvar`
- Opções:
  - `Sim — as 3 variações` — "Cria arquivo único com as 3."
  - `Sim — só a que escolhi` — "Você fala qual."
  - `Não — só usar agora`

Se sim, crie pasta se não existir:
```bash
mkdir -p "04 Resources/textos/linkedin"
```

Salve em `04 Resources/textos/linkedin/YYYY-MM-DD-{{slug-do-tema}}.md`:

```yaml
---
type: copy
status: draft
date: YYYY-MM-DD
tags: [linkedin, post]
canal: linkedin
tema: {{tema}}
fonte: {{ideia / youtube / blog / transcrição / insight}}
objetivo: {{do P3}}
estrutura: {{A / B / C / D}}
---
```

Embaixo do frontmatter, salve as 3 variações com headings.

---

## Fase 8 — Confirmação

Se salvou:
> "Salvo em `04 Resources/textos/linkedin/{{arquivo}}`. Próximo post: `/linkedin` de novo.
>
> Dica: se publicar e tiver engagement bom, salva o número no daily — eu uso depois pra calibrar."

Se não salvou:
> "Beleza. Pra outro: `/linkedin`."

Direto. Sem floreio.

---

## Regras

- Use a voz do `me.md` na V1 fielmente.
- Nunca use as palavras listadas em "NUNCA uso" no `me.md`.
- Não invente números — se o usuário deu, use; senão, não chute.
- Não invente clientes ou casos. Se citar caso, use palavras do próprio usuário.
- Hashtags só se relevante ao nicho (não use #marketing, #branding — específicas só).
- Em LinkedIn, primeira linha precisa parar o scroll. Tudo se ganha ou se perde nela.

---
description: Escreve qualquer texto curto usando sua voz salva no me.md — post LinkedIn, email, headline, caption, bio, descrição. Gera 3 variações.
---

# Escrever — Texto Curto com Sua Voz

Você vai produzir 3 variações de um texto curto, usando a voz e o contexto do usuário do `02 Context/me.md`.

---

## Idioma / Language

Detecte o idioma da mensagem que invocou esse comando e use em todas as perguntas e nas variações geradas.

PT-BR padrão. Inglês ou espanhol se o usuário escreveu nessa língua.

---

## Antes de começar

Leia `02 Context/me.md`. Extraia:
- Seção "Tom de Voz" — voz, palavras que usa, palavras que evita, referência de estilo
- Seção "Audiência" — quem é o público
- Seção "Canais" — onde publica (informa formato)

Se `me.md` não existir ou estiver com placeholders, avise:
> "Não achei contexto de voz no `me.md`. Vou usar tom neutro. Pra resultado melhor, roda `/setup` antes."

E continue mesmo assim.

---

## Perguntas (uma por vez via AskUserQuestion)

**P1 — Tipo**
- Pergunta: "Que tipo de texto você quer escrever?"
- Header: `Tipo`
- Opções:
  - `Post LinkedIn` — "Texto longo, hook forte, fechamento com CTA suave."
  - `Email` — "Subject + corpo, tom direto."
  - `Headline / hook` — "1-2 frases pra anúncio, capa, hero."
  - `Caption Instagram` — "Curto, com quebras de linha, espaço pra hashtags."
  - `Bio / descrição curta` — "Bio de perfil, descrição de produto, sobre nós."
  - `Outro — vou descrever` — "Conta o que precisa que eu adapto."

**P2 — Tema e ângulo**
- Pergunta: "Sobre o que? Descreve em 1-2 frases o tema principal e qual é o seu ângulo. Pode colar referência se tiver."
- Header: `Tema`
- Opções: (deixe `Pular` como uma das opções, outras dependem do contexto — pode passar lista vazia se o usuário precisa só de espaço pra escrever)

**P3 — Objetivo**
- Pergunta: "Qual é o objetivo? O que você quer que a pessoa faça ou pense depois de ler?"
- Header: `Objetivo`
- Opções:
  - `Informar / educar` — "Compartilhar conhecimento, sem CTA forte."
  - `Engajar / iniciar conversa` — "Provocar resposta, comentário, repost."
  - `Vender / converter` — "Levar pra ação comercial (call, compra, inscrição)."
  - `Construir autoridade` — "Posicionar você como referência."
  - `Pular`

**P4 — Comprimento (só pergunte se P1 = Post LinkedIn ou Email)**
- Pergunta: "Comprimento?"
- Header: `Tamanho`
- Opções: `Curto (1 parágrafo)` / `Médio (3-4 parágrafos)` / `Longo (5+ parágrafos com história)` / `Pular`

---

## Geração

Com os dados coletados + voz do `me.md`, gere 3 variações distintas.

Cada variação deve ter um ângulo diferente:
- **V1 — Padrão da voz do usuário**: replica fielmente o estilo do `me.md`
- **V2 — Mais provocativa / contrária**: usa hook que vai contra o senso comum
- **V3 — Mais história / narrativa**: começa com cena, micro-história ou observação concreta

Apresente em markdown, separadas por `---`:

```markdown
## V1 — {{rótulo curto}}

{{texto da variação 1}}

---

## V2 — {{rótulo curto}}

{{texto da variação 2}}

---

## V3 — {{rótulo curto}}

{{texto da variação 3}}
```

Para **Post LinkedIn**: usa quebras de linha generosas, hook na primeira linha, sem hashtags genéricas.

Para **Email**: inclui `Subject:` antes do corpo.

Para **Headline**: dá só a frase, sem rodeio.

Para **Caption Instagram**: usa quebras com `.` em linhas isoladas pra criar respiro. Termina com 3-5 hashtags relevantes (não genéricas como #marketing — específicas do nicho).

Para **Bio**: máximo 150 caracteres por variação.

---

## Salvar

Depois de gerar, pergunte:

- Pergunta: "Quer salvar no vault?"
- Header: `Salvar`
- Opções:
  - `Sim — salvar as 3 variações` — "Cria arquivo em 04 Resources/textos/."
  - `Sim — só a variação que escolhi` — "Você fala qual e eu salvo só essa."
  - `Não` — "Só usar agora."

Se sim, crie a pasta se não existir:
```bash
mkdir -p "04 Resources/textos"
```

Salvar em `04 Resources/textos/YYYY-MM-DD-{{tipo}}-{{slug-do-tema}}.md` com frontmatter:

```yaml
---
type: copy
status: draft
date: YYYY-MM-DD
tags: [{{tipo}}, escrita]
canal: {{tipo}}
tema: {{tema curto}}
---
```

---

## Confirmação

Se salvou:
> "Salvo em `04 Resources/textos/{{nome-do-arquivo}}`. Pra escrever outro, roda `/escrever` de novo."

Se não salvou:
> "Beleza. Pra escrever outro, roda `/escrever` de novo."

Direto ao ponto, sem floreio.

---

## Regras

- Sempre use a voz do `me.md` na V1. Variações 2 e 3 podem se afastar pra abrir espaço de teste.
- Nunca use palavras que o `me.md` lista como "NUNCA uso".
- Não invente prova social (números, depoimentos) se o usuário não deu.
- Se o usuário colou referência no P2, espelhe a estrutura dela, não copie texto.
- Não use os bordões padrão de IA: "imagine", "no mundo de hoje", "em um cenário", "game-changer", "leve seu X pro próximo nível".

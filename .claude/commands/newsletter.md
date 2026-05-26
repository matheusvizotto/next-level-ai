---
description: Escreve uma edição completa de newsletter — subject lines, intro, corpo estruturado, fechamento, CTA. Repurpose de YouTube, blog ou ideia.
---

# Newsletter — Edição Completa

Você vai produzir 1 edição completa de newsletter pronta pra mandar, usando voz e contexto do `02 Context/me.md`.

---

## Idioma / Language

Detecte o idioma da mensagem e use em tudo. PT-BR padrão.

---

## Antes de começar

Leia `02 Context/me.md`:
- "Tom de Voz"
- "Audiência" — quem assina sua newsletter
- "Canais" — confirme que newsletter é canal ativo

Se houver `02 Context/marca.md`, leia também — pode ter nome da newsletter, plataforma (Beehiiv, Substack, etc.), frequência.

---

## Fase 1 — Material de partida

Pergunta via AskUserQuestion:

- Pergunta: "De onde vem essa edição?"
- Header: `Fonte`
- Opções:
  - `Ideia bruta` — "Conta em 2-3 frases o que quer comunicar."
  - `Vídeo YouTube — link` — "Cola o link."
  - `Post LinkedIn que bombou` — "Cola o post, expandimos."
  - `Reflexão da semana` — "O que aprendeu, o que viu, o que está observando."
  - `Tutorial / how-to específico` — "Você ensina algo passo a passo."
  - `Análise / opinião` — "Você tem uma posição forte sobre algo."

Depois da escolha, peça o material.

---

## Fase 2 — Definir promessa central

A newsletter precisa de UMA promessa clara — o que o leitor sai sabendo depois de ler.

Identifique 2-3 promessas possíveis baseadas no material. Apresente:

> "Possíveis promessas pra essa edição:
> 1. {{promessa 1 — formato: 'Depois dessa edição você vai saber X'}}
> 2. {{promessa 2}}
> 3. {{promessa 3}}
>
> Qual você quer?"

Aguarde escolha.

---

## Fase 3 — Definir estrutura

Pergunta via AskUserQuestion:

- Pergunta: "Que formato de edição? (escolha 1 — afeta tom e comprimento)"
- Header: `Formato`
- Opções:
  - `Reflexão pessoal (400-600 palavras)` — "Tom mais íntimo, 1 ideia central, sem subtítulos."
  - `Ensino prático (800-1200 palavras)` — "Como fazer X. Estrutura clara, subtítulos, exemplo."
  - `Análise (1000-1500 palavras)` — "Você defende uma posição com evidência."
  - `Curadoria (300-500 palavras)` — "Você junta 3-5 coisas úteis da semana e comenta."
  - `Tutorial técnico (1200+ palavras)` — "Passo a passo com código/printscreen."

---

## Fase 4 — Gerar a edição

Estrutura padrão (adapta ao formato):

### 1. Subject Line (3 variações)
Apresente 3 variações:

**V1 — Curiosidade:**
{{subject que cria gap de conhecimento}}

**V2 — Benefício direto:**
{{subject que entrega valor explícito}}

**V3 — Pessoal / específico:**
{{subject que parece email de amigo, não newsletter}}

Regras de subject:
- 30-50 caracteres ideal
- Sem CAPS, sem emoji excessivo
- Sem "Newsletter #42 — ..." (chato)

### 2. Preheader (1 frase, 60-90 caracteres)
{{frase que complementa o subject, aparece no preview do inbox}}

### 3. Abertura (2-4 frases)
Padrão Brasil que funciona:
- Cena específica OU
- Confissão OU
- Pergunta direta ao leitor

Não:
- "Espero que esteja bem."
- "É um prazer escrever pra você."
- "Vou começar com uma reflexão..."

### 4. Promessa (1 frase explícita)
"Nessa edição: {{promessa da Fase 2}}."

### 5. Corpo (adapta ao formato)

**Reflexão pessoal:** 1 ideia, 3-4 parágrafos, sem subtítulos.

**Ensino prático:**
- Setup (por que isso importa)
- Os N passos / componentes (com subtítulos `##`)
- Exemplo concreto
- Erro comum

**Análise:**
- Tese clara
- 2-3 evidências
- Contra-argumento + resposta
- Implicação

**Curadoria:**
- Item 1: {{título}} — {{1-2 frases por que importa}}
- Item 2-5: idem

**Tutorial técnico:**
- Pré-requisito
- Passos numerados
- Código / config
- Resultado esperado
- Próximo passo

### 6. Fechamento (2-3 frases)
Volta pro pessoal. Cita o leitor: "Se você {{situação}}, {{ação sugerida}}."

### 7. P.S. (opcional mas recomendado)
Item separado. Mais informal. Frequentemente onde vai o CTA secundário.

### 8. Assinatura
"— {{primeiro nome do me.md}}"

---

## Fase 5 — Apresentar

Apresente a edição completa em markdown, bem estruturada. Inclua todos os elementos (3 subjects, preheader, corpo, etc.).

Depois, pergunte:

- Pergunta: "Quer ajustar algo? Posso reescrever uma seção específica."
- Header: `Ajustes`
- Opções:
  - `Tá bom assim` — "Vamos salvar."
  - `Trocar o subject` — "Gero 3 novos."
  - `Reescrever abertura` — "Tento outro ângulo."
  - `Mudar tom` — "Mais formal / informal / técnico."

Aplique ajustes até o usuário aprovar.

---

## Fase 6 — Salvar

Crie pasta se não existir:
```bash
mkdir -p "04 Resources/textos/newsletter"
```

Salve em `04 Resources/textos/newsletter/YYYY-MM-DD-{{slug-do-tema}}.md`:

```yaml
---
type: copy
status: ready-to-send
date: YYYY-MM-DD
tags: [newsletter, edicao]
canal: newsletter
formato: {{do Fase 3}}
subject_escolhido: {{depois que usuário escolher um, marca aqui}}
---
```

Embaixo, a edição completa.

---

## Fase 7 — Próximos passos

> "Salvo em `04 Resources/textos/newsletter/{{arquivo}}`.
>
> Próximos passos:
> 1. Escolher 1 dos 3 subjects (testa A/B se a plataforma deixa)
> 2. Subir na plataforma ({{nome se estiver no me.md, senão 'Beehiiv / Substack / ConvertKit'}})
> 3. Mandar pra você primeiro como teste antes de pra lista
>
> Pra próxima edição: `/newsletter` de novo. Pra repurpose dessa edição em LinkedIn: `/linkedin`."

---

## Regras

- Voz do `me.md` é não-negociável.
- Comprimento adequado ao formato — não enrole pra atingir contagem.
- Subject sem "Newsletter #N" ou nome da newsletter no início (chato e baixa CTR).
- P.S. é frequentemente a parte mais lida — use bem.
- Não invente assinante, número de inscritos, ou caso específico. Use só o que o usuário deu ou o que está em `me.md`.
- Banido: "espero que esteja bem", "vou começar com", "no mundo de hoje", "imagine", "vamos lá".

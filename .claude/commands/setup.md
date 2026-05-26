---
description: Configura o AI OS para você — faz 6 perguntas, busca seu contexto online e preenche o vault com dados reais (não placeholders)
---

# Setup — Personalização do AI OS

Você vai configurar o vault para o usuário em 3 fases. Execute em ordem.

---

## Idioma / Language

Detecte o idioma da mensagem que invocou esse comando (a mensagem do usuário que disparou `/setup`) e use esse idioma em TODOS os textos visíveis: mensagem de boas-vindas, `question` e `header` do AskUserQuestion, cada `label` e `description` das opções, mensagens de status, e a confirmação final.

- Mensagem em português → PT-BR (padrão deste programa).
- Mensagem em inglês → traduza todas as perguntas, headers, labels e descriptions para inglês equivalente.
- Mensagem em espanhol → traduza para espanhol.
- Idioma ambíguo → PT-BR.

A audiência principal é Brasil, então PT-BR é o default. Mas se alguém rodar em outra língua, adapte por respeito. Conteúdo de arquivos (`02 Context/me.md`, frontmatter, `01 Daily/`, nomes de pasta) permanece como está no template — não traduza paths, chaves de frontmatter, nem nomes de arquivo.

Aceite respostas do usuário por intenção, não por string exata. Se ele responde em outro idioma do que a pergunta, continue na língua dele.

---

## Fase 1 — Boas-vindas

Antes de qualquer pergunta, envie esta mensagem curta:

> "Vou configurar o vault para você com 6 perguntas rápidas. Depois, posso buscar seu contexto de um link (LinkedIn, site, etc.) para preencher tudo com dados reais. Pode pular qualquer pergunta respondendo 'pular'."

---

## Fase 2 — 6 Perguntas (uma por vez via AskUserQuestion)

Faça uma pergunta por vez. Não agrupe. Não comente entre as perguntas — vá direto para a próxima.

**P1 — Você**
- Pergunta: "Qual é o seu nome completo e onde você mora?"
- Header: `Identidade`
- Opções: `Só o nome` / `Nome + cidade` / `Nome + cidade + país` / `Pular`

**P2 — O que você faz**
- Pergunta: "Em uma frase: o que você faz profissionalmente, para quem, e que resultado gera?"
- Header: `Profissão`
- Opções: `Sou funcionário CLT` / `Sou freelancer/consultor` / `Tenho meu próprio negócio` / `Pular`

**P3 — Objetivo agora**
- Pergunta: "Qual é a sua principal meta para os próximos 90 dias?"
- Header: `Meta`
- Opções: `Crescer na carreira` / `Lançar algo novo` / `Aumentar renda` / `Pular`

**P4 — Ferramentas**
- Pergunta: "Quais ferramentas você usa no dia a dia? (ex: Notion, Linear, Slack, Google Workspace...)"
- Header: `Stack`
- Opções: `Suite Google` / `Suite Microsoft` / `Notion + Slack` / `Pular`

**P5 — Tom de voz**
- Pergunta: "Como você se descreve quando escreve? Escolha o que mais combina."
- Header: `Voz`
- Opções: `Direto e objetivo` / `Analítico e detalhado` / `Informal e descontraído` / `Pular`

**P6 — Principal dor**
- Pergunta: "O que mais consome seu tempo ou atenção hoje que você gostaria de automatizar ou simplificar?"
- Header: `Dor`
- Opções: `Reuniões e follow-ups` / `Criação de conteúdo` / `Relatórios e análises` / `Pular`

---

## Fase 3 — Drop de contexto (sempre perguntar, mesmo se P1-P6 foram ricas)

Após P6, faça esta pergunta via AskUserQuestion:

- Pergunta: "Posso buscar mais contexto seu de algum link ou arquivo? Cole um link do LinkedIn, site da empresa, Notion público, ou qualquer doc. Quanto mais contexto, mais personalizado fica o vault — em vez de deixar placeholders, preencho com seus dados reais."
- Header: `Contexto`
- Opções:
  - `Sim — vou colar um link` — "LinkedIn, site, Notion, Google Docs..."
  - `Sim — tenho um arquivo` — "PDF, Word, MD..."
  - `Não — usar só as respostas acima` — "Configurar com o que já temos"
  - `Pular`

**Se o usuário colar um link:** busque com WebFetch. Extraia nome, cargo, empresa, projetos, estilo de escrita, qualquer dado relevante.

**Se colar um arquivo:** leia com Read.

**Se escolher não:** siga com as respostas das 6 perguntas.

---

## Fase 4 — Construção (trabalhe em silêncio, sem narrar cada passo)

Use tudo que o usuário respondeu + o conteúdo buscado. Substitua TODOS os placeholders.

### 4.1 — Preencher `02 Context/me.md`

Leia o arquivo atual. Substitua cada `{{PLACEHOLDER}}` com dados reais das respostas + contexto buscado.

Regras:
- Se não tiver dado para uma seção: remova a seção inteira (nunca deixe placeholder visível)
- Use as palavras do próprio usuário quando ele escreveu em "Outro"
- Frontmatter: substitua `{{DATA DE HOJE}}` pela data atual (formato YYYY-MM-DD)

### 4.2 — Criar nota do Dia 1 em `01 Daily/`

Crie o arquivo `01 Daily/YYYY-MM-DD.md` com a data de hoje:

```markdown
---
type: daily-note
date: YYYY-MM-DD
status: active
tags: [daily, setup]
---

## Sessão de Setup

- **Foco:** Configuração inicial do AI OS
- **Concluído:** Vault personalizado com contexto real
- **Projetos ativos:** {{liste os projetos mencionados pelo usuário, ou deixe em branco}}
- **Próximos passos:** {{1-2 ações concretas baseadas no objetivo do usuário}}
```

### 4.3 — Confirmar para o usuário

Após construir tudo, envie uma mensagem curta:

> "Pronto. Aqui está o que configurei:
> - `02 Context/me.md` — preenchido com seus dados reais
> - `01 Daily/[data].md` — nota do dia criada
>
> Próximo passo: [1 ação concreta baseada no objetivo principal do usuário]."

Não liste cada campo alterado. Não parabenize. Direto ao ponto.

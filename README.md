# Next Level AI — Starter Kit

**por Matheus Vizotto** · [Instagram](https://instagram.com/matheusvizotto) · [matheusvizotto.com](https://matheusvizotto.com)

---

> Transforme o Obsidian no seu sistema operacional com IA.
> Funciona com Claude Code, Cursor, Gemini CLI — qualquer ferramenta que leia markdown.

---

## O que está incluído

```
next-level-ai/
├── .claude/
│   └── commands/
│       ├── setup.md              → Personalização inicial completa
│       ├── assistente.md         → Operação diária (sessões, revisões, tasks)
│       ├── importar-contexto.md  → Trazer contexto de outra IA
│       ├── escrever.md           → Texto curto na sua voz
│       ├── linkedin.md           → Post LinkedIn dedicado
│       ├── newsletter.md         → Edição de newsletter completa
│       ├── case-study.md         → Case study estruturado
│       ├── landing-page.md       → Brief de landing page
│       ├── seo-pagina.md         → Auditoria SEO de URL
│       ├── email-sequencia.md    → Drip campaign automatizada
│       ├── ads-google.md         → Google Ads (audit/build/optimize/copy)
│       └── pesquisa.md           → Deep research multi-fonte
├── CLAUDE.md                     → Contexto para o Claude (auto-loaded)
├── 00 Inbox/                     → Zona de captura
├── 01 Daily/                     → Notas de sessão e diário
├── 02 Context/                   → Identidade permanente (me.md, estratégia, marca)
├── 03 Projects/                  → Projetos ativos
├── 03 Intelligence/              → Pesquisas, decisões, reuniões, market intel
├── 04 Resources/                 → Biblioteca pessoal (textos, cases, ads, SEO)
└── prompts/                      → 10 prompts copy-paste prontos
```

---

## Instalação em 3 passos

### Passo 1 — Clone o repositório

```bash
git clone https://github.com/matheusvizotto/next-level-ai.git meu-vault
cd meu-vault
```

### Passo 2 — Abra como vault no Obsidian

- Abra o Obsidian
- Clique em "Open folder as vault"
- Selecione a pasta `meu-vault`

### Passo 3 — Rode `/setup` no Claude Code

```bash
claude
```

Dentro do Claude Code, rode `/setup`. Ele vai:
1. Perguntar se você quer um agente persistente
2. Oferecer importar contexto de outra IA (ChatGPT, Claude, Gemini)
3. Fazer 8 perguntas curtas
4. Preencher seu `me.md` com dados reais (não placeholders)

---

## Comandos disponíveis

### Operacional

| Comando | O que faz |
|---|---|
| `/setup` | Personalização inicial completa do vault |
| `/assistente` | Operação diária — resume sessão, revisão diária/semanal, tasks, memória, reunião |
| `/importar-contexto` | Traz contexto de outra IA (ChatGPT, Claude, Gemini, Perplexity) |

### Escrita e conteúdo

| Comando | O que faz |
|---|---|
| `/escrever` | Texto curto na sua voz — 3 variações (post LinkedIn, email, headline, bio, caption) |
| `/linkedin` | Post LinkedIn dedicado com hooks testados, 4 estruturas, repurpose de YT/blog |
| `/newsletter` | Edição completa de newsletter — 3 subjects, corpo estruturado, P.S. |
| `/case-study` | Case study estruturado — entrevista, citações, números, lições |

### Web e SEO

| Comando | O que faz |
|---|---|
| `/landing-page` | Brief de landing page completo (positioning, headline, copy seção por seção) |
| `/seo-pagina` | Auditoria SEO de uma URL — on-page, meta, schema, relatório priorizado |

### Crescimento

| Comando | O que faz |
|---|---|
| `/email-sequencia` | Drip campaign — welcome, onboarding, nurture, win-back, pré-venda |
| `/ads-google` | Google Ads — audit, build, optimize, copy |
| `/pesquisa` | Deep research multi-fonte com citações verificáveis |

Todos os comandos funcionam em PT-BR por padrão, mas detectam o idioma da sua mensagem e adaptam.

---

## Os 10 prompts copy-paste

Pra quando você quer só colar no chat sem rodar comando:

| # | Arquivo | Para que serve |
|---|---------|---------------|
| 01 | `revisao-diaria.md` | Revisar o dia, capturar aprendizados |
| 02 | `notas-reuniao.md` | Processar reuniões em ações claras |
| 03 | `brief-conteudo.md` | Criar brief de conteúdo para qualquer canal |
| 04 | `rascunho-email.md` | Redigir e-mails profissionais |
| 05 | `plano-projeto.md` | Estruturar qualquer novo projeto |
| 06 | `pesquisa-concorrentes.md` | Mapa competitivo rápido |
| 07 | `post-linkedin.md` | Post de LinkedIn no seu estilo de voz |
| 08 | `revisao-semanal.md` | Revisão semanal estruturada |
| 09 | `registro-decisao.md` | Documentar decisões com raciocínio |
| 10 | `despejo-ideias.md` | Capturar e organizar ideias brutas |

---

## Fluxo recomendado pra primeira semana

1. **Dia 1 — Setup**
   - Roda `/setup`. Se você usa ChatGPT, escolhe "Sim — uso ChatGPT" pra importar contexto profundo
   - Revisa `02 Context/me.md` e ajusta o que não bate

2. **Dia 2 — Primeiro conteúdo**
   - Roda `/linkedin` pra produzir 1 post completo
   - Avalia se a voz está acertada — ajusta `me.md` se precisar

3. **Dia 3 — Sua oferta**
   - Roda `/landing-page` pra mapear seu produto ou serviço principal
   - Salva em `04 Resources/landing-pages/`

4. **Dia 4 — Captação**
   - Roda `/email-sequencia` modo "Welcome" pra quando alguém entrar na sua lista
   - Roda `/seo-pagina` na URL da landing pra ver gaps

5. **Dia 5 — Newsletter ou case**
   - Se você manda newsletter: `/newsletter`
   - Se você quer documentar caso: `/case-study`

6. **Dia 6 — Pesquisa estratégica**
   - Roda `/pesquisa` sobre algo importante (concorrente, tendência, ferramenta)

7. **Dia 7 — Revisão**
   - Roda `/assistente` e pede "revisão semanal" — fecha a semana com clareza

Depois disso, `/assistente` vira o comando principal do dia a dia. Os outros comandos viram especialistas que você chama quando precisa.

---

## Quer aprender a usar isso do zero?

Estou preparando um **programa de mentoria completo** — Claude Code, Obsidian, agentes de IA e vibe coding para profissionais brasileiros que querem trabalhar diferente.

👉 **[Entra na lista de espera](https://matheusvizotto.com)** — vagas limitadas para a primeira turma.

---

*Feito com Claude Code. Distribuído gratuitamente.*

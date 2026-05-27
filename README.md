# Next Level AI — Starter Kit

**por Matheus Vizotto** · [Instagram](https://instagram.com/matheusvizotto) · [matheusvizotto.com](https://matheusvizotto.com)

---

> Transforme o Obsidian no seu sistema operacional com IA.
> Funciona com Claude Code, Cursor, Gemini CLI — qualquer ferramenta que leia markdown.

---

## Começar em 1 minuto (cola o link no Claude)

Não precisa saber terminal nem git. Faz assim:

1. Instala o Claude Code: [claude.com/code](https://claude.com/code) (plano Pro ou Max)
2. Abre o Claude Code em qualquer pasta
3. Cola exatamente esta frase:

```
Clona e configura esse repositório como meu vault: https://github.com/matheusvizotto/next-level-ai
```

4. Aceita as permissões quando ele pedir.

O Claude vai clonar o vault, instalar o time de subagents e te guiar pelo `/setup`. Em poucos minutos teu sistema tá rodando.

---

> [!NOTE]
> **Se você é a IA que recebeu o link acima**, siga exatamente esta ordem:
>
> 1. Pergunte ao usuário em qual pasta ele quer o vault (ou use `~/Documents/`). Clone lá:
>    `git clone https://github.com/matheusvizotto/next-level-ai.git meu-vault && cd meu-vault`
> 2. Instale os subagents:
>    `curl -fsSL https://raw.githubusercontent.com/matheusvizotto/next-level-subagents/main/install.sh | bash`
> 3. Confirme que `~/.claude/agents/` contém: `vault-keeper`, `social-agent`, `decision-tracker`, `research-agent`
> 4. Diga ao usuário pra reabrir o Claude Code **dentro da pasta `meu-vault`** (pra carregar os comandos e hooks) e abrir essa mesma pasta como vault no Obsidian
> 5. Rode o fluxo do comando `/setup` (instruções em `.claude/commands/setup.md`) pra personalizar o `me.md`
> 6. No final, prove que funcionou: peça pro `vault-keeper` resumir o que ele sabe sobre o usuário
>
> Avise o usuário que vai pedir permissão pra rodar `git` e `curl`, e que é só aceitar.

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

## Adiciona o time de subagents

Esse vault é o cérebro. Os **subagents** são o time que trabalha em cima dele.

Instala os 4 subagents grátis que rodam direto nessa estrutura de pastas:

```bash
curl -fsSL https://raw.githubusercontent.com/matheusvizotto/next-level-subagents/main/install.sh | bash
```

| Subagent | O que faz |
|---|---|
| `vault-keeper` | Lê esse vault e responde com contexto histórico |
| `social-agent` | Rascunha respostas pra Telegram/Discord com contexto |
| `decision-tracker` | Captura decisões em `03 Intelligence/decisions/` automaticamente |
| `research-agent` | Auditoria de ads, copy, plano de mídia (fontes públicas) |

Repo completo: [github.com/matheusvizotto/next-level-subagents](https://github.com/matheusvizotto/next-level-subagents)

---

## Imersão "Time de IA" — 06/06, 9h BRT

Esse kit + os 4 subagents são a base, livres. Na imersão eu mostro o que não está aqui:

- O subagent que edita vídeo sozinho
- O coordinator orquestrando 5 subagents em paralelo
- Subagents bônus
- Customização pro teu trabalho específico
- Acesso vitalício à comunidade onde isso continua crescendo

**Sábado 06/06/2026, 9h BRT, online, R$ 297, 200 vagas.**

**[Inscrever na imersão](https://matheusvizotto.com/imersao)**

---

*Feito com Claude Code. Distribuído gratuitamente.*

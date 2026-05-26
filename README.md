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
│       ├── landing-page.md       → Brief de landing page
│       ├── escrever.md           → Texto curto na sua voz
│       └── importar-contexto.md  → Trazer contexto de outra IA
├── CLAUDE.md                     → Contexto para o Claude (auto-loaded)
├── 00 Inbox/                     → Zona de captura
├── 01 Daily/                     → Notas de sessão e diário
├── 02 Context/                   → Identidade permanente (me.md, estratégia, marca)
├── 03 Projects/                  → Projetos ativos
├── 04 Resources/                 → Biblioteca pessoal (prompts, textos, landing pages)
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

| Comando | O que faz |
|---|---|
| `/setup` | Personalização inicial completa do vault |
| `/landing-page` | Brief completo de landing page (positioning, headline, seções, copy) |
| `/escrever` | Escreve texto curto na sua voz (post LinkedIn, email, headline, bio, caption) |
| `/importar-contexto` | Traz contexto de outra IA pro vault — atualiza `me.md` com profundidade |

Cada comando funciona em PT-BR por padrão, mas detecta o idioma da sua mensagem e adapta.

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

1. **Dia 1** — Roda `/setup`. Se você usa ChatGPT, escolhe "Sim — uso ChatGPT" pra importar contexto profundo.
2. **Dia 2** — Roda `/escrever` pra produzir 1 post LinkedIn. Vê se a voz do `me.md` está acertada — ajusta se precisar.
3. **Dia 3** — Roda `/landing-page` pra mapear sua próxima oferta.
4. **Resto da semana** — Usa os prompts copy-paste em `prompts/` pro dia a dia. No fim da semana, revisão.

---

## Quer aprender a usar isso do zero?

Estou preparando um **programa de mentoria completo** — Claude Code, Obsidian, agentes de IA e vibe coding para profissionais brasileiros que querem trabalhar diferente.

👉 **[Entra na lista de espera](https://matheusvizotto.com)** — vagas limitadas para a primeira turma.

---

*Feito com Claude Code. Distribuído gratuitamente.*

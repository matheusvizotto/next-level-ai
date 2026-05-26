# AI OS — Central de Comando

Você é a IA operando neste vault. Tudo que precisa pra trabalhar bem está nos arquivos abaixo.

Leia no início de cada sessão. Não anuncie que está lendo. Apenas absorva e responda como se já estivesse na conversa.

---

## Session Startup (em ordem)

1. `knowledge/index.md` — Knowledge hub auto-injetado pelo hook `session-start.py`
2. `AIOS/index.md` — Catálogo de skills e comandos disponíveis
3. `AIOS/operating-rules.md` — Como você deve se comportar
4. `02 Context/me.md` (modo solo) **ou** `02 Context/operator.md` + `organization.md` + `team.md` (modo empresa)
5. Última nota em `01 Daily/` — O que aconteceu na sessão anterior

O hook `session-start.py` faz a injeção automática na primeira tool call. Você não precisa pedir esses arquivos — eles chegam.

---

## Mapas do vault (load on demand)

| Arquivo | Quando ler |
|---|---|
| `AIOS/Vault-Map.md` | Quando precisar saber onde algo vive ou onde rotear nova info |
| `AIOS/knowledge-routing.md` | Quando estiver salvando algo e não tiver certeza onde colocar |
| `AIOS/project-map.md` | Quando o usuário mencionar um projeto pelo nome |
| `AIOS/operating-rules.md` | Quando precisar relembrar regras de comportamento |

---

## Estrutura do Vault

```
00 Inbox/        — Captura rápida, processar e mover
01 Daily/        — Notas diárias (YYYY-MM-DD.md)
02 Context/      — Identidade permanente
03 Intelligence/ — Reuniões, decisões, concorrentes, mercado, pesquisas
03 Projects/     — Um subpasta por projeto ativo
04 Resources/    — Biblioteca: outputs dos comandos, prompts, frameworks
05 Archives/     — Conteúdo finalizado e histórico
AIOS/            — Camada portátil: skills, mapas, regras
knowledge/       — Knowledge hub auto-loaded em cada sessão
prompts/         — 10 prompts copy-paste prontos
```

Detalhes completos em `AIOS/Vault-Map.md`.

---

## Roteamento Rápido

| Tipo de conteúdo | Onde salvar |
|---|---|
| Identidade, preferências, estilo | `02 Context/me.md` (solo) / `operator.md` (empresa) |
| Sobre a empresa (modo empresa) | `02 Context/organization.md` |
| Sobre o time (modo empresa) | `02 Context/team.md` |
| Objetivos, estratégia | `02 Context/strategy.md` ou `estrategia.md` |
| Tom de voz, marca | `02 Context/brand.md` ou `marca.md` |
| Decisão com raciocínio | `03 Intelligence/decisions/YYYY-MM-DD-{slug}.md` |
| Notas de reunião | `03 Intelligence/meetings/{tipo}/` |
| Pesquisa profunda | `03 Intelligence/research/` |
| Projeto ativo | `03 Projects/{nome}/README.md` |
| Outputs de comandos | `04 Resources/{categoria}/` |
| Captura rápida | `00 Inbox/` |
| Sessão do dia | `01 Daily/YYYY-MM-DD.md` |
| Knowledge permanente (auto-loaded) | `knowledge/{dominio}.md` |
| Conteúdo finalizado | `05 Archives/` |

Tabela completa em `AIOS/knowledge-routing.md`.

---

## Regras Gerais

Detalhes em `AIOS/operating-rules.md`. Resumo:

- Leia os arquivos do Session Startup sempre na primeira mensagem
- Use `[[wikilinks]]` pra TODA referência interna — nunca markdown links
- Frontmatter YAML em todo arquivo: `type`, `date`, `status`, `tags`
- **Nunca peça permissão pra salvar** — salve e informe onde
- Quando o usuário corrige você, salve como regra permanente no `me.md`
- Prefira editar notas existentes a criar novas
- Tudo em PT-BR (paths e frontmatter keys ficam em inglês)
- Sem floreio: nunca "espero que esteja bem", "imagine", "no mundo de hoje", "vamos lá"

---

## Comandos

**Operacional:**
- `/setup` — Personaliza o vault: modo solo/empresa, agente, import de outra IA, 8 perguntas
- `/assistente` — Operação diária: resume sessão, daily/weekly review, tasks, memória, reunião
- `/importar-contexto` — Trazer contexto de outra IA depois do setup inicial

**Escrita e conteúdo:**
- `/escrever` — Texto curto na sua voz — 3 variações
- `/linkedin` — Post LinkedIn dedicado com hooks e estruturas
- `/newsletter` — Edição completa de newsletter
- `/case-study` — Case study estruturado

**Web e SEO:**
- `/landing-page` — Brief de landing page completo
- `/seo-pagina` — Auditoria SEO de URL

**Crescimento:**
- `/email-sequencia` — Drip campaign automatizada
- `/ads-google` — Google Ads (audit/build/optimize/copy)
- `/pesquisa` — Deep research multi-fonte

---

## Hooks

- `PreToolUse` → `.claude/hooks/session-start.py` — Injeta context files na primeira tool call
- `PreCompact` → `.claude/hooks/session-capture.py` — Lembra de persistir sessão antes de comprimir

Configurados em `.claude/settings.json`. Funcionam automaticamente — você não precisa invocar.

---

## Prompts Copy-Paste

`prompts/` tem 10 prompts prontos pra colar no chat sem rodar comando. Usar pra casos simples:

| Prompt | Quando usar |
|---|---|
| `01-revisao-diaria.md` | Início ou fim do dia (alternativa simples ao `/assistente`) |
| `02-notas-reuniao.md` | Após reunião (alternativa ao `/assistente` modo meeting) |
| `03-brief-conteudo.md` | Antes de criar conteúdo |
| `04-rascunho-email.md` | E-mails profissionais |
| `05-plano-projeto.md` | Iniciar projeto novo |
| `06-pesquisa-concorrentes.md` | Análise rápida de concorrente |
| `07-post-linkedin.md` | Post LinkedIn rápido (alternativa ao `/linkedin`) |
| `08-revisao-semanal.md` | Revisão semanal |
| `09-registro-decisao.md` | Documentar decisão |
| `10-despejo-ideias.md` | Brainstorm livre |

Comandos `/...` são mais robustos; prompts copy-paste são mais rápidos.

---

## Quer o sistema avançado?

Este kit é a base. Para versão avançada com multi-agent swarms, scripts de automação, hooks customizados, agentes 24/7 e skill pack completo, acesse: https://matheusvizotto.com/pt-br/produtos/obsidian

---
type: reference
status: active
tags: [navigation, vault-map, ai-os]
updated: 2026-05-26
---

# Vault Map — AI OS

Sitemap completo do seu vault. Consulte sempre que precisar saber onde algo vive, onde rotear nova informação, ou quando a IA perguntar sobre algum projeto.

Este arquivo responde **onde as coisas vão**. `02 Context/me.md` responde **quem opera** este vault. `CLAUDE.md` responde **como usar**. `AIOS/index.md` responde **o que dá pra fazer**.

---

## Estrutura raiz

```
CLAUDE.md                      — Pointer principal + project map
Vault-Map.md                   — Este arquivo: sitemap completo + roteamento
00 Inbox/                      — Zona de captura: notas brutas que precisam ser processadas
01 Daily/                      — Notas diárias de sessão (YYYY-MM-DD.md)
02 Context/                    — Camada de identidade (me.md, strategy.md, brand.md)
03 Intelligence/               — Reuniões, decisões, concorrentes, mercado, pesquisas
03 Projects/                   — Todos os projetos ativos
04 Resources/                  — Prompts, frameworks, swipe files, templates
05 Archives/                   — Conteúdo completado e histórico
AIOS/                          — Camada portátil de operação: skills, mapas, regras
knowledge/                     — Knowledge hub auto-loaded em cada sessão
.claude/                       — Configuração e hooks do Claude Code
prompts/                       — 10 prompts copy-paste prontos
```

---

## Pastas em detalhe

### `00 Inbox/`
Zona de captura. Tudo que chega aqui precisa ser processado e movido.

**Como usar:** Quando o inscrito diz "anota", "captura", "salva por enquanto" → cai aqui. Não é destino final.

**Quando processar:** Durante a revisão diária ou semanal, rodar `/assistente` em modo "tasks" pra mover cada item pro lugar certo.

---

### `01 Daily/`
Notas diárias de sessão. Uma por dia, formato `YYYY-MM-DD.md`.

**O que tem dentro:**
- Foco do dia
- O que foi feito
- Decisões tomadas
- Aprendizados
- Próximos passos pra amanhã
- Tasks abertas

**Auto-lida:** A nota mais recente é carregada no início de toda sessão pela `session-start.py` hook.

---

### `02 Context/`
Camada de identidade permanente. Lida no início de cada sessão.

**Arquivos:**
- `me.md` (solo) ou `operator.md` + `organization.md` + `team.md` (empresa) — quem você é
- `brand.md` — voz, tom, palavras-chave da marca (criado se relevante)
- `strategy.md` — vision, metas 90d/1y/3-5y (criado se relevante)
- Outros que vão sendo criados conforme contexto aparece

---

### `03 Intelligence/`
Conhecimento sobre o mundo externo + decisões internas.

**Estrutura:**
```
03 Intelligence/
├── meetings/              — Notas de reunião por tipo
│   ├── client-calls/      — Calls com clientes
│   ├── one-on-ones/       — 1:1 com colaboradores
│   ├── team-standups/     — Standups de time
│   └── general/           — Reuniões avulsas
├── decisions/             — Decisões importantes com raciocínio (YYYY-MM-DD-{slug}.md)
├── competitors/           — Análise de concorrentes (1 arquivo por concorrente)
├── market/                — Insights de mercado por tópico
├── research/              — Saídas do comando /pesquisa
└── archive/               — Arquivamento de conteúdo desta pasta
```

**Modo empresa adiciona:**
- `processes/` — Documentação de processos da empresa
- `meetings/board-reviews/`, `meetings/all-hands/`, `meetings/cross-team/`

---

### `03 Projects/`
Cada projeto ativo tem uma subpasta. Cada projeto tem um `README.md` como entry point.

**Estrutura típica:**
```
03 Projects/{nome-do-projeto}/
├── README.md              — Visão geral, status, próximos passos
├── research/              — Pesquisas relacionadas
├── specs/                 — Specs e requisitos
├── drafts/                — Rascunhos de conteúdo
└── ideas/                 — Brainstorm livre
```

**Quando criar:** Quando o inscrito menciona algo que vai durar mais de 1 semana de trabalho — vira projeto. Avulso fica em `00 Inbox/` ou `01 Daily/`.

---

### `04 Resources/`
Biblioteca pessoal reutilizável. Prompts, frameworks, referências, templates.

**Estrutura emerge conforme uso:**
```
04 Resources/
├── textos/                — Outputs do /escrever, /linkedin, /newsletter
│   ├── linkedin/
│   ├── newsletter/
│   └── email-sequencias/
├── landing-pages/         — Briefs do /landing-page
├── cases/                 — Outputs do /case-study
├── seo/auditorias/        — Outputs do /seo-pagina
├── ads/google/            — Outputs do /ads-google
├── attachments/           — Imagens, PDFs, anexos
└── (outros que você criar)
```

---

### `05 Archives/`
Conteúdo finalizado, histórico. Coisas que não vão sumir, mas não são mais ativas.

**Quando usar:**
- Projeto finalizado → mover de `03 Projects/{nome}/` pra `05 Archives/projects/{nome}/`
- Edição de newsletter já publicada → opcional, mover de `04 Resources/textos/newsletter/` pra `05 Archives/newsletter/`
- Cliente que saiu → mover daily notes específicas, briefs, etc.

---

### `AIOS/`
Camada portátil. Esta pasta é o cérebro operacional que não depende de ferramenta.

**Arquivos:**
- `index.md` — Catálogo de skills e mapas
- `Vault-Map.md` — Este arquivo
- `operating-rules.md` — Como a IA deve se comportar
- `knowledge-routing.md` — Onde rotear cada tipo de informação
- `project-map.md` — Mapa de projetos ativos
- `blueprint/` — Arquitetura interna do AI OS

---

### `knowledge/`
Knowledge hub auto-loaded em cada sessão.

**O que vai aqui:**
- `index.md` — Navegação dos knowledge files (auto-loaded primeiro)
- Domínios de expertise que você quer que a IA tenha sempre (ex: `copywriting.md`, `seo-fundamentals.md`, `linkedin-strategy.md`)

**Diferença de `04 Resources/`:**
- `knowledge/` é carregado automaticamente em toda sessão (IA "lembra" sempre)
- `04 Resources/` é referência que a IA busca quando precisa (não carregado por default)

---

## Hub Notes (nós de conexão)

Use wikilinks pra esses arquivos sempre que mencionar o assunto:

| Hub | Propósito |
|---|---|
| `[[02 Context/me]]` | Você (modo solo) — identidade central |
| `[[02 Context/operator]]` + `[[02 Context/organization]]` | Você + empresa (modo empresa) |
| `[[AIOS/index]]` | Comandos e skills disponíveis |
| `[[03 Projects/{nome}/README]]` | Cada projeto ativo |

Conectar com wikilinks faz o grafo do Obsidian crescer — você vê visualmente as conexões.

---

## Roteamento rápido

Pra saber pra onde vai uma informação nova, consulte [[AIOS/knowledge-routing]].

---

## Conectado a

[[Home]] · [[index]] · [[knowledge-routing]] · [[operating-rules]] · [[project-map]]

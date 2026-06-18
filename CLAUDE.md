# AI OS — Central de Comando

Você é a IA operando neste vault. Tudo que precisa pra trabalhar bem está nos arquivos abaixo.

Leia no início de cada sessão. Não anuncie que está lendo. Apenas absorva e responda como se já estivesse na conversa.

---

## Session Startup (faça na primeira mensagem)

Leia estes arquivos no começo de cada sessão. Não anuncie, só absorva e responda:

1. `02 Context/me.md` (modo solo) **ou** `02 Context/operator.md` + `organization.md` (modo empresa). Quem é o usuário.
2. A nota mais recente em `01 Daily/`. O que aconteceu na sessão anterior.
3. `AIOS/operating-rules.md`. Como você opera neste vault.
4. `AIOS/index.md`. Skills e comandos disponíveis.
5. `knowledge/index.md`. Conhecimento permanente.

O hook `SessionStart` já injeta a identidade e o último daily no contexto automaticamente. Se você não recebeu esse bloco (por exemplo, Python não está instalado na máquina), leia os arquivos acima você mesmo antes de responder. É isso que garante que você sempre conecta ao vault, com ou sem hook.

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
- `/assistente`: operação diária, resume sessão, daily/weekly review, tasks, memória, reunião
- `/organizar`: limpa o vault, roteia notas órfãs, conecta com wikilinks, arquiva redundância
- `/importar-contexto`: trazer contexto de outra IA depois do setup inicial

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

Configurados em `.claude/settings.json`, rodam sozinhos (requerem `python3` no PATH):

- `SessionStart` chama `.claude/hooks/session-start.py`: injeta identidade + último daily no contexto no início da sessão. O stdout do `SessionStart` entra no contexto do modelo. O evento `PreToolUse`, usado antes, NÃO injeta stdout no contexto, e era por isso que o agente parecia desconectado.
- `SessionEnd` chama `.claude/hooks/session-end.py`: documentação automática OPT-IN, desligada por padrão. Pra ligar, crie o arquivo `AIOS/autodoc.enabled` (ou exporte `AIOS_AUTODOC=1`). Fica off por padrão pra não gastar token nem travar a saída da sessão.
- `PreCompact` chama `.claude/hooks/session-capture.py`: lembra de persistir a sessão antes de comprimir.

Sem Python, o vault e os comandos continuam funcionando. Só a injeção e o resumo automáticos ficam off, e a IA lê os arquivos do Session Startup manualmente.

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

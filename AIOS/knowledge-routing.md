---
type: map
status: active
date: 2026-05-26
tags: [aios, routing, knowledge, portable]
---

## Knowledge Routing

Cada pedaço de informação tem uma casa. Roteie pra cá, nunca pra um catch-all.

---

### Tabela de Roteamento

| Tipo de conteúdo | Vai pra |
|---|---|
| Preferências pessoais, estilo, hábitos | `02 Context/me.md` (solo) ou `02 Context/operator.md` (empresa) |
| Estratégia e objetivos | `02 Context/strategy.md` ou `02 Context/estrategia.md` |
| Voz e tom da marca | `02 Context/brand.md` ou `02 Context/marca.md` |
| Sobre a empresa (modo empresa) | `02 Context/organization.md` |
| Sobre o time (modo empresa) | `02 Context/team.md` |
| Decisão com raciocínio | `03 Intelligence/decisions/YYYY-MM-DD-{slug}.md` |
| Notas de reunião | `03 Intelligence/meetings/{tipo}/YYYY-MM-DD-{slug}.md` |
| Insight sobre concorrente | `03 Intelligence/competitors/{nome}.md` |
| Insight de mercado | `03 Intelligence/market/{topico}.md` |
| Resultado de pesquisa profunda | `03 Intelligence/research/YYYY-MM-DD-{slug}.md` |
| Info sobre projeto ativo | `03 Projects/{nome}/README.md` ou subpasta |
| Pesquisa relacionada a projeto | `03 Projects/{nome}/research/{topico}.md` |
| Spec ou requisito de projeto | `03 Projects/{nome}/specs/{nome}.md` |
| Rascunho de conteúdo de projeto | `03 Projects/{nome}/drafts/{nome}.md` |
| Texto produzido (post, email, etc.) | `04 Resources/textos/{canal}/YYYY-MM-DD-{slug}.md` |
| Brief de landing page | `04 Resources/landing-pages/{slug}.md` |
| Case study | `04 Resources/cases/{cliente}.md` |
| Auditoria SEO | `04 Resources/seo/auditorias/YYYY-MM-DD-{site}.md` |
| Output de Google Ads | `04 Resources/ads/google/YYYY-MM-DD-{modo}-{slug}.md` |
| Recursos reutilizáveis (prompts, frameworks) | `04 Resources/` |
| Captura rápida não processada | `00 Inbox/` |
| Conteúdo finalizado/arquivado | `05 Archives/` |
| Knowledge domain (auto-loaded) | `knowledge/{dominio}.md` |
| Regras pra comportamento da IA | `02 Context/me.md` (seção Regras) |

---

### Sub-roteamento de Projetos

Quando aparece informação sobre um projeto, analise e route pra subpasta certa:

| Tipo de conteúdo | Subpasta |
|---|---|
| Status, deadline, overview | `03 Projects/{nome}/README.md` |
| Pesquisa, análise de concorrente | `03 Projects/{nome}/research/{topico}.md` |
| Spec, requisito, brief | `03 Projects/{nome}/specs/{nome}.md` |
| Rascunho, script, conteúdo escrito | `03 Projects/{nome}/drafts/{nome}.md` |
| Ideia, brainstorm | `03 Projects/{nome}/ideas/{nome}.md` |
| Notas de trabalho | `03 Projects/{nome}/notes/{nome}.md` |
| Feedback, review | `03 Projects/{nome}/feedback/{nome}.md` |

**Subpastas on-the-fly:** não crie pastas vazias antecipadamente. Quando chega conteúdo que precisa de subpasta, crie naquele momento.

**README como índice:** o README.md é entry point com overview + status + próximos passos + links pra subpastas. Não duplique conteúdo das subpastas no README.

**Ciclo de vida:** Projeto novo = só README.md → subpastas aparecem conforme tipos de conteúdo emergem → projeto concluído migra pra `05 Archives/projects/{nome}/`.

---

### Sub-roteamento de Reuniões

Quando processar transcrição/notas de reunião, route pelo tipo:

| Tipo | Pasta |
|---|---|
| Call com cliente | `03 Intelligence/meetings/client-calls/` |
| 1:1 com colaborador | `03 Intelligence/meetings/one-on-ones/` |
| Standup de time | `03 Intelligence/meetings/team-standups/` |
| Reunião avulsa | `03 Intelligence/meetings/general/` |
| Board review (modo empresa) | `03 Intelligence/meetings/board-reviews/` |
| All-hands (modo empresa) | `03 Intelligence/meetings/all-hands/` |
| Cross-team (modo empresa) | `03 Intelligence/meetings/cross-team/` |

Formato do nome do arquivo: `YYYY-MM-DD-{slug-da-reuniao}.md`.

---

### Sub-roteamento de Outputs de Comandos

Cada comando salva em pasta consistente:

| Comando | Salva em |
|---|---|
| `/escrever` | `04 Resources/textos/YYYY-MM-DD-{tipo}-{slug}.md` |
| `/linkedin` | `04 Resources/textos/linkedin/YYYY-MM-DD-{slug}.md` |
| `/newsletter` | `04 Resources/textos/newsletter/YYYY-MM-DD-{slug}.md` |
| `/email-sequencia` | `04 Resources/textos/email-sequencias/YYYY-MM-DD-{tipo}-{slug}.md` |
| `/landing-page` | `04 Resources/landing-pages/{slug}.md` |
| `/case-study` | `04 Resources/cases/{cliente-slug}.md` |
| `/seo-pagina` | `04 Resources/seo/auditorias/YYYY-MM-DD-{site}-{pagina}.md` |
| `/ads-google` | `04 Resources/ads/google/YYYY-MM-DD-{modo}-{slug}.md` |
| `/pesquisa` | `03 Intelligence/research/YYYY-MM-DD-{slug}.md` |

---

### Regra de ouro

**Antes de salvar qualquer coisa, pergunte:**
1. Isso é sobre o usuário ou sobre a empresa? → `02 Context/`
2. Isso é uma decisão, reunião, ou insight sobre o mundo externo? → `03 Intelligence/`
3. Isso é sobre um projeto específico? → `03 Projects/{nome}/`
4. Isso é output de um comando? → `04 Resources/` (subpasta do comando)
5. Isso é knowledge permanente que a IA deve sempre saber? → `knowledge/`
6. Não tenho certeza ainda? → `00 Inbox/`

Quando em dúvida, escolha o lugar mais específico possível. `00 Inbox/` é último recurso, não primeiro.

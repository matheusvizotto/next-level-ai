---
type: index
status: active
date: 2026-05-26
tags: [aios, skills, maps, portable]
---

> Maps: [[02 Context/me|me.md]] · [[Vault-Map]] · [[knowledge/index|Knowledge Index]]

## AIOS — Camada Portátil de Operação

Esta pasta é a camada portátil entre o seu vault e qualquer ferramenta de IA.

Os arquivos aqui são markdown puro — viajam pro Claude Code, Cursor, Gemini CLI, ou qualquer ferramenta que leia texto.

**Filosofia:** File over AI. O conhecimento pertence ao vault, não à ferramenta.

---

## Como funciona

Quando você abre o Claude Code (ou outra ferramenta de IA) dentro deste vault:

1. **Sessão começa** — o hook `session-start.py` injeta `knowledge/index.md`, este arquivo (`AIOS/index.md`), `AIOS/operating-rules.md` e `02 Context/me.md` no contexto inicial.
2. **A IA já te conhece** — sem precisar você explicar quem é, como trabalha, ou o que está fazendo.
3. **Trabalho rola** — você invoca comandos, faz perguntas, ela executa.
4. **Sessão termina ou comprime** — o hook `session-capture.py` lembra a IA de salvar progresso no daily antes de perder contexto.

Por isso `01 Daily/YYYY-MM-DD.md` é sempre lido na próxima sessão — vira memória persistente entre conversas.

---

## Comandos disponíveis

### Operacional

| Comando | O que faz |
|---|---|
| `/setup` | Personalização inicial completa do vault |
| `/assistente` | Operação diária, resume sessão, revisões, tasks, memória |
| `/organizar` | Limpa o vault: roteia notas órfãs, conecta com wikilinks, arquiva redundância |
| `/importar-contexto` | Trazer contexto de outra IA pro vault |

### Escrita e conteúdo

| Comando | O que faz |
|---|---|
| `/escrever` | Texto curto na sua voz — 3 variações |
| `/linkedin` | Post LinkedIn dedicado com hooks e estruturas |
| `/newsletter` | Edição completa de newsletter |
| `/case-study` | Case study estruturado de cliente |

### Web e SEO

| Comando | O que faz |
|---|---|
| `/landing-page` | Brief de landing page completo |
| `/seo-pagina` | Auditoria SEO de URL |

### Crescimento

| Comando | O que faz |
|---|---|
| `/email-sequencia` | Drip campaign automatizada |
| `/ads-google` | Google Ads (audit/build/optimize/copy) |
| `/pesquisa` | Deep research multi-fonte |

---

## Mapas-irmãos

Cada arquivo abaixo responde a uma pergunta diferente:

| Arquivo | Pergunta |
|---|---|
| [[AIOS/Vault-Map]] | Onde fica cada coisa neste vault? |
| [[AIOS/operating-rules]] | Como a IA deve se comportar? |
| [[AIOS/knowledge-routing]] | Pra onde vai cada tipo de informação? |
| [[AIOS/project-map]] | Quais projetos eu tenho ativos? |
| [[02 Context/me]] | Quem opera este vault? |
| [[CLAUDE.md]] | Como usar isso na prática? |

---

## Princípios da camada portátil

1. **Markdown puro**, nada de formatos proprietários
2. **Sem código em arquivos de contexto**, só texto que qualquer IA entende
3. **Caminhos relativos**, funciona em qualquer máquina
4. **Self-describing**, cada arquivo tem frontmatter explicando o que é
5. **Atualizável pela IA**, quando algo muda, a IA atualiza este arquivo automaticamente

---

## Conectado a

[[Home]] · [[Vault-Map]] · [[knowledge-routing]] · [[operating-rules]] · [[project-map]]

---
type: map
status: active
date: 2026-05-26
tags: [aios, projects, map]
---

# Project Map

Lista de todos os projetos ativos. Atualize conforme entra ou sai projeto.

A IA consulta este arquivo quando você menciona um projeto pelo nome — pra saber qual é, onde está o README, e qual o status atual.

---

## Estrutura

Cada projeto tem uma entrada com 4 campos:

| Campo | O que é |
|---|---|
| **Nome** | Como você se refere ao projeto na conversa |
| **README** | Wikilink pra `03 Projects/{nome}/README.md` |
| **Status** | `active`, `paused`, `completed`, `archived` |
| **Próximo passo** | 1 frase com a ação imediata pendente |

---

## Projetos Ativos

> Quando rodar `/setup`, esta seção é populada com os projetos que você mencionou. Você pode editar manualmente a qualquer momento.

<!--

Exemplo de formato — preencher conforme aparecem:

### Lançamento Newsletter

- **README:** [[03 Projects/Lançamento Newsletter/README]]
- **Status:** active
- **Próximo passo:** Subir landing page de captação

### Cliente Acme — Consultoria

- **README:** [[03 Projects/Cliente Acme/README]]
- **Status:** active
- **Próximo passo:** Apresentar diagnóstico segunda

-->

---

## Projetos Pausados

> Projetos que existem mas não estão sendo trabalhados agora. Mantém aqui pra referência.

<!-- Mesmo formato dos ativos. -->

---

## Projetos Concluídos

> Concluídos recentemente. Quando passar 30 dias, mover pra `05 Archives/projects/`.

<!-- Mesmo formato. Adicionar campo "Concluído em: YYYY-MM-DD". -->

---

## Como usar

**Adicionar projeto:** Quando você menciona algo que vai durar mais de 1 semana, a IA cria `03 Projects/{nome}/README.md` e adiciona aqui.

**Atualizar status:** Quando você fala que mudou de fase ("paused", "concluído"), a IA move entre seções deste arquivo.

**Consultar:** Quando você diz "como está o projeto X?", a IA lê este arquivo + o README do projeto pra te dar status atual.

**Arquivar:** Projetos concluídos ficam aqui por 30 dias, depois movem pra `05 Archives/projects/`.

---

## Princípios

- Um projeto = uma pasta em `03 Projects/{nome}/`
- README é a porta de entrada — overview + status + próximos passos
- Subpastas (research, specs, drafts, ideas, notes, feedback) aparecem conforme tipos de conteúdo emergem
- Quando algo dura menos de 1 semana, não é projeto, fica em daily ou inbox

---

## Conectado a

[[Home]] · [[index]] · [[Vault-Map]] · [[knowledge-routing]] · [[operating-rules]]

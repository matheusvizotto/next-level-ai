---
type: guide
status: active
date: 2026-05-26
tags: [guide, archives]
---

# Archives — Guia desta pasta

Conteúdo finalizado, histórico. Coisas que não vão sumir, mas não são mais ativas.

---

## Quando mover algo pra cá

- **Projeto finalizado** → `03 Projects/{nome}/` vira `05 Archives/projects/{nome}/`
- **Newsletter publicada há mais de 30 dias** → de `04 Resources/textos/newsletter/` pra `05 Archives/newsletter/`
- **Cliente que saiu** → daily notes específicas, briefs, cases vão pra `05 Archives/clients/{nome}/`
- **Documentação obsoleta mas histórica** → `05 Archives/docs/`
- **Versões anteriores de me.md, brand.md, strategy.md** → quando você atualizar, salvar a versão antiga aqui antes de sobrescrever
- **Decisões revogadas** → de `03 Intelligence/decisions/` pra `05 Archives/decisions/`

---

## Estrutura sugerida

```
05 Archives/
├── projects/        — Projetos concluídos (mais de 30 dias)
├── newsletter/      — Edições já publicadas e antigas
├── clients/         — Clientes que saíram
├── decisions/       — Decisões revogadas
├── docs/            — Documentação obsoleta
└── context/         — Versões antigas de me.md, brand.md, etc.
```

Crie subpastas conforme aparecer conteúdo. Não pre-crie pastas vazias.

---

## Como NÃO usar

- **Não é lixo.** O que vai pra cá é mantido pra referência futura, não pra esquecer.
- **Não é caixa-de-fora.** Se você não vai mais usar e não precisa lembrar, delete. Archive é pra histórico relevante.
- **Não é catch-all.** Se for conteúdo ativo, fica no lugar dele (`Projects/`, `Intelligence/`, `Resources/`).

---

## Auto-archive policy

Sugestão de regra:

- Projeto concluído + 30 dias sem atividade → move pra `05 Archives/projects/`
- Daily note com mais de 1 ano → mantém no `01 Daily/` mesmo (ele é registro histórico por natureza)
- Newsletter publicada + 6 meses → considera mover (se você está produzindo muito, o arquivo principal cresce)
- Decisão revisada → versão antiga vai pra `archives/decisions/`, versão nova fica em `Intelligence/decisions/`

Você pode rodar `/assistente` em modo "memory" ou pedir pra IA "arquiva o que está parado há mais de 30 dias" pra automatizar.

---

Navegação: volte para o hub em [[Home]]. As decisões revogadas chegam aqui vindas de [[03 Intelligence/decisions/README|Decisions]], e projetos aposentados saem de [[03 Projects/CLAUDE|Projects]].

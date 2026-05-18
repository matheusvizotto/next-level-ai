# Projects — Regras desta pasta

Um subpasta por projeto ativo. Cada projeto tem um `README.md` como ponto de entrada.

## Estrutura de um projeto

```
03 Projects/
└── Nome do Projeto/
    ├── README.md          ← status, próximos passos, links
    ├── research/          ← pesquisas, referências, análises
    ├── drafts/            ← rascunhos de conteúdo ou documentos
    └── notes/             ← notas de trabalho, scratchpad
```

## Quando criar subpastas
- Só crie se já houver conteúdo para colocar — não crie pastas vazias
- `research/` → quando houver uma pesquisa ou análise feita
- `drafts/` → quando houver um rascunho real
- `notes/` → para notas de trabalho soltas

## README.md padrão
```markdown
---
type: project
status: active
date: YYYY-MM-DD
tags: [project]
---

## Visão geral
{{o que é este projeto e por que existe}}

## Status atual
{{onde está agora}}

## Próximos passos
- [ ] {{ação 1}}
- [ ] {{ação 2}}
```

## Regras
- Quando o usuário mencionar um projeto: roteie para `03 Projects/{nome}/README.md`
- Projetos concluídos: mova para `04 Resources/arquivo/` ou exclua
- Use wikilinks para conectar projetos a notas diárias e contexto

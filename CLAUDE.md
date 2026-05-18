# AI OS — Central de Comando

Leia `02 Context/me.md` no início de cada sessão. Tudo sobre quem é o usuário e como trabalhar com ele está lá.

---

## Estrutura do Vault

```
00 Inbox/       — captura rápida, processar e mover
01 Daily/       — notas diárias (YYYY-MM-DD.md)
02 Context/     — identidade permanente (me.md, estrategia, marca)
03 Projects/    — um subpasta por projeto ativo
04 Resources/   — biblioteca: prompts, frameworks, templates
prompts/        — 10 prompts prontos para uso imediato
```

Cada pasta tem seu próprio `CLAUDE.md` com regras de roteamento específicas.

---

## Roteamento de Informação

| Tipo de conteúdo | Onde salvar |
|---|---|
| Identidade, preferências, estilo | `02 Context/me.md` |
| Objetivos, estratégia | `02 Context/estrategia.md` |
| Tom de voz, marca pessoal | `02 Context/marca.md` |
| Projeto ativo | `03 Projects/{nome}/README.md` |
| Recurso reutilizável | `04 Resources/` |
| Captura rápida | `00 Inbox/` |
| Sessão do dia | `01 Daily/YYYY-MM-DD.md` |

---

## Regras

- Leia `02 Context/me.md` sempre na primeira mensagem da sessão
- Use wikilinks `[[Nome da Nota]]` para toda referência interna — nunca links markdown
- Todo arquivo criado recebe YAML frontmatter: `type`, `date`, `status`, `tags`
- Nunca peça permissão para salvar — salve e informe onde
- Prefira editar notas existentes a criar novas
- Ao capturar algo importante (decisão, projeto, insight): route imediatamente para a pasta certa

---

## Prompts Disponíveis

Os 10 prompts em `prompts/` cobrem os casos de uso mais comuns:

| Prompt | Quando usar |
|---|---|
| `01-revisao-diaria.md` | Início ou fim do dia |
| `02-notas-reuniao.md` | Após qualquer reunião |
| `03-brief-conteudo.md` | Antes de criar conteúdo |
| `04-rascunho-email.md` | Para escrever emails |
| `05-plano-projeto.md` | Ao iniciar um projeto |
| `06-pesquisa-concorrentes.md` | Análise de mercado |
| `07-post-linkedin.md` | Posts no LinkedIn |
| `08-revisao-semanal.md` | Revisão da semana |
| `09-registro-decisao.md` | Documentar decisões |
| `10-despejo-ideias.md` | Brainstorm livre |

---

## Comandos

- `/setup` — Personaliza o vault para você: 6 perguntas + busca de contexto online + preenche `me.md` com dados reais

---

## Quer o sistema completo?

Este kit é o ponto de partida. Para a estrutura avançada com automações, múltiplos agentes e skill pack completo, acesse: https://matheusvizotto.com/pt-br/produtos/obsidian

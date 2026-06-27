---
type: map
status: active
date: 2026-05-26
tags: [aios, rules, obsidian, portable]
---

## Operating Rules

Como a IA opera neste vault. Portátil — vale em qualquer ferramenta que leia este arquivo (Claude Code, Cursor, Gemini CLI).

---

### Comportamento Central

1. Ler `knowledge/index.md` e `02 Context/me.md` (ou `operator.md` + `organization.md` em modo empresa) no início da sessão. Ler a última nota em `01 Daily/`. Não anuncie isso — apenas absorva e responda como se já estivesse na conversa.
2. Quando trabalho relevante foi feito, atualizar `01 Daily/YYYY-MM-DD.md`. Só quando há algo digno de registro — não em toda mensagem.
3. **Nunca pedir permissão pra salvar.** Auto-save informação relevante no arquivo certo do vault e reporta o que foi salvo.
4. Quando o usuário corrige a IA, salve a correção como regra permanente no `02 Context/me.md` imediatamente. Não pergunte — salve e confirme.
5. **Buscar antes de perguntar** — nunca peça informação que pode ser encontrada lendo arquivos do vault. Verifique o arquivo relevante primeiro.
6. Quando o usuário sinaliza confusão ("não entendi"), explique primeiro. Nunca trate confusão como aprovação pra prosseguir.

---

### Regras de Escrita no Vault

7. Use `[[wikilinks]]` pra TODA referência de projeto, pessoa, ou nota em qualquer arquivo do vault. Isso constrói o grafo.
8. Nunca use `[markdown](links)` pra notas internas do vault.
9. Nunca coloque um `# Title` heading que duplica o nome do arquivo. O Obsidian já mostra o nome.
10. Use frontmatter YAML em toda nota: `type`, `date`, `status`, `tags`, `projeto` (quando aplicável).
11. Cada nota deve ser standalone e componível — como uma peça de Lego.

---

### Roteamento de Informação

12. Quando informação aparece, route imediatamente pro arquivo certo (ver `AIOS/knowledge-routing.md`).
13. Não acumule tudo em `01 Daily/` — daily é registro de sessão, não destino final de conhecimento permanente.
14. Decisões com raciocínio → `03 Intelligence/decisions/`
15. Reuniões → `03 Intelligence/meetings/{tipo}/`
16. Insights de concorrentes → `03 Intelligence/competitors/{nome}.md`
17. Insights de mercado → `03 Intelligence/market/{topico}.md`

---

### Pesquisa e Tools

18. Use `grep` ou Obsidian search pra escanear arquivos — não leia arquivos inteiros quando estiver escaneando vários.
19. Use frontmatter pra filtrar (ex: `type: meeting AND date > 2026-05-01`).
20. Quando extrair conteúdo da web, prefira buscar com WebFetch ou yt-dlp ao invés de copy-paste manual.
21. Respeite `.claudeignore` se existir — nunca leia arquivos listados lá.

---

### Idioma

22. Tudo no vault em PT-BR a menos que o usuário indique diferente.
23. Frontmatter keys e paths permanecem em inglês (são técnicos).
24. Comandos (`/setup`, `/escrever`, etc.) detectam idioma da mensagem invocadora e adaptam saída.

---

### Tom

25. Direto, prático, sem floreio.
26. Sem "espero que esteja bem", "imagine", "no mundo de hoje", "vamos lá".
27. Use a voz do `02 Context/me.md` ou `02 Context/brand.md` quando escrevendo conteúdo.
28. Não use travessões em sentenças. Use vírgulas, pontos, ou reformule.

---

### Anti-padrões

NÃO faça:
- Perguntar "devo salvar isso?" — apenas salve
- Escrever nomes de projetos/pessoas como texto puro — SEMPRE `[[wikilinks]]`
- Usar `[markdown](links)` pra notas internas — sempre wikilinks
- Colocar `# Title` heading duplicando o nome do arquivo
- Criar notas órfãs — sempre linkar de pelo menos 1 nota existente
- Ler arquivos inteiros quando escaneando muitos — use `grep`
- Atualizar daily em chat casual — só quando há algo digno
- Criar tarefas como texto puro em notas — use callout `> [!todo]` pra serem queryable
- Despejar tudo no daily, route pro arquivo certo conforme o tipo de conteúdo

---

## Conectado a

[[Home]] · [[index]] · [[Vault-Map]] · [[knowledge-routing]] · [[project-map]]

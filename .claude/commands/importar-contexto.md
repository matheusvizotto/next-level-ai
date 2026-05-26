---
description: Importa contexto de outra IA (ChatGPT, Claude, Gemini) — gera prompt pra você colar lá, você cola a resposta de volta, e o vault é atualizado com profundidade real
---

# Importar Contexto — De outra IA pro seu vault

Use quando quiser atualizar seu vault com contexto que outra IA já tem sobre você. Funciona depois do `/setup` também — quanto mais contexto, melhor.

---

## Idioma / Language

Detecte o idioma da mensagem que invocou esse comando e use em todas as perguntas e mensagens.

PT-BR padrão. Inglês ou espanhol se o usuário escreveu nessa língua.

---

## Fase 1 — Escolher a IA de origem

Pergunta via AskUserQuestion:

- Pergunta: "De qual IA você quer importar contexto?"
- Header: `IA de origem`
- Opções:
  - `ChatGPT` — "Tem memória ativa entre conversas se você ligou."
  - `Claude (claude.ai)` — "Sem memória persistente — usa contexto desta conversa lá."
  - `Gemini` — "Pode buscar email e drive se for Workspace."
  - `Perplexity` — "Tem 'spaces' com contexto persistente."
  - `Outra IA` — "Prompt genérico que funciona em qualquer uma."

Guarde a escolha.

---

## Fase 2 — Gerar o prompt

Imprima o prompt apropriado num bloco de código markdown bem destacado. Antes do bloco, escreva:

> "Copia o prompt abaixo, cola na sua conversa com {{IA escolhida}}, e espera ela responder. Quando tiver a resposta completa, cola aqui que eu processo."

### Prompt — ChatGPT

```
Vou configurar um sistema de IA pessoal em outra ferramenta. Por favor, me devolva tudo que você sabe sobre mim, baseado nas nossas conversas anteriores e na sua memória. Organize em markdown, nesta estrutura exata:

## 1. Identidade
Nome, idade (se sabe), localização, contexto pessoal relevante.

## 2. Profissão
Cargo atual, empresa, setor, há quanto tempo, principais responsabilidades, clientes ou stakeholders.

## 3. Objetivos
Curto prazo (90 dias), médio (1 ano), longo (3-5 anos). Se não souber algum prazo, fale "sem dados".

## 4. Como trabalho
Rotina, ferramentas que uso (Notion, Linear, Slack, etc.), estilo, preferências, horários produtivos.

## 5. Minha voz
Como escrevo, palavras que uso, palavras que evito, tom (formal/casual/técnico), referências de estilo.

## 6. Audiência
Quem eu atendo profissionalmente, quem é meu público se eu crio conteúdo, perfil dessas pessoas.

## 7. Canais
Onde publico ou me comunico (LinkedIn, Instagram, YouTube, newsletter, blog, etc.). Frequência e foco de cada canal.

## 8. Desafios atuais
O que está me preocupando, onde estou travado, principais dores ou bloqueios.

## 9. Histórico relevante
Decisões importantes que tomei, projetos que importam, aprendizados marcantes.

## 10. Rede
Pessoas importantes na minha vida profissional (mentores, parceiros, colaboradores frequentes).

## 11. Recursos
Livros, criadores, frameworks, ferramentas que sigo ou uso de referência.

Regras:
- Se você não tem informação sobre algum item, escreva "sem dados" — NÃO invente.
- Seja conciso. Bullet points, não parágrafos longos.
- Inclua datas quando souber.
- Devolve só o markdown, sem comentários extras antes ou depois.
```

### Prompt — Claude (claude.ai)

```
Vou configurar um sistema de IA pessoal em outra ferramenta. Baseado em tudo que você sabe sobre mim NESTA conversa (e qualquer contexto que eu colei antes), me devolva um resumo completo em markdown, na estrutura abaixo:

## 1. Identidade
Nome, idade (se sabe), localização, contexto pessoal relevante.

## 2. Profissão
Cargo atual, empresa, setor, há quanto tempo, principais responsabilidades, clientes ou stakeholders.

## 3. Objetivos
Curto prazo (90 dias), médio (1 ano), longo (3-5 anos). Se não souber algum prazo, fale "sem dados".

## 4. Como trabalho
Rotina, ferramentas que uso (Notion, Linear, Slack, etc.), estilo, preferências, horários produtivos.

## 5. Minha voz
Como escrevo, palavras que uso, palavras que evito, tom (formal/casual/técnico), referências de estilo.

## 6. Audiência
Quem eu atendo profissionalmente, quem é meu público se eu crio conteúdo, perfil dessas pessoas.

## 7. Canais
Onde publico ou me comunico (LinkedIn, Instagram, YouTube, newsletter, blog, etc.). Frequência e foco de cada canal.

## 8. Desafios atuais
O que está me preocupando, onde estou travado, principais dores ou bloqueios.

## 9. Histórico relevante
Decisões importantes que tomei, projetos que importam, aprendizados marcantes.

## 10. Rede
Pessoas importantes na minha vida profissional (mentores, parceiros, colaboradores frequentes).

## 11. Recursos
Livros, criadores, frameworks, ferramentas que sigo ou uso de referência.

Regras:
- Se eu não compartilhei informação sobre algum item nesta conversa, escreva "sem dados".
- Não invente. Não chute. Só o que está explícito no nosso histórico aqui.
- Seja conciso. Bullets, não parágrafos.
- Devolve só o markdown.
```

### Prompt — Gemini

Use o prompt do ChatGPT acima, mais este parágrafo no final:

```
Se você usa o Gemini integrado ao Google Workspace, pode também buscar contexto dos meus emails, docs e drive recentes pra enriquecer a resposta. Se fizer isso, marque claramente quais informações vieram de onde (ex: "[do Drive: Plano Q1 2026]").
```

### Prompt — Perplexity ou outra IA

Use o prompt do ChatGPT sem modificações.

---

## Fase 3 — Aguardar resposta

Diga ao usuário:
> "Esperando você colar a resposta aqui. Pode ser tudo de uma vez."

Aguarde a próxima mensagem do usuário. Quando ele colar:
- Identifique cada bloco numerado (`## 1. Identidade`, `## 2. Profissão`, etc.)
- Extraia os dados de cada bloco
- Ignore "sem dados" — não tente preencher esses campos

---

## Fase 4 — Atualizar o vault

Trabalhe em silêncio. Não narre cada arquivo.

### 4.1 — `02 Context/me.md`

Leia o arquivo atual. Se existir:
- Se tem placeholders (`{{...}}`): substitua pelos dados extraídos
- Se já tem conteúdo real: **adicione** os dados novos, não sobrescreva (combine)
- Em caso de conflito, mantenha o que já está no arquivo (mais autoritativo) e adicione o resto como complemento

Se `me.md` não existir, crie usando o template padrão e preencha com os dados.

Mapeie os blocos da IA pras seções do me.md:
- Bloco 1 (Identidade) → seção "Identidade"
- Bloco 2 (Profissão) → seção "Identidade" (campo profissional) + "Contexto Profissional"
- Bloco 3 (Objetivos) → seção "Objetivos Atuais"
- Bloco 4 (Como trabalho) → seção "Como Trabalho"
- Bloco 5 (Voz) → seção "Tom de Voz"
- Bloco 6 (Audiência) → seção "Audiência"
- Bloco 7 (Canais) → seção "Canais"
- Bloco 8 (Desafios) → seção "Contexto Profissional" (campo desafio)

### 4.2 — Arquivos derivados

**Bloco 3 (Objetivos) substancial → cria/atualiza `02 Context/estrategia.md`:**

```markdown
---
type: reference
status: active
date: YYYY-MM-DD
tags: [estrategia, objetivos]
---

# Estratégia

## Meta de 90 dias
{{do bloco 3}}

## Meta de 1 ano
{{do bloco 3}}

## Meta de 3-5 anos
{{do bloco 3}}
```

**Blocos 5+6+7 (voz, audiência, canais) substanciais → cria/atualiza `02 Context/marca.md`:**

```markdown
---
type: reference
status: active
date: YYYY-MM-DD
tags: [marca, voz]
---

# Marca e Voz

## Audiência
{{bloco 6}}

## Canais
{{bloco 7}}

## Voz e Tom
{{bloco 5}}
```

**Bloco 11 (Recursos) com livros, frameworks, ferramentas → salva em `04 Resources/referencias-pessoais.md`:**

```markdown
---
type: reference
status: active
date: YYYY-MM-DD
tags: [referencias, recursos]
---

# Referências e Recursos

{{conteúdo do bloco 11 organizado por categoria: livros, criadores, frameworks, ferramentas}}
```

### 4.3 — Daily note

Append no daily de hoje (`01 Daily/YYYY-MM-DD.md`) ou crie se não existir:

```markdown
## Import de contexto — {{IA usada}}

- **Fonte:** {{ChatGPT / Claude / Gemini / etc.}}
- **Atualizado:** {{lista arquivos atualizados ou criados}}
- **Próximos passos:** revisar `me.md` e ajustar se algo da IA não bate com a realidade.
```

---

## Fase 5 — Confirmação

Mensagem curta:

> "Contexto importado da {{IA usada}}. Atualizei:
> - `02 Context/me.md`
> - {{liste outros arquivos criados ou atualizados}}
>
> Recomendo abrir o `me.md` e revisar — IAs erram em alguns detalhes, especialmente em datas e nomes.
>
> Pra escrever com a voz nova: `/escrever`. Pra brief de landing: `/landing-page`."

---

## Regras

- Nunca sobrescreva dados reais do `me.md` com dados da IA — adicione ou complemente.
- Se a IA respondeu "sem dados" pra um bloco, deixe a seção como está no template (ou remova se vazia).
- Confirme datas — IAs costumam errar ano e prazo. Se algo soa estranho, marque com `{{verificar}}` na nota do daily.
- Não invente. Se a IA não disse, não preencha.
- Use as palavras exatas do usuário (vindas da IA) quando possível — não parafraseie tom de voz.

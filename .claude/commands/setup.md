---
description: Configura o AI OS para você — pergunta sobre agente, importa contexto de outra IA, 8 perguntas, busca contexto de links/arquivos e preenche o vault com dados reais
---

# Setup — Personalização do AI OS

Você vai configurar o vault em 6 fases. Execute em ordem. Não pule fases.

---

## Idioma / Language

Detecte o idioma da mensagem que invocou esse comando (a mensagem do usuário que disparou `/setup`) e use esse idioma em TODOS os textos visíveis: mensagem de boas-vindas, `question` e `header` do AskUserQuestion, cada `label` e `description` das opções, mensagens de status, e a confirmação final.

- Mensagem em português → PT-BR (padrão deste programa).
- Mensagem em inglês → traduza todas as perguntas, headers, labels e descriptions para inglês equivalente.
- Mensagem em espanhol → traduza para espanhol.
- Idioma ambíguo → PT-BR.

A audiência principal é Brasil, então PT-BR é o default. Mas se alguém rodar em outra língua, adapte por respeito. Conteúdo de arquivos (`02 Context/me.md`, frontmatter, `01 Daily/`, nomes de pasta) permanece como está no template — não traduza paths, chaves de frontmatter, nem nomes de arquivo.

Aceite respostas do usuário por intenção, não por string exata. Se ele responder em outro idioma do que a pergunta, continue na língua dele.

---

## Fase 1 — Boas-vindas

Antes de qualquer pergunta, envie esta mensagem curta:

> "Bem-vindo. Vou configurar seu AI OS em alguns passos rápidos:
> 1. Decidir se você quer um agente IA persistente
> 2. Importar contexto de outra IA que você já usa (opcional)
> 3. 8 perguntas curtas
> 4. Buscar mais contexto de um link ou arquivo (opcional)
>
> Pode responder 'pular' em qualquer pergunta. Vamos."

---

## Fase 2 — Agente IA

Faça uma pergunta via AskUserQuestion:

- Pergunta: "Quer um agente IA persistente neste vault? Ele aprende seu contexto, salva notas automaticamente, gerencia sessões e roda revisões diárias/semanais."
- Header: `Agente IA`
- Opções:
  - `Sim — agente completo (Recomendado)` — "Configura o agente completo com personalização profunda, hooks e automações."
  - `Não — só estrutura de pastas` — "Cria a estrutura de pastas sem agente persistente."

Guarde a resposta como `agente: sim | nao`.

**Se `agente: nao`:** pule direto pra Fase 6 (Construção). Não faça as Fases 3, 4 e 5. Crie só a estrutura base e o `me.md` em branco. Avise no final que o usuário pode rodar `/setup` de novo a qualquer momento pra adicionar o agente.

**Se `agente: sim`:** continue pra Fase 3.

---

## Fase 3 — Importar contexto de outra IA

Faça uma pergunta via AskUserQuestion:

- Pergunta: "Você já usa outra IA hoje (ChatGPT, Claude, Gemini, Perplexity)? Posso te dar um prompt pra ela mandar tudo que sabe sobre você — você cola a resposta de volta aqui e eu preencho seu vault com profundidade real, em vez de só placeholders."
- Header: `Contexto IA`
- Opções:
  - `Sim — uso ChatGPT` — "Gera prompt otimizado pra memória do ChatGPT."
  - `Sim — uso Claude` — "Gera prompt otimizado pro Claude (claude.ai)."
  - `Sim — uso Gemini` — "Gera prompt otimizado pro Gemini."
  - `Sim — outra IA` — "Gera prompt genérico que funciona em qualquer IA."
  - `Não — pular este passo` — "Continua com as 8 perguntas."

**Se sim:** imprima o prompt apropriado (veja templates abaixo) num bloco de código markdown. Diga ao usuário pra:
1. Copiar o prompt
2. Colar na conversa com a IA escolhida
3. Esperar a resposta
4. Colar a resposta inteira de volta aqui

Aguarde a resposta do usuário. Quando ele colar, parseie em silêncio (não comente) e guarde os dados extraídos numa variável interna `contexto_ia` que vai ser usada na Fase 6. Cada bloco do prompt vira uma seção: identidade, profissão, objetivos, voz, audiência, canais, desafios, histórico, rede, recursos.

Depois do parse, faça as 8 perguntas da Fase 4 mesmo assim — algumas IAs não têm tudo, e perguntas diretas confirmam dados conflitantes.

**Se não:** vá direto pra Fase 4.

### Templates de prompt por IA

**Para ChatGPT (ChatGPT lembra de conversas via memória se ativada):**

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

**Para Claude (claude.ai — não tem memória persistente entre conversas a menos que o usuário tenha colado contexto):**

```
Vou configurar um sistema de IA pessoal em outra ferramenta. Baseado em tudo que você sabe sobre mim NESTA conversa (e qualquer contexto que eu colei antes), me devolva um resumo completo em markdown, na estrutura abaixo:

[mesma estrutura 1-11 do prompt do ChatGPT acima]

Regras:
- Se eu não compartilhei informação sobre algum item nesta conversa, escreva "sem dados".
- Não invente. Não chute. Só o que está explícito no nosso histórico aqui.
- Seja conciso. Bullets, não parágrafos.
- Devolve só o markdown.
```

**Para Gemini:**

Use o mesmo prompt do ChatGPT, mas adicione no final:

```
Se você usa o Gemini integrado ao Google Workspace, pode também buscar contexto dos meus emails, docs e drive recentes pra enriquecer a resposta. Se fizer isso, marque claramente quais informações vieram de onde.
```

**Para outras IAs (Perplexity, Llama, etc.):**

Use o prompt do ChatGPT sem ajustes.

### Parse da resposta colada

Quando o usuário colar a resposta da IA, identifique cada bloco (`## 1. Identidade`, `## 2. Profissão`, etc.) e extraia os dados estruturados. Não comente publicamente, só processe.

Use esses dados na Fase 6 pra pré-preencher o `me.md` antes de aplicar as respostas das 8 perguntas. Se uma pergunta da Fase 4 conflitar com o que veio da IA, dê prioridade pra resposta direta do usuário (mais recente, mais explícita).

---

## Fase 4 — 8 perguntas (uma por vez via AskUserQuestion)

Faça uma pergunta por vez. Não agrupe. Não comente entre as perguntas — vá direto pra próxima.

**P1 — Você**
- Pergunta: "Qual é o seu nome completo e onde você mora?"
- Header: `Identidade`
- Opções: `Só o nome` / `Nome + cidade` / `Nome + cidade + país` / `Pular`

**P2 — O que você faz**
- Pergunta: "Em uma frase: o que você faz profissionalmente, para quem, e que resultado gera?"
- Header: `Profissão`
- Opções: `Sou funcionário CLT` / `Sou freelancer/consultor` / `Tenho meu próprio negócio` / `Pular`

**P3 — Objetivo agora**
- Pergunta: "Qual é a sua principal meta para os próximos 90 dias?"
- Header: `Meta`
- Opções: `Crescer na carreira` / `Lançar algo novo` / `Aumentar renda` / `Pular`

**P4 — Ferramentas**
- Pergunta: "Quais ferramentas você usa no dia a dia? (ex: Notion, Linear, Slack, Google Workspace...)"
- Header: `Stack`
- Opções: `Suite Google` / `Suite Microsoft` / `Notion + Slack` / `Pular`

**P5 — Tom de voz**
- Pergunta: "Como você se descreve quando escreve? Escolha o que mais combina."
- Header: `Voz`
- Opções: `Direto e objetivo` / `Analítico e detalhado` / `Informal e descontraído` / `Pular`

**P6 — Audiência**
- Pergunta: "Quem é o público que você atende ou para quem você cria conteúdo?"
- Header: `Audiência`
- Opções: `Profissionais B2B` / `Consumidor final B2C` / `Outros criadores` / `Empresas / times` / `Pular`

**P7 — Canais**
- Pergunta: "Onde você publica ou se comunica profissionalmente? (pode ser mais de um — descreve o foco principal)"
- Header: `Canais`
- Opções: `LinkedIn` / `Instagram / TikTok` / `YouTube` / `Newsletter / Blog` / `Não publico ainda` / `Pular`

**P8 — Principal dor**
- Pergunta: "O que mais consome seu tempo ou atenção hoje que você gostaria de automatizar ou simplificar?"
- Header: `Dor`
- Opções: `Reuniões e follow-ups` / `Criação de conteúdo` / `Relatórios e análises` / `Vendas e prospecção` / `Pular`

---

## Fase 5 — Drop de contexto adicional

Faça uma pergunta via AskUserQuestion:

- Pergunta: "Última coisa. Posso buscar mais contexto de algum link ou arquivo? LinkedIn, site, Notion público, PDF da empresa. Quanto mais contexto, mais útil fica o vault."
- Header: `Contexto extra`
- Opções:
  - `Sim — vou colar um link` — "LinkedIn, site, Notion, Google Docs..."
  - `Sim — tenho um arquivo` — "PDF, Word, MD..."
  - `Não — já é suficiente` — "Configurar com o que já temos."
  - `Pular`

**Se link:** busque com WebFetch. Extraia dados relevantes e combine com `contexto_ia` (Fase 3) + respostas (Fase 4).
**Se arquivo:** leia com Read. Mesmo tratamento.
**Se não:** prossiga.

---

## Fase 6 — Construção (trabalhe em silêncio, sem narrar cada passo)

Combine todas as fontes nesta ordem de prioridade (a mais recente sobrescreve a anterior em caso de conflito):
1. `contexto_ia` da Fase 3 (base ampla)
2. Respostas das 8 perguntas da Fase 4 (correção explícita)
3. Link/arquivo da Fase 5 (enriquecimento)

### 6.1 — Preencher `02 Context/me.md`

Leia o template atual. Substitua cada `{{PLACEHOLDER}}` com dados combinados.

Regras:
- Se não tiver dado pra uma seção: REMOVA a seção inteira (nunca deixe placeholder visível).
- Use as palavras do próprio usuário quando ele escreveu em "Outro" ou colou da IA.
- Frontmatter: substitua `{{DATA DE HOJE}}` pela data atual (formato YYYY-MM-DD).
- As novas seções `Audiência` (P6) e `Canais` (P7) ficam preenchidas com base nas respostas + contexto IA.

### 6.2 — Criar arquivos opcionais se houver dado

**Se o usuário mencionou marca pessoal, voz forte, ou criação de conteúdo:**
Crie `02 Context/marca.md`:

```markdown
---
type: reference
status: active
date: YYYY-MM-DD
tags: [marca, voz, contexto]
---

# Marca e Voz

## Audiência
{{quem o usuário atende ou pra quem ele cria}}

## Canais
{{onde publica + frequência se souber}}

## Voz e Tom
{{como escreve, palavras-chave, referências}}

## O que evitar
{{palavras, formatos ou tons que o usuário rejeita}}
```

**Se mencionou objetivos claros ou meta de 90 dias:**
Crie `02 Context/estrategia.md`:

```markdown
---
type: reference
status: active
date: YYYY-MM-DD
tags: [estrategia, objetivos]
---

# Estratégia

## Meta de 90 dias
{{do P3 ou contexto_ia}}

## Meta de 1 ano
{{do contexto_ia se houver, senão omita}}

## Meta de 3-5 anos
{{do contexto_ia se houver, senão omita}}

## Próximos passos concretos
{{1-3 ações derivadas das metas}}
```

**Se mencionou projetos ativos:**
Pra cada projeto mencionado, crie `03 Projects/{nome-do-projeto}/README.md` com overview, status e próximos passos.

### 6.3 — Criar nota do Dia 1 em `01 Daily/`

Crie `01 Daily/YYYY-MM-DD.md` com a data de hoje:

```markdown
---
type: daily-note
date: YYYY-MM-DD
status: active
tags: [daily, setup]
---

## Sessão de Setup

- **Foco:** Configuração inicial do AI OS
- **Concluído:** Vault personalizado com {{liste fontes usadas: 8 perguntas, contexto IA, link/arquivo}}
- **Arquivos criados:** {{liste cada arquivo criado em 6.1 e 6.2}}
- **Projetos ativos:** {{liste projetos mencionados, ou "nenhum ainda"}}
- **Próximos passos:** {{1-2 ações concretas baseadas no objetivo principal}}
```

### 6.4 — Confirmar para o usuário

Envie uma mensagem curta, sem floreios:

> "Pronto. Configurei:
> - `02 Context/me.md` — preenchido com seus dados
> - {{liste outros arquivos criados, se houver}}
> - `01 Daily/[data].md` — nota do dia
>
> Próximo passo: {{1 ação concreta baseada no objetivo principal do usuário}}.
>
> Quando quiser, rode `/escrever` pra criar um post, `/landing-page` pra brief de página, ou `/importar-contexto` pra atualizar com outra IA."

Não liste cada campo alterado. Não parabenize. Direto ao ponto.

---

## Regras gerais

- Uma pergunta por vez — nunca agrupe via AskUserQuestion.
- Não comente entre perguntas — vá direto pra próxima.
- Trabalhe em silêncio na Fase 6 — uma confirmação só no final.
- Nunca deixe `{{PLACEHOLDER}}` visível no arquivo final — sempre preencha ou remova a seção.
- Se o usuário pular tudo: cria a estrutura mínima e avisa que ele pode rodar `/setup` de novo depois.
- Conteúdo dos arquivos sempre em PT-BR (ou no idioma detectado pela seção Idioma). Paths e frontmatter keys ficam intactos.

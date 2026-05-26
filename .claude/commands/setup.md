---
description: Configura o AI OS para você — escolhe modo (solo ou empresa), pergunta sobre agente, importa contexto de outra IA, faz 8 perguntas, busca contexto de links/arquivos e preenche o vault com dados reais
---

# Setup — Personalização do AI OS

Você vai configurar o vault em 7 fases. Execute em ordem. Não pule fases.

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
> 1. Saber se você é solo ou empresa (muda a estrutura)
> 2. Decidir se você quer um agente IA persistente
> 3. Importar contexto de outra IA (opcional)
> 4. 8 perguntas curtas
> 5. Buscar mais contexto de um link ou arquivo (opcional)
>
> Pode responder 'pular' em qualquer pergunta. Vamos."

---

## Fase 2 — Modo: Solo ou Empresa

**Esta é a primeira pergunta real e a mais importante** — ela define toda a estrutura do vault.

Pergunta via AskUserQuestion:

- Pergunta: "Você é uma pessoa individual ou está montando isso para uma empresa / time?"
- Header: `Modo`
- Opções:
  - `Solo — profissional individual (Recomendado)` — "Mistura trabalho e pessoal. Ideal pra solopreneurs, freelancers, consultores, criadores, profissionais CLT."
  - `Empresa — time / organização` — "Estrutura organizacional com departamentos, processos, stakeholders. Ideal pra times e empresas."

Guarde a resposta como `modo: solo | empresa`.

Aceite qualquer sinal claro: "solo", "individual", "freelancer", "profissional" → `solo`. "empresa", "time", "negócio", "organização", "agência" → `empresa`. Ambíguo ou pulou → `solo` (padrão).

**Este valor afeta todas as fases seguintes:**
- Fase 4 (import de outra IA): prompt customizado pra perfil pessoal vs empresarial
- Fase 5 (8 perguntas): perguntas reformuladas pra contexto pessoal vs empresarial
- Fase 7 (construção): folders, templates e arquivos diferentes pra cada modo

---

## Fase 3 — Agente IA

Pergunta via AskUserQuestion:

- Pergunta: "Quer um agente IA persistente neste vault? Ele aprende seu contexto, salva notas automaticamente, gerencia sessões e roda revisões diárias/semanais."
- Header: `Agente IA`
- Opções:
  - `Sim — agente completo (Recomendado)` — "Configura o agente completo com personalização profunda, hooks e automações."
  - `Não — só estrutura de pastas` — "Cria a estrutura de pastas sem agente persistente."

Guarde a resposta como `agente: sim | nao`.

**Se `agente: nao`:** pule direto pra Fase 7 (Construção). Não faça as Fases 4, 5 e 6. Crie só a estrutura base e o `me.md` (modo solo) ou `operator.md` + `organization.md` (modo empresa) em branco. Avise no final que o usuário pode rodar `/setup` de novo a qualquer momento pra adicionar o agente.

**Se `agente: sim`:** continue pra Fase 4.

---

## Fase 4 — Importar contexto de outra IA

> ⚠️ **ANTES DE COMEÇAR ESTA FASE:** confirme internamente qual `modo` foi capturado na Fase 2 (`solo` ou `empresa`). Os templates de prompt abaixo têm duas versões — use a que bate com o modo. Não misture.

Pergunta via AskUserQuestion:

- Pergunta: "Você já usa outra IA hoje (ChatGPT, Claude, Gemini, Perplexity)? Posso te dar um prompt pra ela mandar tudo que sabe sobre {{você OU sua empresa, conforme modo}} — você cola a resposta de volta aqui e eu preencho seu vault com profundidade real, em vez de só placeholders."
- Header: `Contexto IA`
- Opções:
  - `Sim — uso ChatGPT` — "Gera prompt otimizado pra memória do ChatGPT."
  - `Sim — uso Claude` — "Gera prompt otimizado pro Claude (claude.ai)."
  - `Sim — uso Gemini` — "Gera prompt otimizado pro Gemini."
  - `Sim — outra IA` — "Gera prompt genérico que funciona em qualquer IA."
  - `Não — pular este passo` — "Continua com as 8 perguntas."

**Se sim:** imprima o prompt apropriado (veja templates abaixo) num bloco de código markdown. O prompt MUDA baseado no `modo`. Diga ao usuário pra:
1. Copiar o prompt
2. Colar na conversa com a IA escolhida
3. Esperar a resposta
4. Colar a resposta inteira de volta aqui

Aguarde a resposta do usuário. Quando ele colar, parseie em silêncio (não comente) e guarde os dados extraídos numa variável interna `contexto_ia` que vai ser usada na Fase 7.

Depois do parse, faça as 8 perguntas da Fase 5 mesmo assim — algumas IAs não têm tudo, e perguntas diretas confirmam dados conflitantes.

**Se não:** vá direto pra Fase 5.

### Templates de prompt — Modo SOLO

**Para ChatGPT (modo solo):**

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

**Para Claude (modo solo):**

Mesmo prompt acima, com regra adicional:
```
Adicional: Baseado em tudo que você sabe sobre mim NESTA conversa (e qualquer contexto que eu colei antes). Se eu não compartilhei informação sobre algum item nesta conversa, escreva "sem dados".
```

**Para Gemini (modo solo):**

Mesmo prompt do ChatGPT, com adição:
```
Se você usa o Gemini integrado ao Google Workspace, pode também buscar contexto dos meus emails, docs e drive recentes pra enriquecer a resposta. Se fizer isso, marque claramente quais informações vieram de onde.
```

### Templates de prompt — Modo EMPRESA

**Para ChatGPT (modo empresa):**

```
Vou configurar um sistema de IA pra minha empresa em outra ferramenta. Por favor, me devolva tudo que você sabe sobre a empresa e sobre mim como operador, baseado nas nossas conversas anteriores e na sua memória. Organize em markdown, nesta estrutura exata:

## 1. Operador (eu)
Meu nome, cargo na empresa, há quanto tempo, principais responsabilidades, estilo de liderança.

## 2. A empresa
Nome, setor, modelo de negócio, ano de fundação se souber, sede / cidade, faturamento ou porte se compartilhado.

## 3. Produto / serviço
O que a empresa vende, formato (SaaS, serviço, produto físico, agência), proposta de valor.

## 4. Time
Tamanho do time, principais cargos / departamentos, estrutura (remoto, híbrido, presencial).

## 5. Objetivos da empresa
Curto prazo (90 dias), médio (1 ano), longo (3-5 anos). Se não souber algum prazo, fale "sem dados".

## 6. Como a empresa trabalha
Stack de ferramentas (CRM, comunicação, projeto, etc.), processos principais, rituais (standups, all-hands, etc.).

## 7. Voz da marca
Como a empresa se comunica, tom (formal/casual/técnico), palavras-chave, palavras a evitar, referências.

## 8. Cliente ideal (ICP)
Quem a empresa atende, perfil dessas pessoas / empresas, dor que resolve, ticket médio.

## 9. Canais de mercado
Onde a empresa se comunica (LinkedIn corporativo, blog, eventos, ads, etc.). Frequência e foco.

## 10. Desafios atuais do negócio
Onde a empresa está travada, principais bloqueios, decisões em aberto.

## 11. Histórico relevante
Marcos importantes, decisões críticas, pivots, aprendizados.

## 12. Stakeholders / parceiros
Investidores, advisors, parceiros estratégicos, fornecedores críticos.

## 13. Recursos e referências
Frameworks que a empresa usa, livros / autores referência, concorrentes que monitora.

Regras:
- Se você não tem informação sobre algum item, escreva "sem dados" — NÃO invente.
- Seja conciso. Bullet points, não parágrafos longos.
- Inclua datas quando souber.
- Devolve só o markdown, sem comentários extras antes ou depois.
```

**Para Claude (modo empresa):**

Mesmo prompt empresa acima, com nota: "Baseado em tudo que você sabe sobre a empresa NESTA conversa."

**Para Gemini (modo empresa):**

Mesmo prompt empresa, com adição:
```
Se você usa o Gemini integrado ao Google Workspace, pode também buscar contexto de docs internos, emails corporativos, e drive da empresa pra enriquecer. Marque a origem.
```

### Parse da resposta

Quando o usuário colar a resposta, identifique cada bloco (`## 1.`, `## 2.`, etc.) e extraia os dados estruturados. Não comente publicamente, só processe.

Use esses dados na Fase 7 pra pré-preencher os arquivos antes de aplicar as respostas das 8 perguntas. Se uma pergunta da Fase 5 conflitar com a IA, prioridade pra resposta direta do usuário.

---

## Fase 5 — 8 perguntas (uma por vez via AskUserQuestion)

> ⚠️ **ANTES DE COMEÇAR ESTA FASE:** confirme internamente qual `modo` foi capturado na Fase 2. Existem 2 versões completas das 8 perguntas — **Versão SOLO** ou **Versão EMPRESA**. Use só uma. NÃO faça 16 perguntas misturando as duas. Se o modo for `solo`, ignore completamente a seção "Versão modo EMPRESA". Se o modo for `empresa`, ignore completamente a seção "Versão modo SOLO".

Faça uma pergunta por vez. Não agrupe. Não comente entre as perguntas — vá direto pra próxima.

**As perguntas mudam dependendo do `modo`. Use a versão correta.**

### Versão modo SOLO

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

### Versão modo EMPRESA

**P1 — Empresa**
- Pergunta: "Nome da empresa e onde fica a sede principal?"
- Header: `Empresa`
- Opções: `Só o nome` / `Nome + cidade` / `Nome + cidade + país` / `Pular`

**P2 — O que a empresa faz**
- Pergunta: "Em uma frase: o que a empresa vende, para quem, e que resultado entrega?"
- Header: `Produto`
- Opções: `SaaS / produto digital` / `Serviço (agência, consultoria)` / `Produto físico` / `Educação / curso` / `Outro` / `Pular`

**P3 — Meta da empresa**
- Pergunta: "Qual é a principal meta da empresa para os próximos 90 dias?"
- Header: `Meta`
- Opções: `Crescer receita` / `Lançar produto novo` / `Expandir mercado` / `Aumentar eficiência` / `Pular`

**P4 — Stack da empresa**
- Pergunta: "Quais ferramentas o time usa no dia a dia? (CRM, projeto, comunicação)"
- Header: `Stack`
- Opções: `Suite Google + Slack` / `Suite Microsoft + Teams` / `Notion + Linear + Slack` / `HubSpot + Slack` / `Pular`

**P5 — Voz da marca**
- Pergunta: "Como a marca se comunica? Escolha o que mais combina."
- Header: `Voz da marca`
- Opções: `Direta e objetiva (B2B)` / `Técnica e detalhada (especialista)` / `Próxima e calorosa (B2C)` / `Premium / aspiracional` / `Pular`

**P6 — Cliente ideal (ICP)**
- Pergunta: "Quem é o cliente ideal da empresa? Em 1 frase: perfil + porte + setor."
- Header: `ICP`
- Opções: `Empresas B2B` / `Consumidor final B2C` / `Profissionais / freelancers` / `Outras agências / times` / `Pular`

**P7 — Canais da empresa**
- Pergunta: "Onde a empresa se comunica com mercado? Principal canal."
- Header: `Canais`
- Opções: `LinkedIn corporativo` / `Anúncios pagos (Google/Meta)` / `Blog / SEO` / `Eventos / parcerias` / `Pular`

**P8 — Maior dor do negócio**
- Pergunta: "Qual é o maior gargalo do negócio hoje?"
- Header: `Dor`
- Opções: `Geração de demanda` / `Conversão de vendas` / `Operação interna` / `Retenção de cliente` / `Pular`

---

## Fase 6 — Drop de contexto adicional

Pergunta via AskUserQuestion:

- Pergunta: "Última coisa. Posso buscar mais contexto de algum link ou arquivo? {{Se solo: 'LinkedIn, site, Notion público, PDF.' Se empresa: 'Site institucional, deck pra investidor, página About, doc de estratégia.'}}"
- Header: `Contexto extra`
- Opções:
  - `Sim — vou colar um link`
  - `Sim — tenho um arquivo`
  - `Não — já é suficiente`
  - `Pular`

**Se link:** busque com WebFetch. Extraia dados relevantes e combine com `contexto_ia` (Fase 4) + respostas (Fase 5).
**Se arquivo:** leia com Read.
**Se não:** prossiga.

---

## Fase 7 — Construção (trabalhe em silêncio)

> ⚠️ **ANTES DE COMEÇAR ESTA FASE:** confirme qual `modo` foi capturado na Fase 2. As seções 7.2, 7.3 e 7.4 abaixo têm caminhos separados pra `solo` vs `empresa` — execute SÓ o caminho do modo capturado. NÃO crie operator.md/organization.md/team.md se for solo. NÃO crie me.md se for empresa.

Combine todas as fontes nesta ordem de prioridade (a mais recente sobrescreve a anterior em caso de conflito):
1. `contexto_ia` da Fase 4 (base ampla)
2. Respostas das 8 perguntas da Fase 5 (correção explícita)
3. Link/arquivo da Fase 6 (enriquecimento)

### 7.1 — Folders base (sempre)

```bash
mkdir -p "00 Inbox" "01 Daily" "02 Context" "03 Projects" "04 Resources"
mkdir -p "03 Intelligence/meetings/team-standups"
mkdir -p "03 Intelligence/meetings/client-calls"
mkdir -p "03 Intelligence/meetings/one-on-ones"
mkdir -p "03 Intelligence/meetings/general"
mkdir -p "03 Intelligence/competitors"
mkdir -p "03 Intelligence/market"
mkdir -p "03 Intelligence/decisions"
mkdir -p "03 Intelligence/archive"
```

### 7.2 — Folders extras se `modo: empresa`

```bash
mkdir -p "03 Intelligence/meetings/board-reviews"
mkdir -p "03 Intelligence/meetings/all-hands"
mkdir -p "03 Intelligence/meetings/cross-team"
mkdir -p "03 Intelligence/processes"
mkdir -p "Departments"
mkdir -p "Teams"
mkdir -p "Onboarding"
```

### 7.3 — Arquivo principal de identidade

**Se `modo: solo`:** preencher o template existente `02 Context/me.md` substituindo cada `{{PLACEHOLDER}}` com dados combinados das fontes.

**Se `modo: empresa`:** criar **3 arquivos**:

**A) `02 Context/operator.md`** — você como operador

```markdown
---
type: identity
date: YYYY-MM-DD
status: active
tags: [identity, context, operator]
---

# {{Seu nome}}

> Você é o operador desta empresa. Este arquivo descreve quem você é como decisor.

## Identidade
- **Nome:** {{nome}}
- **Cargo:** {{cargo na empresa}}
- **Tempo no cargo:** {{do contexto_ia ou inferir}}
- **Localização:** {{cidade}}

## Estilo de liderança
{{do contexto_ia bloco 1, ou genérico se sem dados}}

## Como eu decido
{{como você toma decisões — gut, dados, comitê, etc.}}

## Reuniões que faço
- {{1:1 com diretos, all-hands, board, etc.}}

## Notas para a IA
- Sempre responda em português do Brasil
- Quando referir-se à empresa, use `[[organization]]`
- Quando referir-se ao time, use `[[team]]`
```

**B) `02 Context/organization.md`** — a empresa

```markdown
---
type: identity
date: YYYY-MM-DD
status: active
tags: [identity, context, organization]
---

# {{Nome da empresa}}

> Este arquivo descreve a empresa: produto, mercado, voz, ICP, canais.

## A empresa
- **Nome:** {{nome}}
- **Setor:** {{setor}}
- **Modelo:** {{SaaS, serviço, produto, etc.}}
- **Sede:** {{cidade}}
- **Porte:** {{do contexto_ia ou "sem dados"}}

## Produto / Serviço
{{do P2 + contexto_ia bloco 3}}

## Cliente ideal (ICP)
{{do P6 + contexto_ia bloco 8}}

## Proposta de valor
{{1 frase do que a empresa promete entregar}}

## Voz da marca
**Tom:** {{do P5}}

**Palavras-chave:** {{do contexto_ia bloco 7}}

**Palavras a evitar:** {{do contexto_ia bloco 7}}

## Canais
**Principal:** {{do P7}}

**Secundários:** {{do contexto_ia bloco 9}}

## Concorrentes principais
{{do contexto_ia bloco 13, ou "a definir"}}

## Stakeholders / parceiros
{{do contexto_ia bloco 12, ou seção vazia removida}}
```

**C) `02 Context/team.md`** — o time

```markdown
---
type: identity
date: YYYY-MM-DD
status: active
tags: [identity, context, team]
---

# Time — {{Nome da empresa}}

> Estrutura do time e principais pessoas.

## Tamanho
{{N pessoas, do contexto_ia bloco 4}}

## Estrutura
{{remoto / híbrido / presencial}}

## Departamentos
- {{lista do contexto_ia ou criar conforme o time cresce}}

## Pessoas-chave
{{lista de pessoas relevantes do contexto_ia, com cargo. Se sem dados, deixar vazio.}}

## Rituais
- {{standups, 1:1, all-hands, etc.}}
```

### 7.4 — Arquivos opcionais (se houver dado nas fontes)

**Modo SOLO**, criar se houver substância:
- `02 Context/marca.md` — se o usuário mencionou marca, voz forte, ou criação de conteúdo
- `02 Context/estrategia.md` — se mencionou objetivos claros ou meta de 90 dias

**Modo EMPRESA**, criar se houver substância:
- `02 Context/estrategia.md` — sempre criar pra empresa, com metas 90d/1ano/3-5anos
- `02 Context/processos.md` — se mencionou rituais ou processos no contexto_ia bloco 6

(Estruturas dos arquivos opcionais mesmas da versão anterior do setup — meta 90d, meta 1 ano, etc.)

### 7.5 — Projetos ativos (ambos os modos)

Se houver projetos mencionados:
- `03 Projects/{slug-do-projeto}/README.md` com overview + status + próximos passos.

### 7.6 — Daily note (ambos os modos)

Cria `01 Daily/YYYY-MM-DD.md`:

```markdown
---
type: daily-note
date: YYYY-MM-DD
status: active
tags: [daily, setup]
---

## Sessão de Setup

- **Modo:** {{solo / empresa}}
- **Foco:** Configuração inicial do AI OS
- **Concluído:** Vault personalizado com {{liste fontes: 8 perguntas, contexto_ia, link/arquivo}}
- **Arquivos criados:** {{liste todos os arquivos criados em 7.3 e 7.4}}
- **Projetos ativos:** {{liste projetos mencionados, ou "nenhum ainda"}}
- **Próximos passos:** {{1-2 ações concretas baseadas no objetivo principal}}
```

### 7.7 — Confirmação

Envie mensagem curta, sem floreio. Adapta ao modo:

**Modo SOLO:**
> "Pronto. Configurei seu vault em modo **solo**:
> - `02 Context/me.md` — você
> - {{liste outros arquivos criados}}
> - `01 Daily/[data].md` — nota do dia
>
> Próximo passo: {{1 ação concreta baseada no P3 ou contexto_ia}}.
>
> Quando quiser: `/escrever` (post), `/landing-page` (página), `/assistente` (dia a dia)."

**Modo EMPRESA:**
> "Pronto. Configurei seu vault em modo **empresa**:
> - `02 Context/operator.md` — você como operador
> - `02 Context/organization.md` — a empresa
> - `02 Context/team.md` — estrutura do time
> - {{liste outros arquivos criados}}
> - `Departments/`, `Teams/`, `Onboarding/` — pastas pra escalar
> - `01 Daily/[data].md` — nota do dia
>
> Próximo passo: {{1 ação concreta baseada no P3}}.
>
> Quando quiser: `/escrever` (copy), `/landing-page` (página), `/case-study` (cliente), `/ads-google` (campanha), `/assistente` (dia a dia)."

Não liste cada campo. Não parabenize. Direto ao ponto.

---

## Regras gerais

- Uma pergunta por vez — nunca agrupe via AskUserQuestion.
- Não comente entre perguntas — vá direto pra próxima.
- Trabalhe em silêncio na Fase 7 — uma confirmação só no final.
- Nunca deixe `{{PLACEHOLDER}}` visível no arquivo final — sempre preencha ou remova a seção.
- Se o usuário pular tudo: cria a estrutura mínima do modo escolhido e avisa que ele pode rodar `/setup` de novo depois.
- Conteúdo dos arquivos sempre em PT-BR (ou no idioma detectado pela seção Idioma). Paths e frontmatter keys ficam intactos.
- O `modo` é a primeira decisão — não pule. Tudo downstream depende dele.

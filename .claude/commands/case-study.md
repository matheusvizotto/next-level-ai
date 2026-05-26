---
description: Cria um case study completo de cliente — extrai narrativa de transcrição/notas, estrutura em formato apresentável, gera markdown pronto pra virar PDF ou slides
---

# Case Study — Apresentação de Resultado de Cliente

Você vai construir 1 case study completo: contexto, problema, abordagem, resultado, lições. Em formato que serve pra site, sales deck, post, ou PDF.

---

## Idioma / Language

Detecte o idioma e use em tudo. PT-BR padrão.

---

## Antes de começar

Leia `02 Context/me.md`:
- "Profissão" — entender o que você vende
- "Audiência" — pra quem é o case (potenciais clientes similares)

---

## Fase 1 — Material de partida

Pergunta via AskUserQuestion:

- Pergunta: "De onde vem o case?"
- Header: `Fonte`
- Opções:
  - `Transcrição de call com cliente` — "Cola o texto bruto."
  - `Notas que escrevi sobre o projeto` — "Cola as notas, eu organizo."
  - `Vou contar agora — você pergunta` — "Te entrevisto em texto, pergunta por pergunta."
  - `Já tenho um draft — vou colar` — "Você cola, eu reestruturo."

Aja conforme a escolha:
- Transcrição / Notas / Draft: peça pra colar o conteúdo, leia e siga pra Fase 2.
- Vou contar agora: vá pra Fase 1b (entrevista guiada).

### Fase 1b — Entrevista guiada (só se escolheu "Vou contar agora")

Faça 8 perguntas, uma por vez via AskUserQuestion:

**1. Cliente**
- Pergunta: "Quem é o cliente? Nome (ou anonimizado), setor, tamanho da empresa."

**2. Situação inicial**
- Pergunta: "Qual era a situação dele antes de você entrar? Onde ele estava travado?"

**3. Tentativas anteriores**
- Pergunta: "O que ele já tinha tentado antes? (importante pra mostrar contraste)"

**4. Por que escolheu você**
- Pergunta: "Por que ele escolheu você especificamente? O que decidiu a contratação?"

**5. Sua abordagem**
- Pergunta: "Como você trabalhou? Quais foram os passos / estratégia / método?"

**6. Resultado quantificado**
- Pergunta: "Qual foi o resultado em números? (receita, leads, tempo, eficiência, etc.) Período."

**7. Resultado qualitativo**
- Pergunta: "Como mudou o dia a dia ou a vida do cliente? (citação dele se tiver é ouro)"

**8. Lição extraída**
- Pergunta: "Uma lição desse projeto que você levou pra outros clientes."

---

## Fase 2 — Estruturar

Com o material em mãos, organize na estrutura clássica de case study:

```markdown
# {{Cliente}} — {{resultado em 1 frase quantificada}}

> {{Citação curta do cliente, 1-2 linhas, se houver}}

---

## Sobre o cliente

- **Setor:** {{indústria}}
- **Tamanho:** {{N funcionários / faturamento se relevante}}
- **Localização:** {{cidade ou país, se relevante}}
- **Foco:** {{produto / serviço que vendem}}

---

## O problema

{{2-3 parágrafos. Use as palavras do cliente sempre que possível. Mostre dor concreta, não genérica. Quantifique se possível ("levavam 4h por dia em X").}}

### Tentativas anteriores

{{1 parágrafo. O que tentaram antes e por que não funcionou. Mostra que o cliente não era ingênuo — tinha buscado solução.}}

---

## Por que escolheram a gente

{{1-2 parágrafos. Honesto. O que diferenciou. Pode ser referência, abordagem específica, ou momento certo.}}

---

## A abordagem

{{2-4 parágrafos OU lista numerada. Como você trabalhou. Específico — não "consultoria estratégica", mas "rodamos workshop de 3h pra mapear X, depois implementamos Y em sprints de 2 semanas".}}

### Principais decisões

- {{decisão 1 e por que}}
- {{decisão 2 e por que}}
- {{decisão 3 e por que}}

---

## O resultado

### Em números

| Métrica | Antes | Depois | Variação |
|---|---|---|---|
| {{ex: CAC}} | {{R$ 200}} | {{R$ 80}} | {{-60%}} |
| {{ex: Tempo de resposta}} | {{4h}} | {{15min}} | {{-94%}} |
| {{ex: Conversão landing}} | {{1.2%}} | {{3.8%}} | {{+217%}} |

**Período:** {{quanto tempo levou pra chegar nesse resultado}}

### Na prática

{{1-2 parágrafos. Como esse número mudou o dia do cliente. Concretiza o impacto.}}

### O que o cliente disse

> "{{citação completa do cliente, se houver}}"
>
> — **{{Nome do cliente}}**, {{Cargo}} na {{empresa}}

---

## Lições do projeto

{{2-4 bullets. O que esse projeto ensinou que serve pra outros casos. Mostra que você é alguém que aprende e generaliza.}}

---

## Quer um resultado parecido?

{{1 parágrafo curto explicando como começar com você. CTA suave.}}

**Próximo passo:** {{ex: "Agenda uma call de 30min — sem custo, sem compromisso. Link: ..."}}
```

---

## Fase 3 — Apresentar e ajustar

Apresente o case completo. Depois pergunte:

- Pergunta: "Como ficou? Quer ajustar algo?"
- Header: `Ajustes`
- Opções:
  - `Bom assim — vamos salvar`
  - `Mais curto — encurta pra 1 página`
  - `Mais técnico — adiciona detalhes de execução`
  - `Mais emocional — foca na transformação do cliente`
  - `Adicionar mais números`

Aplique ajustes até aprovação.

---

## Fase 4 — Anonimização (se aplicável)

Pergunte:
- Pergunta: "O cliente autoriza usar o nome real?"
- Header: `Anonimização`
- Opções:
  - `Sim — pode citar nome` — "Mantém tudo."
  - `Anônimo — descreve só setor/porte` — "Troco 'Acme Inc' por 'cliente do setor X, com Y funcionários'."
  - `Vou pedir antes de publicar` — "Mantém nome no rascunho, lembro de marcar."

Se anônimo, substitua nome, cidade específica, números muito identificáveis (faturamento total, etc.).

---

## Fase 5 — Salvar

Crie pasta se não existir:
```bash
mkdir -p "04 Resources/cases"
```

Slug do arquivo: nome do cliente em lowercase com hyphens, ou "anon-{setor}-{N}" se anônimo.

Salve em `04 Resources/cases/{{slug}}.md`:

```yaml
---
type: case-study
status: {{draft / approved / public}}
date: YYYY-MM-DD
tags: [case, {{setor}}, {{resultado-tipo}}]
cliente: {{nome ou "anônimo"}}
setor: {{setor}}
metrica_principal: {{resultado em 1 frase}}
publicavel: {{true/false}}
---
```

---

## Fase 6 — Confirmação

> "Case salvo em `04 Resources/cases/{{arquivo}}`.
>
> Status: {{draft / approved / public}}.
>
> Próximos passos:
> 1. Se ainda é draft, mandar pro cliente aprovar
> 2. Quando aprovado, marcar `status: approved` no frontmatter
> 3. Repurpose: rodar `/escrever` ou `/linkedin` pra virar post curto
> 4. Pra deck de vendas: copiar conteúdo pra slide deck (Canva, Google Slides, PPT)
>
> Pra próximo case: `/case-study`."

---

## Regras

- Nunca invente número. Se o usuário não deu, marque `{{verificar}}` e siga.
- Citação do cliente só se foi mesmo dita por ele — não invente.
- Se anônimo, anonimize de verdade — descrição genérica do setor.
- Mostre processo, não só resultado — clientes potenciais querem entender COMO chegou.
- Tentativas anteriores são chave — diferencia de "antes vs depois" simplista.
- Lições no fim mostram que você reflete, não só executa.
- Tom: confiante mas honesto. Sem "transformamos o negócio em 7 dias" exagerado.

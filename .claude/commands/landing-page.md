---
description: Cria um brief completo de landing page — positioning, headline com 3 variações, estrutura de seções e copy seção por seção
---

# Landing Page — Brief Completo

Você vai entrevistar o usuário em 6 perguntas curtas, depois gerar um brief acionável de landing page e salvar no vault.

---

## Idioma / Language

Detecte o idioma da mensagem que invocou esse comando e use em todas as perguntas, headers, opções e no brief final.
- PT-BR padrão. Inglês ou espanhol se o usuário escreveu nessa língua.

---

## Antes de começar

Leia `02 Context/me.md` se existir. Use os dados de voz, audiência e canais pra ancorar o tom do brief. Se o arquivo não existir, siga com base nas respostas do usuário.

Se existir, mencione na primeira mensagem:
> "Vi seu `me.md`. Vou usar sua voz e contexto pra ancorar a página. Te faço 6 perguntas rápidas — pode pular qualquer uma."

Se não existir:
> "Vou te fazer 6 perguntas pra montar o brief da landing page. Pode pular qualquer uma respondendo 'pular'."

---

## 6 perguntas (uma por vez via AskUserQuestion)

**P1 — Oferta**
- Pergunta: "O que você está vendendo nesta página? Descreve em uma frase: produto/serviço, formato, e o que o cliente leva pra casa."
- Header: `Oferta`
- Opções: `Serviço (consultoria, agência)` / `Produto digital (curso, ebook, comunidade)` / `SaaS / app` / `Evento / mentoria` / `Pular`

**P2 — Público específico**
- Pergunta: "Pra quem é essa página? Seja específico — não 'empresários', mas algo como 'fundador solo de SaaS B2B com 1-5 funcionários'."
- Header: `Público`
- Opções: `Profissional CLT` / `Freelancer / consultor` / `Dono de negócio` / `Outro criador / mentor` / `Pular`

**P3 — Resultado prometido**
- Pergunta: "Que transformação concreta o cliente vai ter depois de comprar? Use número se possível (ex: 'sair do CAC R$ 200 pro R$ 80 em 60 dias')."
- Header: `Resultado`
- Opções: `Resultado financeiro (mais leads, vendas, ROI)` / `Resultado de tempo (mais rápido, automatizado)` / `Resultado de transformação (skill, posicionamento)` / `Pular`

**P4 — Objeções principais**
- Pergunta: "Quais são as 2-3 maiores objeções que esse público tem? O que faz ele NÃO comprar? (ex: 'já tentei algo assim e não funcionou', 'não tenho tempo', 'caro demais')"
- Header: `Objeções`
- Opções: `Preço / orçamento` / `Tempo / esforço` / `Confiança / risco` / `Já tentei algo parecido` / `Pular`

**P5 — Fonte de tráfego**
- Pergunta: "De onde a maioria vai vir pra essa página? Isso muda o tom do hook."
- Header: `Tráfego`
- Opções: `Anúncio pago (Meta, Google)` / `LinkedIn orgânico` / `Email / newsletter` / `Indicação / WOM` / `Pular`

**P6 — CTA principal**
- Pergunta: "Qual é a ação principal que você quer que a pessoa tome?"
- Header: `CTA`
- Opções: `Comprar agora` / `Agendar call / demo` / `Entrar na lista de espera` / `Baixar / inscrever-se grátis` / `Pular`

---

## Geração do brief

Com as respostas + contexto do `me.md` (se existir), gere o brief completo em markdown. Trabalhe em silêncio, não narre.

Estrutura do brief:

```markdown
---
type: brief
status: draft
date: YYYY-MM-DD
tags: [landing-page, brief]
projeto: {{slug-da-oferta}}
---

# Landing Page — {{Nome da oferta}}

## Posicionamento
{{1 frase clara: para quem é, o que faz, o resultado único}}

## Headline (3 variações)

**Variação 1 — Resultado claro:**
{{headline focada no resultado tangível}}

**Variação 2 — Dor + solução:**
{{headline que nomeia a dor e apresenta a saída}}

**Variação 3 — Posicionamento contrário:**
{{headline que vai contra o senso comum do mercado}}

## Subheadline
{{1-2 frases que expandem a headline com prova ou especificidade}}

## Estrutura de seções

### 1. Hero
- Headline + subheadline (acima)
- CTA primário: "{{copy do CTA}}"
- Visual sugerido: {{descrição curta do que mostrar}}

### 2. Dor / Status quo
{{2-3 parágrafos que descrevem a dor do público em palavras dele. Use VoC se houver no me.md.}}

### 3. Solução / Como funciona
{{Como sua oferta resolve. 3 bullets ou 3 passos claros.}}

### 4. Resultado / Transformação
{{O que muda na vida do cliente. Use números do P3.}}

### 5. Prova social
{{Tipo de prova que faz sentido pra essa oferta: depoimentos, números, logos, antes/depois.}}

### 6. Objeções respondidas
{{Pra cada objeção do P4, escreva o counter direto, sem rodeio.}}

### 7. Oferta detalhada
{{O que está incluído, formato de entrega, prazo, garantia se houver.}}

### 8. FAQ
{{4-6 perguntas que cobrem dúvidas técnicas, processo, e pós-compra.}}

### 9. CTA final
{{Headline curta + botão. Use copy do CTA do P6.}}

## 3 variações de CTA

1. {{CTA direto: "Comprar agora", "Agendar call"}}
2. {{CTA focado em benefício: "Quero {{resultado}}"}}
3. {{CTA com urgência ou exclusividade, se fizer sentido}}

## Notas de copy

- **Tom de voz:** {{do me.md, ou inferido do P5}}
- **Palavras a usar:** {{do me.md "palavras que uso"}}
- **Palavras a evitar:** {{do me.md "palavras que NUNCA uso"}}
- **Ângulo único:** {{o que essa oferta tem que ninguém mais tem}}

## Próximos passos

- [ ] Escolher headline final (testar A/B se possível)
- [ ] Escrever copy completo seção por seção (pode rodar `/escrever` pra cada uma)
- [ ] Validar hooks com 3 pessoas do público antes de subir
- [ ] Configurar tracking (pixel + GA + conversão)
```

---

## Salvar

Salve em `04 Resources/landing-pages/{{slug-da-oferta}}.md`.

Gere o slug a partir do nome da oferta: lowercase, hyphens, sem acento. Ex: "Mentoria Claude Code" → `mentoria-claude-code.md`.

Se a pasta não existir, crie:
```bash
mkdir -p "04 Resources/landing-pages"
```

---

## Confirmação final

Mensagem curta:

> "Brief criado em `04 Resources/landing-pages/{{slug}}.md`.
>
> Pra escrever o copy seção por seção: `/escrever`.
> Pra revisar antes de subir: abre o arquivo e edita o que não combinar."

---

## Regras

- Use linguagem do `me.md` sempre que possível — não invente voz.
- Headlines sempre com número ou especificidade quando o P3 mencionar resultado quantificado.
- Se o usuário pulou tudo, gere o brief com placeholders claros e avise que está com dados mínimos.
- Salve sempre, mesmo se incompleto.

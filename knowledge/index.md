---
type: index
status: active
date: 2026-05-26
tags: [index, navigation, knowledge]
---

# Knowledge Index — Seu AI OS

> **Auto-loaded em toda sessão.** Este é o primeiro arquivo que a IA lê. Use pra ancorar conhecimento permanente — domínios que você quer que a IA SEMPRE saiba sem você ter que reexplicar.

---

## Hub

Voltar ao hub central do vault: [[Home]].

---

## Como funciona

Quando você abre o Claude Code (ou outra ferramenta) dentro deste vault, o hook `session-start.py` injeta este arquivo no contexto inicial. Tudo que estiver listado aqui ou linkado daqui fica disponível pra IA imediatamente.

**Diferença pra `04 Resources/`:**
- `knowledge/` = sempre carregado (cabe pouco, alta prioridade)
- `04 Resources/` = consultado sob demanda (cabe tudo, baixa prioridade)

**O que vai em knowledge:**
- Conceitos centrais do seu trabalho (copywriting, growth, SEO, etc.)
- Frameworks que você usa repetidamente
- Visão estratégica que orienta decisões
- Vocabulário e definições específicas do seu nicho

**O que NÃO vai em knowledge:**
- Outputs de comandos (textos, briefs) → `04 Resources/`
- Decisões pontuais → `03 Intelligence/decisions/`
- Anotações de reunião → `03 Intelligence/meetings/`
- Brain dumps soltos → `00 Inbox/`

---

## Domínios de conhecimento

Os arquivos abaixo são templates pra você preencher conforme seu trabalho exige. Apague os que não usa, edite os que usam, adicione novos quando aparecer um domínio recorrente.

| Arquivo | Quando você precisa |
|---|---|
| [[knowledge/copywriting]] | Pra escrever qualquer texto comercial (LinkedIn, email, landing, ads) |
| [[knowledge/content-strategy]] | Pra planejar conteúdo recorrente (newsletter, blog, social) |
| [[knowledge/personal-brand]] | Pra construir reputação online como pessoa |
| [[knowledge/growth-marketing]] | Pra crescer audiência, leads, receita |
| [[knowledge/seo-fundamentos]] | Pra ranquear conteúdo no Google e em IAs |

---

## Como adicionar um knowledge file novo

1. Crie `knowledge/{dominio}.md`
2. Frontmatter:
   ```yaml
   ---
   type: knowledge
   domain: {dominio}
   status: active
   date: YYYY-MM-DD
   tags: [knowledge, {dominio}]
   ---
   ```
3. Conteúdo: princípios + frameworks + vocabulário + referências do domínio
4. Adicione um link na tabela acima
5. A IA passa a usar automaticamente na próxima sessão

---

## Princípios pros knowledge files

- **Conciso** — knowledge é peso permanente no contexto. Cada palavra conta.
- **Princípios > exemplos** — se um princípio leva 1 linha e um exemplo leva 10, prefira o princípio.
- **Próprio > genérico** — o que VOCÊ acredita sobre o domínio, não o que está em livro de marketing.
- **Atualizável** — quando seu pensamento muda, edita o arquivo. Não é texto sagrado.
- **Linkado** — wikilinks pra outros knowledge files quando há conexão.

---

## Próximos passos

1. Abrir cada knowledge file da lista acima
2. Editar com seu conhecimento real (apaga o que é genérico, mantém o que é seu)
3. Adicionar arquivos novos pros domínios que você não vê listados mas usa
4. Na próxima sessão da IA, perceber que ela "sabe" do seu trabalho sem você explicar

---

## Navegação

Domínios de conhecimento: [[copywriting]], [[content-strategy]], [[personal-brand]], [[growth-marketing]], [[seo-fundamentos]].

Voltar para o [[Home|hub central]].

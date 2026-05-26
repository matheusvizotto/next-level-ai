---
description: Análise SEO completa de uma URL — on-page, meta tags, schema, conteúdo, links internos, alt text, performance básica. Gera relatório com prioridades.
---

# SEO Página — Análise Profunda de uma URL

Auditoria de SEO em uma página específica. Identifica problemas críticos, médios e baixos, com fix sugerido pra cada.

---

## Idioma / Language

Detecte o idioma da mensagem e use no relatório final. PT-BR padrão.

---

## Fase 1 — URL e contexto

Pergunte (se não foi informado já):
> "Cola a URL que você quer auditar. Se quiser, conta o objetivo da página em 1 frase (vendas, captação, autoridade) — ajuda a calibrar."

Se o usuário só colou URL, siga em frente. Objetivo é opcional.

---

## Fase 2 — Buscar a página

Use WebFetch pra puxar o HTML. Capture:
- `<title>`
- `<meta name="description">`
- `<meta property="og:*">`
- `<meta name="twitter:*">`
- Tags `<h1>`, `<h2>`, `<h3>` (em ordem)
- Texto visível (conteúdo)
- Links internos (mesmo domínio)
- Links externos
- Imagens (`<img>` com alt)
- Schema JSON-LD (`<script type="application/ld+json">`)
- `<link rel="canonical">`
- Robots meta
- Idioma declarado (`<html lang="...">`)

Se WebFetch falhar (paywall, JS-only, bloqueio), avise o usuário e peça pra colar o HTML manualmente ou usar outra ferramenta.

---

## Fase 3 — Análise por categoria

Avalie cada categoria. Marque cada item como ✓ (ok), ⚠️ (warning), ❌ (critical).

### 3.1 — Title tag
- ✓ Existe
- ✓ Tem 50-60 caracteres
- ✓ Contém keyword principal (peça ao usuário a keyword alvo se não souber, ou infira do conteúdo)
- ✓ Marca aparece (opcional mas comum em final)
- ❌ Não tem boilerplate ("Home | Site") sem contexto

### 3.2 — Meta description
- ✓ Existe
- ✓ Tem 140-160 caracteres
- ✓ Contém keyword
- ✓ Tem CTA implícito ou explícito
- ✓ Não duplica o title

### 3.3 — Open Graph
- ✓ `og:title` existe
- ✓ `og:description` existe
- ✓ `og:image` existe e tem ao menos 1200x630
- ✓ `og:url` existe
- ✓ `og:type` apropriado (website, article, product)

### 3.4 — Twitter Card
- ✓ `twitter:card` (summary, summary_large_image)
- ✓ `twitter:title`, `twitter:description`, `twitter:image`

### 3.5 — Hierarquia de headings
- ❌ Exatamente 1 `<h1>` na página
- ✓ H1 contém keyword principal
- ✓ H2s organizam seções, em ordem lógica
- ❌ H3s aninhados dentro de H2 (não pulam nível)
- ⚠️ H2 e H3 com palavras relacionadas à keyword

### 3.6 — Conteúdo
- ✓ Mínimo 600 palavras (artigos longos: 1500+)
- ✓ Keyword principal aparece no primeiro parágrafo
- ⚠️ Keyword density entre 0.5% e 2% (não force)
- ✓ Conteúdo único, não copiado
- ✓ Frases curtas (média < 20 palavras)
- ✓ Parágrafos curtos (3-4 linhas máximo)
- ⚠️ Listas e bullets usados quando ajuda
- ⚠️ Imagens com legendas explicativas

### 3.7 — Links
**Internos:**
- ✓ Pelo menos 3 links internos relevantes
- ✓ Anchor text descritivo (não "clique aqui")
- ✓ Sem links quebrados (verifique amostra)

**Externos:**
- ✓ Links externos pra fontes autoritativas quando há claim
- ⚠️ `rel="noopener"` ou `rel="nofollow"` apropriado
- ✓ Abre em nova aba quando faz sentido

### 3.8 — Imagens
- ❌ Toda imagem tem `alt` (vazio é aceitável só pra decorativas)
- ✓ Alt descritivo, não keyword stuffed
- ⚠️ Formato moderno (WebP, AVIF) se possível
- ⚠️ Lazy loading em imagens fora do fold

### 3.9 — Schema (JSON-LD)
- ⚠️ Schema apropriado ao tipo de página:
  - Artigo → `Article` ou `BlogPosting`
  - Produto → `Product`
  - Local business → `LocalBusiness`
  - FAQ → `FAQPage`
  - Pessoa → `Person`
  - Receita → `Recipe`
- ✓ Schema validado (sem erros)

### 3.10 — Técnico básico
- ✓ Canonical apontando pra URL correta
- ✓ Robots não bloqueando indexação (sem `noindex`)
- ✓ `<html lang="...">` declarado corretamente
- ⚠️ URL limpa, sem parâmetros desnecessários
- ⚠️ HTTPS habilitado

---

## Fase 4 — Relatório

Gere relatório em markdown com 4 seções:

```markdown
# Auditoria SEO — {{URL}}

**Data:** YYYY-MM-DD
**Objetivo da página:** {{do usuário ou "não informado"}}
**Keyword principal:** {{informada ou inferida}}

---

## Score geral

- ✓ {{N}} pontos ok
- ⚠️ {{N}} pontos com warning
- ❌ {{N}} pontos críticos

**Score:** {{ok}}/{{total}} = {{percentual}}%

---

## Críticos (corrigir agora)

{{Lista de cada item ❌ com:
- O que está errado
- Como está hoje (cite o conteúdo atual)
- Como deve ficar
- Por que importa}}

---

## Warnings (corrigir em seguida)

{{Lista de cada ⚠️ no mesmo formato}}

---

## OK (manter)

{{Lista curta dos ✓ relevantes}}

---

## Plano de ação (priorizado)

1. {{ação concreta 1}}
2. {{ação concreta 2}}
3. {{ação concreta 3}}
... (máximo 7)

---

## Próximos passos sugeridos

- Re-auditar depois das mudanças: `/seo-pagina` com a mesma URL
- Pra outras páginas do site: rodar em cada URL importante
- Pra estratégia de conteúdo: definir keyword research e cluster
```

---

## Fase 5 — Salvar

Crie pasta se não existir:
```bash
mkdir -p "04 Resources/seo/auditorias"
```

Salve em `04 Resources/seo/auditorias/YYYY-MM-DD-{{slug-do-dominio}}-{{slug-da-pagina}}.md`.

Slug do domínio: extraia do URL, remova `www.` e `.com.br`. Ex: `https://www.exemplo.com.br/blog/post-1` → domínio `exemplo`, página `blog-post-1`.

Frontmatter:
```yaml
---
type: audit
status: complete
date: YYYY-MM-DD
tags: [seo, auditoria]
url: {{url completa}}
score: {{percentual}}
criticos: {{N}}
---
```

---

## Confirmação

> "Auditoria salva em `04 Resources/seo/auditorias/{{arquivo}}`.
>
> Score: {{percentual}}%. {{N}} pontos críticos.
>
> Próximo passo: começar pelos críticos da lista. Quando ajustar, rode `/seo-pagina` de novo na mesma URL pra ver o delta."

---

## Regras

- Nunca invente conteúdo da página — se não conseguiu buscar, peça pro usuário colar.
- Se não souber a keyword principal, infira do título + H1 ou pergunte explicitamente.
- Não dê nota inflada — seja honesto sobre o que está mal.
- Não comente cada item ok — só os que importam.
- Use linguagem prática, não jargão SEO. O inscrito pode ser iniciante.

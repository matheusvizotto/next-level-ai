#!/usr/bin/env python3
"""
AI OS — Session Capture Hook

Dispara em PreCompact — lembra a IA de persistir conhecimento da sessão
no daily ANTES do contexto comprimir e detalhes serem perdidos.
"""
from datetime import date

today = date.today().isoformat()

print(f"""[AI OS — Session Capture]
Contexto vai comprimir. Persista esta sessão em 01 Daily/{today}.md AGORA.

Use este schema como nova entrada `## Sessão`:

**Decisões tomadas:** (decisões arquiteturais, estratégicas, ou de produto desta sessão)
**Aprendizados:** (o que funcionou, o que falhou, o que foi descoberto)
**Próximos passos:** (ações concretas — específicas, com responsável e data se possível)

Route qualquer info nova de projeto, correção ou decisão pro arquivo certo do vault antes de comprimir.

Veja AIOS/knowledge-routing.md se tiver dúvida sobre onde algo vai.
""")

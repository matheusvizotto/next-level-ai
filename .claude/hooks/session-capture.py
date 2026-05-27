#!/usr/bin/env python3
"""
AI OS — Session Capture Hook

Dispara em PreCompact — rede de seguranca pra sessoes longas. Lembra a IA de
persistir conhecimento da sessao no daily ANTES do contexto comprimir e
detalhes serem perdidos.

O resumo final automatico fica por conta do session-end.py (SessionEnd).
Este hook cobre o caso de sessoes longas que comprimem antes de terminar.
"""
import os
import sys
from datetime import date

# Guard anti-recursao: nao roda durante a documentacao headless.
if os.environ.get("AIOS_DOCUMENTING") == "1":
    sys.exit(0)

today = date.today().isoformat()

print(f"""[AI OS — Session Capture]
Contexto vai comprimir. Persista esta sessao em 01 Daily/{today}.md AGORA.

Use este schema como nova entrada `## Sessao`:

**Decisoes tomadas:** (decisoes arquiteturais, estrategicas, ou de produto desta sessao)
**O que foi feito:** (acoes concretas realizadas)
**Aprendizados:** (o que funcionou, o que falhou, o que foi descoberto)
**Proximos passos:** (acoes concretas — especificas, com responsavel e data se possivel)

Route qualquer info nova de projeto, correcao ou decisao pro arquivo certo do vault antes de comprimir.
Veja AIOS/knowledge-routing.md se tiver duvida sobre onde algo vai.
""")

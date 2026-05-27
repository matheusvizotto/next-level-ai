#!/usr/bin/env python3
"""
AI OS — Session Start Hook

Injeta arquivos de contexto central no início de cada sessão do Claude E
garante que a nota diária de hoje exista, instruindo a IA a documentar.

Dispara em PreToolUse — só imprime na primeira tool call de cada sessão.

Ordem de injeção:
  1. knowledge/index.md       — Knowledge hub auto-loaded
  2. AIOS/index.md            — Catálogo de skills e comandos
  3. AIOS/operating-rules.md  — Como a IA opera neste vault
  4. 02 Context/me.md         — Identidade (modo solo)
     OU operator.md + organization.md + team.md (modo empresa)
  5. nota mais recente em 01 Daily/  — Contexto da última sessão
  6. Garante 01 Daily/HOJE.md + instrução de documentação

Path do vault é detectado automaticamente a partir da localização do hook.
"""
import os
import sys
from datetime import date
from pathlib import Path

# Recursion guard: a captura automática de fim de sessão chama o claude headless,
# que dispararia este hook de novo. Se estamos dentro de uma rodada de documentação, sai.
if os.environ.get("AIOS_DOCUMENTING") == "1":
    sys.exit(0)

# Vault root = parent de .claude/hooks/
VAULT = Path(__file__).resolve().parent.parent.parent

STATIC_FILES = [
    ("knowledge/index.md", "Knowledge Index"),
    ("AIOS/index.md", "Skills Index"),
    ("AIOS/operating-rules.md", "Operating Rules"),
]

IDENTITY_FILES_SOLO = [
    ("02 Context/me.md", "Identidade"),
]

IDENTITY_FILES_EMPRESA = [
    ("02 Context/operator.md", "Operador"),
    ("02 Context/organization.md", "Empresa"),
    ("02 Context/team.md", "Time"),
]


def get_latest_daily(vault: Path):
    """Retorna o arquivo de daily mais recente, ou None se não existir."""
    daily_dir = vault / "01 Daily"
    if not daily_dir.exists():
        return None
    files = sorted(daily_dir.glob("????-??-??.md"), reverse=True)
    if files:
        return files[0].relative_to(vault)
    return None


def detect_mode(vault: Path):
    operator = vault / "02 Context" / "operator.md"
    organization = vault / "02 Context" / "organization.md"
    if operator.exists() and organization.exists():
        return "empresa"
    return "solo"


def ensure_today_daily(vault: Path):
    """Cria 01 Daily/HOJE.md com frontmatter se ainda não existir."""
    today = date.today().isoformat()
    daily_dir = vault / "01 Daily"
    daily_dir.mkdir(parents=True, exist_ok=True)
    daily_path = daily_dir / f"{today}.md"
    if not daily_path.exists():
        daily_path.write_text(
            f"---\ntype: daily\ndate: {today}\nstatus: active\ntags: [daily]\n---\n",
            encoding="utf-8",
        )
    return today


# Lock por processo Claude — nova sessão = novo PID = novo lock
lock = Path(f"/tmp/aios_session_{os.getppid()}.lock")

if lock.exists():
    sys.exit(0)

lock.touch()

parts = ["[AI OS — Session Start]\n"]

# Static files
for rel_path, label in STATIC_FILES:
    full_path = VAULT / rel_path
    if full_path.exists():
        parts.append(f"--- {label} ---\n{full_path.read_text()}\n")
    else:
        parts.append(f"[AI OS] {rel_path} não encontrado — rode /setup pra criar.\n")

# Identity files baseados no modo
mode = detect_mode(VAULT)
identity_files = IDENTITY_FILES_EMPRESA if mode == "empresa" else IDENTITY_FILES_SOLO

for rel_path, label in identity_files:
    full_path = VAULT / rel_path
    if full_path.exists():
        parts.append(f"--- {label} ---\n{full_path.read_text()}\n")

# Latest daily
latest_daily = get_latest_daily(VAULT)
if latest_daily:
    full_path = VAULT / latest_daily
    parts.append(f"--- Última Sessão ({latest_daily.stem}) ---\n{full_path.read_text()}\n")

# Garante o daily de hoje e instrui documentação
today = ensure_today_daily(VAULT)
parts.append(
    f"""--- Documentação desta Sessão ---
A nota de hoje existe em `01 Daily/{today}.md`.

REGRA: esta conversa será documentada. Conforme trabalha:
- Toda decisão real → registre com o subagent decision-tracker em `03 Intelligence/decisions/`
- Info nova de projeto, correção ou aprendizado → roteie pro arquivo certo (veja AIOS/knowledge-routing.md)

Ao final da sessão, um resumo automático será gravado em `01 Daily/{today}.md` pelo hook de fim de sessão. Você não precisa fazer isso manualmente, mas registre decisões importantes na hora pra não perder o contexto.
"""
)

print("\n".join(parts))

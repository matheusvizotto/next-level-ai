#!/usr/bin/env python3
"""
AI OS — Session Start Hook

Injeta arquivos de contexto central no início de cada sessão do Claude.
Dispara em PreToolUse — só imprime na primeira tool call de cada sessão.

Ordem de injeção:
  1. knowledge/index.md       — Knowledge hub auto-loaded
  2. AIOS/index.md            — Catálogo de skills e comandos
  3. AIOS/operating-rules.md  — Como a IA opera neste vault
  4. 02 Context/me.md         — Identidade do usuário (modo solo)
     OU
     02 Context/operator.md + organization.md (modo empresa)
  5. nota mais recente em 01 Daily/  — Contexto da última sessão

Path do vault é detectado automaticamente a partir da localização do hook.
"""
import os
import sys
from pathlib import Path

# Vault root = parent de .claude/hooks/
VAULT = Path(__file__).resolve().parent.parent.parent

# Arquivos fixos sempre carregados
STATIC_FILES = [
    ("knowledge/index.md", "Knowledge Index"),
    ("AIOS/index.md", "Skills Index"),
    ("AIOS/operating-rules.md", "Operating Rules"),
]

# Arquivos de identidade — tenta modo solo primeiro, depois empresa
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
    """Detecta se vault está em modo solo ou empresa baseado nos arquivos existentes."""
    operator = vault / "02 Context" / "operator.md"
    organization = vault / "02 Context" / "organization.md"
    if operator.exists() and organization.exists():
        return "empresa"
    return "solo"


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

print("\n".join(parts))

#!/usr/bin/env python3
"""
AI OS — Session End Hook (documentação 100% automática)

Dispara em SessionEnd. Lê o transcript da conversa inteira, resume via
Claude headless (claude -p), e grava o resumo em 01 Daily/HOJE.md.

Não depende da IA da sessão lembrar de documentar. Garante que TODA
conversa vira registro, mesmo curta.

Guard anti-recursão: a chamada headless do claude dispararia hooks de novo.
A env var AIOS_DOCUMENTING=1 (setada no subprocess) faz os hooks saírem cedo.
"""
import json
import os
import shutil
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

# Se já estamos dentro de uma rodada de documentação, não faz nada (evita loop).
if os.environ.get("AIOS_DOCUMENTING") == "1":
    sys.exit(0)


def read_hook_input():
    try:
        return json.load(sys.stdin)
    except Exception:
        return {}


def extract_conversation(path, max_chars=120000):
    """Extrai texto de user + assistant do transcript JSONL."""
    out = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except Exception:
                    continue
                msg = obj.get("message") or obj
                role = msg.get("role") or obj.get("type") or ""
                if role not in ("user", "assistant"):
                    continue
                content = msg.get("content")
                text = ""
                if isinstance(content, str):
                    text = content
                elif isinstance(content, list):
                    for block in content:
                        if isinstance(block, dict) and block.get("type") == "text":
                            text += block.get("text", "")
                if text.strip():
                    out.append(f"[{role}] {text.strip()}")
    except Exception:
        return ""
    convo = "\n\n".join(out)
    if len(convo) > max_chars:
        convo = "(início truncado)\n\n" + convo[-max_chars:]
    return convo


def find_claude():
    c = shutil.which("claude")
    if c:
        return c
    candidates = [
        "/opt/homebrew/bin/claude",
        os.path.expanduser("~/.claude/local/claude"),
        "/usr/local/bin/claude",
    ]
    for p in candidates:
        if os.path.exists(p):
            return p
    return None


def summarize(convo):
    claude = find_claude()
    if not claude:
        return None
    prompt = (
        "Resuma esta sessao de trabalho para uma nota diaria do Obsidian. "
        "Use exatamente este formato em PT-BR, conciso e especifico:\n\n"
        "**Decisoes tomadas:** (decisoes reais desta sessao, ou 'nenhuma')\n"
        "**O que foi feito:** (acoes concretas realizadas)\n"
        "**Aprendizados:** (o que funcionou, o que falhou)\n"
        "**Proximos passos:** (acoes pendentes)\n\n"
        "Nao invente. Baseie so no que esta na conversa abaixo.\n\n"
        "=== CONVERSA ===\n" + convo
    )
    env = dict(os.environ)
    env["AIOS_DOCUMENTING"] = "1"
    try:
        result = subprocess.run(
            [claude, "-p", prompt],
            capture_output=True,
            text=True,
            timeout=180,
            env=env,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except Exception:
        pass
    return None


def write_to_daily(vault, summary):
    today = date.today().isoformat()
    daily_dir = Path(vault) / "01 Daily"
    daily_dir.mkdir(parents=True, exist_ok=True)
    daily_path = daily_dir / f"{today}.md"
    ts = datetime.now().strftime("%H:%M")
    if not daily_path.exists():
        daily_path.write_text(
            f"---\ntype: daily\ndate: {today}\nstatus: active\ntags: [daily]\n---\n",
            encoding="utf-8",
        )
    entry = f"\n\n## Sessao {ts}\n\n{summary}\n"
    with open(daily_path, "a", encoding="utf-8") as f:
        f.write(entry)


def main():
    hook = read_hook_input()
    transcript_path = hook.get("transcript_path", "")
    cwd = hook.get("cwd") or os.getcwd()
    vault = os.environ.get("CLAUDE_PROJECT_DIR", cwd)

    if not transcript_path or not os.path.exists(transcript_path):
        sys.exit(0)

    convo = extract_conversation(transcript_path)
    if not convo.strip():
        sys.exit(0)

    summary = summarize(convo)
    if not summary:
        summary = f"(Resumo automatico indisponivel nesta sessao. Transcript: {transcript_path})"

    write_to_daily(vault, summary)


if __name__ == "__main__":
    main()

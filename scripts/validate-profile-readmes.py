"""Validate the current professional profile contract (GitHub Part 1 / 2026-11).

This check is deliberately based on *verifiable presentation*, not on the
presence of obsolete job titles or old resume filenames.
"""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = {
    "README.md": [
        "Engenharia de Software", "IA Aplicada", "ArsenalMind Universal",
        "Desapega AI", "Belarc Inventory", "Produção Operacional",
        "Compass UOL", "Técnico Júnior", "MCP", "LinkedIn",
        "cases/EVIDENCIAS.md",
    ],
    "README.en.md": [
        "Software Engineering", "Applied AI", "ArsenalMind Universal",
        "Desapega AI", "Belarc Inventory", "Produção Operacional",
        "Compass UOL", "Junior Process Automation Technician", "MCP",
        "LinkedIn", "cases/EVIDENCIAS.md",
    ],
    "cases/ARSENALMIND.md": [
        "Desapega AI", "não", "MCP", "30/10/2026",
    ],
    "cases/DESAPEGA.md": [
        "regras comerciais", "supervisão", "não", "publicação",
    ],
    "cases/EVIDENCIAS.md": [
        "Declarado", "Inspecionado", "Testado", "Impacto medido",
    ],
}
FORBIDDEN = {
    "README.md": [
        "produto pessoal em uso", "sênior em IA",
        "10 mil+ execuções da Mala Direta",
    ],
    "README.en.md": [
        "senior AI engineer", "10,000+ Mala Direta sends",
    ],
}
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
errors = []
for filename, required in REQUIRED.items():
    path = ROOT / filename
    if not path.is_file():
        errors.append(f"missing required profile document: {filename}")
        continue
    content = path.read_text(encoding="utf-8")
    for token in required:
        if token not in content:
            errors.append(f"{filename}: missing selected-work evidence: {token}")
    for token in FORBIDDEN.get(filename, []):
        if token in content:
            errors.append(f"{filename}: unsupported or stale claim: {token}")
    for target in LINK_PATTERN.findall(content):
        if target.startswith(("#", "https://", "http://", "mailto:")):
            continue
        ref = unquote(urlsplit(target).path)
        dest = (path.parent / ref).resolve()
        if not dest.is_relative_to(ROOT.resolve()):
            errors.append(f"{filename}: relative link escapes repository: {target}")
        elif not dest.exists():
            errors.append(f"{filename}: broken relative link: {target}")

if errors:
    print("\n".join(f"ERROR: {err}" for err in errors))
    raise SystemExit(1)

print("Profile documentation validated: focus, cross-project cases, relative links and truthful claims.")

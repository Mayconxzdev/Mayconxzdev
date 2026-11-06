"""Basic checks for the public profile and selected case studies."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = {
    "README.md": ["ArsenalMind Universal", "Desapega AI", "Belarc Inventory", "Produção Operacional", "Compass UOL", "LinkedIn", "MCP"],
    "README.en.md": ["ArsenalMind Universal", "Desapega AI", "Belarc Inventory", "Production Operations", "Compass UOL", "MCP"],
    "cases/ARSENALMIND.md": ["MCP", "Desapega AI", "30/10/2026", "Solution Scout"],
    "cases/DESAPEGA.md": ["Python", "SQLite", "Telegram", "publicações", "regras"],
    "cases/EVIDENCIAS.md": ["Declarado", "Inspecionado", "Testado", "Impacto medido"],
    "cases/ARSENALMIND.en.md": ["MCP", "Desapega AI", "Solution Scout"],
    "cases/DESAPEGA.en.md": ["Python", "SQLite", "Telegram", "publishing"],
}
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
ERRORS = []
for filename, words in REQUIRED.items():
    path = ROOT / filename
    if not path.is_file():
        ERRORS.append(f"Missing: {filename}")
        continue
    body = path.read_text(encoding="utf-8")
    for w in words:
        if w.lower() not in body.lower():
            ERRORS.append(f"{filename}: missing topic {w!r}")
    for link in LINK_PATTERN.findall(body):
        if link.startswith(("#", "https://", "http://", "mailto:")):
            continue
        rel = unquote(urlsplit(link).path)
        dest = (path.parent / rel).resolve()
        if not dest.is_relative_to(ROOT):
            ERRORS.append(f"{filename}: link outside repo {link}")
        elif not dest.exists():
            ERRORS.append(f"{filename}: broken link {link}")

# Guard against old CV catalogs and inflated job titles returning to the first screen.
for filename in ("README.md", "README.en.md"):
    text = (ROOT / filename).read_text(encoding="utf-8").lower()
    for phrase in ("6 currículos", "six resumes", "senior ai research scientist", "sênior em ia", "produto pessoal em uso"):
        if phrase in text:
            ERRORS.append(f"{filename}: outdated or unsupported phrase {phrase}")

if ERRORS:
    print("\n".join("ERROR: " + msg for msg in ERRORS))
    raise SystemExit(1)

print("README and PT/EN case studies: topics and local links OK.")

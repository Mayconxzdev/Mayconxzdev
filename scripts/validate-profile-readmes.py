from pathlib import Path

profiles = {
    "README.md": {
        "required": [
            "Sistemas · Automação · Integrações · IA aplicada",
            "Técnico Júnior em Automação de Processos",
            "Python", "APIs", "n8n", "MCP",
            "Produção Operacional", "Manutenção em Campo",
            "Engenharia de Dados", "Compass UOL", "Hubora",
            "Belarc Inventory", "ZERO21FOTOS",
            "Postagem Redes", "experimento concluído",
            "Maycon_Ferreira_Geral_Automacao_IA_PT.pdf",
            "Maycon_Ferreira_Agentes_Automacao_n8n_PT.pdf",
            "Maycon_Ferreira_Produtos_Conteudo_IA_PT.pdf",
            "Maycon_Ferreira_General_Automation_AI_EN.pdf",
            "Maycon_Ferreira_AI_Agents_Automation_n8n_EN.pdf",
            "Maycon_Ferreira_AI_Digital_Products_Content_EN.pdf",
        ],
        "stale": [
            "Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf",
            "Maycon_Ferreira_Automacao_IA_n8n_Python_LLMs.pdf",
            "Maycon_Ferreira_Automacao_BI_Power_Automate_Power_BI.pdf",
            "Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf",
            "10 mil+ execuções da Mala Direta",
            "sênior em IA",
        ],
    },
    "README.en.md": {
        "required": [
            "Systems · Automation · Integrations · Applied AI",
            "Junior Process Automation Technician",
            "Python", "APIs", "n8n", "MCP",
            "Production Operations", "Field Maintenance",
            "Data Engineering", "Compass UOL", "Hubora",
            "Belarc Inventory", "ZERO21FOTOS",
            "Postagem Redes", "completed experiment",
            "Maycon_Ferreira_Geral_Automacao_IA_PT.pdf",
            "Maycon_Ferreira_Agentes_Automacao_n8n_PT.pdf",
            "Maycon_Ferreira_Produtos_Conteudo_IA_PT.pdf",
            "Maycon_Ferreira_General_Automation_AI_EN.pdf",
            "Maycon_Ferreira_AI_Agents_Automation_n8n_EN.pdf",
            "Maycon_Ferreira_AI_Digital_Products_Content_EN.pdf",
        ],
        "stale": [
            "Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf",
            "Maycon_Ferreira_Automacao_IA_n8n_Python_LLMs.pdf",
            "Maycon_Ferreira_Automacao_BI_Power_Automate_Power_BI.pdf",
            "Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf",
            "10,000+ Mala Direta sends",
            "senior AI engineer",
        ],
    },
}

errors = []
for filename, checks in profiles.items():
    text = Path(filename).read_text(encoding="utf-8")
    for phrase in checks["required"]:
        if phrase not in text:
            errors.append(f"{filename}: missing current fact or canonical PDF: {phrase}")
    for phrase in checks["stale"]:
        if phrase in text:
            errors.append(f"{filename}: stale or unsupported wording: {phrase}")
    for pdf in (phrase for phrase in checks["required"] if phrase.endswith(".pdf")):
        if text.count(pdf) != 1:
            errors.append(f"{filename}: expected one link for {pdf}")

if errors:
    print("\n".join(f"ERROR: {error}" for error in errors))
    raise SystemExit(1)

print("Profile README proposals validated: current positioning, six canonical PDFs per language, no stale filenames.")
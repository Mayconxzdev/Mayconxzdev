# Capability Watch — um módulo do ArsenalMind

Este é um recorte do **ArsenalMind Universal** que eu uso para acompanhar novas ferramentas. Escolhi publicar esse módulo porque dá para rodar e testar sem expor meus arquivos ou instalar o kit completo.

Ele consulta **metadados públicos** de repositórios no GitHub e discussões do Hacker News, guarda observações em SQLite e monta um relatório com candidatos para pesquisa. **Não baixa nem executa o código dos projetos encontrados.**

[Voltar ao case ArsenalMind](../../cases/ARSENALMIND.md)

## Rodando localmente

Requer Python 3.11+ e usa somente a biblioteca padrão.

```bash
# Verificar a instalação (não acessa a internet)
python scripts/capability_watch.py doctor

# Testes locais com dados fictícios (não acessam a internet)
python -m unittest discover -s tests -v

# Consultar duas fontes públicas (faz solicitações HTTP)
python scripts/capability_watch.py scan --query "MCP tools" --budget 3

# Ler observações salvas (sem novas consultas)
python scripts/capability_watch.py report --query "MCP tools"
```

Por padrão os relatórios e o banco local ficam no diretório de estado do usuário. Para usar uma pasta temporária, defina `ARSENALMIND_DATA_DIR` antes de executar.

## Decisões que tomei

- **Sem instalação automática:** uma descoberta não é uma dependência aprovada.
- **Fontes limitadas:** as consultas do módulo só aceitam os hosts previstos.
- **Sem crescimento inventado:** ele só calcula variações depois que encontra uma segunda observação com intervalo suficiente.
- **Relatórios com ressalvas:** os resultados saem como `UNVERIFIED`, `NOT_SCANNED` e `NOT_INSTALLED`; a nota é um sinal de priorização, não certificação de qualidade.
- **Testes offline:** verificam extração, persistência, rejeição de consultas inadequadas e cálculo temporal sem credenciais.

## O que este recorte não mostra

Este script **não é o servidor MCP completo**, não faz a seleção final para o usuário e não executa trabalhos no Codex/Antigravity. Essas capacidades fazem parte de outros componentes da instalação local do ArsenalMind.

Também não fiz uma comparação A/B de desempenho dos agentes usando este módulo. Ele é um exemplo executável de como registro e filtro descobertas, não uma promessa de que a ferramenta encontra sempre a melhor alternativa.

O código foi retirado do **ArsenalMind Kit 2.3.0**. Mantive a licença MIT do kit e os testes originais para permitir a avaliação independente.

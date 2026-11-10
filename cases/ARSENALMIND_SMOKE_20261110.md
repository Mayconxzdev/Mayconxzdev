# ArsenalMind MCP: teste real de aceitação (10/11/2026)

**Origem:** comando local executado no PC autorizado nesta auditoria, usando o script existente de aceitação MCP. A execução não incluiu dados corporativos nem exigiu instalar ferramentas adicionais.

## O que foi executado

O script iniciou o servidor MCP local via Node e enviou requisições JSON-RPC por stdio, incluindo:

- initialize
- tools/list
- tools/call com arsenalmind_plan, usando tarefa genérica sobre um aplicativo Windows para PDFs
- tools/call com arsenalmind_health

## Resultado observado

| Check | Resultado |
| --- | --- |
| Processo do servidor executável | PASS |
| initialize retornou serverInfo.name = arsenalmind | PASS |
| tools/list retornou pelo menos 15 ferramentas | PASS |
| arsenalmind_plan anunciado | PASS |
| arsenalmind_health anunciado | PASS |
| arsenalmind_plan retornou isError = false | PASS |
| arsenalmind_health retornou isError = false | PASS |

**23 ferramentas anunciadas; 7/7 checks PASS.** O processo terminou sem conteúdo relevante em stderr.

**Limites:** este teste comprova conectividade e respostas de algumas ferramentas no runtime local observado. Não prova que cada uma das 23 ferramentas esteja funcional, que o kit inteiro foi testado, que o capability-router esteja ativo em todas as IDEs, que o agente escolheu a melhor skill ou que existem ganhos de desempenho mensurados. A instalação local e suas configurações completas não são publicadas aqui.

## English summary

On November 10, 2026, I ran the existing local MCP acceptance script on the authorised Windows computer. It launched the server over stdio, successfully completed initialize and tools/list, and invoked arsenalmind_plan and arsenalmind_health with successful responses. The script reported **23 listed tools and all 7 checks passing**. This is a directly observed local smoke test, not a public end-to-end benchmark or verification of all agent clients.

[Case PT](ARSENALMIND.md) · [Case EN](ARSENALMIND.en.md) · [Demonstration guide](DEMO_ENTREVISTA.md)

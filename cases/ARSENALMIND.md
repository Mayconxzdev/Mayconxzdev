# ArsenalMind Universal

**Ferramentas MCP, pesquisa de tecnologias e seleção de capacidades para agentes**

[Voltar ao perfil](../README.md) · [English](ARSENALMIND.en.md) · [Desapega AI](DESAPEGA.md)

## Por que fiz

Eu usava Codex e Antigravity para criar coisas muito diferentes e percebia um problema: os agentes tendiam a indicar ferramentas conhecidas mesmo quando talvez já existisse algo mais adequado. Como acompanho repositórios e lançamentos com frequência, queria reunir essa pesquisa em uma ferramenta que eu pudesse usar no dia a dia.

Foi assim que comecei o ArsenalMind. A ideia não era montar um agente que fizesse tudo sozinho, e sim ajudar os agentes que já uso a **descobrir, comparar e selecionar recursos** com mais critério.

## O que construí

A instalação que mantenho em casa reúne módulos que evoluíram em etapas:

- **Servidor MCP:** ferramentas de diagnóstico, descoberta e planejamento acessíveis por clientes compatíveis.
- **Tech Intelligence:** um radar para consultar fontes públicas e manter histórico de descobertas.
- **Solution Scout:** pesquisa repositórios e documentação para montar listas de alternativas relacionadas a uma tarefa.
- **Skills:** instruções reutilizáveis para descoberta, revisão crítica e verificação de entregas.

Separei **encontrar uma ferramenta** de **aprovar seu uso**. O radar pode descobrir um projeto promissor, mas isso não comprova que ele funciona bem ou que pode ser instalado com segurança.

## Onde já usei: Desapega AI

Em 30/10/2026, usei o ArsenalMind na pesquisa técnica do [Desapega AI](DESAPEGA.md), um assistente de revenda que fiz para meu irmão.

Pesquisei alternativas de modelos locais e possibilidades de integração, comparei requisitos e riscos e organizei pontos que precisariam ser testados. A partir daí, trabalhei no Desapega como um projeto próprio, com regras comerciais em código e etapas sujeitas à aprovação do vendedor.

Esse é um exemplo real de **apoio à pesquisa e à decisão técnica**. Não tenho um benchmark mostrando quantas horas o ArsenalMind economizou nem posso dizer que ele escreveu ou colocou o Desapega em produção sozinho.

## Algumas escolhas que fiz

| Escolha | Motivo |
| --- | --- |
| MCP e skills separados | Uma coisa é executar ferramentas; outra é orientar a pesquisa e a revisão. |
| Fontes variadas | Não depender apenas de repositórios populares, mas também não recomendar novidade sem avaliar. |
| Sem auto-instalação dos resultados | Evitar introduzir código desconhecido no computador apenas porque apareceu numa busca. |
| Histórico de descobertas | Conseguir voltar a uma alternativa e entender por que ela foi considerada. |

## Demonstração completa e módulo público

Consigo demonstrar o ArsenalMind completo no meu ambiente local, incluindo descoberta de skills e a apresentação do motivo de selecionar uma ferramenta. O `arsenal-capability-router` diferencia capacidades planejadas, citadas e efetivamente invocadas nos relatórios que vejo durante a execução. **Essa é uma funcionalidade relatada e demonstrável localmente, mas não há uma captura independente de toda a jornada publicada.** Preparei um [roteiro de demonstração com evidências esperadas](DEMO_ENTREVISTA.md), sem expor dados de trabalho ou configurações privadas.

[Teste MCP local observado em 10/11/2026: 7/7 checks, 23 ferramentas anunciadas](ARSENALMIND_SMOKE_20261110.md). O smoke test comprova algumas chamadas do servidor, mas não uma avaliação de qualidade de todos os agentes.

## Um módulo que dá para executar

Publiquei o [Capability Watch](../samples/arsenalmind-capability-watch/README.md), um recorte real do radar com testes offline e instruções para reproduzir. Ele ajuda a entender a parte de coleta e histórico, mas não representa sozinho o ArsenalMind inteiro.

## Estado atual e o que quero validar melhor

Uso o ArsenalMind localmente. A versão doméstica inclui o pacote 2.3.0, com runtime MCP 2.2.1 e módulos adicionais de radar e skills. Existem testes de componentes e registros de integração, mas ainda não publiquei um pacote independente que permita a qualquer pessoa reproduzir todo o fluxo de ponta a ponta.

O próximo teste que quero fazer é simples: dar a mesma tarefa de pesquisa e implementação a um agente **com e sem ArsenalMind**, comparar as escolhas, verificar o resultado final e repetir o experimento. Isso é mais útil do que anunciar que a ferramenta encontrou centenas de repositórios.

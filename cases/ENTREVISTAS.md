# Preparação para entrevistas: experiências verificáveis

Este material organiza **exemplos narrados pelo autor** e links públicos. Não é uma transcrição de entrevista nem um teste de contratação aprovado. Respostas devem preservar o que foi feito, o que é hipótese e o que ainda não foi medido.

## Exemplo 1 — Banco duplicado durante desenvolvimento assistido por IA

**Situação relatada:** um agente criou uma segunda cópia de um banco de dados real, causando duplicação no sistema.

**Ação efetivamente relatada:** comparei a nomenclatura dos arquivos e as datas para identificar a cópia criada posteriormente; utilizei essa investigação para resolver o problema.

**Resultado declarado:** o incidente foi resolvido. Não há, nesta publicação, log, diff ou teste automatizado específico dessa correção.

**O que não devo afirmar:** que executei PRAGMA database_list, que fiz backup restaurável, que criei migrações ou que implementei reconciliação automática. Esses procedimentos seriam boas práticas de verificação, mas não foram confirmados na conversa sobre o incidente.

**Pergunta adversarial:** como provar qual banco a aplicação acessava? A data e o nome são pistas, não substituem inspecionar o caminho de conexão, conteúdo e comportamento da aplicação.

## Exemplo 2 — Implantação em computadores diferentes

**Situação relatada:** máquinas Windows tinham configurações diferentes, gerando necessidades de diagnóstico e adaptação.

**Ação:** investiguei as diferenças e busquei correções para fazer os sistemas funcionarem nos ambientes utilizados.

**Resultado:** participei de instalação e suporte. Não há inventário de falhas, benchmark nem taxa de sucesso publicada para todas as máquinas.

**Pergunta adversarial:** quais diferenças de SO, permissões, rede, dependências ou drivers causaram problemas? Posso explicar um caso concreto ao vivo, sem inventar a causa de todas as máquinas.

## Exemplo 3 — Treinar pessoas no uso do sistema

**Situação relatada:** usuários precisavam aprender a operar ferramentas internas.

**Ação:** expliquei os fluxos, apoiei o uso e ajustei problemas encontrados na rotina.

**Resultado:** treinamento e suporte prestados; tempo economizado e satisfação ainda não foram medidos.

**Pergunta adversarial:** como verificar que o treinamento funcionou? Demonstração de uma tarefa completa, observação dos erros e feedback dos usuários.

## Exemplo 4 — ArsenalMind e transparência

**Problema:** escolher ferramentas recentes para agentes sem depender sempre das mesmas sugestões.

**Solução relatada:** toolkit de pesquisa e MCP com capability-router anunciando capacidades, motivos e distinção entre plano e uso efetivo.

**Evidência pública:** Capability Watch Python com testes offline. Demonstração completa do kit local pode ser feita pelo criador, mas ainda não há um registro público de ponta a ponta.

**Pergunta adversarial:** onde está o recibo de uma chamada real? Mostrar chamada, resultado, data, versão e teste, sem expor dados privados.

## Como apresentar minha relação com IA

Comecei a aprender programação antes de utilizar agentes. Hoje uso IA para acelerar pesquisa e implementação. Consigo explicar a lógica, revisar resultados e investigar problemas, mas certas alterações sem assistência levariam mais tempo. Não devo me apresentar como especialista independente em todas as linguagens, nem omitir a assistência quando ela é relevante.

## Checklist antes de uma entrevista

- Selecionar a versão do currículo adequada à vaga.
- Ter uma demonstração reproduzível com dados sintéticos e testes reais.
- Distinguir experiência própria, coautoria, treinamento e uso real relatado.
- Saber apresentar um incidente com situação, ação e resultado, sem criar métricas.
- Explicar um trecho de código sem depender integralmente do agente.
- Tratar títulos, certificados, domínio de idioma e autorização corporativa com precisão.
- Evitar prometer maturidade sênior de MLOps, SRE, AI Reliability ou Rust apenas por uso em projetos.

[Perfil](../README.md) · [Demonstração do ArsenalMind](DEMO_ENTREVISTA.md)

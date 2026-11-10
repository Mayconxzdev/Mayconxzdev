# ArsenalMind: roteiro de demonstração técnica

Este roteiro é um **procedimento para entrevista**, não uma homologação já realizada por um avaliador externo. O ArsenalMind completo está em uma instalação local privada; o [Capability Watch](../samples/arsenalmind-capability-watch/README.md) é o recorte público reproduzível.

## Cenário: redesenhar um site com pesquisa de ferramentas

**Objetivo:** pedir a um agente para avaliar alternativas de design, incluindo uma ferramenta como ScrollCraft. Mostrar por que uma alternativa foi considerada, o que o agente de fato usou e como foi verificado.

| Passo | O que mostrar | Evidência aceitável |
| --- | --- | --- |
| 1. Ambiente | Cliente, versão do ArsenalMind, projeto demonstrativo e restrições | Captura do setup sem caminhos privados |
| 2. Solicitação | Pedido original e critério de qualidade | Prompt e requisitos registrados |
| 3. Plano | Skills anunciadas, motivo e disponibilidade real | Saída do capability-router distinguindo selecionada/citada |
| 4. Descoberta | Fontes e candidatos considerados, inclusive alternativas descartadas | Consulta do radar e links públicos revisados |
| 5. Chamada | Pelo menos uma execução efetiva do MCP ou da CLI | Resposta real da ferramenta, com hora, status e identificador da chamada |
| 6. Resultado | Artefato, diff e explicação da escolha | Resultado observável em projeto fictício |
| 7. Validação | Teste, comando e retorno real; incluir um caso de falha | Log do teste, exit code, screenshot real quando aplicável |
| 8. Revisão | Erros, limitações e o que faria diferente | Registro do resultado que não transforma falhas em sucesso |

## Perguntas difíceis que o entrevistador pode fazer

**O aviso de que usará a skill prova execução?** Não. O anúncio é intenção. A comprovação requer a chamada e seu retorno. O usuário afirma que o capability-router diferencia essas etapas; esta página ainda não contém recibos de uma sessão específica.

**A ferramenta encontrada foi instalada automaticamente?** Não deve ser. Descoberta, avaliação de segurança, aprovação e execução são etapas separadas.

**Você consegue mostrar o MCP funcionando?** O criador afirma que consegue fazer uma demonstração completa na máquina local. O módulo público não prova, sozinho, a execução do kit inteiro.

**Como validar sem confiar apenas na narrativa do agente?** Conferir o estado anterior e posterior, o diff, o comando de teste, seu resultado e falhas. MCP Inspector pode auxiliar quando a conexão e o runtime estiverem disponíveis.

## Exercícios adversariais

1. Pedido sem correspondência de skill: o agente deve declarar a lacuna, sem fingir que executou algo.
2. Ferramenta com licença inadequada: o radar pode descobrir, mas a seleção deve rejeitar.
3. Chamada com erro: o resultado não pode aparecer como executado com sucesso.
4. Projeto com dados privados: usar fixture sintética; não divulgar diretórios locais, tokens ou nomes de clientes.
5. Mesma tarefa com e sem ArsenalMind: comparar qualidade e tempo usando o mesmo ambiente antes de declarar ganho de desempenho.

## O que já é comprovável publicamente

O Capability Watch oferece script Python e testes offline no repositório. A jornada completa, os recibos do servidor MCP local, a comparação A/B e a segurança de toda a instalação **ainda dependem de evidências adicionais**. O objetivo deste guia é permitir uma demonstração honesta e repetível, não criar resultados fictícios.

[Voltar ao case](ARSENALMIND.md) · [Perfil](../README.md)

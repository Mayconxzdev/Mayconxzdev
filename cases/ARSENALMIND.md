# ArsenalMind Universal — descoberta e avaliação de tecnologias para agentes

**Tipo:** ferramenta pessoal de desenvolvimento e pesquisa.  
**Direção técnica:** MCP, descoberta de capacidades, developer tooling e critérios de verificação.  
**Estado:** módulos locais existentes e testes documentados; **não** é um serviço SaaS nem um agente autônomo universal em produção.

[Voltar ao perfil](../README.md) · [Aplicação relacionada: Desapega AI](DESAPEGA.md) · [Método de evidências](EVIDENCIAS.md)

## Por que foi criado

Ferramentas, skills, modelos e repositórios mudam rapidamente. Eu queria que meus agentes não ficassem limitados a um catálogo antigo, nem escolhessem uma biblioteca só porque já a conheciam.

O ArsenalMind reúne uma camada de ferramentas MCP, skills para pesquisa e revisão crítica e um radar tecnológico para levantar alternativas. Seu propósito é **ajudar na decisão de engenharia**, não instalar automaticamente qualquer novidade.

## O que existe na instalação pessoal

- Runtime MCP em Node para diagnóstico, planejamento e descoberta de ferramentas; teste documentado de inicialização, listagem e chamadas.
- **Tech Intelligence:** radar com registros e histórico local para fontes públicas, incluindo pesquisa em repositórios e documentação.
- **Solution Scout:** busca de candidatos por problema, consulta a README/licenças/metadados e produção de shortlist com ressalvas.
- Skills de descoberta, análise crítica e verificação de entregas, utilizadas como orientação de trabalho com Codex/Antigravity.
- Política de **não confundir descoberta com aprovação**: candidatos são leads até passarem por análise, teste e decisão.

As verificações documentadas são de diferentes datas e camadas. Por exemplo, há testes isolados de MCP e suítes de scripts; o registro de 208 leads em uma execução do radar **não significa 208 soluções testadas**. Configuração em IDE também não comprova uso de todas as funcionalidades em execução ponta a ponta.

## Aplicação concreta: Desapega AI

Em **30/10/2026**, usei as ferramentas MCP do ArsenalMind e scripts de descoberta em pesquisa para o Desapega AI. O registro local `PESQUISA_ARSENALMIND_MODELOS_20261030.md` descreve:

1. Pesquisa de alternativas de modelos locais e integrações de marketplaces.
2. Comparação documental de custos, compatibilidade, licenças e riscos.
3. Identificação de testes necessários em regras de preço, extensão de navegador e confirmação de publicações.
4. Recomendação de validar regras comerciais por código determinístico e manter controles de aprovação humana.

**Escopo da evidência:** o ArsenalMind ajudou a pesquisar e planejar; a implementação do Desapega é um projeto separado. Essa execução não comprova melhoria quantitativa, uso continuado de cada skill em IDE nem homologação de todas as integrações externas.

## Decisões de engenharia

| Decisão | Motivo / trade-off |
| --- | --- |
| MCP e skills separadas | Acesso a ferramentas de execução distinto das instruções de pesquisa. |
| Fontes diversas e alternativas pouco populares | Reduz dependência de rankings, mas aumenta o volume de candidatos irrelevantes. |
| Radar não instala automaticamente | Reduz riscos de supply chain e permissões excessivas. |
| Estados de evidência separados | Resultado de busca não vira afirmação de ferramenta funcional. |
| Plano não é execução | Arquiteturas propostas requerem implementação e testes próprios. |

## Limitações e próximos critérios de comprovação

- Não há benchmark independente demonstrando que a ferramenta melhora qualidade/tempo de entrega em comparação a agentes sem ArsenalMind.
- Parte das integrações foi validada em subprocessos, não em cenários completos dentro de cada IDE.
- A escolha final de bibliotecas ainda depende de revisão humana de licença, riscos e compatibilidade.
- O código integral é local e não está disponibilizado neste repositório; **este estudo de caso não substitui uma demonstração reproduzível**.

**Próxima demonstração ideal:** mesma tarefa de pesquisa e implementação com e sem ArsenalMind, com critérios pré-registrados, ferramentas escolhidas, justificativas, tempo e resultado funcional comparável. Publicar somente fixtures sintéticas, código autorizado e logs sanitizados.

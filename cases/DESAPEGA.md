# Desapega AI — assistente de revenda com IA e regras comerciais

**Tipo:** projeto pessoal para ajudar um familiar que revende produtos.  
**Direção técnica:** IA aplicada, integrações, estado persistente, validação determinística e supervisão humana (*human-in-the-loop*).  
**Estado:** há componentes e testes locais; o vendedor relatou uso para sugestões de revenda e publicação de anúncios. **O mecanismo de publicação externa ainda não foi revalidado de forma independente**.

[Voltar ao perfil](../README.md) · [ArsenalMind e pesquisa técnica](ARSENALMIND.md) · [Método de evidências](EVIDENCIAS.md)

## Problema e usuário

O vendedor precisava transformar fotos e descrições informais em anúncios, obter sugestões e lidar com possíveis negociações sem revelar seu preço mínimo nem assumir compromissos sem aprovação.

O projeto foi pensado para operar com uma conversa simples pelo Telegram e recursos locais no Windows, evitando um painel complexo como requisito para o usuário.

## Componentes presentes no código examinado

| Camada | Responsabilidade |
| --- | --- |
| Interpretação assistida por IA | Apoio na leitura de pedidos e elaboração de sugestões; não é a fonte final de regras de negócio. |
| Regras determinísticas | Validação de preços, restrições de negociação e confirmação de informações. |
| Estado local | SQLite, filas e prevenção de processamento duplicado em cenários documentados. |
| Aprovação humana | Decisões comerciais sensíveis devem depender do vendedor. |
| Integrações | Telegram, extensões e conectores de marketplaces em **estágios diferentes de implementação**. |

## O que foi observado e o que ainda não foi comprovado

- **Código inspecionado:** módulos de segurança comercial e testes de jornada sintética; registros de oito casos marcados como aprovados.
- **Relato do usuário:** o vendedor utilizou o sistema para pedir recomendações e publicar anúncios automaticamente.
- **Documentação de versões:** arquivos mais antigos apontam canais de marketplace ainda assistidos ou bloqueados por autorização; alguns relatórios posteriores afirmam uma automação mais ampla.
- **Pendente:** vincular a publicação relatada à versão/código exatos, verificar logs de confirmação da plataforma sem dados pessoais, confirmar conformidade com as regras de cada serviço e medir impacto real.

Não declaro vendas fechadas, economia de horas ou compatibilidade permanente com OLX/Facebook/Mercado Livre sem registros verificáveis.

## Por que é um trabalho de engenharia

Há uma separação explícita entre **interpretação probabilística** e **execução de ações sujeitas a regras**. Isso permite testar limites de preço, recusas, estados de anúncio e aprovação sem depender apenas do texto gerado pelo modelo.

Há também trabalho de validação de idempotência, falhas e persistência. Os testes registrados **não equivalem à homologação de todas as integrações externas**.

## Relação com ArsenalMind

O ArsenalMind foi utilizado para pesquisar alternativas de modelos locais e mecanismos de integração para o Desapega. O relatório interno datado de 30/10/2026 documenta essa pesquisa; isso é evidência de apoio à decisão, não de que o ArsenalMind publicou anúncios ou escreveu automaticamente todo o sistema.

## Distribuição e privacidade

O código da instalação contém dados privados, arquivos de configuração e informações de sessão. **Não é disponibilizado aqui.** Qualquer demonstração pública deve ser independente, sem tokens, cookies, contas reais, mensagens de compradores ou automação que contorne regras de plataforma.

Um case de uso real tem valor mesmo quando alguns recursos ainda precisam ser homologados — desde que essa distinção seja transparente.

# Desapega AI

**Assistente de revenda que fiz para meu irmão**

[Voltar ao perfil](../README.md) · [English](DESAPEGA.en.md) · [Como o ArsenalMind entrou na pesquisa](ARSENALMIND.md)

## Por que fiz

Meu irmão revende produtos e boa parte do tempo dele ia para pesquisar preço, preparar anúncios e acompanhar interessados. Eu quis facilitar essa rotina sem criar um sistema complicado de usar.

A ideia foi trabalhar por conversa: ele envia informações do produto, pede sugestões de revenda e decide o que quer anunciar. Algumas ações podem ser automatizadas, mas preço mínimo, negociação e fechamento precisam continuar sob controle dele.

## O que desenvolvi

- **Python e SQLite** para manter produtos, estado das conversas e pendências.
- **Telegram** como um dos canais de interação, sem depender de um painel complexo.
- Regras de negócio fora do modelo de IA: limites de preço, condições de pagamento, confirmações e decisões sensíveis.
- Tratamento de mensagens duplicadas, retomada de estado e testes de fluxos com dados fictícios.
- Conectores e automações de navegador para publicação e acompanhamento, desenvolvidos em versões diferentes.

Também usei o [ArsenalMind](ARSENALMIND.md) para pesquisar modelos locais, integração com serviços e riscos antes de definir parte das soluções.

## O que aconteceu na prática

Meu irmão **já usou o sistema para pedir sugestões e publicar anúncios**. Ele relatou publicações automáticas nas plataformas, não apenas textos preparados para copiar.

O projeto, porém, passou por várias versões. Algumas documentações antigas ainda registram publicação assistida ou integrações não homologadas. Antes de apresentar essa publicação automática como funcionalidade estável, preciso relacionar os anúncios à versão exata, ao mecanismo usado e aos retornos das plataformas. Não vou divulgar sessões, mensagens de compradores ou contas para demonstrar isso.

Nos testes locais que examinei, há componentes de validação comercial e cenários de estado e negociação, mas eles não substituem uma homologação de todas as integrações externas.

## Uma decisão importante

Eu não quis deixar o modelo de IA decidir tudo. Ele ajuda a interpretar um pedido ou sugerir um anúncio; as restrições de preço e de negociação precisam ser verificadas por regras explícitas. Se uma ação pode comprometer o vendedor, ela deve exigir confirmação.

## O que ainda falta

Quero consolidar as versões que ficaram espalhadas, revisar integrações e permissões de cada plataforma e medir resultados concretos, como tempo gasto por anúncio ou propostas recebidas. Ainda não tenho esses números organizados e não declaro vendas concluídas automaticamente pelo robô.

O código integral e as configurações da instalação não estão públicos porque existem sessões e dados pessoais envolvidos. Este case descreve o trabalho sem expor essas informações.

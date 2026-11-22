# Movimento de interface

## Inventário e decisão

1. Identifique o fluxo, o gatilho, frequência, elemento, tecnologia, propriedades animadas e comportamento ao interromper. Avalie a experiência em velocidade normal e em repetição rápida.
2. Associe o movimento a feedback, continuidade espacial, orientação ou revelação útil. Simplifique movimentos frequentes e preserve resposta imediata a entradas do usuário.
3. Defina início e fim coerentes com controle e direção. Ajuste duração e curva no componente. Encurte deslocamentos pequenos e teste reversão de estado, mudança de rota, troca rápida de abas e gestos abortados.
4. Use transições interrompíveis para alterações de estado reversíveis. Use keyframes ou API de animação quando a sequência exigir controle independente. Reuse a biblioteca existente quando ela cumprir a tarefa.
5. Preserve conteúdo, status e controles na versão com movimento reduzido. Leia a preferência da plataforma, incluindo `prefers-reduced-motion` na web. Substitua grandes deslocamentos, zoom, parallax e repetições decorativas por resposta imediata ou mudança discreta quando isso fizer sentido.

## Medição e correção

- Em web, comece por `transform` e `opacity` quando mantiverem o layout e o resultado desejados. Confirme composição no perfil. Filtros, máscaras, sombras, mídia grande e camadas demais podem causar pintura ou consumo de memória.
- Compare gravações equivalentes no mesmo dispositivo, taxa de atualização, fluxo e condições. Observe frames longos, trabalho da thread principal, layout e pintura, incluindo interação simultânea. Para estimar orçamento use 1000 ÷ Hz em milissegundos.
- Procure leituras e escritas de layout intercaladas, trabalho por frame no render do framework, listeners frequentes e promoções de camada sem evidência de benefício. Use `will-change` pontualmente e somente com medição que justifique.
- Resolva primeiro atraso em ações críticas, movimento que dificulta uso ou hangs. Em seguida, corrija continuidade, frequência e polimento. Registre antes/depois, comportamento com redução de movimento e itens que exigem dispositivo físico.

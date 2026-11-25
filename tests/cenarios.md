# Cenários de validação

Execute em uma cópia descartável do projeto, com dados fictícios. Os critérios são uma lista de observação. Uma sessão de agente, um teste automatizado e um teste em aparelho físico registram evidências distintas.

| Cenário e entrada | Pedido de teste | Critérios observáveis |
| --- | --- | --- |
| Restaurante institucional novo. Marca fictícia Serra de Sal, cozinha regional, reservas por telefone, horários e cardápio simples. | “Use `criar` para implementar uma página institucional. Priorize consulta ao cardápio.” | O menu tem destino funcional, a ordem de leitura se mantém em 360 e 1280 px e a página usa apenas dados fornecidos. |
| Landing comercial nova. Serviço fictício de manutenção de climatização, formulário local de demonstração. | “Use `criar` para implementar a landing. O formulário precisa ter carregamento, sucesso e erro simulados.” | A oferta e a ação aparecem cedo, os campos têm rótulo, valores sobrevivem ao erro e a simulação é identificável. |
| Dashboard [de amostra](fixtures/pedidos.html). | “Use `melhorar` para facilitar a triagem de pedidos. Preserve o filtro funcional.” | O filtro continua operando com teclado e toque. Layout reflow em 360 px. Registre medidas e console quando disponíveis. |
| App Android de cadastro. Briefing fictício com três campos, carregamento assíncrono e erro recuperável. | “Use `criar` para planejar a tela, sem editar. Inclua primeira execução e recuperação de falha.” | Propõe retorno, insets, exposição de campos com teclado, alvos de toque e testes de TalkBack. Não cria arquivos nem declara teste em aparelho. |
| Site inconsistente. Use o dashboard de amostra com ações conflitantes, largura fixa e contraste baixo. | “Use `auditar` para revisar esta interface e priorizar as falhas da triagem.” | Fornece evidência e prioridade, inclui notas ou NV com justificativa e mantém idênticos o conteúdo, configuração e arquivos do projeto. |
| Excesso de movimento. Use a transição dos filtros no dashboard de amostra. | “Use `animacoes` para corrigir o painel de filtros.” | O painel mantém seu estado em interações rápidas e movimento reduzido. Alterações respeitam a função do filtro. Declara medições de desempenho apenas quando executadas. |

## Variações de controle

- Repita a auditoria com acesso apenas ao briefing. A nota visual fica NV.
- Peça “analise as animações” sem solicitar correções. Compare o estado inicial e final do projeto e confira ausência de escritas.
- Invoque cada modo explicitamente e repita um pedido sem o nome do modo, para observar se a intenção é interpretada corretamente.
- Para testar o instalador em uma pasta temporária, execute `npx skills add /caminho/do/repositorio --list`. Em seguida, execute `npx skills add /caminho/do/repositorio --skill design-profissional --agent codex claude-code --copy --yes` e compare as pastas instaladas com a original.
- Execute o auxiliar opcional com `python3 design-profissional/scripts/contraste.py '#000' '#fff'`. A razão esperada é 21:1.

## Regressões de qualidade comercial

- Em `criar`, forneça domínio de demonstração, depoimentos fictícios e promessas sem fonte. Exija identificação da demonstração, retirada antes da publicação e nenhum testemunho apresentado como real.
- Em `melhorar`, inclua favicon padrão, emojis como ícones, selos, escala de espaçamento inconsistente e teclado que cobre checkout. Exija correção autorizada e evidência em Android e iOS; sem dispositivo, NV.
- Em `auditar`, forneça domínio de plataforma aprovado, logotipo tipográfico intencional, sequência numerada válida e atribuição obrigatória. Não devem ser classificados automaticamente como falhas. Compare os arquivos antes e depois.
- Em qualquer modo, uma avaliação falsa, promessa enganosa, violação de privacidade ou formulário essencial bloqueado impede aprovação; ausência de teste obrigatório resulta em pendência, não em falha inventada.

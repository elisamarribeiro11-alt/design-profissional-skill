---
name: design-profissional
description: Planeje, crie, melhore ou audite o design visual e a experiência de sites, frontends e apps web ou nativos. Use para direção de arte, redesign, design systems, análise de layouts e interfaces, responsividade, acessibilidade, microinterações e otimização de animações de interface.
---

# Design profissional

Conduza o design a partir da tarefa principal do usuário, da identidade do projeto e das condições reais de uso. Use os componentes, ferramentas e convenções disponíveis no projeto.

## Modo e escopo

Aceite `criar`, `melhorar`, `auditar` e `animacoes` como argumentos ou instruções em linguagem natural. Reconheça `animações` como alias. Quando o modo não for explícito, use o verbo e o escopo do pedido. Se houver ambiguidade sobre editar arquivos, faça diagnóstico e proponha o próximo passo.

| Modo | Trabalho | Escrita |
| --- | --- | --- |
| criar | Planejar uma interface nova e construí-la quando solicitado | Edite se o pedido autorizar a criação |
| melhorar | Inspecionar fluxos e código atuais, priorizar gargalos e aplicar melhorias | Edite dentro do escopo solicitado |
| auditar | Investigar a interface e entregar achados, rubrica e recomendações | Mantenha o projeto, as configurações e os arquivos intactos. Entregue o relatório na resposta |
| animacoes | Inventariar, avaliar, implementar ou otimizar movimento | Edite apenas quando o pedido solicitar implementação ou correções de movimento |

Pedidos de planejamento e avaliação são somente leitura. No modo auditar use capturas já disponíveis, inspeção em execução e ferramentas de leitura. Se uma verificação puder gravar arquivos, dados ou disparar efeitos externos, use uma cópia descartável com dados fictícios ou registre a limitação.

## Fluxo de trabalho

1. **Diagnóstico.** Identifique produto, público, tarefa principal, marca, telas, plataforma, stack e restrições. Em projetos existentes, leia os componentes, estilos, tokens, rotas e testes pertinentes. Abra a interface quando possível e registre o fluxo, estado e viewport da evidência inicial. Diferencie fatos observados, hipóteses e dados ausentes. Evite inventar recursos, conteúdo comercial ou métricas.
2. **Planejamento visual.** Leia [os nove princípios](references/principios-design.md) e aplique todos. Defina direção de arte, prioridade do conteúdo e das ações, grid, pontos de quebra guiados pelo conteúdo, escala tipográfica, papéis de cor, espaçamento, componentes e seus estados. Escolha onde o movimento melhora compreensão ou feedback. Relacione cada mudança relevante a uma tarefa, problema ou atributo da marca e defina como verificá-la.
3. **Implementação.** Quando autorizada, aplique mudanças nos pontos de entrada reais. Reuse tokens, componentes e contratos que atendam ao objetivo. Preserve arquitetura, integrações, rotas, dados e comportamentos existentes fora do escopo. Valide fluxos completos, inclusive falhas e recuperação. Restrinja deps novas àquelas com benefício concreto. Em trabalho visual, use a marca e o conteúdo como ponto de partida para composição, fotos, textura ou assimetria. Justifique efeitos como vidro, gradientes, sombras, movimento e cartões pela função ou intenção visual.
4. **Revisão.** Percorra os nove princípios no resultado e use a [rubrica de 14 dimensões](references/auditoria-visual.md) quando houver superfície observável. Registre impacto, evidência e prioridade. Corrija dentro do escopo autorizado. Se não houver acesso à interface, apresente o que foi inspecionado e o que falta observar, sem pontuação visual presumida.
5. **Validação.** Execute os testes aplicáveis do projeto quando disponíveis. Confira viewports estreitas e largas, texto real, zoom, teclado, foco, toque, estados dos fluxos, console e requisições relacionadas. Quando houver movimento, confira redução de movimento e capture um perfil do fluxo na ferramenta disponível. Faça capturas comparáveis no mesmo estado, tamanho e tema quando autorizado. Informe o ambiente, os resultados efetivamente observados e as verificações pendentes. Use evidências de execução para afirmar aprovações.

## Controle obrigatório de qualidade comercial

Nos modos `criar`, `melhorar` e `auditar`, leia e execute integralmente o [checklist dos 11 critérios](references/qualidade-comercial.md), inclusive quando o pedido tiver escopo parcial. Classifique cada critério como conforme, problema, NV ou NA com justificativa e evidência; NV nunca equivale a aprovação. Mapeie os achados à rubrica existente, sem criar dimensões novas. Preserve o modo `auditar` somente leitura: recomende correções e não edite o projeto. Em `criar` e `melhorar`, corrija o que estiver autorizado e registre qualquer problema fora do escopo como pendente.

Antes de considerar concluído, revise desktop e mobile, identidade e formulários aplicáveis; teste Android e iOS com teclado virtual, modais e checkout quando aplicáveis e disponíveis. Registre aparelho ou emulador, ambiente, rota, estado e resultado. Emulação de viewport não prova comportamento do teclado físico. Se não puder testar, registre NV e não declare aprovação global. Achados críticos de avaliações falsas, promessas enganosas, formulários essenciais bloqueados ou violações de privacidade bloqueiam aprovação independentemente da nota.

## Direção de arte premium editorial e cinematográfica

Nos modos `criar`, `melhorar` e `auditar`, avalie obrigatoriamente a adequação desta direção à marca, ao público e à tarefa. Priorize-a em landing pages, portfólios e vitrines quando houver intenção de impacto visual. Não imponha efeitos experimentais a formulários, dashboards ou fluxos transacionais.

- Tipografia expressiva em escala fluida, títulos de grande impacto, contraste de pesos e hierarquia editorial; preserve legibilidade e quebras naturais.
- Composição autoral com grids assimétricos, espaço negativo intencional, imagens em grande escala, sobreposições controladas e alternância de ritmo entre seções. Evite repetição de cartões genéricos, gradientes e ornamentos sem função.
- Direção de arte baseada na identidade real da marca; use fotografias e mídia autorizadas, enquadramento cuidadoso e tratamento visual consistente. Identifique imagens ilustrativas quando necessário.
- Movimento cinematográfico quando pertinente: revelações progressivas, máscaras, transições entre imagens, parallax moderado e microinterações de hover/foco. Cada efeito deve ter finalidade e alternativa estática.
- Preserve rolagem nativa, navegação por teclado, foco, contraste, conteúdo acessível e ações comerciais claras. Respeite prefers-reduced-motion; não dependa de cursor, hover ou animação para acessar conteúdo.
- Adapte a composição ao mobile em vez de apenas reduzir o desktop. Evite cortes de conteúdo, deslocamento horizontal e efeitos que prejudiquem toque ou leitura.
- Prefira CSS e APIs nativas para movimento simples; considere bibliotecas apenas quando justificadas pela complexidade. Priorize transform/opacity, mídia otimizada e carregamento progressivo sem atrasar conteúdo essencial.

**Aplicação por modo:** em criar, defina conceito visual, composição do hero, narrativa de seções e plano de movimento antes de implementar. Em melhorar, compare a interface atual com esse conceito, preserve identidade e fluxos e corrija padrões genéricos dentro do escopo. Em auditar, avalie autoria visual, hierarquia, composição, mídia, movimento e adaptação mobile; registre evidência, impacto e correção proposta na rubrica existente, sem editar. Em animacoes, aplique as mesmas salvaguardas ao movimento solicitado.

**Critérios de aceite:** inspecione desktop e mobile, verifique ausência de conteúdo cortado e scroll horizontal indevido, teste foco/toque e redução de movimento, confirme que CTAs permanecem utilizáveis e que mídia e animações não bloqueiam a navegação. Registre resultados reais e verificações não realizadas. Não copie integralmente layouts de referência nem prometa qualidade visual sem inspeção.

## Referências sob demanda

| Contexto | Recurso |
| --- | --- |
| Fluxos, conteúdo, estados e ações de risco | [UI/UX](references/ui-ux.md) |
| Tokens, componentes e integração com frontend | [Design system](references/design-system.md) |
| Toque, PWA, Android e iOS | [Design mobile](references/mobile-design.md) |
| Modo `animacoes`, gesto, transição ou desempenho de movimento | [Animações](references/animacoes.md) |
| Semântica, teclado, zoom e verificações WCAG | [Acessibilidade](references/acessibilidade.md) |
| Auditoria que precise registrar várias ocorrências | [Modelo de relatório](assets/relatorio-auditoria.md), preenchido na resposta em `auditar` |
| Exemplos de decisões para produtos distintos | [Exemplos práticos](references/exemplos-praticos.md) |

## Entrega

Ao criar ou melhorar, resuma as decisões ligadas ao objetivo, o trabalho realizado, a evidência de validação e as pendências. Em auditorias, ordene achados por impacto na tarefa e indique a correção verificável. Em movimento, informe o elemento, gatilho, função, comportamento com redução de movimento e dados de desempenho observados. Distinga achados de design de falhas técnicas.

# Acessibilidade

Use [WCAG 2.2](https://www.w3.org/TR/WCAG22/) como referência web. Aplique requisitos explicitados pelo projeto. Para apps nativos, combine objetivos de acessibilidade com as APIs e padrões da plataforma.

| Verificação | Método |
| --- | --- |
| Contraste de texto (1.4.3, AA) | Passe 4,5:1 para texto comum e 3:1 para texto grande conforme definição WCAG. Observe exceções normativas, temas, imagens, sobreposições e estados reais. |
| Contraste não textual (1.4.11, AA) | Passe 3:1 em relação a cores adjacentes quando a informação visual for necessária para identificar controles, estados ou partes de gráficos. Verifique exceções normativas. |
| Teclado e foco (2.1.1, 2.4.7, 2.4.11) | Navegue com Tab e Shift+Tab. Acione controles, feche sobreposições e confira foco visível, sequência lógica e retorno. Em AA, confira que conteúdo criado pelo autor não encobre totalmente o item focado. |
| Redimensionamento e reflow (1.4.4, 1.4.10) | Teste texto a 200% e reflow em largura equivalente a 320 CSS px para conteúdo vertical, conforme os critérios. Considere exceções para conteúdo com necessidade de layout bidimensional. |
| Tamanho de alvo (2.5.8, AA) | Verifique 24 × 24 CSS px ou uma exceção aplicável, como espaçamento suficiente. Considere tamanhos maiores para toque frequente. |
| Semântica e feedback | Confira nome, função e valor de controles, rótulos, headings, ordem de leitura, texto alternativo, mensagens de estado e erros de formulário. |
| Movimento | Teste preferência reduzida, controle de movimento automático conforme 2.2.2 e regras sobre flashes. Animação a partir de interações é o critério 2.3.3, nível AAA, com as condições previstas na norma. |

Para pares sólidos sRGB em hexadecimal, o helper opcional `scripts/contraste.py` calcula a razão e classifica os limiares de 3:1 e 4,5:1. Use inspeção do render para superfícies translúcidas, fundos com gradiente ou imagem. Registre conteúdo, estado e par medido. Combine verificação automatizada disponível com uso manual de teclado e tecnologia assistiva. Uma varredura parcial não fundamenta declaração de conformidade.

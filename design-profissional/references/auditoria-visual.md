# Rubrica de revisão

Use 0 a 5 por dimensão observada. Registre rota, estado, viewport, tema e método ou artefato. Para evidência insuficiente, escreva **NV** (não verificado). Use **NA** (não aplicável) quando a dimensão genuinamente não se aplica. Um fluxo sem animação pode ter **NA** após inspeção. Classifique a avaliação como julgamento de design (J), verificação técnica (T) ou combinação (J/T).

| Nota | Âncora observável |
| --- | --- |
| 0 | Falha generalizada ou tarefa essencial bloqueada. |
| 1 | Falhas graves e recorrentes comprometem o fluxo. |
| 2 | O fluxo funciona com atrito relevante ou problemas repetidos. |
| 3 | Atende ao básico no recorte observado, com lacunas localizadas. |
| 4 | Bom resultado no recorte verificado, com ajustes menores identificados. |
| 5 | Atende aos critérios aplicáveis no recorte testado, com evidência representativa suficiente e sem falhas materiais observadas. |

| Dimensão | Tipo | Critério para justificar |
| --- | --- | --- |
| Layout | J/T | Ordem dos blocos, grid, adequação a conteúdo e estabilidade. |
| Alinhamento | J | Eixos, bordas e linhas de base em componentes equivalentes. |
| Hierarquia | J | Reconhecimento da tarefa, da ordem de leitura e da ação principal. |
| Proximidade | J | Associação entre grupos, controles, rótulos e feedback. |
| Equilíbrio | J | Peso visual e densidade a serviço do objetivo. |
| Consistência | J/T | Reuso de papéis, variantes, padrões e estados entre telas. |
| Cores | J | Coerência semântica, adequação a marca, público e tema. |
| Contraste | J/T | Legibilidade, distinção hierárquica e razões aplicáveis de texto e controles. |
| Espaçamento | J/T | Ritmo, separação de grupos, distância interna e aderência à escala. |
| Usabilidade | J/T | Conclusão de tarefa, erros evitados, recuperação e feedback. |
| Responsividade | T | Reflow, largura mínima, zoom, orientação, recortes e controles disponíveis. |
| Acessibilidade | T | Semântica, nomes, teclado, foco, estados e testes disponíveis com tecnologia assistiva. |
| Qualidade das animações | J/T | Propósito, cadência, continuidade, interrupção e movimento reduzido. |
| Desempenho | T | Evidência de medição com ambiente, fluxo e métrica definidos. |

Apresente nota, justificativa e evidência. Em dimensões mistas, explicite que parte foi medida e que parte é julgamento. Evite média quando houver dimensões NV ou NA. Mesmo com dados completos, trate bloqueios como prioritários e mantenha as notas individuais.

## Priorização dos achados

- **P0** para tarefa essencial bloqueada, perda de dados ou barreira grave de acesso.
- **P1** para atrito recorrente que afeta tarefa importante ou grupos de usuários.
- **P2** para ajuste localizado de coerência ou polimento.

Associe cada achado a uma ação proposta e a uma verificação reproduzível. Se a interface não puder ser observada, reporte somente o alcance da revisão de código ou briefing e deixe as dimensões visuais como NV.

## Integração dos 11 critérios

Execute o [checklist comercial](qualidade-comercial.md) em criar, melhorar e auditar. Seus itens mapeiam para as 14 dimensões acima, sem adicionar dimensões nem contar o mesmo problema duas vezes na pontuação. Conteúdo comercial e privacidade exigem achados e bloqueios próprios mesmo quando não houver nota visual pertinente.

A severidade do achado é **Crítico**, **Alto**, **Médio** ou **Baixo**; preserve P0/P1/P2 como prioridade operacional quando útil: Crítico normalmente P0, Alto P1, Médio ou Baixo P2, ajustando ao contexto. Avaliações falsas, promessas enganosas, preenchimento de formulário essencial impedido e violação de privacidade bloqueiam aprovação. NV e NA seguem as regras existentes; NV em verificação obrigatória impede aprovação global.

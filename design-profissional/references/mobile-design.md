# Design mobile

| Superfície | Verificações |
| --- | --- |
| Web/PWA | Veja Safari iOS e Chrome Android conforme o público. Confira safe areas em tela cheia, barras dinâmicas, teclado, rotação, seleção de texto, scroll e gestos nativos. Use unidades dinâmicas de viewport e insets só onde o layout exigir. |
| Android nativo | Adote componentes e comportamento de navegação da stack. Confira retorno do sistema, insets, teclado e escalas de fonte. Use alvos de toque de pelo menos 48 dp como referência do Android. |
| iOS nativo | Confira gesto de retorno, rolagem, áreas seguras, teclado e Dynamic Type. Use 44 × 44 pt como referência prática de área de toque. |

- Garanta que controles fiquem visíveis com teclado aberto, inclusive em formulários, barras fixas e bottom sheets. Teste alcance das ações mais frequentes e regiões de toque separadas.
- Use interação de toque que dispense hover. Em web, preserve zoom e gestos de rolagem do navegador. Limite ajustes de gesto ao componente e forneça alternativa de toque simples e teclado quando pertinente.
- Confira contraste, VoiceOver ou TalkBack, ordem de foco e conteúdo pronunciado em mudanças importantes, conforme o ambiente. Verifique textos longos em escala aumentada.
- Registre o ambiente observado. Diferencie simulação de viewport, emulação, simulador e aparelho físico.

Referências oficiais: [Android](https://developer.android.com/guide/topics/ui/accessibility/apps), [Apple](https://developer.apple.com/design/human-interface-guidelines/accessibility).

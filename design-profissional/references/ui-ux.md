# Fluxos, conteúdo e estados

- Trace a sequência da entrada ao resultado para a ação principal, com rotas de volta e retomada. Organize a navegação por tarefas e use rótulos que descrevam o destino.
- Use controles com função, estado e consequência identificáveis. Ações destrutivas devem ter prevenção proporcional ao custo do erro. Ofereça desfazer quando o sistema suporta reversão confiável.
- Em formulários, rotule os campos, indique restrições antes do envio, preserve valores após erro e associe mensagens aos campos. Valide no momento em que a pessoa pode agir sobre a mensagem.
- Reduza envios duplicados no estado pendente. Mostre o resultado do envio e um próximo passo explícito. Garanta que erros recuperáveis ofereçam nova tentativa.
- Diferencie vazio inicial, filtro sem resultados, erro de carregamento, carregamento e sucesso. Mantenha altura e posição estáveis quando isso evita saltos e perda de contexto.
- Verifique textos longos, valores extremos, nomes reais, estados sem permissão e indisponibilidade relevante. Use conteúdo fictício identificado só em protótipos ou testes.
- Teste o fluxo de ponta a ponta. Verifique teclado e foco em menus, diálogos e ações críticas. Confirme a resposta do sistema, não apenas a alteração de aparência do botão.

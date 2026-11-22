# Design system e frontend

1. Inventarie componentes e estilos já utilizados. Agrupe diferenças por função e anote onde a aparência representa comportamento, estado ou hierarquia.
2. Exponha tokens por papel no mecanismo já usado pelo projeto, como CSS, tema do framework ou recursos nativos. Comece por superfícies, texto, borda, foco, marca e estados semânticos. Inclua escalas de tipo, espaçamento e formas apenas conforme houver repetição.
3. Para tipografia, escolha família, peso, altura de linha e largura de leitura com amostras reais. Confira acentos, números, quebras, fonte de fallback e estabilidade durante carregamento. Use variação expressiva onde a marca pede.
4. Modele variantes e estados por intenção. Exemplo: ação principal, secundária e destrutiva com estados normal, foco, pressionado, desabilitado e pendente, conforme aplicáveis.
5. Em projetos legados, migre primeiro os componentes do fluxo em escopo. Preserve APIs e contratos quando possível e verifique outros consumidores antes de tocar tokens globais.
6. Teste componentes em contexto, com temas existentes, textos extensos e densidades representativas. Use imagem ou ícone quando a representação tiver função clara. Preserve a identificação pelos rótulos quando a iconografia for ambígua.
7. Preserve a responsividade do conteúdo. Use colunas fluidas e pontos de quebra onde leitura ou manipulação degradarem. Em tabelas, permita rolagem deliberada ou mude a apresentação preservando cabeçalhos, dados e ações.

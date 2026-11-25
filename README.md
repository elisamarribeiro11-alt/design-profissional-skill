# Design Profissional

Versão 1.1.0.

Skill de direção de arte, UI/UX e engenharia de frontend para Codex e Claude Code. Planeja, cria e melhora interfaces com base na tarefa do usuário, na marca e nas restrições do projeto. Audita o resultado com nove princípios de design e uma rubrica de 14 dimensões.

Funciona com HTML/CSS/JS, React, Vue, Svelte, frameworks web, PWA, React Native, Flutter, SwiftUI, Android nativo e outras stacks de interface. A execução e os testes dependem das ferramentas do projeto.

## Instalação

No terminal e na raiz do projeto, use o [instalador de skills](https://github.com/vercel-labs/skills):

```bash
npx skills add elisamarribeiro11-alt/design-profissional-skill --skill design-profissional --agent codex claude-code --copy --yes
```

O comando instala a skill no projeto. Para listar o conteúdo antes de instalar, execute:

```bash
npx skills add elisamarribeiro11-alt/design-profissional-skill --list
```

Para instalação manual, copie a pasta [design-profissional](design-profissional/) inteira para `.agents/skills/` no Codex ou `.claude/skills/` no Claude Code. No Codex Cloud, mantenha a cópia em `.agents/skills/design-profissional/` na revisão do projeto que a tarefa vai usar, quando a descoberta de skills do repositório estiver disponível.

## Modos

| Modo | Claude Code | Codex | O que faz |
| --- | --- | --- | --- |
| Criar | `/design-profissional criar` | `$design-profissional criar` | Define direção visual e implementa uma interface nova quando solicitado. |
| Melhorar | `/design-profissional melhorar` | `$design-profissional melhorar` | Investiga a interface e aplica melhorias dentro do escopo. |
| Auditar | `/design-profissional auditar` | `$design-profissional auditar` | Entrega achados com evidência e rubrica, em modo somente leitura. |
| Animações | `/design-profissional animacoes` | `$design-profissional animacoes` | Avalia movimento e aplica correções quando solicitado. |

Acrescente o pedido após o modo. Em ambientes que não expõem atalhos, escreva em linguagem natural, por exemplo: “Use a skill design-profissional no modo auditar para revisar o fluxo de filtros deste dashboard”.

## Prompts

- “Crie a página de um restaurante regional com cardápio e localização. Use a marca e as fotos disponíveis no projeto.”
- “Melhore o formulário desta landing page. Preserve o endpoint e teste envio, erro e sucesso.”
- “Audite o dashboard em 360 e 1280 px. Priorize os problemas que atrasam o atendimento e cite a evidência de cada nota.”
- “Otimize as animações dos filtros. Confira cliques rápidos, movimento reduzido e o tempo de quadro no ambiente disponível.”

## Controle de qualidade comercial

Nos modos criar, melhorar e auditar, a skill verifica 11 critérios de identidade, domínio, conteúdo comercial, privacidade e formulários. As verificações se integram à rubrica de 14 dimensões; fatos não verificados permanecem pendentes. Avaliações falsas, promessas enganosas, violações de privacidade e formulários essenciais bloqueados impedem aprovação. O modo auditar permanece somente leitura.

Execute as verificações estruturais com `python3 -m unittest discover -s tests -v`. Elas verificam a presença das regras e não substituem a avaliação do comportamento do agente nem testes reais em Android e iOS.

## Limitações

- A skill orienta o agente por meio de instruções. A seleção automática e o acesso a navegador, simulador, aparelho e ferramentas de teste dependem do ambiente.
- Sem interface observável, a auditoria registra o alcance da revisão e deixa notas visuais pendentes.
- O script opcional de contraste usa Python 3.9+ e avalia somente cores sólidas sRGB. A skill funciona sem Python.
- Os [cenários reproduzíveis](tests/cenarios.md) definem os fluxos, os sinais esperados e as evidências a coletar.

## Créditos e licença

O conteúdo original é disponibilizado sob [licença MIT](LICENSE). O [levantamento de referências](REFERENCIAS.md) documenta as fontes consultadas, os conceitos aproveitados e as decisões de integração. A distribuição contém instruções, exemplos e código originais.

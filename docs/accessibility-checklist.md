# Checklist de Acessibilidade — valber-lab

Baseado nas diretrizes WCAG 2.1 (nível AA).

---

## Percepção

- [ ] Todas as imagens têm texto alternativo (`alt`) descritivo
- [ ] Gráficos e visualizações têm descrição textual complementar (callout ou legenda)
- [ ] O contraste de texto sobre fundo é de pelo menos 4.5:1 (texto normal) e 3:1 (texto grande)
- [ ] Informações não são transmitidas apenas por cor (usa-se também forma, texto ou ícone)
- [ ] Tabelas têm cabeçalhos (`<th>`) corretamente definidos
- [ ] Não há conteúdo piscante ou animações que possam causar convulsões

## Operabilidade

- [ ] Toda funcionalidade é acessível por teclado (Tab, Enter, Espaço, Esc)
- [ ] O foco do teclado é visível em todos os elementos interativos
- [ ] Não há armadilhas de foco (o usuário consegue sair de qualquer componente com teclado)
- [ ] Links de salto ("pular para o conteúdo") estão disponíveis
- [ ] O tempo de sessão, se houver, pode ser estendido

## Compreensibilidade

- [ ] O idioma da página está declarado (`lang="pt-BR"` no HTML)
- [ ] Links são descritivos (não use "clique aqui" ou "leia mais" sem contexto)
- [ ] Formulários têm rótulos (`<label>`) associados aos campos
- [ ] Mensagens de erro são claras e indicam como corrigir o problema
- [ ] A linguagem é clara e acessível ao público-alvo (professores, estudantes, profissionais)

## Robustez

- [ ] O HTML é válido e bem formado
- [ ] Componentes de interface têm nome, papel e valor acessíveis (ARIA quando necessário)
- [ ] O site funciona em leitores de tela (testado com NVDA ou VoiceOver)
- [ ] O site funciona com zoom de até 200% sem perda de funcionalidade

## Responsividade e dispositivos móveis

- [ ] O layout é responsivo e funciona em telas pequenas (320px+)
- [ ] Elementos interativos têm área de toque de pelo menos 44×44 px
- [ ] Texto pode ser aumentado sem quebrar o layout

---

## Ferramentas de verificação recomendadas

- [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/)
- [axe DevTools](https://www.deque.com/axe/) — extensão de navegador
- Lighthouse (Google Chrome DevTools) — aba Accessibility
- [Colour Contrast Checker](https://colourcontrast.cc/)

---

*Este checklist deve ser revisado a cada versão significativa do site.*

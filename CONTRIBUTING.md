# Guia de Contribuição — valber-lab

Obrigado pelo interesse em contribuir com o Laboratório de Direito, Economia e Tecnologia!

---

## Como contribuir

### 1. Reportando erros

Se você encontrou um erro técnico, conceitual ou metodológico:

1. Verifique se já existe uma [issue aberta](https://github.com/valbergregory/valber-lab/issues) sobre o problema
2. Se não existir, abra uma nova issue usando o template adequado
3. Descreva claramente o problema, onde ele está e o que deveria ser diferente

### 2. Sugestões de melhoria

Abra uma issue com o título `[sugestão] Descrição breve`.

### 3. Contribuindo com código ou conteúdo

1. Faça um fork do repositório
2. Crie uma branch com nome descritivo: `git checkout -b feat/nome-da-contribuicao`
3. Faça suas alterações com commits claros
4. Abra um Pull Request para a branch `main`

---

## Padrão de branches

| Prefixo | Uso |
|---------|-----|
| `feat/` | Nova funcionalidade ou conteúdo |
| `fix/` | Correção de erro |
| `docs/` | Documentação |
| `test/` | Testes |
| `chore/` | Tarefas de manutenção |

Exemplo: `feat/laboratorio-sql`, `fix/link-quebrado-projetos`

---

## Padrão de commits (Conventional Commits)

Use o padrão:

```
tipo: descrição curta em minúsculas (máx. 72 caracteres)

[opcional: corpo do commit com mais detalhes]
```

Tipos válidos:
- `feat` — novo conteúdo ou funcionalidade
- `fix` — correção de erro
- `docs` — documentação
- `test` — testes
- `ci` — configuração de CI/CD
- `chore` — manutenção geral
- `style` — formatação, sem mudança de lógica

Exemplos:
```
feat: adicionar análise de dados em painel ao laboratório R
fix: corrigir link quebrado na página de projetos
docs: atualizar instruções de instalação no README
```

---

## Organização de código

- Código Python deve seguir PEP 8
- Código R deve seguir o style guide do tidyverse (snake_case, espaços antes de `<-`)
- Arquivos Quarto devem ter frontmatter YAML completo (título, descrição, data se for post)
- Dados simulados devem incluir `set.seed()` (R) ou `np.random.seed()` (Python)

---

## Proteção de dados

**Não inclua:**
- Dados pessoais identificáveis (CPF, nome, endereço, e-mail de terceiros)
- Dados de processos judiciais sigilosos
- Notas, frequências ou informações acadêmicas de alunos
- Informações internas de instituições públicas

**Se precisar usar dados reais:**
- Anonymize antes de incluir
- Use apenas dados de domínio público
- Documente a fonte

---

## Reprodutibilidade

Toda análise ou exemplo de código deve:

- Ser executável após `git clone` e instalação das dependências
- Incluir `set.seed()` ou equivalente para resultados determinísticos
- Ter as dependências documentadas em `requirements.txt` ou `renv.lock`
- Funcionar no GitHub Actions

---

## Pull Requests

- PRs devem ser direcionados à branch `main`
- Descreva claramente o que foi alterado e por quê
- Certifique-se de que os testes passam (`pytest tests/ -v`)
- Mantenha o escopo do PR focado — um PR por funcionalidade ou correção

---

## Licença das contribuições

Ao contribuir com código, você concorda que sua contribuição será licenciada sob a [MIT License](LICENSE).

Textos e materiais acadêmicos têm condições específicas descritas na [Política de Uso](privacidade.qmd).

# Laboratório de Direito, Economia e Tecnologia

[![GitHub Pages](https://github.com/valbergregory/valber-lab/actions/workflows/publish.yml/badge.svg)](https://github.com/valbergregory/valber-lab/actions/workflows/publish.yml)
[![Verificações](https://github.com/valbergregory/valber-lab/actions/workflows/checks.yml/badge.svg)](https://github.com/valbergregory/valber-lab/actions/workflows/checks.yml)
[![Licença: MIT](https://img.shields.io/badge/Licença-MIT-blue.svg)](LICENSE)
[![Quarto](https://img.shields.io/badge/Quarto-1.4+-blue?logo=quarto)](https://quarto.org)
[![Python](https://img.shields.io/badge/Python-3.11+-yellow?logo=python)](https://python.org)
[![R](https://img.shields.io/badge/R-4.3+-blue?logo=r)](https://www.r-project.org)

**Portfólio acadêmico e tecnológico de Valber Gregory Barbosa Costa Bezerra Santos**

Professor · UFAL Penedo · Analista Judiciário · Doutor em Economia

> *Direito, Economia e Tecnologia aplicados à pesquisa, ao ensino e à solução de problemas públicos e sociais.*

🌐 **Site:** https://valbergregory.github.io/valber-lab

---

## Sobre

Este repositório documenta uma trajetória de aprendizagem progressiva em análise de dados, econometria, programação e desenvolvimento de sistemas — aplicados às áreas de Direito, Economia e Administração Pública.

**Não é um portfólio de projetos prontos.** É um laboratório em funcionamento, com projetos em diferentes estágios, exemplos didáticos e reflexões sobre a prática de pesquisa reproduzível.

**In English:** This is the academic and technology portfolio of Valber Gregory (Professor at UFAL · PhD in Economics · Judicial Analyst). It documents an interdisciplinary learning track combining Law, Economics, Data Analysis, and Information Systems — with 18 planned projects from August 2026 to July 2027. Content is primarily in Portuguese.

---

## Demonstração

> Captura de tela será inserida após a primeira publicação no GitHub Pages.
> Visualize localmente com `quarto preview` após a instalação.

---

## Tecnologias

| Ferramenta | Uso |
|-----------|-----|
| [Quarto](https://quarto.org) | Site, documentos reproduzíveis |
| R | Análise estatística, econometria |
| Python | Análise de dados, APIs, automação |
| SQL | Bancos de dados, dados públicos |
| C++ | Métodos numéricos, algoritmos |
| Java | Sistemas, orientação a objetos |
| GitHub Actions | CI/CD, publicação automatizada |
| GitHub Pages | Hospedagem do site |

---

## Estrutura

```
valber-lab/
├── _quarto.yml              # Configuração do site Quarto
├── index.qmd                # Página inicial
├── sobre.qmd                # Sobre o autor
├── projetos.qmd             # Trilha de 18 projetos
├── trilha.qmd               # Planejamento mensal
├── pesquisa.qmd             # Linhas de pesquisa
├── ensino.qmd               # Materiais didáticos
├── publicacoes.qmd          # Publicações acadêmicas
├── contato.qmd              # Contato
├── privacidade.qmd          # Política de uso
├── styles.css               # CSS personalizado
├── requirements.txt         # Dependências Python
├── labs/
│   ├── r/                   # Laboratório R
│   ├── python/              # Laboratório Python
│   ├── sql/                 # Laboratório SQL
│   ├── cpp/                 # Laboratório C++
│   └── java/                # Laboratório Java
├── posts/                   # Diário de evolução (blog)
├── data/                    # Dados (raw e processed)
├── assets/                  # Imagens e ícones
├── scripts/                 # Scripts auxiliares
├── tests/                   # Testes com pytest
├── docs/                    # Documentação adicional
└── .github/workflows/       # GitHub Actions
```

---

## Instalação e execução local

### Pré-requisitos

- [Quarto](https://quarto.org/docs/get-started/) ≥ 1.4
- Python ≥ 3.11
- R ≥ 4.3 (opcional — usado nos laboratórios R)
- Git

### 1. Clonar o repositório

```bash
git clone https://github.com/valbergregory/valber-lab.git
cd valber-lab
```

### 2. Criar e ativar ambiente Python

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar (Linux/macOS)
source venv/bin/activate

# Ativar (Windows)
venv\Scripts\activate
```

### 3. Instalar dependências Python

```bash
pip install -r requirements.txt
```

### 4. Restaurar ambiente R (opcional)

```r
# No R ou RStudio:
install.packages("renv")
renv::restore()
```

Se `renv.lock` não estiver disponível, instale os pacotes manualmente:

```r
install.packages(c("ggplot2", "dplyr", "broom", "knitr", "scales"))
```

### 5. Visualizar o site localmente

```bash
quarto preview
```

O site abrirá em `http://localhost:4321`.

---

## Renderização

```bash
# Renderizar o site completo
quarto render

# Renderizar uma página específica
quarto render index.qmd

# Usar o script auxiliar
bash scripts/render_site.sh
```

O site será gerado em `_site/`.

---

## Testes

```bash
# Executar todos os testes
pytest tests/ -v

# Verificar estrutura do projeto
python scripts/check_project.py

# Teste rápido de um módulo
pytest tests/test_structure.py::test_exemplo_python_analise_financeira -v
```

---

## Publicação no GitHub Pages

A publicação é automática via GitHub Actions:

1. Qualquer push na branch `main` dispara o workflow `publish.yml`
2. O Quarto é instalado e renderiza o site no runner
3. O site é publicado diretamente no GitHub Pages via `actions/deploy-pages`
4. **A pasta `_site` não é commitada na branch principal**

Para publicação manual:

```bash
# Na interface GitHub: Actions → "Publicar no GitHub Pages" → Run workflow
```

---

## Configuração inicial do GitHub Pages

Após criar o repositório no GitHub:

1. Vá em **Settings → Pages**
2. Em "Source", selecione **GitHub Actions**
3. Faça um push na branch `main`
4. O workflow publicará o site automaticamente

URL resultante: `https://valbergregory.github.io/valber-lab/`

---

## Comandos de manutenção

```bash
# Verificar estado do repositório
git status

# Criar nova postagem no diário
mkdir posts/YYYY-MM-DD-titulo && touch posts/YYYY-MM-DD-titulo/index.qmd

# Atualizar dependências Python
pip install --upgrade -r requirements.txt

# Verificar estrutura após alterações
python scripts/check_project.py

# Reverter a última alteração (antes do push)
git revert HEAD

# Reverter a um commit específico
git log --oneline  # encontrar o hash
git revert <hash>
```

---

## Contribuição

Veja [CONTRIBUTING.md](CONTRIBUTING.md) para o guia completo.

```bash
# Fork → clone → nova branch → alterações → PR
git checkout -b feat/minha-contribuicao
git commit -m "feat: descrição da contribuição"
git push origin feat/minha-contribuicao
# Abrir Pull Request no GitHub
```

---

## Licença

O **código-fonte** deste projeto está sob a [Licença MIT](LICENSE).

**Textos, análises, tutoriais e materiais acadêmicos** têm condições específicas de uso — consulte a [Política de Uso e Privacidade](https://valbergregory.github.io/valber-lab/privacidade.html). Se utilizar conteúdo deste laboratório em pesquisas, cite adequadamente:

```
SANTOS, Valber Gregory Barbosa Costa Bezerra. Laboratório de Direito,
Economia e Tecnologia. Penedo: UFAL, 2026. Disponível em:
https://valbergregory.github.io/valber-lab. Acesso em: [data].
```

---

## Contato

- **GitHub:** [github.com/valbergregory](https://github.com/valbergregory)
- **E-mail institucional:** *[a inserir]*
- **Lattes:** *[link a inserir]*
- **Instituição:** UFAL — Unidade Educacional de Penedo · Curso de Sistemas de Informação

---

## Segurança

Para reportar vulnerabilidades, consulte [SECURITY.md](SECURITY.md).

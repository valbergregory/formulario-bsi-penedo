# Changelog

Todas as mudanças notáveis deste projeto são documentadas aqui.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/)
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

---

## [0.1.0] — 2026-08-01

### Adicionado
- Estrutura inicial do projeto Quarto website
- Páginas institucionais: Início, Sobre, Projetos, Trilha, Pesquisa, Ensino, Publicações, Contato, Privacidade
- Laboratório R: índice, estatística descritiva, regressão linear
- Laboratório Python: índice, tratamento de dados, análise financeira
- Laboratório SQL: índice com exemplos introdutórios
- Laboratório C++: índice com exemplos de métodos numéricos
- Laboratório Java: índice com orientação a objetos e exemplos jurídicos
- Diário de Evolução: três postagens iniciais (agosto 2026)
- GitHub Actions: workflows de verificação (checks.yml) e publicação (publish.yml)
- Testes com pytest: `tests/test_structure.py`
- Script de verificação: `scripts/check_project.py`
- Script de renderização: `scripts/render_site.sh`
- Documentação: README.md, CONTRIBUTING.md, SECURITY.md, LICENSE
- Checklist de acessibilidade: `docs/accessibility-checklist.md`
- Arquivos de configuração: `.gitignore`, `requirements.txt`
- Identidade visual: `styles.css` com suporte a modo claro e escuro
- Templates de issues e pull request

### Infraestrutura
- GitHub Pages configurado via GitHub Actions (não commit da pasta `_site`)
- `freeze: auto` para análises R e Python
- Suporte a dark mode via Quarto (temas cosmo/darkly)

---

## [Não lançado]

### Planejado para versões futuras
- Módulo SQL para Pesquisadores (setembro 2026)
- Painel de Indicadores Econômicos Municipais (outubro 2026)
- Laboratório de Econometria Aplicada (outubro 2026)
- Exemplos R com dados reais (IBGE, IPEA)
- Versão expandida em inglês
- Integração com Plataforma Lattes

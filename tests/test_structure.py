"""
test_structure.py — Testes de estrutura do projeto valber-lab

Verifica a existência de arquivos e diretórios obrigatórios,
e a sintaxe básica dos arquivos principais.

Uso:
    pytest tests/ -v
"""

import os
import re
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def caminho(*partes):
    return os.path.join(ROOT, *partes)


# ── Arquivos obrigatórios ──────────────────────────────────────────────────

ARQUIVOS_OBRIGATORIOS = [
    "_quarto.yml",
    "index.qmd",
    "sobre.qmd",
    "projetos.qmd",
    "trilha.qmd",
    "pesquisa.qmd",
    "ensino.qmd",
    "publicacoes.qmd",
    "contato.qmd",
    "privacidade.qmd",
    "styles.css",
    "requirements.txt",
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    ".gitignore",
    "SECURITY.md",
]

PAGINAS_LABORATORIO = [
    "labs/r/index.qmd",
    "labs/r/estatistica-descritiva.qmd",
    "labs/r/regressao-linear.qmd",
    "labs/python/index.qmd",
    "labs/python/tratamento-dados.qmd",
    "labs/python/analise-financeira.qmd",
    "labs/sql/index.qmd",
    "labs/cpp/index.qmd",
    "labs/java/index.qmd",
]

POSTS = [
    "posts/index.qmd",
    "posts/_metadata.yml",
    "posts/2026-08-01-criacao-laboratorio/index.qmd",
    "posts/2026-08-08-trilha-linguagens/index.qmd",
    "posts/2026-08-15-projetos-reproduziveis/index.qmd",
]

WORKFLOWS = [
    ".github/workflows/publish.yml",
    ".github/workflows/checks.yml",
]

SCRIPTS = [
    "scripts/check_project.py",
    "scripts/render_site.sh",
]

DIRETORIOS = [
    "labs/r",
    "labs/python",
    "labs/sql",
    "labs/cpp",
    "labs/java",
    "posts",
    "scripts",
    "tests",
    "assets",
    "data",
    ".github/workflows",
]


@pytest.mark.parametrize("arquivo", ARQUIVOS_OBRIGATORIOS)
def test_arquivo_obrigatorio_existe(arquivo):
    assert os.path.isfile(caminho(arquivo)), f"Arquivo obrigatório ausente: {arquivo}"


@pytest.mark.parametrize("pagina", PAGINAS_LABORATORIO)
def test_pagina_laboratorio_existe(pagina):
    assert os.path.isfile(caminho(pagina)), f"Página de laboratório ausente: {pagina}"


@pytest.mark.parametrize("post", POSTS)
def test_post_existe(post):
    assert os.path.isfile(caminho(post)), f"Post ausente: {post}"


@pytest.mark.parametrize("workflow", WORKFLOWS)
def test_workflow_existe(workflow):
    assert os.path.isfile(caminho(workflow)), f"Workflow ausente: {workflow}"


@pytest.mark.parametrize("script", SCRIPTS)
def test_script_existe(script):
    assert os.path.isfile(caminho(script)), f"Script ausente: {script}"


@pytest.mark.parametrize("diretorio", DIRETORIOS)
def test_diretorio_existe(diretorio):
    assert os.path.isdir(caminho(diretorio)), f"Diretório ausente: {diretorio}/"


# ── Conteúdo dos arquivos principais ─────────────────────────────────────

def test_quarto_yml_tem_title():
    with open(caminho("_quarto.yml")) as f:
        conteudo = f.read()
    assert "title:" in conteudo, "_quarto.yml deve conter 'title:'"
    assert "website" in conteudo, "_quarto.yml deve conter 'website'"


def test_index_tem_conteudo_minimo():
    with open(caminho("index.qmd")) as f:
        conteudo = f.read()
    assert "Valber" in conteudo, "index.qmd deve mencionar o autor"
    assert "Laboratório" in conteudo, "index.qmd deve mencionar o laboratório"


def test_sobre_tem_secoes():
    with open(caminho("sobre.qmd")) as f:
        conteudo = f.read()
    assert "Formação" in conteudo or "formação" in conteudo.lower()
    assert "Pesquisa" in conteudo or "pesquisa" in conteudo.lower()


def test_projetos_tem_18_projetos():
    with open(caminho("projetos.qmd")) as f:
        conteudo = f.read()
    # Verifica que os projetos principais estão listados
    projetos_esperados = [
        "SQL para Pesquisadores",
        "Painel de Indicadores",
        "Econometria",
        "Analisador Financeiro",
        "Calculadora de Prazos",
    ]
    for p in projetos_esperados:
        assert p in conteudo, f"Projeto '{p}' não encontrado em projetos.qmd"


def test_trilha_tem_meses():
    with open(caminho("trilha.qmd")) as f:
        conteudo = f.read()
    meses = ["Agosto 2026", "Setembro 2026", "Outubro 2026", "Novembro 2026"]
    for mes in meses:
        assert mes in conteudo, f"Mês '{mes}' não encontrado na trilha"


def test_requirements_nao_vazio():
    with open(caminho("requirements.txt")) as f:
        linhas = [l.strip() for l in f if l.strip() and not l.startswith("#")]
    assert len(linhas) > 0, "requirements.txt deve ter pelo menos uma dependência"


def test_gitignore_exclui_venv():
    with open(caminho(".gitignore")) as f:
        conteudo = f.read()
    assert "venv" in conteudo or ".venv" in conteudo, ".gitignore deve excluir ambientes virtuais"


def test_gitignore_exclui_env():
    with open(caminho(".gitignore")) as f:
        conteudo = f.read()
    assert ".env" in conteudo, ".gitignore deve excluir arquivos .env"


def test_readme_tem_secoes_principais():
    with open(caminho("README.md")) as f:
        conteudo = f.read()
    secoes = ["Instalação", "Renderiz", "GitHub Pages", "Licença"]
    for s in secoes:
        assert s in conteudo or s.lower() in conteudo.lower(), \
            f"README.md deve conter seção '{s}'"


def test_sem_credenciais_obvias():
    padroes = [
        re.compile(r"ghp_[A-Za-z0-9]{36}"),
        re.compile(r"sk-[A-Za-z0-9]{32,}"),
        re.compile(r"password\s*=\s*['\"][^'\"]{4,}['\"]", re.IGNORECASE),
    ]
    extensoes = {".py", ".r", ".qmd", ".md", ".yml", ".yaml", ".txt"}
    skip_dirs = {"venv", ".venv", "_site", "__pycache__", ".git"}

    for dirpath, dirs, filenames in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for fname in filenames:
            if os.path.splitext(fname)[1].lower() not in extensoes:
                continue
            fpath = os.path.join(dirpath, fname)
            with open(fpath, encoding="utf-8", errors="ignore") as f:
                conteudo = f.read()
            for padrao in padroes:
                match = padrao.search(conteudo)
                assert not match, \
                    f"Possível credencial em {os.path.relpath(fpath, ROOT)}: '{match.group()}'"


def test_posts_tem_frontmatter():
    posts_qmd = [
        "posts/2026-08-01-criacao-laboratorio/index.qmd",
        "posts/2026-08-08-trilha-linguagens/index.qmd",
        "posts/2026-08-15-projetos-reproduziveis/index.qmd",
    ]
    for post in posts_qmd:
        with open(caminho(post)) as f:
            conteudo = f.read()
        assert "title:" in conteudo, f"{post} deve ter 'title:' no frontmatter"
        assert "date:" in conteudo, f"{post} deve ter 'date:' no frontmatter"


# ── Verificação dos exemplos Python ──────────────────────────────────────

def test_exemplo_python_dataframe():
    """Verifica que o exemplo de tratamento de dados Python executa sem erro."""
    import pandas as pd
    import numpy as np

    np.random.seed(42)
    n = 20
    df = pd.DataFrame({
        "id":     range(1, n + 1),
        "valor":  np.random.uniform(100, 1000, n).round(2),
        "tipo":   np.random.choice(["A", "B", "C"], n),
    })
    df.loc[0, "valor"] = np.nan

    # Tratamento
    df["valor"] = df["valor"].fillna(df["valor"].median())

    assert df["valor"].isna().sum() == 0
    assert len(df) == n


def test_exemplo_python_analise_financeira():
    """Verifica o cálculo dos indicadores financeiros."""
    import pandas as pd

    dados = {
        "empresa":          ["Teste S.A."],
        "ativo_circulante": [200.0],
        "estoques":         [50.0],
        "passivo_circulante": [100.0],
        "passivo_total":    [150.0],
        "ativo_total":      [400.0],
        "receita_liquida":  [500.0],
        "lucro_liquido":    [50.0],
        "patrim_liquido":   [250.0],
    }
    df = pd.DataFrame(dados)

    df["liq_corrente"] = df["ativo_circulante"] / df["passivo_circulante"]
    df["liq_seca"]     = (df["ativo_circulante"] - df["estoques"]) / df["passivo_circulante"]
    df["margem_liq"]   = df["lucro_liquido"] / df["receita_liquida"] * 100
    df["endividamento"] = df["passivo_total"] / df["ativo_total"] * 100

    assert df["liq_corrente"].iloc[0] == pytest.approx(2.0, rel=1e-3)
    assert df["liq_seca"].iloc[0] == pytest.approx(1.5, rel=1e-3)
    assert df["margem_liq"].iloc[0] == pytest.approx(10.0, rel=1e-3)
    assert df["endividamento"].iloc[0] == pytest.approx(37.5, rel=1e-3)

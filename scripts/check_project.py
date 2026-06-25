#!/usr/bin/env python3
"""
check_project.py — Verificação da estrutura do projeto valber-lab

Verifica:
- Existência dos arquivos essenciais
- Existência dos diretórios obrigatórios
- Links internos simples em arquivos .qmd e .md
- Ausência de credenciais óbvias

Uso:
    python scripts/check_project.py

Retorna 0 se tudo estiver correto; 1 se houver problemas críticos.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
    "labs/r/index.qmd",
    "labs/r/estatistica-descritiva.qmd",
    "labs/r/regressao-linear.qmd",
    "labs/python/index.qmd",
    "labs/python/tratamento-dados.qmd",
    "labs/python/analise-financeira.qmd",
    "labs/sql/index.qmd",
    "labs/cpp/index.qmd",
    "labs/java/index.qmd",
    "posts/index.qmd",
    "posts/_metadata.yml",
    "posts/2026-08-01-criacao-laboratorio/index.qmd",
    "posts/2026-08-08-trilha-linguagens/index.qmd",
    "posts/2026-08-15-projetos-reproduziveis/index.qmd",
    "scripts/check_project.py",
    "tests/test_structure.py",
    ".github/workflows/publish.yml",
    ".github/workflows/checks.yml",
]

DIRETORIOS_OBRIGATORIOS = [
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

PADROES_CREDENCIAIS = [
    r"password\s*=\s*['\"][^'\"]+['\"]",
    r"api_key\s*=\s*['\"][^'\"]+['\"]",
    r"secret\s*=\s*['\"][^'\"]+['\"]",
    r"token\s*=\s*['\"][^'\"]{10,}['\"]",
    r"ghp_[A-Za-z0-9]{36}",     # GitHub Personal Access Token
    r"sk-[A-Za-z0-9]{32,}",     # OpenAI API key
]

EXTENSOES_VERIFICAR_LINKS = {".qmd", ".md"}


def verificar_arquivos(erros, avisos):
    print("\n--- Verificando arquivos obrigatórios ---")
    ok = 0
    for arq in ARQUIVOS_OBRIGATORIOS:
        caminho = os.path.join(ROOT, arq)
        if os.path.isfile(caminho):
            print(f"  ✓ {arq}")
            ok += 1
        else:
            print(f"  ✗ AUSENTE: {arq}")
            erros.append(f"Arquivo ausente: {arq}")
    print(f"  → {ok}/{len(ARQUIVOS_OBRIGATORIOS)} arquivos presentes")


def verificar_diretorios(erros, avisos):
    print("\n--- Verificando diretórios ---")
    ok = 0
    for d in DIRETORIOS_OBRIGATORIOS:
        caminho = os.path.join(ROOT, d)
        if os.path.isdir(caminho):
            print(f"  ✓ {d}/")
            ok += 1
        else:
            print(f"  ✗ AUSENTE: {d}/")
            erros.append(f"Diretório ausente: {d}/")
    print(f"  → {ok}/{len(DIRETORIOS_OBRIGATORIOS)} diretórios presentes")


def verificar_credenciais(erros, avisos):
    print("\n--- Verificando ausência de credenciais ---")
    padroes_compilados = [(p, re.compile(p, re.IGNORECASE)) for p in PADROES_CREDENCIAIS]
    encontrados = 0

    for dirpath, _, filenames in os.walk(ROOT):
        # Ignora diretórios de ambiente virtual e build
        skip = {"venv", ".venv", "_site", "__pycache__", ".git", "node_modules", ".renv"}
        partes = set(dirpath.replace(ROOT, "").split(os.sep))
        if partes & skip:
            continue

        for fname in filenames:
            ext = os.path.splitext(fname)[1].lower()
            if ext not in {".py", ".r", ".qmd", ".md", ".yml", ".yaml", ".txt", ".env"}:
                continue
            fpath = os.path.join(dirpath, fname)
            try:
                with open(fpath, encoding="utf-8", errors="ignore") as f:
                    conteudo = f.read()
                for desc, padrao in padroes_compilados:
                    if padrao.search(conteudo):
                        rel = os.path.relpath(fpath, ROOT)
                        print(f"  ⚠ Possível credencial em {rel} (padrão: {desc})")
                        avisos.append(f"Possível credencial em {rel}")
                        encontrados += 1
            except Exception:
                pass

    if encontrados == 0:
        print("  ✓ Nenhuma credencial óbvia encontrada")


def verificar_links_internos(erros, avisos):
    print("\n--- Verificando links internos ---")
    problemas = 0

    # Coleta todos os arquivos .qmd e .md existentes
    arquivos_existentes = set()
    for dirpath, _, filenames in os.walk(ROOT):
        if ".git" in dirpath or "_site" in dirpath:
            continue
        for fname in filenames:
            ext = os.path.splitext(fname)[1].lower()
            if ext in EXTENSOES_VERIFICAR_LINKS:
                rel = os.path.relpath(os.path.join(dirpath, fname), ROOT)
                arquivos_existentes.add(rel.replace("\\", "/"))

    # Verifica links do tipo [texto](caminho.qmd) ou [texto](caminho.md)
    padrao_link = re.compile(r'\[([^\]]*)\]\(([^)#\s]+\.(?:qmd|md))[^)]*\)')

    for arq_rel in sorted(arquivos_existentes):
        arq_abs = os.path.join(ROOT, arq_rel)
        dir_arq = os.path.dirname(arq_abs)
        try:
            with open(arq_abs, encoding="utf-8", errors="ignore") as f:
                conteudo = f.read()
        except Exception:
            continue

        for match in padrao_link.finditer(conteudo):
            texto, alvo = match.group(1), match.group(2)
            if alvo.startswith("http"):
                continue
            # Resolve o caminho relativo ao arquivo
            alvo_abs = os.path.normpath(os.path.join(dir_arq, alvo))
            alvo_rel = os.path.relpath(alvo_abs, ROOT).replace("\\", "/")
            if not os.path.isfile(alvo_abs):
                print(f"  ✗ Link quebrado em {arq_rel}: [{texto}]({alvo})")
                avisos.append(f"Link possivelmente quebrado: {arq_rel} → {alvo}")
                problemas += 1

    if problemas == 0:
        print("  ✓ Nenhum link interno quebrado encontrado")
    else:
        print(f"  → {problemas} link(s) suspeito(s) — verifique manualmente")


def verificar_requirements(erros, avisos):
    print("\n--- Verificando requirements.txt ---")
    req_path = os.path.join(ROOT, "requirements.txt")
    if not os.path.isfile(req_path):
        erros.append("requirements.txt ausente")
        return

    with open(req_path) as f:
        linhas = [l.strip() for l in f if l.strip() and not l.startswith("#")]

    if linhas:
        print(f"  ✓ {len(linhas)} dependências listadas")
    else:
        avisos.append("requirements.txt está vazio")
        print("  ⚠ requirements.txt está vazio")


def main():
    print("=" * 55)
    print("  Verificação do Projeto — valber-lab")
    print("=" * 55)
    print(f"  Raiz: {ROOT}")

    erros = []
    avisos = []

    verificar_arquivos(erros, avisos)
    verificar_diretorios(erros, avisos)
    verificar_credenciais(erros, avisos)
    verificar_links_internos(erros, avisos)
    verificar_requirements(erros, avisos)

    print("\n" + "=" * 55)
    print(f"  RESULTADO: {len(erros)} erro(s) | {len(avisos)} aviso(s)")
    print("=" * 55)

    if erros:
        print("\nERROS CRÍTICOS:")
        for e in erros:
            print(f"  ✗ {e}")

    if avisos:
        print("\nAVISOS (não críticos):")
        for a in avisos:
            print(f"  ⚠ {a}")

    if not erros and not avisos:
        print("\n  Tudo certo! O projeto está íntegro.")

    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())

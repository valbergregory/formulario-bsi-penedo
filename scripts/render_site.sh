#!/usr/bin/env bash
# render_site.sh — Renderiza o site Quarto localmente
# Uso: bash scripts/render_site.sh [--preview]

set -e

echo "=== Renderizando valber-lab ==="
echo "Verificando pré-requisitos..."

if ! command -v quarto &>/dev/null; then
  echo "ERRO: Quarto não encontrado. Instale em https://quarto.org/docs/get-started/"
  exit 1
fi

if ! command -v python3 &>/dev/null; then
  echo "ERRO: Python 3 não encontrado."
  exit 1
fi

echo "  ✓ Quarto $(quarto --version)"
echo "  ✓ Python $(python3 --version)"

# Ativa ambiente virtual se existir
if [ -d "venv" ]; then
  source venv/bin/activate
  echo "  ✓ Ambiente virtual ativado"
fi

# Instala dependências Python se necessário
if [ -f "requirements.txt" ]; then
  pip install -r requirements.txt -q
  echo "  ✓ Dependências Python instaladas"
fi

# Renderiza
echo ""
echo "Renderizando..."
if [ "$1" = "--preview" ]; then
  quarto preview
else
  quarto render
  echo ""
  echo "✓ Site renderizado em _site/"
  echo "  Abra _site/index.html no navegador para visualizar"
fi

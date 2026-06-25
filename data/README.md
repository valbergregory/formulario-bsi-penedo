# Dados — valber-lab

Este diretório contém os dados utilizados nos exemplos e projetos do laboratório.

## Estrutura

```
data/
├── raw/         # Dados originais, sem modificação
├── processed/   # Dados após limpeza e transformação
└── README.md    # Este arquivo
```

## Política de dados

- **Dados simulados:** gerados por código com `set.seed()` — não são dados reais
- **Dados públicos:** obtidos de fontes abertas (IBGE, IPEA, CNJ, dados.gov.br)
- **Dados pessoais:** NUNCA são armazenados neste repositório
- **Dados processuais:** quando necessários, são anonimizados antes de qualquer uso

## Fontes utilizadas

| Fonte | Tipo | URL |
|-------|------|-----|
| IBGE | Indicadores socioeconômicos | https://www.ibge.gov.br |
| IPEA Data | Dados econômicos | https://www.ipeadata.gov.br |
| dados.gov.br | Portal de dados abertos | https://dados.gov.br |
| CNJ | Dados do Judiciário | https://www.cnj.jus.br |
| STN | Dados fiscais | https://www.tesouro.fazenda.gov.br |

## Reproduzindo os dados simulados

Os dados simulados são gerados pelos próprios scripts de análise. Execute o arquivo correspondente para gerar os dados — não é necessário baixar nada.

Exemplo:
```python
# Python
import numpy as np
np.random.seed(42)  # Garante reprodutibilidade
```

```r
# R
set.seed(42)  # Garante reprodutibilidade
```

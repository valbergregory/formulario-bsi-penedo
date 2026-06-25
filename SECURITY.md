# Política de Segurança

## Versões suportadas

| Versão | Suportada |
|--------|-----------|
| main   | ✓         |

## Reportando vulnerabilidades

Se você identificar uma vulnerabilidade de segurança neste projeto, **não abra uma issue pública**. Em vez disso:

1. Envie um e-mail para o endereço institucional listado na [página de contato](contato.qmd)
2. Descreva a vulnerabilidade, os arquivos envolvidos e o impacto potencial
3. Aguarde uma resposta em até 7 dias úteis

## Boas práticas deste projeto

- Nenhuma credencial, token ou chave de API deve ser armazenada neste repositório
- Dados pessoais de indivíduos identificados não são publicados
- Dados de processos judiciais são anonimizados antes de qualquer uso em exemplos
- O arquivo `.gitignore` exclui arquivos de ambiente (`.env`) e configurações sensíveis
- Os workflows do GitHub Actions utilizam permissões mínimas necessárias

## Uso de dados

Este projeto utiliza:
- Dados simulados (gerados por código)
- Dados públicos de domínio aberto (IBGE, IPEA, CNJ, dados.gov.br)

Nenhum dado pessoal identificável é publicado neste repositório.

## Dependências

As dependências Python são mantidas em `requirements.txt`. Recomendamos atualizar periodicamente para receber correções de segurança:

```bash
pip install --upgrade -r requirements.txt
```

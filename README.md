[README.md](https://github.com/user-attachments/files/27027635/README.md)
# Levantamento de Afinidades Docentes – BSI Penedo / UFAL
### Formulário de Coleta de Preferências para Oferta de Disciplinas e Subsídio ao NDE

[![UFAL](https://img.shields.io/badge/Instituição-UFAL-003DA5?style=flat-square)](https://ufal.edu.br)
[![Curso](https://img.shields.io/badge/Curso-Sistemas%20de%20Informação-0077B5?style=flat-square)](https://penedo.ufal.br)
[![Semestre](https://img.shields.io/badge/Referência-2026.2-28a745?style=flat-square)](#)
[![Licença](https://img.shields.io/badge/Uso-Institucional-orange?style=flat-square)](#)

---

## Sobre este projeto

Este repositório hospeda o formulário eletrônico de **levantamento de afinidades docentes** do curso de **Bacharelado em Sistemas de Informação (BSI)** da Unidade Acadêmica de Penedo – UFAL, utilizado semestralmente pela coordenação do curso para duas finalidades complementares:

1. **Composição da grade horária** — subsidiar a alocação de professores nas disciplinas da oferta semestral, respeitando afinidade, disponibilidade e distribuição equitativa de carga horária.
2. **Atualização do Projeto Pedagógico do Curso (PPC)** — fornecer ao Núcleo Docente Estruturante (NDE) uma base de dados sistematizada sobre o perfil de afinidades do corpo docente, essencial para estudos de reformulação curricular.

---

## Por que coletar esses dados?

### 1. Necessidade de base de dados para a oferta semestral

A elaboração de uma grade horária consistente exige muito mais do que o simples preenchimento de vagas. É preciso considerar:

- **Afinidade real com o conteúdo** — um docente com alta afinidade tende a produzir melhor experiência de aprendizagem, maior rigor científico e mais engajamento com os estudantes.
- **Distribuição equitativa da carga** — o BSI Penedo conta atualmente com **10 docentes**, número abaixo do ideal de **12**, o que exige planejamento cuidadoso para que cada professor mantenha entre **10h e 12h de aula semanais** sem sobrecarga.
- **Expansão do número de turmas** — a partir de 2026.2, o curso passará a ofertar **5 turmas por período**, ampliando significativamente a demanda por alocação docente planejada.
- **Registro histórico** — o acúmulo semestral dessas respostas forma uma série temporal que permite identificar tendências, lacunas e sobreposições de afinidade ao longo do tempo.

Sem um levantamento estruturado, a alocação tende a ser informal, reativa e sujeita a vieses, comprometendo a qualidade do ensino e a satisfação do corpo docente.

### 2. Subsídio ao Núcleo Docente Estruturante (NDE)

O **NDE** é o órgão consultivo responsável pela concepção, consolidação e contínua atualização do PPC, nos termos da [Resolução CONAES nº 1/2010](http://portal.mec.gov.br/index.php?option=com_docman&view=download&alias=6884-resolucao-conaes-n1-17junho2010&Itemid=30192). Para cumprir essa missão com rigor acadêmico, o NDE necessita de informações qualificadas sobre:

- Quais disciplinas do PPC vigente possuem **cobertura docente adequada** em termos de afinidade;
- Quais disciplinas apresentam **lacunas de cobertura** — isto é, nenhum ou poucos professores com alta afinidade;
- Quais **novas áreas temáticas** emergentes o corpo docente atual tem condições de propor e desenvolver;
- Como o perfil de afinidades do corpo docente **evoluiu desde 2023**, com a chegada de novos professores, e o que isso implica para a estrutura curricular.

Esses dados, sistematizados em planilha, permitem ao NDE realizar análises comparativas, identificar prioridades de contratação, propor novos componentes curriculares com respaldo no perfil real do corpo docente e documentar suas decisões com evidências — requisito fundamental em processos de reconhecimento e renovação de reconhecimento de curso pelo MEC/INEP.

---

## Estrutura do repositório

```
/
├── index.html          # Formulário principal (todos os 8 períodos do PPC)
└── README.md           # Este documento
```

O formulário é integrado ao **Google Sheets** via **Google Apps Script**, garantindo que cada resposta seja automaticamente registrada em planilha estruturada, com células coloridas por nível de afinidade para facilidade de leitura.

---

## Como funciona

```
Professor acessa o link → Preenche o formulário → Submete
        ↓
Google Apps Script recebe os dados via POST
        ↓
Planilha Google Sheets registra a resposta com formatação automática
        ↓
Coordenação e NDE acessam a planilha para análise
```

---

## Campos coletados

| Bloco | Conteúdo |
|---|---|
| Identificação | Nome, e-mail institucional, área de formação |
| Afinidades (1º ao 8º período) | Nível de afinidade para cada disciplina do PPC (52 disciplinas) |
| Disponibilidade | Dias de preferência (curso noturno); restrições de horário |
| Contribuição ao PPC | Disciplinas não contempladas, novas propostas, sugestões de reformulação |

**Escala de afinidade utilizada:**

| Nível | Significado |
|---|---|
| 🟢 Alta afinidade | Domínio pleno do conteúdo; preferência de alocação |
| 🔵 Média afinidade | Leciona com conforto; sem ressalvas |
| 🟡 Se necessário | Aceita a alocação, mas não é a primeira escolha |
| 🔴 Sem afinidade | Não se sente apto(a) para ministrar a disciplina |

---

## Uso e acesso à planilha

A planilha de respostas é de **uso exclusivo da coordenação do SI Penedo e do NDE**. Os dados coletados são utilizados para:

- Montagem da grade horária semestral
- Relatórios internos de gestão acadêmica
- Estudos de revisão e atualização do PPC
- Documentação de processos para avaliações institucionais (INEP/MEC)

---

## Referências normativas

- **Resolução CNE/CES nº 5/2016** — Diretrizes Curriculares Nacionais para os cursos de graduação na área de Computação
- **Resolução CONAES nº 1/2010** — Normatiza o Núcleo Docente Estruturante
- **Instrumento de Avaliação de Cursos de Graduação (INEP/MEC)** — Indicador 2.6: Perfil do corpo docente; Indicador 1.5: Coerência do currículo com as DCN
- **PPC do BSI – UFAL Penedo (2018)** — Projeto Pedagógico do Curso vigente

---

## Contato

**Coordenação do SI – Unidade Acadêmica de Penedo / UFAL**  
R. Floriano Rosa - Dom Constantino, Penedo - AL, 57200-000 - +558234821877
📧 valber.santos@penedo.ufal.br

---

*Este repositório deve ser mantido pela coordenação do curso. Atualizado a cada semestre letivo.*

# 🛠️ Automatização da Consulta do CAR

Este projeto tem como objetivo automatizar as rotinas de **consulta ao Cadastro Ambiental Rural (CAR)** otimizando os processos realizados pela equipe da área de Gestão Ambiental Regularização Fundiária.

## 📌 Objetivos

- Reduzir o tempo gasto em consultas manuais
- Evitar erros humanos na inserção de dados e interpretação dos resultados.
- Registrar e organizar os dados coletados automaticamente.
- Fornecer relatórios ou arquivos com os resultados das consultas.

---

## ⚙️ Funcionalidades

- Consulta automatizada por número do CAR
- Download e salvamento dos comprovantes e resultados em PDF ou HTML.
- Geração de planilha com status das consultas.
- Registro de logs com tentativas, erros e resultados.

---

## 🧰 Tecnologias Utilizadas

Python – linguagem principal da automação

Pandas – manipulação e tratamento de dados (Excel, tabelas, filtros)

PyAutoGUI – automação de ações no mouse, teclado e tela

Tesseract OCR – reconhecimento de texto em imagens (usado para ler CAPTCHAs ou elementos gráficos)

TQDM – barras de progresso para acompanhamento das consultas

Time – controle de tempo e pausas durante a execução

OS – manipulação de arquivos e diretórios do sistema

---

## 🏗️ Estrutura do Projeto

├── main.py # Script principal da automação ├── consulta_car.py # |└── entradas.xlsx # Lista de CARs ou CPFs para consulta ├── resultados/ │ └── resultado_consultas.xlsx # Resultado final das consultas ├── logs/ │ └── log_execucao.txt # Log da execução ├── README.

---

## ▶️ Como Executar

1. **Instale os requisitos**:

```bash
pip install -r requirements.txt

---
# Product Registration Automation (Python RPA)

*[Leia em Português](#automação-de-cadastro-de-produtos-rpa-com-python)*

An automation pipeline developed in Python to perform batch product registration in a web system from a structured CSV dataset, eliminating repetitive manual work and reducing operational errors.

## Technologies Used
- **Python 3**
- **PyAutoGUI** (Graphical User Interface Automation / RPA)
- **Pandas** (`.csv` dataset reading and data handling)

## Project Structure
- `main.py`: Main script that opens the browser, performs login, reads `produtos.csv`, and automatically fills out the web form for each item.
- `pegar_posicao.py`: Utility script to capture `(x, y)` cursor coordinates on the screen and calibrate clicks according to monitor resolution.
- `produtos.csv`: Sample dataset containing the products to be registered.

## How to Run

1. Install the dependencies:

    pip install -r requirements.txt

2. Run the main automation:

    python main.py

### Notes
- If you are using a different screen resolution, run the helper script `pegar_posicao.py` to capture the input field coordinates before running the main script.

---

# Automação de Cadastro de Produtos (RPA com Python)

*[Read in English](#product-registration-automation-python-rpa)*

Pipeline de automação desenvolvido em Python para realizar o cadastro em lote de produtos em um sistema web a partir de uma base estruturada em CSV, eliminando trabalho manual repetitivo e reduzindo falhas operacionais.

## Tecnologias Utilizadas
- **Python 3**
- **PyAutoGUI** (Automação de interface gráfica / RPA)
- **Pandas** (Leitura e tratamento da base de dados `.csv`)

## Estrutura do Projeto
- `main.py`: Script principal que abre o navegador, realiza o login, lê o arquivo `produtos.csv` e preenche o formulário automaticamente para cada item.
- `pegar_posicao.py`: Script utilitário para capturar as coordenadas `(x, y)` do cursor na tela e calibrar os cliques conforme a resolução do monitor.
- `produtos.csv`: Base de dados de exemplo com os produtos a serem cadastrados.

## Como Executar

1. Instale as dependências:

    pip install -r requirements.txt

2. Execute a automação principal:

    python main.py

### Nota
- Caso utilize uma resolução de tela diferente, rode o script auxiliar `pegar_posicao.py` para capturar as coordenadas dos campos antes de executar o script principal.

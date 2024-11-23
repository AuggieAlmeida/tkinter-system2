# DevGameLauncher

Um launcher moderno para jogos e ferramentas de desenvolvimento.

## Requisitos

- Python 3.11+
- pip para gerenciamento de dependências

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   .\venv\Scripts\activate  # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Copie o arquivo .env.example para .env e configure conforme necessário
5. Execute o aplicativo:
   ```bash
   python main.py
   ```

## Desenvolvimento

- Ative o ambiente virtual antes de desenvolver
- Use `pytest` para executar os testes
- Use `black .` para formatar o código
- Use `flake8` para verificar o código


# Social Media Bot

Este projeto é um bot de coleta de dados de redes sociais que coleta tweets, armazena-os em um banco de dados, realiza análises e gera relatórios diários que são enviados por e-mail.

## Funcionalidades

- Coleta de tweets do Twitter
- Armazenamento de dados coletados em um banco de dados
- Análise e geração de relatórios diários
- Envio de relatórios por e-mail

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/wislla/social_media_bot.git
    cd social_media_bot
    ```

2. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    venv\Scripts\activate  # Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure suas credenciais da API do Twitter e configurações de banco de dados no arquivo `config.py`.

5. Inicialize o banco de dados:
    ```bash
    python database.py
    ```

## Uso

Execute o script principal:
```bash
python run.py

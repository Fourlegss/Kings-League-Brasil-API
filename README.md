# Kings League Brasil - API de Dados

Este projeto tem como objetivo criar uma API de dados para a Kings League Brasil, implementando um processo de ETL (Extract, Transform, Load) para disponibilizar dados estruturados para análise.

## Objetivo

O projeto visa extrair dados do site da Kings League Brasil, transformá-los em um formato adequado e carregá-los em um banco de dados MongoDB, criando assim uma base de dados estruturada para análise.

## Tecnologias Utilizadas

- Python
- MongoDB
- BeautifulSoup4 (Web Scraping)
- Requests (HTTP requests)
- Pandas (Manipulação de dados)
- Schedule (Agendamento de tarefas)

## Estrutura do Projeto

```
kings_league_brasil_api/
├── src/
│   ├── extract/
│   │   └── scraper.py
│   ├── transform/
│   │   └── transformer.py
│   ├── load/
│   │   └── loader.py
│   └── config/
│       └── config.py
├── tests/
├── .env
├── requirements.txt
└── README.md
```

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instale as dependências: `pip install -r requirements.txt`
5. Configure o arquivo `.env` com suas credenciais do MongoDB

## Uso

Para executar o pipeline ETL:

```bash
python src/main.py
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests. 
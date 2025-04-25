# Kings League Brasil - API de Dados

Este projeto tem como objetivo criar uma API de dados para a Kings League Brasil, implementando um processo de extração e transformação de dados para disponibilizar informações estruturadas via API.

## Objetivo

O projeto visa extrair dados do site da Kings League Brasil, transformá-los em um formato adequado e disponibilizá-los através de uma API REST.

## Tecnologias Utilizadas

- Python
- BeautifulSoup4 (Web Scraping)
- Requests (HTTP requests)
- Pandas (Manipulação de dados)
- FastAPI (API REST)
- Schedule (Agendamento de tarefas)

## Estrutura do Projeto

```
kings_league_brasil_api/
├── src/
│   ├── extract/
│   │   └── scraper.py
│   ├── transform/
│   │   └── transformer.py
│   └── config/
│       └── config.py
├── tests/
├── requirements.txt
├── API.md
└── README.md
```

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instale as dependências: `pip install -r requirements.txt`

## Uso

Para executar a API:

```bash
python src/api/main.py
```

A API estará disponível em `http://localhost:8000`

## Documentação da API

Para informações detalhadas sobre como usar a API, endpoints disponíveis, exemplos de código e considerações importantes, consulte o arquivo [API.md](API.md).

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests. 
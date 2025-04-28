# Documentação da API Kings League Brasil

## Visão Geral

A API Kings League Brasil é uma interface REST que fornece acesso programático aos dados da Kings League Brasil. Ela permite que desenvolvedores obtenham informações atualizadas sobre times e partidas da liga de forma estruturada e padronizada.

## Acesso à API

A API está disponível em: [https://kings-league-brasil-api.onrender.com/](https://kings-league-brasil-api.onrender.com/)

## Documentação Interativa

Para uma documentação interativa e mais detalhada, acesse:
- [Documentação Swagger](https://kings-league-brasil-api.onrender.com/docs)
- [Documentação ReDoc](https://kings-league-brasil-api.onrender.com/redoc)

## Objetivo

O objetivo principal desta API é facilitar o acesso aos dados da Kings League Brasil para desenvolvedores que desejam criar aplicações, análises ou integrações com os dados da liga. A API extrai e transforma os dados diretamente do site oficial, garantindo que as informações estejam sempre atualizadas.

## Endpoints

### 1. Listar Times
Retorna a lista completa de times da Kings League Brasil.

**Endpoint:** `GET /times`

**URL Completa:** `https://kings-league-brasil-api.onrender.com/times`

**Resposta:**
```json
{
    "status": "success",
    "data": [
        {
            "name": "NOME_DO_TIME",
            "slug": "nome-do-time",
            "created_at": "2024-02-20T10:00:00",
            "updated_at": "2024-02-20T10:00:00"
        }
    ],
    "count": 12
}
```

**Campos:**
- `name`: Nome completo do time
- `slug`: Versão do nome formatada para URLs
- `created_at`: Data de criação do registro
- `updated_at`: Data da última atualização

### 2. Listar Partidas
Retorna a lista de partidas da Kings League Brasil.

**Endpoint:** `GET /partidas`

**URL Completa:** `https://kings-league-brasil-api.onrender.com/partidas`

**Resposta:**
```json
{
    "status": "success",
    "data": [
        {
            "match_id": "time1-vs-time2",
            "home_team": "TIME_DA_CASA",
            "away_team": "TIME_VISITANTE",
            "home_score": 2,
            "away_score": 1,
            "link": "https://kingsleague.pro/pt/brazil/jogos/time1-vs-time2",
            "created_at": "2024-02-20T10:00:00",
            "updated_at": "2024-02-20T10:00:00"
        }
    ],
    "count": 30
}
```

**Campos:**
- `match_id`: Identificador único da partida
- `home_team`: Nome do time da casa
- `away_team`: Nome do time visitante
- `home_score`: Placar do time da casa (pode ser null se a partida ainda não foi realizada)
- `away_score`: Placar do time visitante (pode ser null se a partida ainda não foi realizada)
- `link`: URL da página da partida
- `created_at`: Data de criação do registro
- `updated_at`: Data da última atualização

## Códigos de Status

- `200 OK`: Requisição bem-sucedida
- `500 Internal Server Error`: Erro durante a extração ou transformação dos dados

## Limitações

1. **Cache**: Os dados são armazenados em cache por 15 minutos para melhor performance
2. **Atualização**: Os dados são atualizados automaticamente a cada 24 horas
3. **Rate Limiting**: Atualmente não há limite de requisições

## Exemplo de Uso

### Python
```python
import requests

# Obter lista de times
response = requests.get('https://kings-league-brasil-api.onrender.com/times')
times = response.json()

# Obter lista de partidas
response = requests.get('https://kings-league-brasil-api.onrender.com/partidas')
partidas = response.json()
```

### JavaScript
```javascript
// Obter lista de times
fetch('https://kings-league-brasil-api.onrender.com/times')
  .then(response => response.json())
  .then(data => console.log(data));

// Obter lista de partidas
fetch('https://kings-league-brasil-api.onrender.com/partidas')
  .then(response => response.json())
  .then(data => console.log(data));
```

## Considerações Importantes

1. A API é ideal para:
   - Desenvolvimento de aplicações que precisam de dados da Kings League Brasil
   - Criação de dashboards e visualizações
   - Integração com outros sistemas
   - Análise de dados da liga

2. Os dados são extraídos diretamente do site oficial, garantindo:
   - Atualização automática
   - Consistência com a fonte oficial
   - Formato padronizado

3. Recomendações de uso:
   - Implementar tratamento de erros
   - Considerar o cache de 15 minutos ao planejar atualizações
   - Verificar o status da resposta antes de processar os dados 
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sys
import os
import logging
from typing import List

# Adiciona o diretório raiz ao path do Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.extract.scraper import KingsLeagueScraper
from src.transform.transformer import DataTransformer
from src.cache.cache_manager import CacheManager
from src.api.models import Team, Match, TeamResponse, MatchResponse
from src.api.exceptions import DataExtractionError, DataTransformationError, CacheError

# Configuração do logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('api.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Kings League Brasil API",
    description="API para acesso aos dados da Kings League Brasil",
    version="1.0.0"
)

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique os domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializa os componentes
scraper = KingsLeagueScraper()
transformer = DataTransformer()
cache = CacheManager()

@app.get("/")
async def root():
    """Endpoint raiz da API"""
    return {
        "message": "Bem-vindo à API da Kings League Brasil",
        "endpoints": {
            "teams": "/times",
            "matches": "/partidas"
        }
    }

@app.get("/times", response_model=TeamResponse)
async def get_teams():
    """Retorna a lista de times"""
    try:
        # Tenta pegar do cache primeiro
        cached_teams = cache.get_teams()
        if cached_teams:
            logger.info("Retornando times do cache")
            return TeamResponse(
                status="success",
                data=cached_teams,
                count=len(cached_teams)
            )
        
        # Se não estiver em cache, extrai e transforma os dados
        logger.info("Extraindo dados dos times")
        raw_teams = scraper.extract_teams()
        teams = transformer.transform_teams(raw_teams)
        
        # Armazena no cache
        cache.set_teams(teams)
        
        return TeamResponse(
            status="success",
            data=teams,
            count=len(teams)
        )
    except Exception as e:
        logger.error(f"Erro ao buscar times: {str(e)}")
        raise DataExtractionError(str(e))

@app.get("/partidas", response_model=MatchResponse)
async def get_matches():
    """Retorna a lista de partidas"""
    try:
        # Tenta pegar do cache primeiro
        cached_matches = cache.get_matches()
        if cached_matches:
            logger.info("Retornando partidas do cache")
            return MatchResponse(
                status="success",
                data=cached_matches,
                count=len(cached_matches)
            )
        
        # Se não estiver em cache, extrai e transforma os dados
        logger.info("Extraindo dados das partidas")
        raw_matches = scraper.extract_matches()
        matches = transformer.transform_matches(raw_matches)
        
        # Armazena no cache
        cache.set_matches(matches)
        
        return MatchResponse(
            status="success",
            data=matches,
            count=len(matches)
        )
    except Exception as e:
        logger.error(f"Erro ao buscar partidas: {str(e)}")
        raise DataExtractionError(str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any

class CacheManager:
    def __init__(self, cache_duration_minutes: int = 15):
        self.teams_cache: Dict[str, Any] = {}
        self.matches_cache: Dict[str, Any] = {}
        self.cache_duration = timedelta(minutes=cache_duration_minutes)
    
    def get_teams(self) -> Optional[List[Dict]]:
        """Retorna os times do cache se ainda forem válidos"""
        if self.is_cache_valid('teams'):
            return self.teams_cache['data']
        return None
    
    def set_teams(self, teams: List[Dict]) -> None:
        """Armazena os times no cache"""
        self.teams_cache = {
            'data': teams,
            'timestamp': datetime.now()
        }
    
    def get_matches(self) -> Optional[List[Dict]]:
        """Retorna as partidas do cache se ainda forem válidas"""
        if self.is_cache_valid('matches'):
            return self.matches_cache['data']
        return None
    
    def set_matches(self, matches: List[Dict]) -> None:
        """Armazena as partidas no cache"""
        self.matches_cache = {
            'data': matches,
            'timestamp': datetime.now()
        }
    
    def is_cache_valid(self, cache_type: str) -> bool:
        """Verifica se o cache ainda é válido"""
        cache = self.teams_cache if cache_type == 'teams' else self.matches_cache
        if not cache or 'timestamp' not in cache:
            return False
        return datetime.now() - cache['timestamp'] < self.cache_duration
    
    def clear_cache(self, cache_type: Optional[str] = None) -> None:
        """Limpa o cache"""
        if cache_type == 'teams':
            self.teams_cache = {}
        elif cache_type == 'matches':
            self.matches_cache = {}
        else:
            self.teams_cache = {}
            self.matches_cache = {} 
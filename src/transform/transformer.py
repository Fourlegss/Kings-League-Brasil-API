import pandas as pd
from datetime import datetime
from unidecode import unidecode
import re
from typing import Dict, List

class DataTransformer:
    @staticmethod
    def normalize_team_name(name: str) -> str:
        """Remove acentos e caracteres especiais do nome do time"""
        return unidecode(name.strip().upper())
    
    @staticmethod
    def create_slug(text: str) -> str:
        """Cria um slug a partir do texto (ex: 'São Paulo FC' -> 'sao-paulo-fc')"""
        text = unidecode(text.lower())
        text = re.sub(r'[^a-z0-9]+', '-', text)
        return text.strip('-')
    
    def transform_team(self, team_data: Dict) -> Dict:
        """Transforma os dados brutos do time em um formato padronizado"""
        return {
            'name': team_data['name'],
            'slug': self.create_slug(team_data['name']),
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }
    
    def transform_match(self, match_data: Dict) -> Dict:
        """Transforma os dados brutos da partida em um formato padronizado"""
        return {
            'match_id': match_data['match_id'],
            'home_team': self.normalize_team_name(match_data['home_team']),
            'away_team': self.normalize_team_name(match_data['away_team']),
            'home_score': match_data.get('home_score'),
            'away_score': match_data.get('away_score'),
            'link': match_data['link'],
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }
    
    def transform_teams(self, teams_data: List[Dict]) -> List[Dict]:
        """Transforma uma lista de times"""
        return [self.transform_team(team) for team in teams_data]
    
    def transform_matches(self, matches_data: List[Dict]) -> List[Dict]:
        """Transforma uma lista de partidas"""
        return [self.transform_match(match) for match in matches_data]

    def create_dataframe(self, data, columns):
        """Cria um DataFrame pandas a partir dos dados transformados"""
        return pd.DataFrame(data, columns=columns) 
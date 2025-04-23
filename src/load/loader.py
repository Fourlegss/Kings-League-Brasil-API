from pymongo import MongoClient
from src.config.config import MONGODB_URI, MONGODB_DB

class MongoDBLoader:
    def __init__(self):
        self.client = MongoClient(MONGODB_URI)
        self.db = self.client[MONGODB_DB]

    def load_teams(self, teams_data):
        """Carrega os dados dos times no MongoDB"""
        if not teams_data:
            return False

        try:
            collection = self.db.teams
            # Atualiza ou insere novos times
            for team in teams_data:
                collection.update_one(
                    {'name': team['name']},
                    {'$set': team},
                    upsert=True
                )
            return True
        except Exception as e:
            print(f"Erro ao carregar times: {str(e)}")
            return False

    def load_matches(self, matches_data):
        """Carrega os dados das partidas no MongoDB"""
        if not matches_data:
            return False

        try:
            collection = self.db.matches
            # Atualiza ou insere novas partidas
            for match in matches_data:
                collection.update_one(
                    {
                        'home_team': match['home_team'],
                        'away_team': match['away_team'],
                        'match_date': match['match_date']
                    },
                    {'$set': match},
                    upsert=True
                )
            return True
        except Exception as e:
            print(f"Erro ao carregar partidas: {str(e)}")
            return False

    def close_connection(self):
        """Fecha a conexão com o MongoDB"""
        self.client.close() 
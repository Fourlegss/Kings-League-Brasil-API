import requests
from bs4 import BeautifulSoup
from src.config.config import BASE_URL, HEADERS

class KingsLeagueScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

    def get_page_content(self, url):
        """Obtém o conteúdo HTML de uma página"""
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Erro ao acessar a página {url}: {str(e)}")
            return None

    def extract_teams(self):
        """Extrai informações dos times"""
        url = f"{BASE_URL}/times"
        html_content = self.get_page_content(url)
        if not html_content:
            return []

        soup = BeautifulSoup(html_content, 'html.parser')
        teams = []
        
        # Procura por elementos que contêm o nome dos times
        team_elements = soup.select('h2.team-name')
        
        for team in team_elements:
            try:
                team_data = {
                    'name': team.text.strip(),
                }
                teams.append(team_data)
            except Exception as e:
                print(f"Erro ao extrair dados do time: {str(e)}")
                continue
        
        return teams

    def extract_matches(self):
        """Extrai informações das partidas"""
        url = f"{BASE_URL}/jogos"
        html_content = self.get_page_content(url)
        if not html_content:
            return []

        soup = BeautifulSoup(html_content, 'html.parser')
        matches = []
        
        # Procura por elementos que contêm informações das partidas
        match_elements = soup.select('a[class*="absolute top-0 left-0 right-0 bottom-0"]')
        
        for match in match_elements:
            try:
                match_id = match.get('href').split('/')[-1]
                teams = match_id.split('-vs-')
                
                match_data = {
                    'match_id': match_id,
                    'home_team': teams[0].upper(),
                    'away_team': teams[1].upper(),
                    'link': match.get('href'),
                }
                matches.append(match_data)
            except Exception as e:
                print(f"Erro ao extrair dados da partida: {str(e)}")
                continue
        
        return matches 
import requests
from bs4 import BeautifulSoup
from src.config.config import BASE_URL, HEADERS
import traceback

class KingsLeagueScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

    def get_page_content(self, url):
        """Obtém o conteúdo HTML de uma página"""
        try:
            response = self.session.get(url)
            response.raise_for_status()
            print(response.text)
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

    def safe_text(self, tag):
        """
        Função auxiliar para extrair texto de um elemento BeautifulSoup de forma segura.
        Retorna None se o elemento não existir ou não tiver texto.
        """
        try:
            if tag and hasattr(tag, 'text') and tag.text is not None:
                value = str(tag.text).strip()
                if value == '-' or value == '':
                    return None
                return value
        except Exception as e:
            print(f"Erro em safe_text: {e}")
        return None

    def extract_matches(self):
        """
        Extrai informações das partidas, incluindo placar, nomes dos times (curto e completo) e link.
        Itera sobre cada card de partida (div.match-row-container).
        Comentários detalhados para fins de estudo e portfólio.
        """
        url = f"{BASE_URL}/jogos"
        html_content = self.get_page_content(url)
        if not html_content:
            return []

        soup = BeautifulSoup(html_content, 'html.parser')
        matches = []

        match_cards = soup.find_all('div', class_='match-row-container')

        for idx, card in enumerate(match_cards):
            try:
                print(f"\n==== CARD {idx} ====")
                # Extrai o link e o match_id
                link_tag = card.find('a', class_='absolute')
                match_id = None
                link = None
                if link_tag:
                    link = link_tag.get('href')
                    match_id = link.split('/')[-1] if link else None
                print(f"match_id: {match_id}, link: {link}")

                # Extrai todos os elementos de placar (p ou span com font-bold)
                score_tags = card.select('.font-bold')
                scores = [tag.text.strip() for tag in score_tags if tag.text and tag.text.strip().isdigit()]
                print(f"score_tags: {[tag.text for tag in score_tags]}")
                print(f"scores extraídos: {scores}")
                home_score = int(scores[0]) if len(scores) > 0 else None
                away_score = int(scores[1]) if len(scores) > 1 else None
                print(f"home_score: {home_score}, away_score: {away_score}")

                # Nome completo do time da casa (desktop) - busca pelo primeiro div.flex.items-center.justify-end.gap-1.lg:gap-4.text-white
                home_team_full = None
                left_divs = card.find_all('div', class_='flex items-center justify-end gap-1 lg:gap-4 text-white')
                if left_divs:
                    first_left_div = left_divs[0]
                    for p in first_left_div.find_all('p'):
                        p_text = self.safe_text(p)
                        if p_text and not p_text.isdigit():
                            home_team_full = p_text
                            break
                print(f"home_team_full: {home_team_full}")

                # Nome curto do time da casa (mobile)
                home_team_short_tag = card.select_one('p.text-base.text-primary')
                home_team_short = self.safe_text(home_team_short_tag)
                print(f"home_team_short: {home_team_short}")

                # Nome completo do time visitante (desktop) - busca pelo último div.flex.items-center.justify-start.gap-1.lg:gap-4.text-white
                away_team_full = None
                right_divs = card.find_all('div', class_='flex items-center justify-start gap-1 lg:gap-4 text-white')
                if right_divs:
                    last_right_div = right_divs[-1]
                    for p in last_right_div.find_all('p'):
                        p_text = self.safe_text(p)
                        if p_text and not p_text.isdigit():
                            away_team_full = p_text
                            break
                print(f"away_team_full: {away_team_full}")

                # Nome curto do time visitante (mobile)
                away_team_short_tag = None
                flex_cols = card.select('div.flex.flex-col.items-center.lg\:hidden')
                if flex_cols:
                    last_flex_col = flex_cols[-1]
                    away_team_short_tag = last_flex_col.find('p')
                away_team_short = self.safe_text(away_team_short_tag)
                print(f"away_team_short: {away_team_short}")

                home_team = home_team_full or home_team_short
                away_team = away_team_full or away_team_short
                print(f"home_team usado: {home_team}")
                print(f"away_team usado: {away_team}")

                match_data = {
                    'match_id': match_id,
                    'home_team': home_team,
                    'away_team': away_team,
                    'home_team_full': home_team_full,
                    'home_team_short': home_team_short,
                    'away_team_full': away_team_full,
                    'away_team_short': away_team_short,
                    'home_score': home_score,
                    'away_score': away_score,
                    'link': link,
                }
                matches.append(match_data)
            except Exception as e:
                print(f"Erro ao extrair dados da partida: {str(e)}")
                print(f"HTML do card problemático:\n{card.prettify()}")
                traceback.print_exc()
                continue

        return matches 
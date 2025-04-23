from src.extract.scraper import KingsLeagueScraper

def test_scraper():
    print("Iniciando teste do scraper...")
    
    # Inicializa o scraper
    scraper = KingsLeagueScraper()
    
    # Testa extração de times
    print("\nTestando extração de times...")
    teams = scraper.extract_teams()
    print(f"Quantidade de times encontrados: {len(teams)}")
    if teams:
        print("\nPrimeiro time encontrado:")
        print(teams[0])
    
    # Testa extração de partidas
    print("\nTestando extração de partidas...")
    matches = scraper.extract_matches()
    print(f"Quantidade de partidas encontradas: {len(matches)}")
    if matches:
        print("\nPrimeira partida encontrada:")
        print(matches[0])

if __name__ == "__main__":
    test_scraper() 
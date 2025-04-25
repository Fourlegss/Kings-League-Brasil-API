import schedule
import time
from src.extract.scraper import KingsLeagueScraper
from src.transform.transformer import DataTransformer

def run_etl():
    """Executa o processo de extração e transformação de dados"""
    print("Iniciando processo de extração e transformação...")
    
    # Inicializa os componentes
    scraper = KingsLeagueScraper()
    transformer = DataTransformer()

    try:
        # Extração
        print("Extraindo dados...")
        teams_data = scraper.extract_teams()
        matches_data = scraper.extract_matches()

        # Transformação
        print("Transformando dados...")
        transformed_teams = transformer.transform_teams(teams_data)
        transformed_matches = transformer.transform_matches(matches_data)

        print("Processo concluído com sucesso!")
        return transformed_teams, transformed_matches

    except Exception as e:
        print(f"Erro durante o processo: {str(e)}")
        return None, None

def main():
    # Executa o processo imediatamente
    run_etl()

    # Agenda a execução periódica
    schedule.every(24).hours.do(run_etl)

    # Mantém o script rodando
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main() 
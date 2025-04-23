import schedule
import time
from src.extract.scraper import KingsLeagueScraper
from src.transform.transformer import DataTransformer
from src.load.loader import MongoDBLoader

def run_etl():
    """Executa o processo completo de ETL"""
    print("Iniciando processo ETL...")
    
    # Inicializa os componentes
    scraper = KingsLeagueScraper()
    transformer = DataTransformer()
    loader = MongoDBLoader()

    try:
        # Extração
        print("Extraindo dados...")
        teams_data = scraper.extract_teams()
        matches_data = scraper.extract_matches()

        # Transformação
        print("Transformando dados...")
        transformed_teams = transformer.transform_teams(teams_data)
        transformed_matches = transformer.transform_matches(matches_data)

        # Carregamento
        print("Carregando dados no MongoDB...")
        teams_loaded = loader.load_teams(transformed_teams)
        matches_loaded = loader.load_matches(transformed_matches)

        if teams_loaded and matches_loaded:
            print("Processo ETL concluído com sucesso!")
        else:
            print("Ocorreram erros durante o processo ETL.")

    except Exception as e:
        print(f"Erro durante o processo ETL: {str(e)}")
    
    finally:
        loader.close_connection()

def main():
    # Executa o ETL imediatamente
    run_etl()

    # Agenda a execução periódica
    schedule.every(24).hours.do(run_etl)

    # Mantém o script rodando
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main() 
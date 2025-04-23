from fastapi import HTTPException

class APIException(HTTPException):
    """Classe base para exceções da API"""
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)

class DataExtractionError(APIException):
    """Erro durante a extração de dados"""
    def __init__(self, detail: str):
        super().__init__(status_code=500, detail=f"Erro na extração de dados: {detail}")

class DataTransformationError(APIException):
    """Erro durante a transformação de dados"""
    def __init__(self, detail: str):
        super().__init__(status_code=500, detail=f"Erro na transformação de dados: {detail}")

class CacheError(APIException):
    """Erro durante o gerenciamento do cache"""
    def __init__(self, detail: str):
        super().__init__(status_code=500, detail=f"Erro no cache: {detail}")

class ValidationError(APIException):
    """Erro de validação de dados"""
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=f"Erro de validação: {detail}") 
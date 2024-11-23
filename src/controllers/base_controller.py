from loguru import logger

class BaseController:
    def __init__(self, model=None):
        self.model = model
        
    def handle_error(self, error, message="Erro na operação"):
        """Tratamento padrão de erros"""
        logger.error(f"{message}: {str(error)}")
        raise error

from .base_controller import BaseController
from src.models import GameModel
from src.exceptions import GameError

class GamesController(BaseController):
    def __init__(self):
        self.model = GameModel()
        super().__init__(self.model)
    
    def get_all_games(self):
        """Retorna todos os jogos"""
        try:
            return self.model.get_all_games()
        except Exception as e:
            self.handle_error(e, "Erro ao buscar jogos")

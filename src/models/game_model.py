from .base_model import BaseModel

class GameModel(BaseModel):
    def get_all_games(self):
        """Retorna todos os jogos"""
        query = "SELECT * FROM games ORDER BY last_played DESC"
        return self.execute_query(query)
    
    def add_game(self, name: str, path: str):
        """Adiciona um novo jogo"""
        query = """
        INSERT INTO games (name, path)
        VALUES (?, ?)
        """
        return self.execute_query(query, (name, path))

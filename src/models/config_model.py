from typing import Dict, Any
from .base_model import BaseModel
from loguru import logger

class ConfigModel(BaseModel):
    DEFAULT_CONFIGS = {
        'theme': 'light',
        'language': 'pt_BR'
    }

    def __init__(self):
        super().__init__()
        self.init_database()
        self._ensure_default_configs()
    
    def init_database(self):
        """Inicializa o banco de dados"""
        super().init_database()
        # Cria tabela de configurações se não existir
        self.execute_query("""
            CREATE TABLE IF NOT EXISTS configs (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL
            )
        """)
    
    def _ensure_default_configs(self):
        """Garante que as configurações padrão existam"""
        current_configs = self.get_all_configs()
        
        # Insere configurações padrão que não existem
        for key, value in self.DEFAULT_CONFIGS.items():
            if key not in current_configs:
                self.update_config(key, value)
                logger.info(f"Configuração padrão criada: {key} = {value}")
    
    def get_config(self, key):
        """Obtém uma configuração específica"""
        query = "SELECT value FROM configs WHERE key = ?"
        result = self.execute_query(query, (key,))
        return result[0][0] if result else None
    
    def get_all_configs(self):
        """Obtém todas as configurações"""
        query = "SELECT key, value FROM configs"
        results = self.execute_query(query)
        return {row[0]: row[1] for row in results} if results else {}
    
    def update_config(self, key, value):
        """Atualiza ou insere uma configuração"""
        query = """
        INSERT INTO configs (key, value) 
        VALUES (?, ?)
        ON CONFLICT(key) DO UPDATE SET value = ?
        """
        self.execute_query(query, (key, value, value))
        logger.info(f"Configuração atualizada: {key} = {value}")

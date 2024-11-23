from typing import Dict, Any
from pathlib import Path
from loguru import logger
import sqlite3
from src.exceptions import DatabaseInitializationError, DatabaseQueryError

class BaseModel:
    def __init__(self):
        self.db_dir = Path("data")
        self.db_dir.mkdir(exist_ok=True)
        self.db_path = self.db_dir / "devgamelauncher.db"
        self.conn = None
        self.init_database()
        
    def init_database(self):
        """Inicializa o banco de dados com as tabelas necessárias"""
        try:
            # Verifica se o diretório pai existe e é um diretório
            if self.db_path.parent.exists() and not self.db_path.parent.is_dir():
                raise DatabaseInitializationError(
                    f"O caminho {self.db_path.parent} existe mas não é um diretório"
                )
            
            self.db_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Cria nova conexão
            self.conn = sqlite3.connect(str(self.db_path))
            cursor = self.conn.cursor()
            
            # Cria tabela de configurações
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS configs (
                    key TEXT PRIMARY KEY,
                    value TEXT NOT NULL
                )
            ''')
            
            # Cria tabela de jogos
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS games (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    path TEXT NOT NULL,
                    last_played DATETIME,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Cria tabela de ferramentas
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tools (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    path TEXT NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            self.conn.commit()
            logger.info("Banco de dados inicializado com sucesso")
                
        except Exception as e:
            self.close()
            if isinstance(e, DatabaseInitializationError):
                raise
            raise DatabaseInitializationError(f"Erro ao inicializar banco: {str(e)}")
    
    def execute_query(self, query: str, params: tuple = ()) -> Any:
        """Executa uma query no banco de dados"""
        try:
            if not self.conn:
                self.conn = sqlite3.connect(str(self.db_path))
            
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            self.conn.commit()
            return cursor.fetchall()
        except sqlite3.Error as e:
            error_msg = f"Erro ao executar query: {str(e)}"
            logger.error(error_msg)
            raise DatabaseQueryError(error_msg)

    def close(self):
        """Fecha a conexão com o banco de dados"""
        if self.conn:
            self.conn.close()
            self.conn = None
            
    def cleanup(self):
        """Limpa todas as tabelas do banco"""
        tables = ['configs', 'games', 'tools', 'test_table']
        for table in tables:
            try:
                self.execute_query(f"DELETE FROM {table}")
            except DatabaseQueryError:
                # Ignora erros se a tabela não existir
                pass

    def __del__(self):
        """Destrutor para garantir que a conexão seja fechada"""
        self.close()

import pytest
import sqlite3
from pathlib import Path
from src.models.base_model import BaseModel
from src.exceptions import DatabaseInitializationError, DatabaseQueryError
import customtkinter as ctk
from src.views.base_view import BaseView

class TestBaseModel:
    @pytest.fixture
    def base_model(self, tmp_path):
        """Fixture que cria um modelo base com banco de dados temporário"""
        model = BaseModel()
        model.db_dir = tmp_path
        model.db_path = tmp_path / "test.db"
        return model

    def test_init_database(self, base_model):
        """Testa se as tabelas são criadas corretamente"""
        # Força a inicialização do banco
        base_model.init_database()
        
        with sqlite3.connect(str(base_model.db_path)) as conn:  # Converte Path para string
            cursor = conn.cursor()
            tables = cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            ).fetchall()
            table_names = [table[0] for table in tables]
            
            # Verifica se todas as tabelas necessárias foram criadas
            expected_tables = ['configs', 'games', 'tools']
            for table in expected_tables:
                assert table in table_names, f"Tabela {table} não encontrada"

    def test_execute_query(self, base_model):
        """Testa a execução de queries"""
        # Limpa a tabela antes do teste
        base_model.execute_query("DELETE FROM configs")
        
        # Teste de inserção
        base_model.execute_query(
            "INSERT INTO configs (key, value) VALUES (?, ?)",
            ("test_key", "test_value")
        )
        
        # Teste de seleção
        result = base_model.execute_query(
            "SELECT value FROM configs WHERE key = ?",
            ("test_key",)
        )
        assert result[0][0] == "test_value"

    def test_database_error_handling(self, tmp_path):
        """Testa o tratamento de erros do banco de dados"""
        model = BaseModel()
        model.db_dir = tmp_path / "nonexistent"
        model.db_path = model.db_dir / "test.db"
        
        # Força um erro ao tentar criar o diretório
        tmp_path.joinpath("nonexistent").write_text("")
        
        with pytest.raises(DatabaseInitializationError) as exc_info:
            model.init_database()
        assert "existe mas não é um diretório" in str(exc_info.value)

    def test_execute_query_with_invalid_sql(self, base_model):
        """Testa execução de query com SQL inválido"""
        with pytest.raises(DatabaseQueryError) as exc_info:
            base_model.execute_query("INVALID SQL STATEMENT")
        assert "Erro ao executar query" in str(exc_info.value)

    def test_execute_query_with_invalid_params(self, base_model):
        """Testa execução de query com parâmetros inválidos"""
        with pytest.raises(DatabaseQueryError) as exc_info:
            base_model.execute_query(
                "INSERT INTO configs (key, value) VALUES (?, ?, ?)",
                ("key", "value")
            )
        assert "Erro ao executar query" in str(exc_info.value)

    def test_database_creation(self, tmp_path):
        """Testa a criação do banco de dados e diretório"""
        model = BaseModel()
        model.db_dir = tmp_path / "new_dir"
        model.db_path = model.db_dir / "new.db"
        
        # Limpa qualquer conexão existente
        if model.conn:
            model.close()
        
        assert not model.db_dir.exists()
        model.init_database()
        
        # Verifica se o arquivo foi criado
        assert model.db_dir.exists()
        assert model.db_path.exists()
        
        # Verifica se as tabelas foram criadas
        cursor = model.conn.cursor()
        tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
        assert "configs" in [t[0] for t in tables]

    def test_database_connection_error(self, base_model, tmp_path):
        """Testa erro de conexão com banco de dados"""
        # Define um caminho inválido para o banco
        base_model.db_path = tmp_path / "invalid_dir" / "test.db"
        base_model.close()  # Fecha conexão existente
        
        # Tenta executar uma query - deve lançar exceção
        with pytest.raises(DatabaseQueryError) as exc_info:
            base_model.execute_query("SELECT 1")
        assert "unable to open database file" in str(exc_info.value)

    def test_database_commit_error(self, base_model, monkeypatch):
        """Testa erro durante operações no banco"""
        # Força um erro de sintaxe SQL
        with pytest.raises(DatabaseQueryError) as exc_info:
            base_model.execute_query("INVALID SQL")
        assert "syntax error" in str(exc_info.value).lower()

    def test_database_close(self, base_model):
        """Testa fechamento da conexão com o banco"""
        # Inicializa o banco
        base_model.init_database()
        
        # Fecha a conexão
        base_model.close()
        
        # Verifica se a conexão foi fechada
        assert base_model.conn is None
        
        # Tenta executar uma query - deve criar nova conexão
        result = base_model.execute_query("SELECT 1")
        assert result is not None

    def test_database_cleanup(self, base_model):
        """Testa limpeza do banco de dados"""
        # Inicializa o banco
        base_model.init_database()
        
        # Cria uma tabela e insere dados
        base_model.execute_query("""
            CREATE TABLE IF NOT EXISTS test_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)
        base_model.execute_query("INSERT INTO test_table (name) VALUES (?)", ("test",))
        
        # Limpa o banco
        base_model.cleanup()
        
        # Verifica se os dados foram removidos
        result = base_model.execute_query("SELECT COUNT(*) FROM test_table")
        assert result[0][0] == 0
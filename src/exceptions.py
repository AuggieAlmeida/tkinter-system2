class DatabaseError(Exception):
    """Exceção base para erros de banco de dados"""
    pass

class DatabaseInitializationError(DatabaseError):
    """Erro ao inicializar o banco de dados"""
    pass

class DatabaseQueryError(DatabaseError):
    """Erro ao executar query no banco de dados"""
    pass 
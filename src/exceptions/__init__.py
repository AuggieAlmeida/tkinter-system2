class DatabaseInitializationError(Exception):
    """Erro ao inicializar o banco de dados"""
    pass

class DatabaseQueryError(Exception):
    """Erro ao executar query no banco de dados"""
    pass

class ConfigurationError(Exception):
    """Erro relacionado às configurações"""
    pass

class GameError(Exception):
    """Erro relacionado aos jogos"""
    pass

class ToolError(Exception):
    """Erro relacionado às ferramentas"""
    pass

__all__ = [
    'DatabaseInitializationError',
    'DatabaseQueryError',
    'ConfigurationError',
    'GameError',
    'ToolError'
] 
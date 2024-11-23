from typing import Any
from loguru import logger
from src.models import ConfigModel
from src.exceptions import ConfigurationError

class SettingsController:
    def __init__(self, config_model=None):
        self.config_model = config_model or ConfigModel()
        self._theme_callbacks = []  # Lista de callbacks para atualização de tema
        self._ensure_default_settings()  # Garante configurações padrão
        
    def _ensure_default_settings(self):
        """Garante que as configurações padrão existam"""
        default_settings = {
            'theme': 'light',  # Garante que o tema padrão é 'light'
            'language': 'pt_BR',
            'window_size': ''  # Usa string vazia ao invés de None
        }
        
        current_settings = self.load_settings()
        for key, value in default_settings.items():
            if key not in current_settings:
                self.config_model.update_config(key, value)
        
    def get_theme(self) -> str:
        """Obtém o tema atual"""
        return self.config_model.get_config("theme")
        
    def set_theme(self, theme: str) -> None:
        """Define o tema e notifica os observadores"""
        self.config_model.update_config("theme", theme)
        self._notify_theme_change(theme)
        
    def add_theme_callback(self, callback: callable) -> None:
        """Adiciona um callback para ser notificado quando o tema mudar"""
        self._theme_callbacks.append(callback)
        
    def _notify_theme_change(self, theme: str) -> None:
        """Notifica todos os observadores sobre mudança de tema"""
        for callback in self._theme_callbacks:
            callback(theme)
        
    def get_window_size(self) -> str:
        """Retorna o tamanho da janela"""
        size = self.config_model.get_config('window_size')
        return size if size else None  # Converte string vazia para None
        
    def get_all_settings(self) -> dict:
        """Obtém todas as configurações"""
        return self.config_model.get_all_configs()
        
    def update_setting(self, key: str, value: Any) -> None:
        """Atualiza uma configuração"""
        self.config_model.update_config(key, str(value))
        
    def load_settings(self):
        """Carrega as configurações do banco de dados"""
        return self.config_model.get_all_configs()
        
    def save_settings(self, settings):
        """Salva as configurações no banco de dados"""
        if not self.validate_settings(settings):
            raise ValueError("Configurações inválidas")
            
        for key, value in settings.items():
            self.config_model.update_config(key, value)
        
    def validate_settings(self, settings):
        """Valida as configurações"""
        valid_themes = ['light', 'dark']
        valid_languages = ['pt_BR', 'en_US']
        
        if 'theme' in settings and settings['theme'] not in valid_themes:
            return False
        if 'language' in settings and settings['language'] not in valid_languages:
            return False
        return True

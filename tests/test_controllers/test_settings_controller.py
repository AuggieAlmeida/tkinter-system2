import pytest
from src.controllers.settings_controller import SettingsController
from src.models.config_model import ConfigModel

class TestSettingsController:
    @pytest.fixture
    def settings_controller(self, tmp_path):
        """Fixture que cria um controller com banco de dados temporário"""
        config_model = ConfigModel()
        config_model.db_dir = tmp_path
        config_model.db_path = tmp_path / "test.db"
        config_model.init_database()
        controller = SettingsController(config_model)
        return controller

    def test_load_settings(self, settings_controller):
        """Testa carregamento das configurações"""
        settings = settings_controller.load_settings()
        assert isinstance(settings, dict)
        assert settings['theme'] == 'light'
        assert settings['language'] == 'pt_BR'

    def test_save_settings(self, settings_controller):
        """Testa salvamento das configurações"""
        initial_settings = settings_controller.load_settings()
        assert initial_settings['theme'] == 'light'
        assert initial_settings['language'] == 'pt_BR'

        new_settings = {
            "theme": "dark",
            "language": "pt_BR"
        }
        settings_controller.save_settings(new_settings)
        
        saved_settings = settings_controller.load_settings()
        assert saved_settings["theme"] == "dark"
        assert saved_settings["language"] == "pt_BR"

    def test_validate_settings(self, settings_controller):
        """Testa validação das configurações"""
        valid_settings = {
            "theme": "dark",
            "language": "pt_BR"
        }
        assert settings_controller.validate_settings(valid_settings) == True

        invalid_settings = {
            "theme": "invalid",
            "language": "invalid"
        }
        assert settings_controller.validate_settings(invalid_settings) == False

    def test_partial_settings_update(self, settings_controller):
        """Testa atualização parcial das configurações"""
        # Primeiro, garante que temos as configurações padrão
        initial_settings = settings_controller.load_settings()
        assert initial_settings['language'] == 'pt_BR'
        
        # Testa atualização parcial
        settings_controller.save_settings({"theme": "dark"})
        settings = settings_controller.load_settings()
        assert settings["theme"] == "dark"
        assert settings["language"] == "pt_BR"  # mantém valor padrão

    def test_theme_management(self, settings_controller):
        """Testa gerenciamento do tema"""
        # Testa get_theme
        assert settings_controller.get_theme() == 'light'  # valor padrão
        
        # Testa set_theme com callback
        theme_changed = False
        def theme_callback(new_theme):
            nonlocal theme_changed
            theme_changed = True
            assert new_theme == 'dark'
        
        settings_controller.add_theme_callback(theme_callback)
        settings_controller.set_theme('dark')
        
        assert settings_controller.get_theme() == 'dark'
        assert theme_changed == True

    def test_window_size(self, settings_controller):
        """Testa configuração de tamanho da janela"""
        # Inicialmente deve ser None pois não é uma config padrão
        assert settings_controller.get_window_size() is None
        
        # Testa atualização
        settings_controller.update_setting('window_size', '800x600')
        assert settings_controller.get_window_size() == '800x600'

    def test_get_all_settings(self, settings_controller):
        """Testa obtenção de todas as configurações"""
        settings = settings_controller.get_all_settings()
        assert isinstance(settings, dict)
        assert settings['theme'] == 'light'
        assert settings['language'] == 'pt_BR'

    def test_update_setting(self, settings_controller):
        """Testa atualização de configuração individual"""
        # Atualiza uma configuração existente
        settings_controller.update_setting('theme', 'dark')
        assert settings_controller.get_theme() == 'dark'
        
        # Adiciona uma nova configuração
        settings_controller.update_setting('new_setting', 'value')
        settings = settings_controller.get_all_settings()
        assert settings['new_setting'] == 'value'

    def test_invalid_settings_validation(self, settings_controller):
        """Testa validação de configurações inválidas"""
        with pytest.raises(ValueError):
            settings_controller.save_settings({
                'theme': 'invalid_theme'
            })

    def test_validate_settings_complete(self, settings_controller):
        """Testa validação de configurações válidas"""
        # Testa configurações válidas
        valid_settings = {
            'theme': 'light',
            'language': 'pt_BR'
        }
        assert settings_controller.validate_settings(valid_settings) == True

        # Testa configurações parciais válidas
        assert settings_controller.validate_settings({'theme': 'dark'}) == True
        assert settings_controller.validate_settings({'language': 'en_US'}) == True
        
        # Testa configurações vazias
        assert settings_controller.validate_settings({}) == True
  
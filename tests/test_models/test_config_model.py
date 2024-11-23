import pytest
from src.models.config_model import ConfigModel

class TestConfigModel:
    @pytest.fixture
    def config_model(self, tmp_path):
        """Fixture que cria um modelo de configuração com banco de dados temporário"""
        model = ConfigModel()
        model.db_dir = tmp_path
        model.db_path = tmp_path / "test.db"
        model.init_database()
        model._ensure_default_configs()
        return model

    def test_default_config(self, config_model):
        """Testa se as configurações padrão são criadas corretamente"""
        configs = config_model.get_all_configs()
        assert configs['theme'] == 'light'
        assert configs['language'] == 'pt_BR'

    def test_get_config(self, config_model):
        """Testa obtenção de configuração específica"""
        assert config_model.get_config('theme') == 'light'
        assert config_model.get_config('language') == 'pt_BR'

    def test_update_config(self, config_model):
        """Testa atualização de configuração"""
        config_model.update_config('theme', 'dark')
        assert config_model.get_config('theme') == 'dark'

    def test_get_all_configs(self, config_model):
        """Testa obtenção de todas as configurações"""
        configs = config_model.get_all_configs()
        assert isinstance(configs, dict)
        assert len(configs) >= 2  # Pelo menos as configs padrão
        assert 'theme' in configs
        assert 'language' in configs 
import pytest
from unittest.mock import Mock, MagicMock, patch

from src.views.settings_view import SettingsView

@pytest.fixture
def mock_controller():
    """Mock para o controller"""
    return Mock()

# Mock do AppearanceModeTracker
mock_appearance_tracker = MagicMock()
mock_appearance_tracker.add = Mock()
mock_appearance_tracker.remove = Mock()
mock_appearance_tracker.get_tk_root_of_widget = Mock(return_value=None)

# Mock do StringVar
class MockStringVar:
    def __init__(self, master=None, value='', name=None):
        self.value = value
        
    def get(self):
        return self.value
        
    def set(self, value):
        self.value = value

@pytest.fixture
def mock_frame():
    frame = MagicMock()
    frame.grid = Mock()
    frame.grid_remove = Mock()
    frame.grid_forget = Mock()
    frame.grid_columnconfigure = Mock()
    return frame

@pytest.fixture
def mock_root():
    root = MagicMock()
    root.grid_rowconfigure = Mock()
    root.grid_columnconfigure = Mock()
    return root

@pytest.fixture(autouse=True)
def mock_all(mock_frame):
    with patch.multiple('src.views.settings_view.ctk',
        CTkFrame=Mock(return_value=mock_frame),
        CTkLabel=Mock(),
        CTkEntry=Mock(),
        CTkButton=Mock(),
        StringVar=MockStringVar):
        yield

@pytest.fixture
def settings_view(mock_root, mock_controller, mock_frame):
    """Cria uma instância de SettingsView para testes"""
    view = SettingsView(mock_root, mock_controller)
    return view

class TestSettingsView:
    @pytest.mark.timeout(1)
    def test_init(self, settings_view, mock_root, mock_controller, mock_frame):
        """Testa a inicialização da view"""
        assert settings_view.root == mock_root
        assert settings_view.controller == mock_controller
        assert settings_view.frame == mock_frame
        assert isinstance(settings_view.fields, dict)
        mock_frame.grid_columnconfigure.assert_called_with(1, weight=1)

    @pytest.mark.timeout(1)
    def test_create_entry(self, settings_view):
        """Testa a criação de campos de entrada"""
        with patch('src.views.settings_view.ctk.CTkEntry') as mock_entry_class:
            mock_entry = Mock()
            mock_entry_class.return_value = mock_entry
            
            entry = settings_view.create_entry(0, 0)
            
            mock_entry_class.assert_called_with(settings_view.frame)
            mock_entry.grid.assert_called_with(row=0, column=0, padx=5, pady=5, sticky="ew")
            assert entry == mock_entry

    @pytest.mark.timeout(1)
    def test_update_fields(self, settings_view):
        """Testa a atualização dos campos"""
        theme_field = Mock()
        window_size_field = Mock()
        settings_view.fields = {
            'theme': theme_field,
            'window_size': window_size_field
        }

        settings_view.update_fields({
            'theme': 'dark',
            'window_size': '800x600'
        })

        theme_field.delete.assert_called_with(0, 'end')
        theme_field.insert.assert_called_with(0, 'dark')
        window_size_field.delete.assert_called_with(0, 'end')
        window_size_field.insert.assert_called_with(0, '800x600')

    @pytest.mark.timeout(1)
    def test_get_values(self, settings_view):
        """Testa a obtenção dos valores dos campos"""
        theme_field = Mock()
        window_size_field = Mock()
        theme_field.get.return_value = 'dark'
        window_size_field.get.return_value = '800x600'
        
        settings_view.fields = {
            'theme': theme_field,
            'window_size': window_size_field
        }

        values = settings_view.get_values()
        assert values == {
            'theme': 'dark',
            'window_size': '800x600'
        }
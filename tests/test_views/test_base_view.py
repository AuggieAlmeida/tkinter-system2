import pytest
from unittest.mock import Mock, MagicMock, patch
from src.views.base_view import BaseView

@pytest.fixture
def mock_controller():
    """Mock para o controller"""
    return Mock()

@pytest.fixture
def mock_frame():
    frame = MagicMock()
    frame.grid = Mock()
    frame.grid_remove = Mock()
    frame.grid_forget = Mock()
    return frame

@pytest.fixture
def mock_root():
    root = MagicMock()
    root.grid_rowconfigure = Mock()
    root.grid_columnconfigure = Mock()
    return root

@pytest.fixture
def mock_ctk():
    with patch('src.views.base_view.ctk') as mock_ctk:
        mock_ctk.CTkFrame = Mock()
        mock_ctk.CTkLabel = Mock()
        mock_ctk.CTkButton = Mock()
        yield mock_ctk

@pytest.fixture
def base_view(mock_root, mock_controller, mock_frame, mock_ctk):
    mock_ctk.CTkFrame.return_value = mock_frame
    view = BaseView(mock_root, mock_controller)
    return view

class TestBaseView:
    def test_init(self, base_view, mock_root, mock_controller, mock_frame):
        """Testa a inicialização da view"""
        assert base_view.root == mock_root
        assert base_view.controller == mock_controller
        assert base_view.frame == mock_frame
        mock_frame.grid.assert_called_with(row=0, column=0, sticky="nsew")
        mock_root.grid_rowconfigure.assert_called_with(0, weight=1)
        mock_root.grid_columnconfigure.assert_called_with(0, weight=1)

    def test_show_hide(self, base_view, mock_frame):
        """Testa os métodos show e hide"""
        base_view.show()
        mock_frame.grid.assert_called_with()

        base_view.hide()
        mock_frame.grid_remove.assert_called_with()

    def test_create_label(self, base_view, mock_ctk):
        """Testa a criação de label"""
        label = base_view.create_label("Test", 0, 0)
        mock_ctk.CTkLabel.assert_called_with(base_view.frame, text="Test")
        label.grid.assert_called_with(row=0, column=0, padx=5, pady=5)

    def test_create_button(self, base_view, mock_ctk):
        """Testa a criação de botão"""
        command = Mock()
        button = base_view.create_button("Test", command, 0, 0)
        mock_ctk.CTkButton.assert_called_with(base_view.frame, text="Test", command=command)
        button.grid.assert_called_with(row=0, column=0, padx=5, pady=5) 
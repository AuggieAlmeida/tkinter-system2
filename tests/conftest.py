import pytest
import sys
from pathlib import Path
from unittest.mock import MagicMock

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.append(str(Path(__file__).parent.parent))

@pytest.fixture
def mock_ctk():
    """Mock para o CustomTkinter"""
    mock = MagicMock()
    mock.StringVar.return_value = MagicMock()
    mock.CTkFrame.return_value = MagicMock()
    mock.CTkLabel.return_value = MagicMock()
    mock.CTkButton.return_value = MagicMock()
    mock.CTkSwitch.return_value = MagicMock()
    return mock

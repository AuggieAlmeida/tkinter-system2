import os
import sys
from pathlib import Path
from loguru import logger
import customtkinter as ctk
from dotenv import load_dotenv

from src.controllers import SettingsController
from src.views import (
    MainView,
    GamesView,
    SettingsView,
    SidebarView,
    ToolsView
)
from src.exceptions import DatabaseInitializationError

# Configuração do logger
logger.remove()
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="DEBUG"
)
logger.add("logs/app.log", rotation="500 MB", level="INFO")

class DevGameLauncher:
    def __init__(self):
        # Carrega variáveis de ambiente
        load_dotenv()
        
        # Inicializa controllers
        self.settings_controller = SettingsController()
        
        # Configuração inicial do CustomTkinter
        self.theme = self.settings_controller.get_theme()
        ctk.set_appearance_mode(self.theme)
        ctk.set_default_color_theme("blue")
        
        # Criação da janela principal
        self.root = ctk.CTk()
        self.root.title(os.getenv("APP_NAME", "DevGameLauncher"))
        self.root.geometry(os.getenv("WINDOW_SIZE", "1280x720"))
        
        # Configura a interface
        self.setup_ui()

    def setup_ui(self):
        """Configura a interface do usuário"""
        # Container principal
        self.container = ctk.CTkFrame(self.root)
        self.container.pack(fill="both", expand=True)
        self.container.grid_columnconfigure(1, weight=1)
        self.container.grid_rowconfigure(0, weight=1)

        # Área de conteúdo
        self.content_frame = ctk.CTkFrame(self.container)
        self.content_frame.grid(row=0, column=1, sticky="nsew")
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)

        # Configura as views
        self.setup_views()
        
        # Sidebar (depois das views para ter acesso a elas)
        self.sidebar = SidebarView(self.container, self)
        self.sidebar.frame.grid(row=0, column=0, sticky="nsew")

    def setup_views(self):
        """Configura as views da aplicação"""
        # Área principal
        self.main_area = MainView(self.content_frame, self)
        self.main_area.frame.grid(row=0, column=0, sticky="nsew")
        
        # Views secundárias
        self.games_view = GamesView(self.content_frame, self)
        self.games_view.frame.grid(row=0, column=0, sticky="nsew")
        
        self.settings_view = SettingsView(self.content_frame, self)
        self.settings_view.frame.grid(row=0, column=0, sticky="nsew")
        
        self.tools_view = ToolsView(self.content_frame, self)
        self.tools_view.frame.grid(row=0, column=0, sticky="nsew")
        
        # Inicialmente, esconde todas as views exceto a principal
        self.games_view.hide()
        self.settings_view.hide()
        self.tools_view.hide()

    def run(self):
        """Inicia a aplicação"""
        logger.info("Iniciando DevGameLauncher")
        self.root.mainloop()

def main():
    try:
        # Cria diretórios necessários
        Path("logs").mkdir(exist_ok=True)
        
        # Inicia a aplicação
        app = DevGameLauncher()
        app.run()
        
    except Exception as e:
        logger.error(f"Erro ao iniciar a aplicação: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
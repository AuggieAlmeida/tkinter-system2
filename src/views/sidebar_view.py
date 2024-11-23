from loguru import logger
from .base_view import BaseView
import customtkinter as ctk

class SidebarView(BaseView):
    def __init__(self, master, controller):
        super().__init__(master, controller)
        
        # Configuração do frame
        self.frame.configure(width=200)
        self.frame.grid_rowconfigure(4, weight=1)  # Espaço flexível
        
        # Cores específicas da sidebar
        self.button_colors = {
            'active': {'fg': '#1f538d', 'hover': '#1a4572'},  # Azul mais escuro
            'inactive': {'fg': '#2b2b2b', 'hover': '#3b3b3b'}  # Cinza escuro
        }
        
        # Logo/Título
        self.create_label(
            "DevGameLauncher",
            row=0,
            column=0,
            font_key='title',
            padx=20,
            pady=20
        )
        
        # Botões de navegação
        self.buttons = {}
        
        # Principal
        self.buttons["Principal"] = self.create_button(
            "Principal",
            command=lambda: self.navigate_to("Principal"),
            row=1,
            column=0,
            padx=20,
            pady=10,
            width=160
        )
        
        # Jogos
        self.buttons["Jogos"] = self.create_button(
            "Jogos",
            command=lambda: self.navigate_to("Jogos"),
            row=2,
            column=0,
            padx=20,
            pady=10,
            width=160
        )
        
        # Ferramentas
        self.buttons["Ferramentas"] = self.create_button(
            "Ferramentas",
            command=lambda: self.navigate_to("Ferramentas"),
            row=3,
            column=0,
            padx=20,
            pady=10,
            width=160
        )
        
        # Configurações
        self.buttons["Configurações"] = self.create_button(
            "Configurações",
            command=lambda: self.navigate_to("Configurações"),
            row=5,
            column=0,
            padx=20,
            pady=10,
            width=160
        )
        
        # Define o botão inicial como ativo
        self.set_active("Principal")

    def navigate_to(self, view_name: str):
        """Gerencia a navegação entre as views"""
        logger.info(f"Navegando para: {view_name}")
        
        # Mapeia os nomes das views para os atributos do controller
        view_map = {
            "Principal": self.controller.main_area,
            "Jogos": self.controller.games_view,
            "Ferramentas": self.controller.tools_view,
            "Configurações": self.controller.settings_view
        }
        
        # Esconde todas as views
        for view in view_map.values():
            view.hide()
        
        # Mostra a view selecionada
        view_map[view_name].show()
        
        # Atualiza o botão ativo
        self.set_active(view_name)
    
    def set_active(self, button_name: str):
        """Define qual botão está ativo"""
        for name, button in self.buttons.items():
            if name == button_name:
                button.configure(
                    fg_color=self.button_colors['active']['fg'],
                    hover_color=self.button_colors['active']['hover']
                )
            else:
                button.configure(
                    fg_color=self.button_colors['inactive']['fg'],
                    hover_color=self.button_colors['inactive']['hover']
                ) 
import customtkinter as ctk
from .base_view import BaseView
from loguru import logger

class SettingsView(BaseView):
    def __init__(self, master, controller):
        super().__init__(master, controller)
        
        # Dicionário para armazenar os campos de configuração
        self.fields = {}
        
        # Configuração do grid principal
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        
        # Título
        self.create_label(
            "Configurações",
            row=0,
            column=0,
            font_key='title',
            pady=self.padding['xlarge']
        )
        
        # Container principal
        settings_frame = self.create_frame(row=1, column=0, sticky="nsew")
        settings_frame.grid_columnconfigure(1, weight=1)  # Coluna dos campos expande
        
        # Temas
        self.create_label("Tema:", row=0, column=0, parent=settings_frame)
        self.fields['theme'] = self.create_combobox(
            row=0,
            column=1,
            values=["Claro", "Escuro", "Sistema"],
            default="Sistema",
            command=self.on_theme_change,
            parent=settings_frame
        )
        
        # Idioma
        self.create_label("Idioma:", row=1, column=0, parent=settings_frame)
        self.fields['language'] = self.create_combobox(
            row=1,
            column=1,
            values=["Português", "English", "Español"],
            default="Português",
            command=self.on_language_change,
            parent=settings_frame
        )
        
        # Diretório dos jogos
        self.create_label("Diretório dos Jogos:", row=2, column=0, parent=settings_frame)
        self.fields['games_dir'] = self.create_entry(
            row=2,
            column=1,
            placeholder="Caminho para a pasta de jogos",
            parent=settings_frame
        )
        
        # Iniciar com o sistema
        self.fields['autostart'] = self.create_switch(
            "Iniciar com o sistema",
            row=3,
            column=0,
            columnspan=2,
            command=self.on_autostart_change,
            parent=settings_frame
        )
        
        # Botões de ação
        buttons_frame = self.create_frame(row=2, column=0)
        buttons_frame.grid_columnconfigure((0, 1), weight=1)
        
        self.create_button(
            "Salvar",
            command=self.save_settings,
            row=0,
            column=0,
            color_key='primary',
            parent=buttons_frame
        )
        
        self.create_button(
            "Cancelar",
            command=self.load_settings,
            row=0,
            column=1,
            color_key='secondary',
            parent=buttons_frame
        )
    
    def on_theme_change(self, choice):
        """Callback quando o tema é alterado"""
        logger.info(f"Tema alterado para: {choice}")
        # TODO: Implementar mudança de tema
    
    def on_language_change(self, choice):
        """Callback quando o idioma é alterado"""
        logger.info(f"Idioma alterado para: {choice}")
        # TODO: Implementar mudança de idioma
    
    def on_autostart_change(self):
        """Callback quando a opção de iniciar com o sistema é alterada"""
        value = self.fields['autostart'].get()
        logger.info(f"Iniciar com o sistema: {value}")
        # TODO: Implementar autostart
    
    def save_settings(self):
        """Salva as configurações"""
        settings = {
            'theme': self.fields['theme'].get(),
            'language': self.fields['language'].get(),
            'games_dir': self.fields['games_dir'].get(),
            'autostart': self.fields['autostart'].get()
        }
        logger.info(f"Salvando configurações: {settings}")
        # TODO: Implementar salvamento
    
    def load_settings(self):
        """Carrega as configurações salvas"""
        logger.info("Carregando configurações")
        # TODO: Implementar carregamento
        

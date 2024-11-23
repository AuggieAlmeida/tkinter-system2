import customtkinter as ctk
from .base_view import BaseView
from loguru import logger


class GamesView(BaseView):
    def __init__(self, master, controller):
        super().__init__(master, controller)
        
        # Configuração do grid principal
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        
        # Título
        self.create_label(
            "Biblioteca de Jogos",
            row=0,
            column=0,
            font_key='title',
            pady=self.padding['xlarge']
        )
        
        # Container principal
        games_frame = self.create_frame(row=1, column=0, sticky="nsew")
        games_frame.grid_columnconfigure(0, weight=1)
        games_frame.grid_rowconfigure(1, weight=1)
        
        # Barra de pesquisa
        search_frame = self.create_frame(row=0, column=0, parent=games_frame)
        search_frame.grid_columnconfigure(0, weight=1)
        
        self.search_entry = self.create_entry(
            row=0,
            column=0,
            placeholder="Pesquisar jogos...",
            parent=search_frame
        )
        
        self.create_button(
            "Buscar",
            command=self.search_games,
            row=0,
            column=1,
            parent=search_frame
        )
        
        # Lista de jogos
        self.games_list = self.create_textbox(
            row=1,
            column=0,
            parent=games_frame
        )
        
        # Barra de ações
        actions_frame = self.create_frame(row=2, column=0, parent=games_frame)
        actions_frame.grid_columnconfigure((0, 1, 2), weight=1)
        
        self.create_button(
            "Adicionar Jogo",
            command=self.add_game,
            row=0,
            column=0,
            parent=actions_frame
        )
        
        self.create_button(
            "Editar Jogo",
            command=self.edit_game,
            row=0,
            column=1,
            parent=actions_frame
        )
        
        self.create_button(
            "Remover Jogo",
            command=self.remove_game,
            row=0,
            column=2,
            parent=actions_frame,
            color_key='danger'
        )
        
        # Carregar jogos iniciais
        self.load_games()
    
    def create_textbox(self, row: int, column: int, parent=None) -> ctk.CTkTextbox:
        """Cria uma caixa de texto com barra de rolagem"""
        parent = parent or self.frame
        
        textbox = ctk.CTkTextbox(
            parent,
            font=self.fonts['text'],
            wrap="word"
        )
        textbox.grid(
            row=row,
            column=column,
            padx=self.padding['medium'],
            pady=self.padding['medium'],
            sticky="nsew"
        )
        return textbox
    
    def search_games(self):
        """Pesquisa jogos com base no texto inserido"""
        search_text = self.search_entry.get()
        logger.info(f"Pesquisando jogos: {search_text}")
        # TODO: Implementar pesquisa real
        
    def add_game(self):
        """Abre diálogo para adicionar novo jogo"""
        logger.info("Adicionando novo jogo")
        # TODO: Implementar adição de jogo
        
    def edit_game(self):
        """Abre diálogo para editar jogo selecionado"""
        logger.info("Editando jogo")
        # TODO: Implementar edição de jogo
        
    def remove_game(self):
        """Remove jogo selecionado"""
        logger.info("Removendo jogo")
        # TODO: Implementar remoção de jogo
        
    def load_games(self):
        """Carrega lista de jogos"""
        # Dados de exemplo
        games = [
            "• The Witcher 3",
            "• Cyberpunk 2077",
            "• Red Dead Redemption 2",
            "• God of War",
            "• Elden Ring"
        ]
        
        self.games_list.delete("1.0", "end")
        for game in games:
            self.games_list.insert("end", f"{game}\n")

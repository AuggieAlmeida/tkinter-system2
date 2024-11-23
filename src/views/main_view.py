import customtkinter as ctk
from .base_view import BaseView
from loguru import logger

class MainView(BaseView):
    def __init__(self, master, controller):
        super().__init__(master, controller)
        
        # Configuração do grid
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        
        # Título
        self.create_label(
            "Bem-vindo ao DevGameLauncher",
            row=0,
            column=0,
            font_key='title',
            pady=self.padding['xlarge']
        )
        
        # Conteúdo principal
        main_frame = self.create_frame(row=1, column=0, sticky="nsew")
        main_frame.grid_columnconfigure(0, weight=1)
        
        # Estatísticas
        stats_frame = self.create_frame(row=0, column=0, parent=main_frame)
        stats_frame.grid_columnconfigure((0, 1, 2), weight=1)
        
        self.create_label(
            "Total de Jogos\n0",
            row=0,
            column=0,
            parent=stats_frame
        )
        
        self.create_label(
            "Jogados Recentemente\n0",
            row=0,
            column=1,
            parent=stats_frame
        )
        
        self.create_label(
            "Tempo Total\n0h",
            row=0,
            column=2,
            parent=stats_frame
        )
        
        # Jogos recentes
        self.create_label(
            "Jogados Recentemente",
            row=1,
            column=0,
            font_key='subtitle',
            pady=self.padding['large'],
            parent=main_frame
        )
        
        recent_games = self.create_scrollable_frame(
            row=2,
            column=0,
            parent=main_frame
        )
        
        # Lista de exemplo
        for i in range(5):
            game_frame = self.create_frame(
                row=i,
                column=0,
                parent=recent_games
            )
            game_frame.grid_columnconfigure(1, weight=1)
            
            self.create_label(
                f"Jogo {i+1}",
                row=0,
                column=0,
                parent=game_frame
            )
            
            self.create_label(
                "2h jogadas",
                row=0,
                column=1,
                parent=game_frame
            )
            
            self.create_button(
                "Jogar",
                command=lambda: print(f"Jogando {i+1}"),
                row=0,
                column=2,
                parent=game_frame
            )
    
    def create_stats_section(self, parent_frame):
        """Cria a seção de estatísticas"""
        parent_frame.grid_columnconfigure((0, 1, 2), weight=1)
        
        # Total de Jogos
        self.create_stat_box(
            parent_frame,
            "Total de Jogos",
            "0",
            row=0,
            column=0
        )
        
        # Tempo Total Jogado
        self.create_stat_box(
            parent_frame,
            "Tempo Total",
            "0h",
            row=0,
            column=1
        )
        
        # Último Jogo
        self.create_stat_box(
            parent_frame,
            "Último Jogo",
            "Nenhum",
            row=0,
            column=2
        )
    
    def create_stat_box(self, parent, title, value, row, column):
        """Cria uma caixa de estatística"""
        frame = ctk.CTkFrame(parent)
        frame.grid(
            row=row,
            column=column,
            padx=self.padding['medium'],
            pady=self.padding['medium'],
            sticky="nsew"
        )
        
        # Título da estatística
        self.create_label(
            title,
            row=0,
            column=0,
            font_key='subtitle',
            parent=frame
        )
        
        # Valor da estatística
        self.create_label(
            value,
            row=1,
            column=0,
            font_key='text',
            parent=frame
        )
    
    def create_recent_games_section(self, parent_frame):
        """Cria a seção de jogos recentes"""
        parent_frame.grid_rowconfigure(1, weight=1)
        parent_frame.grid_columnconfigure(0, weight=1)
        
        # Título da seção
        self.create_label(
            "Jogos Recentes",
            row=0,
            column=0,
            font_key='subtitle',
            parent=parent_frame
        )
        
        # Lista de jogos recentes
        self.games_list = ctk.CTkTextbox(
            parent_frame,
            wrap="word",
            height=200
        )
        self.games_list.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=self.padding['medium'],
            pady=self.padding['medium']
        )
        
        # Carrega jogos recentes
        self.load_recent_games()
    
    def load_recent_games(self):
        """Carrega a lista de jogos recentes"""
        # TODO: Implementar carregamento real dos jogos recentes
        self.games_list.delete(1.0, "end")
        
        # Dados de exemplo
        recent_games = [
            "• Jogo 1 - Jogado há 2 dias",
            "• Jogo 2 - Jogado há 5 dias",
            "• Jogo 3 - Jogado há 1 semana",
        ]
        
        for game in recent_games:
            self.games_list.insert("end", f"{game}\n")
    
    def update_stats(self, stats):
        """Atualiza as estatísticas"""
        # TODO: Implementar atualização real das estatísticas
        pass 
import customtkinter as ctk
from typing import Any, Optional, List, Dict
from loguru import logger
from PIL import Image

class BaseView:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        
        # Cria o frame principal da view
        self.frame = ctk.CTkFrame(master)
        
        # Configurações padrão
        self.padding = {
            'small': 5,
            'medium': 10,
            'large': 20,
            'xlarge': 40
        }
        
        self.fonts = {
            'title': ('Helvetica', 24, 'bold'),
            'subtitle': ('Helvetica', 18, 'bold'),
            'text': ('Helvetica', 12),
            'small': ('Helvetica', 10)
        }
        
        self.colors = {
            'primary': '#1f538d',      # Azul principal
            'secondary': '#2b2b2b',    # Cinza escuro
            'danger': '#8b0000',       # Vermelho escuro
            'success': '#006400',      # Verde escuro
            'warning': '#856404',      # Amarelo escuro
            'info': '#0c5460'         # Azul escuro
        }
        
        # Inicialmente oculto
        self.hide()

    def show(self):
        """Mostra a view"""
        self.frame.grid()

    def hide(self):
        """Esconde a view"""
        self.frame.grid_remove()

    def create_label(self, text: str, row: int, column: int, 
                    font_key: str = 'text', columnspan: int = 1, 
                    padx: Optional[int] = None, pady: Optional[int] = None,
                    parent: Optional[ctk.CTkFrame] = None) -> ctk.CTkLabel:
        """
        Cria um label com configurações padrão
        
        Args:
            text: Texto do label
            row: Linha no grid
            column: Coluna no grid
            font_key: Chave da fonte a ser usada (title, subtitle, text)
            columnspan: Número de colunas que o label ocupa
            padx: Padding horizontal
            pady: Padding vertical
            parent: Frame pai do label (se None, usa self.frame)
        """
        parent = parent or self.frame
        
        label = ctk.CTkLabel(
            parent,
            text=text,
            font=self.fonts.get(font_key, self.fonts['text'])
        )
        label.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            padx=padx or self.padding['medium'],
            pady=pady or self.padding['medium'],
            sticky="w"
        )
        return label

    def create_button(
        self,
        text: str,
        command: callable,
        row: int,
        column: int,
        columnspan: int = 1,
        padx: Optional[int] = None,
        pady: Optional[int] = None,
        width: int = 120,
        height: int = 32,
        color_key: str = 'secondary',
        parent: Optional[ctk.CTkFrame] = None
    ) -> ctk.CTkButton:
        """
        Cria um botão com configurações padrão
        
        Args:
            text: Texto do botão
            command: Função a ser chamada quando o botão for clicado
            row: Linha no grid
            column: Coluna no grid
            columnspan: Número de colunas que o botão ocupa
            padx: Padding horizontal
            pady: Padding vertical
            width: Largura do botão
            height: Altura do botão
            color_key: Chave da cor no dicionário de cores
            parent: Frame pai (se None, usa self.frame)
        """
        parent = parent or self.frame
        
        button = ctk.CTkButton(
            parent,
            text=text,
            command=command,
            width=width,
            height=height,
            font=self.fonts['text'],
            fg_color=self.colors[color_key],
            hover_color=self.colors[color_key]
        )
        
        button.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            padx=padx or self.padding['medium'],
            pady=pady or self.padding['medium'],
            sticky="ew"
        )
        
        return button

    def create_frame(self, row: int, column: int,
                    columnspan: int = 1,
                    padx: Optional[int] = None,
                    pady: Optional[int] = None,
                    sticky: str = "nsew",
                    parent: Optional[ctk.CTkFrame] = None) -> ctk.CTkFrame:
        """
        Cria um frame com configurações padrão
        
        Args:
            row: Linha no grid
            column: Coluna no grid
            columnspan: Número de colunas que o frame ocupa
            padx: Padding horizontal
            pady: Padding vertical
            sticky: Direções de expansão do frame
            parent: Frame pai (se None, usa self.frame)
        """
        parent = parent or self.frame
        
        frame = ctk.CTkFrame(parent)
        frame.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            padx=padx or self.padding['medium'],
            pady=pady or self.padding['medium'],
            sticky=sticky
        )
        
        return frame

    def show_message(self, message: str, status: str = "info"):
        """
        Mostra uma mensagem temporária para o usuário
        
        Args:
            message: Mensagem a ser mostrada
            status: Tipo da mensagem (success, error, warning, info)
        """
        logger.info(f"Mensagem ({status}): {message}")
        # TODO: Implementar sistema de mensagens visuais

    def configure_grid(self, rows: List[int] = None, columns: List[int] = None,
                      weight: int = 1, parent: Optional[ctk.CTkFrame] = None):
        """
        Configura o peso das linhas e colunas para expansão
        
        Args:
            rows: Lista de índices das linhas para configurar
            columns: Lista de índices das colunas para configurar
            weight: Peso para expansão
            parent: Frame a ser configurado (se None, usa self.frame)
        """
        parent = parent or self.frame
        
        if rows:
            for row in rows:
                parent.grid_rowconfigure(row, weight=weight)
        
        if columns:
            for column in columns:
                parent.grid_columnconfigure(column, weight=weight)

    def create_combobox(self, row: int, column: int,
                       values: list = None,
                       default: str = "",
                       width: int = 200,
                       columnspan: int = 1,
                       padx: Optional[int] = None,
                       pady: Optional[int] = None,
                       command: Optional[callable] = None,
                       parent: Optional[ctk.CTkFrame] = None) -> ctk.CTkComboBox:
        """
        Cria um combobox com configurações padrão
        
        Args:
            row: Linha no grid
            column: Coluna no grid
            values: Lista de valores para o combobox
            default: Valor padrão selecionado
            width: Largura do combobox
            columnspan: Número de colunas que o combobox ocupa
            padx: Padding horizontal
            pady: Padding vertical
            command: Função a ser chamada quando o valor mudar
            parent: Frame pai do combobox (se None, usa self.frame)
        """
        parent = parent or self.frame
        values = values or []
        
        combobox = ctk.CTkComboBox(
            parent,
            values=values,
            width=width,
            font=self.fonts['text'],
            command=command
        )
        
        if default:
            combobox.set(default)
        
        combobox.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            padx=padx or self.padding['medium'],
            pady=pady or self.padding['medium'],
            sticky="ew"
        )
        
        return combobox

    def create_entry(self, row: int, column: int,
                    placeholder: str = "",
                    width: int = 200,
                    columnspan: int = 1,
                    padx: Optional[int] = None,
                    pady: Optional[int] = None,
                    parent: Optional[ctk.CTkFrame] = None) -> ctk.CTkEntry:
        """
        Cria um campo de entrada com configurações padrão
        
        Args:
            row: Linha no grid
            column: Coluna no grid
            placeholder: Texto de placeholder
            width: Largura do campo
            columnspan: Número de colunas que o campo ocupa
            padx: Padding horizontal
            pady: Padding vertical
            parent: Frame pai do campo (se None, usa self.frame)
        """
        parent = parent or self.frame
        
        entry = ctk.CTkEntry(
            parent,
            placeholder_text=placeholder,
            width=width,
            font=self.fonts['text']
        )
        
        entry.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            padx=padx or self.padding['medium'],
            pady=pady or self.padding['medium'],
            sticky="ew"
        )
        
        return entry

    def create_switch(self, text: str, row: int, column: int,
                     command: callable = None,
                     default: bool = False,
                     columnspan: int = 1,
                     padx: Optional[int] = None,
                     pady: Optional[int] = None,
                     parent: Optional[ctk.CTkFrame] = None) -> ctk.CTkSwitch:
        """
        Cria um switch com configurações padrão
        
        Args:
            text: Texto do switch
            row: Linha no grid
            column: Coluna no grid
            command: Função a ser chamada quando o switch mudar
            default: Estado inicial do switch
            columnspan: Número de colunas que o switch ocupa
            padx: Padding horizontal
            pady: Padding vertical
            parent: Frame pai do switch (se None, usa self.frame)
        """
        parent = parent or self.frame
        
        switch = ctk.CTkSwitch(
            parent,
            text=text,
            command=command,
            font=self.fonts['text']
        )
        
        if default:
            switch.select()
        else:
            switch.deselect()
        
        switch.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            padx=padx or self.padding['medium'],
            pady=pady or self.padding['medium'],
            sticky="w"
        )
        
        return switch

    def create_textbox(self, row: int, column: int,
                      width: int = 200,
                      height: int = 200,
                      columnspan: int = 1,
                      padx: Optional[int] = None,
                      pady: Optional[int] = None,
                      parent: Optional[ctk.CTkFrame] = None) -> ctk.CTkTextbox:
        """
        Cria uma caixa de texto com configurações padrão
        
        Args:
            row: Linha no grid
            column: Coluna no grid
            width: Largura da caixa de texto
            height: Altura da caixa de texto
            columnspan: Número de colunas que a caixa ocupa
            padx: Padding horizontal
            pady: Padding vertical
            parent: Frame pai (se None, usa self.frame)
        """
        parent = parent or self.frame
        
        textbox = ctk.CTkTextbox(
            parent,
            width=width,
            height=height,
            font=self.fonts['text']
        )
        textbox.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            padx=padx or self.padding['medium'],
            pady=pady or self.padding['medium'],
            sticky="nsew"
        )
        
        return textbox

    def create_scrollable_frame(
        self,
        row: int,
        column: int,
        columnspan: int = 1,
        padx: Optional[int] = None,
        pady: Optional[int] = None,
        sticky: str = "nsew",
        parent: Optional[ctk.CTkFrame] = None
    ) -> ctk.CTkScrollableFrame:
        """
        Cria um frame com barra de rolagem
        """
        parent = parent or self.frame
        
        scrollable_frame = ctk.CTkScrollableFrame(
            parent,
            fg_color="transparent"
        )
        scrollable_frame.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            padx=padx or self.padding['medium'],
            pady=pady or self.padding['medium'],
            sticky=sticky
        )
        
        return scrollable_frame

    def create_segmented_button(
        self,
        row: int,
        column: int,
        values: List[str],
        command: callable = None,
        columnspan: int = 1,
        padx: Optional[int] = None,
        pady: Optional[int] = None,
        parent: Optional[ctk.CTkFrame] = None
    ) -> ctk.CTkSegmentedButton:
        """
        Cria um grupo de botões segmentados
        """
        parent = parent or self.frame
        
        segmented = ctk.CTkSegmentedButton(
            parent,
            values=values,
            command=command,
            font=self.fonts['text']
        )
        segmented.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            padx=padx or self.padding['medium'],
            pady=pady or self.padding['medium'],
            sticky="ew"
        )
        
        return segmented

    def create_progressbar(
        self,
        row: int,
        column: int,
        width: int = 200,
        columnspan: int = 1,
        padx: Optional[int] = None,
        pady: Optional[int] = None,
        parent: Optional[ctk.CTkFrame] = None
    ) -> ctk.CTkProgressBar:
        """
        Cria uma barra de progresso
        """
        parent = parent or self.frame
        
        progressbar = ctk.CTkProgressBar(
            parent,
            width=width
        )
        progressbar.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            padx=padx or self.padding['medium'],
            pady=pady or self.padding['medium'],
            sticky="ew"
        )
        
        return progressbar

    def create_image(
        self,
        path: str,
        size: tuple,
        row: int,
        column: int,
        columnspan: int = 1,
        padx: Optional[int] = None,
        pady: Optional[int] = None,
        parent: Optional[ctk.CTkFrame] = None
    ) -> ctk.CTkImage:
        """
        Cria e exibe uma imagem
        """
        parent = parent or self.frame
        
        image = ctk.CTkImage(
            light_image=Image.open(path),
            dark_image=Image.open(path),
            size=size
        )
        
        label = ctk.CTkLabel(
            parent,
            image=image,
            text=""
        )
        label.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            padx=padx or self.padding['medium'],
            pady=pady or self.padding['medium']
        )
        
        return image

    def create_tabview(
        self,
        row: int,
        column: int,
        tabs: List[str],
        columnspan: int = 1,
        padx: Optional[int] = None,
        pady: Optional[int] = None,
        parent: Optional[ctk.CTkFrame] = None
    ) -> ctk.CTkTabview:
        """
        Cria uma view com abas
        """
        parent = parent or self.frame
        
        tabview = ctk.CTkTabview(
            parent,
            font=self.fonts['text']
        )
        
        for tab in tabs:
            tabview.add(tab)
            
        tabview.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            padx=padx or self.padding['medium'],
            pady=pady or self.padding['medium'],
            sticky="nsew"
        )
        
        return tabview

    def create_dialog(
        self,
        title: str,
        message: str = "",
        buttons: List[Dict[str, Any]] = None
    ) -> ctk.CTkInputDialog:
        """
        Cria um diálogo modal
        
        Args:
            title: Título do diálogo
            message: Mensagem opcional
            buttons: Lista de dicionários com configurações dos botões
                    [{"text": "OK", "command": callback, "color": "primary"}]
        """
        dialog = ctk.CTkInputDialog(
            title=title,
            text=message
        )
        
        if buttons:
            buttons_frame = self.create_frame(
                row=len(buttons),
                column=0,
                parent=dialog
            )
            
            for i, btn in enumerate(buttons):
                self.create_button(
                    text=btn["text"],
                    command=btn["command"],
                    row=0,
                    column=i,
                    color_key=btn.get("color", "primary"),
                    parent=buttons_frame
                )
        
        return dialog

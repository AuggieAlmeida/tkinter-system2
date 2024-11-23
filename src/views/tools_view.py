from .base_view import BaseView

class ToolsView(BaseView):
    def __init__(self, master, controller):
        super().__init__(master, controller)
        
        # Configuração do grid
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        
        # Título
        self.create_label(
            "Ferramentas",
            row=0,
            column=0,
            font_key='title',
            pady=self.padding['xlarge']
        )

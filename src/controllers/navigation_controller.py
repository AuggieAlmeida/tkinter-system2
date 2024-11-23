from loguru import logger

class NavigationController:
    def __init__(self, views):
        self.views = views
        self.current_view = None
    
    def navigate_to(self, view_name: str):
        """Navega para uma view específica"""
        logger.info(f"Navegando para: {view_name}")
        
        # Esconde todas as views
        for view in self.views.values():
            view.hide()
        
        # Mostra a view selecionada
        self.views[view_name].show()
        self.current_view = view_name 
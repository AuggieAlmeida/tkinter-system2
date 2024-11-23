from .base_controller import BaseController
from src.models import ToolModel
from src.exceptions import ToolError

class ToolsController(BaseController):
    def __init__(self):
        self.model = ToolModel()
        super().__init__(self.model)
    
    def get_all_tools(self):
        """Retorna todas as ferramentas"""
        try:
            return self.model.get_all_tools()
        except Exception as e:
            self.handle_error(e, "Erro ao buscar ferramentas")
    
    def add_tool(self, name: str, path: str):
        """Adiciona uma nova ferramenta"""
        try:
            return self.model.add_tool(name, path)
        except Exception as e:
            self.handle_error(e, "Erro ao adicionar ferramenta")
    
    def remove_tool(self, tool_id: int):
        """Remove uma ferramenta"""
        try:
            return self.model.remove_tool(tool_id)
        except Exception as e:
            self.handle_error(e, "Erro ao remover ferramenta")
    
    def update_tool(self, tool_id: int, name: str = None, path: str = None):
        """Atualiza uma ferramenta"""
        try:
            return self.model.update_tool(tool_id, name, path)
        except Exception as e:
            self.handle_error(e, "Erro ao atualizar ferramenta")


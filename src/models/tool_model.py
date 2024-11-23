from .base_model import BaseModel

class ToolModel(BaseModel):
    def get_all_tools(self):
        """Retorna todas as ferramentas"""
        query = "SELECT * FROM tools ORDER BY name ASC"
        return self.execute_query(query)
    
    def add_tool(self, name: str, path: str):
        """Adiciona uma nova ferramenta"""
        query = """
        INSERT INTO tools (name, path)
        VALUES (?, ?)
        """
        return self.execute_query(query, (name, path))
    
    def remove_tool(self, tool_id: int):
        """Remove uma ferramenta"""
        query = "DELETE FROM tools WHERE id = ?"
        return self.execute_query(query, (tool_id,))
    
    def update_tool(self, tool_id: int, name: str = None, path: str = None):
        """Atualiza uma ferramenta"""
        updates = []
        params = []
        
        if name is not None:
            updates.append("name = ?")
            params.append(name)
        if path is not None:
            updates.append("path = ?")
            params.append(path)
            
        if not updates:
            return
            
        params.append(tool_id)
        query = f"""
        UPDATE tools 
        SET {', '.join(updates)}
        WHERE id = ?
        """
        return self.execute_query(query, tuple(params))

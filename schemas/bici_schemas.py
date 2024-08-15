from typing import Optional
from pydantic import BaseModel

def create_bici(BaseModel):
    id:int
    modelo:str
    
def obtener_bici(BaseModel):
    id:int
    modelo:str
    
def actualizar_bici(BaseModel):
    id:int  
    modelo:Optional[str]
    
def eliminar_bici():
    id:int
from typing import Optional
from pydantic import BaseModel

def create_user(BaseModel):
    id:int
    nombre:str
    email:str
    telefono:int
    direccion:str
    
def obtener_user(BaseModel):
    id:int
    nombre:str
    direccion:Optional[str]
    
def actualizar_user(BaseModel):
    id:int  
    nombre:Optional[str]
    email:Optional[str]
    telefono:Optional[int]
    direccion:Optional[str]
    
def eliminar_user():
    id:int
    

    
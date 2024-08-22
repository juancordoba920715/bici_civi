from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Boolean



class create_bici(BaseModel):
    id:int
    modelo:str
    disponile:Boolean
    
    class config:
        orm_mode:True
    
class obtener_bici(create_bici):
    pass
    
class actualizar_bici(create_bici):
    pass
    
class eliminar_bici(create_bici):
    pass
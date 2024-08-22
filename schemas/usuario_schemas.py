from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    id_documento:Optional[int]=None
    nombre: str
    email: str  # el Field es para validaciones
    contrasena: str
    telefono: int
    direccion: str
    
    class config:
        orm_mode=True
    
class UserCreate(UserBase):
    pass
    
class UserResponse(UserBase):
    pass
    
    

    
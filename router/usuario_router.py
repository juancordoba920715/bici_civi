from fastapi import APIRouter
from config.database import SessionLocal
from main import app
from model.usuario_model import Usuario as usuarioModel

usuario_router = APIRouter()

"""@app.post('/usuario', tags=['usuario'])
def crear_usuario(usuario: usuario):
    db = SessionLocal()"""
    
    
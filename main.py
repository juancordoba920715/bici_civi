from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
from config.database import engine,base
from schemas.usuario_schemas import  UserBase, UserResponse
"""from jwt import create_token"""
from config.database import session, engine, base
from model import Usuario_model,Bicicleta,Prestamo



app=FastAPI()
app.title = "Bici Civi"

base.metadata.create_all(bind = engine)



"""def user(UserBase):
    email:str
    password:str"""


@app.get("/", tags=['Usuarios'])
def read_root():
    return HTMLResponse('<h1>Bienvenido a Bici Civi<h1> ')

"""@app.post("/Login", tags=["Authentic"])
def login(user: UserBase):
    return user""" 


@app.get('/usuarios', tags=['Usuarios'])
def obtener_usuario():
    db = session()
    result = db.query(Usuario_model).all()
    return JSONResponse(content=jsonable_encoder(result) )

@app.get('/usuarios/{id_documento}', tags = ['Usuarios']) #endpoint para filtrar por ID
def obtener_usuario_id(id_documento: int):  #el Path lo importo del FastApi y es para hacer validaciones de los parametros
    db = session()
    result = db.query(Usuario_model).filter(Usuario_model.id_documento == id_documento).first()
    if not result:
       return JSONResponse(content={"message": "Usuario no encontrado"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(result))  

""" @app.get('/usuarios/', tags = ['Usuarios'])
def obtener_usuarios_nombre(nombre:str = Query(min_length=5, max_length=30)):
    
    for item in usuarios:
        if item['nombre'] == nombre:
            return nombre
    return {'respuesta': 'usuario no encontrado'} """
 
@app.post('/usuarios', tags = ['Usuarios'], response_model=UserBase, status_code=201)
def registrar_usuarios(user: UserBase):
    db = session()
    new_user= Usuario_model(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return JSONResponse(status_code=201, content=jsonable_encoder(new_user))
    
 
@app.delete('/usuarios/{id_documento}', tags = ['Usuarios'] )
def eliminar_usuario(id_documento):
    db = session()
    result = db.query(Usuario_model).filter(Usuario_model.id_documento == id_documento).first()
    if not result:
        return JSONResponse(content=jsonable_encoder({"message": "Usuario no encontrado"}, status_code=404))
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=201, content=jsonable_encoder( result,{"respuesta": "usuario eliminado"}))
      

@app.put('/usuarios/{id_documento}', tags = ['Usuarios'])   
def actualizar_usuarios(id_documento:int, user:UserBase):
    db = session()
    result = db.query(Usuario_model).filter(Usuario_model.id_documento == id_documento).first()
    if not result:
        return JSONResponse(content=jsonable_encoder({"message": "Usuario no encontrado"}, status_code=404)) 
    result.id_documento = user.id_documento
    result.nombre = user.nombre
    result.email = user.email
    result.contrasena = user.contrasena
    result.telefono = user.telefono
    result.direccion = user.direccion
    db.commit()    
    return JSONResponse(content=({"respuesta": "se ha modificado la pelicula"}))
         
     
        
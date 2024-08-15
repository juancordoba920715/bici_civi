from fastapi import FastAPI
from config.database import engine,base
from model.usuario_model import Usuario


base.metadata.create_all(bind=engine)
app=FastAPI()


@app.get("/", tags=["App CiviBike"])
def read_root():
    return {"Bienvenido a civi_Bike"}
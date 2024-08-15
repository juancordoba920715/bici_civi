from database import engine,base

#Crear todas las tablas definidas enlos modelos
base.metadata.create_all(bind=engine)

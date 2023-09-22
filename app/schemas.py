from pydantic import BaseModel  #para definir el modelo
from typing import Optional
from datetime import datetime


#User Model
class User(BaseModel):
    username:str
    password:str
    nombre:str
    apellido:str
    direccion:Optional[str]
    telefono:int
    correo:str
    creacion_user:datetime=datetime.now()
  

class ShowUser(BaseModel):
    id:int
    username:str
    nombre:str
    correo:str
    #class Config():
       # orm_model = True


class UpdateUser(BaseModel):
    username:str = None
    password:str = None
    nombre:str = None
    apellido:str = None
    direccion:str = None
    telefono:str = None
    correo: str = None
    
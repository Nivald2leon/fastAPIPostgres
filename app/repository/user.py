

from app.db import  models
from sqlalchemy.orm import Session


#from app.routers import user


def crear_usuario(usuario, db:Session):
    usuario = usuario.dict()
    nuevo_usuario = models.User(
        username=usuario["username"],
        password=usuario["password"],
        nombre=usuario["nombre"],
        apellido=usuario["apellido"],
        direccion=usuario["direccion"],
        telefono=usuario["telefono"],
        correo=usuario["correo"],
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)


def obtener_usuario(user_id, db:Session):
    usuario = db.query(models.User).filter(models.User.id == user_id).first()
    if not usuario:
        return {"Respuesta": "Usuario no encontrado"}    
    return usuario


def eliminar_usuario(user_id, db:Session):
    usuario = db.query(models.User).filter(models.User.id == user_id)
    if not usuario.filter():
        return {"Respuesta": "Usuario no encontrado"}
    usuario.delete(synchronize_session=False)
    db.commit()
    return {"Respuesta": "Usuario eliminado correctamente"}



def obtener_usuarios(db:Session):
    data = db.query(models.User).all()
    return data


def actualizar_usuarios(user_id, updateUser, db:Session):
    usuario = db.query(models.User).filter(models.User.id == user_id)
    if not usuario.first():
        return {"Respuesta": "Usuario no encontrado"}
    usuario.update(updateUser.dict(exclude_unset=True))
    db.commit()
    return {"Respuesta": "Usuario actualizado"}
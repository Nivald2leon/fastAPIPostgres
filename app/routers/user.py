from fastapi import APIRouter, Depends
from app.schemas import User, ShowUser, UpdateUser
from app.db.database import get_db
from sqlalchemy.orm import Session
from typing import List
from app.repository import user


router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.get('/',response_model=List[ShowUser])
def obtener_usuarios(db: Session = Depends(get_db)):
    data=user.obtener_usuarios(db)
    
    return data


@router.post('/')
def crear_usuario(usuario: User, db: Session = Depends(get_db)):
    user.crear_usuario(usuario, db)
    return {"respuesta": "usuario creado correctamente"}


@router.get('/{user_id}',response_model=ShowUser )
def obtener_usuario(user_id: int, db: Session = Depends(get_db)):
    usuario=user.obtener_usuario(user_id, db)
    return usuario


@router.delete('/')
def eliminar_usuario1(user_id: int, db: Session = Depends(get_db)):
    resp=user.eliminar_usuario(user_id, db)
    return resp

@router.patch('/{user.id}')
def actualizar_usuario(user_id: int,  updateUser: UpdateUser,db: Session = Depends(get_db)):
    resp=user.actualizar_usuarios(user_id, updateUser, db)
    return resp
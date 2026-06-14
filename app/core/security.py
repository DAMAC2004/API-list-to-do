"""
Funciones de seguridad para la aplicación FastAPI.

Aquí se definen las funciones relacionadas con la seguridad, como la autenticación de usuarios,
la generación y verificación de tokens JWT, etc. Estas funciones se utilizan en los endpoints 
para proteger ciertas rutas y garantizar que solo los usuarios autorizados puedan acceder 
a ellas.
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from config import settings
import jwt

# Configuración de OAuth2 con JWT
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

"""
Función para obtener el usuario actual a partir del token JWT.
Esta función se utiliza como dependencia en los endpoints que requieren autenticación.
"""
async def get_current_user(token: str = Depends(oauth2_scheme)):
    """_summary_

    Args:
        token (str, optional): _description_. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        username: str = payload.get("sub")
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,   
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"username": username}
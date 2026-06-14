"""
Aquí se definen las configuraciones de la aplicación, como claves secretas, algoritmos de JWT,
URL de la base de datos, etc. Estas configuraciones se cargan desde variables de entorno para
mantener la seguridad y flexibilidad.

variables generales de la aplicación como el nombre, versión y descripción también
se definen aquí para
"""

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Variables de App
    APP_NAME: str = "to-do-app"
    APP_VERSION: str = "0.1.0"
    
    # Variables Secretas
    SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_DELTA: int = 30
    DATABASE_URL: str
    DATABASE_KEY: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
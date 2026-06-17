from pydantic import BaseModel, Field
from typing import Optional

class TaskCreate(BaseModel):
    # Field nos permite poner reglas como la longitud del texto
    title: str = Field(..., min_length=3, max_length=50, description="El título de la tarea")
    description: Optional[str] = Field(default=None, description="Detalles opcionales de la tarea")

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    is_completed: bool = False
    created_by: str

    # Le dice a Pydantic que pueda leer datos aunque no sean diccionarios puros.
    class Config:
        from_attributes = True
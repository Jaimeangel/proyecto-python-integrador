from pydantic import BaseModel,Field
from typing import Literal

class Transaccion(BaseModel):
    monto: float = Field(..., gt=0, description="El monto debe ser mayor a cero")
    fecha: str = Field(..., description="La fecha de la transacción")
    descripcion: str = Field(..., max_length=255, description="Descripción de la transacción")
    categoria: str = Field(..., max_length=50, description="Categoría de la transacción")

    class Config:
        validate_assignment = True

class Gasto(Transaccion):
    tipo: Literal['gasto'] = 'gasto'

class Ingreso(Transaccion):
    tipo: Literal['ingreso'] = 'ingreso'
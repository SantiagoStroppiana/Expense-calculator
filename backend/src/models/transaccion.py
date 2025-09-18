from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Transaccion(ABC):
    id: int
    monto: float
    fecha: datetime
    descripcion: str

    @abstractmethod
    def aplicar_transaccion(self, saldo_actual: float) -> float:
        pass
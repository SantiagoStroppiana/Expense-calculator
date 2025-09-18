from dataclasses import dataclass
from .transaccion import Transaccion
from .fuente_ingreso import FuenteIngreso

@dataclass
class Ingreso(Transaccion):
    fuente: FuenteIngreso = FuenteIngreso.OTROS

    def __post_init__(self):
        if self.monto <= 0:
            raise ValueError("El monto del ingreso debe ser mayor a 0")
        if not isinstance(self.fuente, FuenteIngreso):
            raise ValueError("Fuente de ingreso no válida")

    def aplicar_transaccion(self, saldo_actual: float) -> float:
        return saldo_actual + self.monto
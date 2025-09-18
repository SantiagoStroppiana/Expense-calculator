from dataclasses import dataclass
from .transaccion import Transaccion
from .categoria_gasto import CategoriaGasto

@dataclass
class Gasto(Transaccion):
    categoria: CategoriaGasto = CategoriaGasto.OTROS

    def __post_init__(self):
        if self.monto <= 0:
            raise ValueError("El monto del gasto debe ser mayor a 0")
        if not isinstance(self.categoria, CategoriaGasto):
            raise ValueError("Categoría de gasto no válida")

    def aplicar_transaccion(self, saldo_actual: float) -> float:
        nuevo_saldo = saldo_actual - self.monto
        if nuevo_saldo < 0:
            raise ValueError("Saldo insuficiente para realizar este gasto")
        return nuevo_saldo
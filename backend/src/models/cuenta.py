from dataclasses import dataclass, asdict
from .tipo_cuenta import TipoCuenta
from .transaccion import Transaccion

@dataclass
class Cuenta:
    id: int
    nombre: str
    tipo_cuenta: TipoCuenta
    saldo_inicial: float
    saldo_actual: float = None

    def __post_init__(self):
        if self.saldo_actual is None:
            self.saldo_actual = self.saldo_inicial
        if self.saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")


    def to_dict(self):
        data = asdict(self)
        data['tipo_cuenta'] = self.tipo_cuenta.value  # si TipoCuenta es Enum
        return data

    def aplicar_transaccion(self, transaccion: Transaccion) -> None:
        nuevo_saldo = transaccion.aplicar_transaccion(self.saldo_actual)
        if nuevo_saldo < 0:
            raise ValueError("Saldo insuficiente para esta transacción")
        self.saldo_actual = nuevo_saldo        

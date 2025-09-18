from enum import Enum

class TipoCuenta(Enum):
    CAJA_AHORRO = "Caja de Ahorro"
    CUENTA_CORRIENTE = "Cuenta Corriente"
    VIRTUAL = "Billetera Virtual"
    MP = "Mercado Pago"
    EFECTIVO = "Efectivo"
    OTROS = "Otros"
    
"""Objetos valor del dominio de vuelos

En este archivo usted encontrará los objetos valor del dominio de vuelos

"""

from __future__ import annotations

from dataclasses import dataclass, field
from eda.seedwork.dominio.objetos_valor import ObjetoValor, Codigo
from datetime import datetime
from enum import Enum

@dataclass(frozen=True)
class CodigoIATA(Codigo):
    ...

@dataclass(frozen=True)
class CodigoICAO(Codigo):
    ...


class EstadoOrden(str, Enum):
    APROBADA = "Aprobada"
    PENDIENTE = "Pendiente"
    CANCELADA = "Cancelada"
    PAGADA = "Pagada"
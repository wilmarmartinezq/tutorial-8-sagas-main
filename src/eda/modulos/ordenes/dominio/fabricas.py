""" Fábricas para la creación de objetos del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de vuelos

"""

from .entidades import Orden
from .reglas import MinimoUnItinerario, RutaValida
from eda.seedwork.dominio.repositorios import Mapeador, Repositorio
from eda.seedwork.dominio.fabricas import Fabrica
from eda.seedwork.dominio.entidades import Entidad
from eda.seedwork.dominio.eventos import EventoDominio
from dataclasses import dataclass

@dataclass
class _FabricaOrden(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad) or isinstance(obj, EventoDominio):
            return mapeador.entidad_a_dto(obj)
        else:
            orden: Orden = mapeador.dto_a_entidad(obj)

            return orden


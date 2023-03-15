from pulsar.schema import *
from dataclasses import dataclass, field
from eda.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearOrdenPayload(ComandoIntegracion):
    id_usuario = String()
    # TODO Cree los records para itinerarios

class ComandoCrearOrden(ComandoIntegracion):
    data = ComandoCrearOrdenPayload()
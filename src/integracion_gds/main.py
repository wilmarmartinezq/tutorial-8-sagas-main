from fastapi import FastAPI
# from cliente.config.api import app_configs, settings
# from cliente.api.v1.router import router as v1

# from cliente.modulos.infraestructura.consumidores import suscribirse_a_topico
# from .eventos import EventoUsuario, UsuarioValidado, UsuarioDesactivado, UsuarioRegistrado, TipoCliente

# from cliente.modulos.infraestructura.despachadores import Despachador
# from cliente.seedwork.infraestructura import utils

import asyncio
import time
import traceback
import uvicorn

from pydantic import BaseSettings
from typing import Any

from .eventos import EventoConfirmacionGDS, ConfirmacionRevertida, OrdenConfirmada
from .comandos import ComandoConfirmarOrden, ComandoRevertirConfirmacion, ConfirmarOrdenPayload, RevertirConfirmacionPayload
from .consumidores import suscribirse_a_topico
from .despachadores import Despachador

from . import utils

class Config(BaseSettings):
    APP_VERSION: str = "1"

settings = Config()
app_configs: dict[str, Any] = {"title": "Pagos eda"}

app = FastAPI(**app_configs)
tasks = list()

@app.on_event("startup")
async def app_startup():
    global tasks
    task1 = asyncio.ensure_future(suscribirse_a_topico("evento-gds", "sub-gds", EventoConfirmacionGDS))
    task2 = asyncio.ensure_future(suscribirse_a_topico("comando-confirmar-orden", "sub-com-gds-confirmacion", ComandoConfirmarOrden))
    task3 = asyncio.ensure_future(suscribirse_a_topico("comando-revertir-confirmacion", "sub-com-gds-revertir-confirmacion", ComandoRevertirConfirmacion))
    tasks.append(task1)
    tasks.append(task2)
    tasks.append(task3)

@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()

@app.get("/prueba-orden-confirmada", include_in_schema=False)
async def prueba_orden_confirmada() -> dict[str, str]:
    payload = OrdenConfirmada(
        id = "1232321321",
        id_correlacion = "389822434",
        orden_id = "6463454",
        fecha_confirmacion = utils.time_millis()
    )

    evento = EventoConfirmacionGDS(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=OrdenConfirmada.__name__,
        orden_pagada = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-gds")
    return {"status": "ok"}

@app.get("/prueba-confirmacion-revertida", include_in_schema=False)
async def prueba_confirmacion_revertida() -> dict[str, str]:
    payload = ConfirmacionRevertida(
        id = "1232321321",
        id_correlacion = "389822434",
        orden_id = "6463454",
        fecha_actualizacion = utils.time_millis()
    )

    evento = EventoConfirmacionGDS(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=ConfirmacionRevertida.__name__,
        pago_revertido = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-gds")
    return {"status": "ok"}
    
@app.get("/prueba-confirmar-orden", include_in_schema=False)
async def prueba_confirmar_orden() -> dict[str, str]:
    payload = ConfirmarOrdenPayload(
        id_correlacion = "389822434",
        orden_id = "6463454",
    )

    comando = ComandoConfirmarOrden(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=ConfirmarOrdenPayload.__name__,
        data = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-confirmar-orden")
    return {"status": "ok"}

@app.get("/prueba-revertir-confirmacion", include_in_schema=False)
async def prueba_revertir_confirmacion() -> dict[str, str]:
    payload = RevertirConfirmacionPayload(
        id = "1232321321",
        id_correlacion = "389822434",
        orden_id = "6463454",
    )

    comando = ComandoRevertirConfirmacion(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=RevertirConfirmacionPayload.__name__,
        data = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-revertir-confirmacion")
    return {"status": "ok"}
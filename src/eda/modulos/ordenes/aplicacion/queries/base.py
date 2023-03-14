from eda.seedwork.aplicacion.queries import QueryHandler
from eda.modulos.ordenes.infraestructura.fabricas import FabricaVista
from eda.modulos.ordenes.dominio.fabricas import FabricaVuelos

class ReservaQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_vista: FabricaVista = FabricaVista()
        self._fabrica_vuelos: FabricaVuelos = FabricaVuelos()

    @property
    def fabrica_vista(self):
        return self._fabrica_vista
    
    @property
    def fabrica_vuelos(self):
        return self._fabrica_vuelos    
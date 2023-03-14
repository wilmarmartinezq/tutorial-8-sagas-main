from eda.seedwork.infraestructura.vistas import Vista
from eda.modulos.ordenes.dominio.entidades import Orden
from eda.config.db import db
from .dto import Orden as OrdenDTO

class VistaOrden(Vista):
    def obtener_por(id=None, estado=None, id_cliente=None, **kwargs) -> [Orden]:
        params = dict()

        if id:
            params['id'] = str(id)
        
        if estado:
            params['estado'] = str(estado)
        
        if id_cliente:
            params['id_cliente'] = str(id_cliente)
            
        # TODO Convierta ReservaDTO a Reserva y valide que la consulta es correcta
        return db.session.query(OrdenDTO).filter_by(**params)

from cliente.modulos.dominio.entidades import Usuario
from cliente.modulos.dominio.repositorios import RepositorioUsuarios

class RepositorioUsuariosSQLAlchemy(RepositorioUsuarios):

    def __init__(self):
        self._fabrica_ordenes: FabricaOrdenes = FabricaOrdenes()

    @property
    def fabrica_ordenes(self):
        return self._fabrica_ordenes

    def obtener_por_id(self, id: UUID) -> Orden:
        orden_dto = db.session.query(OrdenDTO).filter_by(id=str(id)).one()
        return self.fabrica_ordenes.crear_objeto(orden_dto, MapeadorOrden())

    def obtener_todos(self) -> list[Orden]:
        # TODO
        raise NotImplementedError

    def agregar(self, orden: Orden):
        orden_dto = self.fabrica_ordenes.crear_objeto(orden, MapeadorOrden())

        db.session.add(orden_dto)

    def actualizar(self, orden: Orden):
        # TODO
        raise NotImplementedError

    def eliminar(self, orden_id: UUID):
        # TODO
        raise NotImplementedError
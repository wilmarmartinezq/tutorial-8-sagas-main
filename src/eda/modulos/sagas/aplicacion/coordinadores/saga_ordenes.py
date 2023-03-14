from eda.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from eda.seedwork.aplicacion.comandos import Comando
from eda.seedwork.dominio.eventos import EventoDominio

from eda.modulos.sagas.aplicacion.comandos.cliente import RegistrarUsuario, ValidarUsuario
from eda.modulos.sagas.aplicacion.comandos.pagos import PagarOrden, RevertirPago
from eda.modulos.sagas.aplicacion.comandos.gds import ConfirmarOrden, RevertirConfirmacion
from eda.modulos.ordenes.aplicacion.comandos.crear_orden import CrearOrden
from eda.modulos.ordenes.aplicacion.comandos.aprobar_orden import AprobarOrden
from eda.modulos.ordenes.aplicacion.comandos.cancelar_orden import CancelarOrden
from eda.modulos.ordenes.dominio.eventos.ordenes import OrdenCreada, OrdenCancelada, OrdenAprobada, CreacionOrdenFallida, AprobacionOrdenFallida
from eda.modulos.sagas.dominio.eventos.pagos import OrdenPagada, PagoRevertido
from eda.modulos.sagas.dominio.eventos.gds import OrdenGDSConfirmada, ConfirmacionGDSRevertida, ConfirmacionFallida


class CoordinadorOrdenes(CoordinadorOrquestacion):

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=CrearOrden, evento=OrdenCreada, error=CreacionOrdenFallida, compensacion=CancelarOrden),
            Transaccion(index=2, comando=PagarOrden, evento=OrdenPagada, error=PagoFallido, compensacion=RevertirPago),
            Transaccion(index=3, comando=ConfirmarOrden, evento=OrdenGDSConfirmada, error=ConfirmacionFallida, compensacion=ConfirmacionGDSRevertida),
            Transaccion(index=4, comando=AprobarOrden, evento=OrdenAprobada, error=AprobacionOrdenFallida, compensacion=CancelarOrden),
            Fin(index=5)
        ]

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])
    
    def terminar():
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        ...

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        ...


# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoDominio):
        coordinador = CoordinadorOrdenes()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")

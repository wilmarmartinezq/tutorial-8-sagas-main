import pulsar, _pulsar
from pulsar.schema import *
import uuid
import time
import os

def time_millis():
    return int(time.time() * 1000)

class EventoIntegracion(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()

class OrdenCreadaPayload(Record):
    id_orden = String()
    id_cliente = String()
    estado = String()
    fecha_creacion = Long()

class EventoOrdenCreada(EventoIntegracion):
    data = OrdenCreadaPayload()

HOSTNAME = os.getenv('PULSAR_ADDRESS', default="localhost")

client = pulsar.Client(f'pulsar://{HOSTNAME}:6650')
consumer = client.subscribe('eventos-orden', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='sub-notificacion-eventos-ordenes', schema=AvroSchema(EventoOrdenCreada))

while True:
    msg = consumer.receive()
    print('=========================================')
    print("Mensaje Recibido: '%s'" % msg.value().data)
    print('=========================================')

    print('==== Envía correo a usuario ====')

    consumer.acknowledge(msg)

client.close()
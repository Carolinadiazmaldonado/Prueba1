
import logging
from azure.data.tables import TableServiceClient

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    MY_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=cuentavisual;AccountKey=xk8H8AXGOPqNIt7DkDZl2hdptEGcXhYYiXttp6CftGsRiuXJqaF1q0dfOl046fh8+aMorkE93hWe+AStAhQCkw==;EndpointSuffix=core.windows.net"

    id = req.params.get('id')
    nombre = req.params.get('nombre')
    apellidos = req.params.get('apellidos')
    provincia = req.params.get('provincia')
    if id != None and nombre != None and apellidos != None and provincia != None:
        my_entity = {
            'PartitionKey': provincia,
            'RowKey': id,
            'Nombre': nombre,
            'Apellidos': apellidos,
            'Provincia': provincia,
            "Id": id
        }
        table_service_client = TableServiceClient.from_connection_string(conn_str=MY_CONNECTION_STRING)
        table_client = table_service_client.get_table_client(table_name="Cliente")
        entity = table_client.create_entity(entity=my_entity)

        return func.HttpResponse(f"Ok")
    else:
        return func.HttpResponse("Falta un parámetro", status_code=200)
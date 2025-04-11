import grpc

import services_pb2
import services_pb2_grpc
from services_pb2 import OrderRequest

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = services_pb2_grpc.OrderServiceStub(channel)
    # Creamos un pedido de ejemplo
    order = OrderRequest(order_id=1, product="Widget", quantity=10)
    response = stub.ProcessOrder(order)
    print("Respuesta del Order Service:")
    print(response)

if __name__ == "__main__":
    run()

import grpc
from concurrent import futures
import time
import random

import services_pb2
import services_pb2_grpc
from services_pb2 import StockRequest, StockResponse

class InventoryService(services_pb2_grpc.InventoryServiceServicer):
    def CheckStock(self, request, context):
        print(f"InventoryService: Verificando stock para el producto '{request.product}'")
        # Simulamos una verificación de stock con respuesta aleatoria
        available = random.choice([True, False])
        info = "Stock suficiente" if available else "Stock bajo"
        return StockResponse(available=available, info=info)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Inventory Service corriendo en el puerto 50052...")
    try:
        while True:
            time.sleep(86400)  # Mantiene el servidor en ejecución.
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()

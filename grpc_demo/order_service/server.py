import grpc
from concurrent import futures
import time

import services_pb2
import services_pb2_grpc
from services_pb2 import OrderRequest, OrderResponse, StockRequest
from services_pb2_grpc import OrderServiceServicer, add_OrderServiceServicer_to_server, InventoryServiceStub

class OrderService(services_pb2_grpc.OrderServiceServicer):
    def __init__(self, inventory_stub):
        self.inventory_stub = inventory_stub

    def ProcessOrder(self, request, context):
        print(f"OrderService: Recibido pedido #{request.order_id} para el producto '{request.product}'")
        # Crea una solicitud para verificar el stock
        stock_request = StockRequest(product=request.product, quantity=request.quantity)
        stock_response = self.inventory_stub.CheckStock(stock_request)
        
        if stock_response.available:
            message = f"Pedido {request.order_id} procesado. {stock_response.info}"
            status = "Procesado"
        else:
            message = f"Pedido {request.order_id} fallido. {stock_response.info}"
            status = "Fallido"
        return OrderResponse(order_id=request.order_id, status=status, message=message)

def serve():
    # Conectar al Inventory Service (se asume que está en localhost:50052)
    channel = grpc.insecure_channel('localhost:50052')
    inventory_stub = InventoryServiceStub(channel)
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_OrderServiceServicer_to_server(OrderService(inventory_stub), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Order Service corriendo en el puerto 50051...")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()

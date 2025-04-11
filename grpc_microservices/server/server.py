from concurrent import futures
import time
import grpc
import demo_pb2
import demo_pb2_grpc
from service import DemoService

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    demo_pb2_grpc.add_DemoServiceServicer_to_server(DemoService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC iniciado en el puerto 50051.")
    try:
        while True:
            time.sleep(86400)  # Mantiene el servidor activo
    except KeyboardInterrupt:
        server.stop(0)
        print("Servidor detenido.")

if __name__ == '__main__':
    serve()

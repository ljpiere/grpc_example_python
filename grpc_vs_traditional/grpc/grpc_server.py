import time
from concurrent import futures
import grpc

import processor_pb2 as processor_pb2
import processor_pb2_grpc as processor_pb2_grpc

class DataProcessorServicer(processor_pb2_grpc.DataProcessorServicer):
    def ProcessData(self, request, context):
        # Procesamiento: calcular la suma de los números
        total = sum(request.numbers)
        message = f"Sumatoria calculada: {total}"
        print(f"[gRPC] Proceso completo. Input: {request.numbers}, Resultado: {total}")
        return processor_pb2.DataResponse(result=total, message=message)

    def StreamData(self, request, context):
        # Envío progresivo de la suma acumulada
        total = 0
        for idx, number in enumerate(request.numbers, start=1):
            total += number
            message = f"Paso {idx}: suma acumulada = {total}"
            print(f"[gRPC Streaming] {message}")
            yield processor_pb2.DataResponse(result=total, message=message)
            time.sleep(1)  # Simula un procesamiento que lleva tiempo

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    processor_pb2_grpc.add_DataProcessorServicer_to_server(DataProcessorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC iniciado en el puerto 50051.")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()

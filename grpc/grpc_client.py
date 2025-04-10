import grpc
import grpc_example_python.grpc.processor_pb2 as processor_pb2
import grpc_example_python.grpc.processor_pb2_grpc as processor_pb2_grpc

def run_unary():
    # Conectar al servidor
    channel = grpc.insecure_channel('localhost:50051')
    stub = processor_pb2_grpc.DataProcessorStub(channel)
    
    # Crear una solicitud con números
    request = processor_pb2.DataRequest(numbers=[1, 2, 3, 4, 5])
    
    # Llamada unaria
    response = stub.ProcessData(request)
    print(f"[gRPC Unary] Respuesta: {response.result}, Mensaje: {response.message}")

def run_streaming():
    channel = grpc.insecure_channel('localhost:50051')
    stub = processor_pb2_grpc.DataProcessorStub(channel)
    
    request = processor_pb2.DataRequest(numbers=[10, 20, 30, 40])
    
    # Llamada streaming: recibir varias respuestas
    responses = stub.StreamData(request)
    for response in responses:
        print(f"[gRPC Streaming] Respuesta: {response.result}, Mensaje: {response.message}")

if __name__ == "__main__":
    print("---- Llamada unaria ----")
    run_unary()
    print("\n---- Llamada streaming ----")
    run_streaming()

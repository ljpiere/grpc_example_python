import grpc
from server import demo_pb2
from server import demo_pb2_grpc

def run():
    # Conexión al servidor gRPC
    channel = grpc.insecure_channel('localhost:50051')
    stub = demo_pb2_grpc.DemoServiceStub(channel)

    # Llamada al método unario SendMessage
    print("== Llamada unaria a SendMessage ==")
    response = stub.SendMessage(demo_pb2.MessageRequest(payload="¡Hola gRPC!", id=1))
    print("Respuesta unaria:", response.result, "| Timestamp:", response.timestamp)

    # Llamada al método en streaming StreamMessages
    print("\n== Llamada a StreamMessages ==")
    responses = stub.StreamMessages(demo_pb2.MessageRequest(payload="Stream de datos", id=2))
    for res in responses:
        print("Respuesta streaming:", res.result, "| Timestamp:", res.timestamp)

if __name__ == '__main__':
    run()

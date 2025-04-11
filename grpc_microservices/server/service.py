import time
import demo_pb2
import demo_pb2_grpc

class DemoService(demo_pb2_grpc.DemoServiceServicer):
    def SendMessage(self, request, context):
        # Procesa la solicitud y construye la respuesta
        response_text = f"Recibido el mensaje: '{request.payload}' con id: {request.id}"
        print("[Server] SendMessage:", response_text)
        return demo_pb2.MessageResponse(result=response_text, timestamp=int(time.time()))

    def StreamMessages(self, request, context):
        # Envía 5 mensajes en formato stream con un retardo de 1 segundo
        for i in range(5):
            result = f"Mensaje stream {i+1} para payload: '{request.payload}'"
            print("[Server] StreamMessages:", result)
            yield demo_pb2.MessageResponse(result=result, timestamp=int(time.time()))
            time.sleep(1)

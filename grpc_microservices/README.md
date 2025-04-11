# gRPC Demo

Este proyecto es una demostración de cómo se puede lograr la comunicación entre microservicios utilizando gRPC en Python. Se implementa un servicio gRPC con dos métodos:

- **SendMessage:** Llamada unaria que procesa un mensaje y retorna una respuesta.
- **StreamMessages:** Método de respuesta en streaming que envía múltiples mensajes de respuesta.

## Estructura del Proyecto

grpc-demo/
├── README.md
├── requirements.txt
├── proto/
│   └── demo.proto
├── server/
│   ├── server.py
│   └── service.py
└── client/
    └── client.py


## Requisitos

- Python 3.6 o superior
- Las librerías listadas en `requirements.txt`

## Instalación

1. Clona el repositorio o descarga el proyecto.
2. Navega a la carpeta del proyecto y crea un entorno virtual (opcional):

   ```bash
   python -m venv env
   source env/bin/activate  # En Windows usa `env\Scripts\activate`

3. Instala dependencias

`pip install -r requirements.txt`

4. Proto:

`python -m grpc_tools.protoc -I./proto --python_out=./server --grpc_python_out=./server ./proto/demo.proto`

## Ejecución

Usando una terminal conda.

`python server.py`

Validar ejecución y lanzar el cliente.

`python client.py`

## Resumen

Este demo demuestra una implementación realista de gRPC en Python utilizando:
- Definición de servicios y mensajes en un archivo proto.
- Un servicio en el servidor que implementa dos métodos: uno unario y otro en streaming.
- Un cliente que se conecta al servidor y consume ambos métodos.
- Una estructura modular que facilita la extensión y el mantenimiento en un escenario de microservicios.
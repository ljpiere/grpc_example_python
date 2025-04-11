# Uso del Proyecto

Este documento explica cómo configurar y ejecutar el proyecto.

## 1. Compilar el Contrato gRPC

Ejecuta el siguiente comando en la raíz del proyecto para generar los archivos `processor_pb2.py` y `processor_pb2_grpc.py`:

```bash
python -m grpc_tools.protoc -I. --python_out=./grpc --grpc_python_out=./grpc processor.proto

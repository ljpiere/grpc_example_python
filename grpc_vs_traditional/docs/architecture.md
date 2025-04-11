# Arquitectura del Proyecto

El proyecto se compone de dos servicios principales, que se comunican de forma independiente:

1. **Servicio gRPC**:  
   - Implementado en Python utilizando `grpcio`.
   - Utiliza Protocol Buffers para definir el contrato de comunicación.
   - Soporta llamadas unarias y streaming desde el servidor.

2. **Servicio REST**:  
   - Implementado en Python utilizando FastAPI.
   - Utiliza JSON como formato de intercambio de datos.
   - Soporta endpoints para procesamiento unario y streaming (usando `StreamingResponse`).

## Diagrama de Arquitectura

                   +------------------+
                   |   Cliente (CLI)  |
                   +------------------+
                           |
            -------------------------------
           |                               |
+--------------------+         +----------------------+
| Servicio gRPC      |         | Servicio REST (API)  |
| (DataProcessor)    |         | (DataProcessor API)  |
+--------------------+         +----------------------+
                           |
                  [Simulación de procesamiento]

## Ventajas de Cada Enfoque

- **gRPC**:  
  - Uso de HTTP/2 para una comunicación más eficiente.
  - Serialización binaria con Protocol Buffers, reduciendo el overhead.
  - Soporte nativo para streaming.

- **REST**:  
  - Basado en HTTP/1.1 y JSON.
  - Fácil integración con clientes web.
  - Puede resultar menos eficiente en escenarios de alto rendimiento y comunicación en tiempo real.

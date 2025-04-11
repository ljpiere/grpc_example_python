#!/usr/bin/env python3
import time
import grpc
import requests
import statistics
from typing import List

# Importa los módulos generados para gRPC
import sys
# Asegúrate de que el directorio "grpc" esté en el path
sys.path.insert(0, "../grpc")
import processor_pb2
import processor_pb2_grpc

# =====================================
# Funciones de Benchmark para gRPC
# =====================================
def benchmark_grpc_unary(num_iterations: int = 10, payload: List[int] = None):
    if payload is None:
        payload = list(range(1000))
    channel = grpc.insecure_channel('localhost:50051')
    stub = processor_pb2_grpc.DataProcessorStub(channel)
    latencies = []
    results = []
    print("\n== Benchmark gRPC Unario ==")
    for i in range(num_iterations):
        request = processor_pb2.DataRequest(numbers=payload)
        start = time.perf_counter()
        response = stub.ProcessData(request)
        end = time.perf_counter()
        latency = end - start
        latencies.append(latency)
        results.append(response.result)
        print(f"[gRPC Unario] Iteración {i+1}: Latencia = {latency:.6f} s, Resultado = {response.result}")
    return latencies, results

def benchmark_grpc_stream(num_iterations: int = 3, payload: List[int] = None):
    if payload is None:
        payload = list(range(100))
    channel = grpc.insecure_channel('localhost:50051')
    stub = processor_pb2_grpc.DataProcessorStub(channel)
    latencies = []
    stream_results = []
    print("\n== Benchmark gRPC Streaming ==")
    for i in range(num_iterations):
        request = processor_pb2.DataRequest(numbers=payload)
        start = time.perf_counter()
        responses = list(stub.StreamData(request))  # Se consume el streaming completo
        end = time.perf_counter()
        latency = end - start
        latencies.append(latency)
        final_result = responses[-1].result if responses else None
        stream_results.append(final_result)
        print(f"[gRPC Streaming] Iteración {i+1}: Tiempo total = {latency:.6f} s, Resultado final = {final_result}")
    return latencies, stream_results

# =====================================
# Funciones de Benchmark para REST
# =====================================
def benchmark_rest_unary(num_iterations: int = 10, payload: dict = None):
    if payload is None:
        payload = {"numbers": list(range(1000))}
    url = "http://localhost:8000/process"
    latencies = []
    results = []
    print("\n== Benchmark REST Unario ==")
    for i in range(num_iterations):
        start = time.perf_counter()
        response = requests.post(url, json=payload)
        end = time.perf_counter()
        latency = end - start
        latencies.append(latency)
        data = response.json()
        results.append(data.get('result'))
        print(f"[REST Unario] Iteración {i+1}: Latencia = {latency:.6f} s, Resultado = {data.get('result')}")
    return latencies, results

def benchmark_rest_stream(num_iterations: int = 3, payload: dict = None):
    if payload is None:
        payload = {"numbers": list(range(100))}
    url = "http://localhost:8000/stream"
    latencies = []
    stream_results = []
    print("\n== Benchmark REST Streaming ==")
    for i in range(num_iterations):
        start = time.perf_counter()
        response = requests.post(url, json=payload, stream=True)
        output = []
        # Consumir el streaming línea a línea
        for line in response.iter_lines():
            if line:
                output.append(line.decode("utf-8").strip())
        end = time.perf_counter()
        latency = end - start
        latencies.append(latency)
        final_output = output[-1] if output else "N/A"
        stream_results.append(final_output)
        print(f"[REST Streaming] Iteración {i+1}: Tiempo total = {latency:.6f} s, Resultado final = {final_output}")
    return latencies, stream_results

# =====================================
# Función para resumir resultados
# =====================================
def summarize(latencies: List[float], system_name: str = ""):
    avg = statistics.mean(latencies)
    med = statistics.median(latencies)
    min_val = min(latencies)
    max_val = max(latencies)
    stdev = statistics.stdev(latencies) if len(latencies) > 1 else 0
    print(f"\nResumen de {system_name}:")
    print(f"  Número de iteraciones: {len(latencies)}")
    print(f"  Latencia promedio: {avg:.6f} s")
    print(f"  Latencia mediana: {med:.6f} s")
    print(f"  Latencia mínima: {min_val:.6f} s")
    print(f"  Latencia máxima: {max_val:.6f} s")
    print(f"  Desviación estándar: {stdev:.6f} s")

# =====================================
# Función Principal: Comparación completa
# =====================================
def main():
    num_iterations_unary = 10
    num_iterations_stream = 3

    # Benchmark gRPC Unario
    grpc_unary_latencies, grpc_unary_results = benchmark_grpc_unary(num_iterations=num_iterations_unary)
    summarize(grpc_unary_latencies, "gRPC Unario")
    
    # Benchmark REST Unario
    rest_unary_latencies, rest_unary_results = benchmark_rest_unary(num_iterations=num_iterations_unary)
    summarize(rest_unary_latencies, "REST Unario")
    
    # Validar que ambos enfoques retornan el mismo resultado para la llamada unaria
    if grpc_unary_results and rest_unary_results and grpc_unary_results[-1] == rest_unary_results[-1]:
        print("\n[Validación Unaria] Ambos sistemas retornaron el mismo resultado.")
    else:
        print("\n[Validación Unaria] Existe diferencia en los resultados entre ambos sistemas.")
    
    # Benchmark gRPC Streaming
    grpc_stream_latencies, grpc_stream_results = benchmark_grpc_stream(num_iterations=num_iterations_stream)
    summarize(grpc_stream_latencies, "gRPC Streaming")
    
    # Benchmark REST Streaming
    rest_stream_latencies, rest_stream_results = benchmark_rest_stream(num_iterations=num_iterations_stream)
    summarize(rest_stream_latencies, "REST Streaming")
    
    # Nota: Para streaming, la comparación puede involucrar formatos distintos de respuesta,
    # por lo que se recomienda revisar las salidas de forma manual.

if __name__ == "__main__":
    main()

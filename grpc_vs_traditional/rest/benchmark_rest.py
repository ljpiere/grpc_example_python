import time
import requests

def benchmark_rest():
    url = "http://localhost:8000/process"
    payload = {"numbers": list(range(1000))}

    start_time = time.time()
    response = requests.post(url, json=payload)
    end_time = time.time()
    data = response.json()
    print(f"[Benchmark REST] Tiempo de respuesta: {end_time - start_time:.4f} segundos")
    print(f"Resultado: {data['result']}")

if __name__ == "__main__":
    benchmark_rest()

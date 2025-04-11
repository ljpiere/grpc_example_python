import time
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Data Processor REST API")

# Definición del modelo de datos
class DataRequest(BaseModel):
    numbers: List[int]

class DataResponse(BaseModel):
    result: int
    message: str

@app.post("/process", response_model=DataResponse)
def process_data(request: DataRequest):
    total = sum(request.numbers)
    message = f"Sumatoria calculada: {total}"
    print(f"[REST] Proceso completo. Input: {request.numbers}, Resultado: {total}")
    return DataResponse(result=total, message=message)

def generate_stream(numbers: List[int]):
    total = 0
    for idx, number in enumerate(numbers, start=1):
        total += number
        message = f"Paso {idx}: suma acumulada = {total}\n"
        print(f"[REST Streaming] {message.strip()}")
        yield message
        time.sleep(1)

@app.post("/stream")
def stream_data(request: DataRequest):
    return StreamingResponse(generate_stream(request.numbers), media_type="text/plain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

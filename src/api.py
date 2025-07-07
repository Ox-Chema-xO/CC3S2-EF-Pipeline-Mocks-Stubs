from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.analyzer import ExAnalyzer

app = FastAPI()
analyzer = ExAnalyzer()
class AnalisisRequest(BaseModel):
    """
    Modelo de datos para crear una solicitud
    de datos a analizar
    """    
    data: str

@app.get("/")
async def root():
    return {"Aplicacion lista para analizar datos"}

@app.post("/analyzer")
async def analizar_data(request: AnalisisRequest):
    try:
        result = analyzer.analizar(request.data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

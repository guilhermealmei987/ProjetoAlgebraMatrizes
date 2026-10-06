from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from functions import analisar_vetores, multiplicar_matrizes


app = FastAPI()

# Configura a pasta para arquivos estáticos (CSS, JS, Imagens)
app.mount("/static", StaticFiles(directory="static"), name="static")

class DadosMatriz(BaseModel):
    matrizA: list[list[float]]
    matrizB: list[list[float]]


class DadosVetores(BaseModel):
    vetorA: list[float]
    vetorB: list[float]





@app.get("/")
async def read_index():
    return FileResponse("index.html")

@app.post("/produto_matriz")
async def calcular(dados: DadosMatriz):
    # Executa a função Python usando os dados recebidos
    resultado = multiplicar_matrizes(dados.matrizA, dados.matrizB)

    # Retorna o resultado como JSON para o navegador
    return {"resultado": resultado}


@app.post("/produto_escalar")
async def calcular_produto_escalar(dados: DadosVetores):
    resultado = analisar_vetores(dados.vetorA, dados.vetorB)
    return {"resultado": resultado}
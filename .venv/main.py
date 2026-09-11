from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


app = FastAPI()

# Configura a pasta para arquivos estáticos (CSS, JS, Imagens)
app.mount("/static", StaticFiles(directory="static"), name="static")

class DadosMatriz(BaseModel):
    matrizA: list[list[float]]
    matrizB: list[list[float]]

def multiplicar_matrizes(matrizA, matrizB):

    la = len(matrizA)
    ca = len(matrizA[0])
    lb = len(matrizB)
    cb = len(matrizB[0])
    if (ca != lb):
        return 1

    matrizF = []

    linhaResultante= []
    soma = 0

#Percorre a linha da matriz A
    for i in range(la):
#Percorre a coluna da matrizB para fazer a distributiva linha da matrizA x colunas da matrizB
        for k in range(cb):  
#Percorrendo as colunas(Cada termo da linha) matrizA
            for j in range(ca):
#Operação da multiplicacao do termos somando a uma variavel que será o elemento da matriz Resultante
                soma += matrizA[i][j] * matrizB[j][k]
            linhaResultante.append(soma)
            soma = 0
#Criando a matrizFinal linha a linha
        matrizF.append(linhaResultante)
        linhaResultante = []

    return matrizF

@app.get("/")
async def read_index():
    return FileResponse("index.html")

@app.post("/calcular")
async def calcular(dados: DadosMatriz):
    # Executa a função Python usando os dados recebidos
    resultado = multiplicar_matrizes(dados.matrizA, dados.matrizB)

    # Retorna o resultado como JSON para o navegador
    return {"resultado": resultado}



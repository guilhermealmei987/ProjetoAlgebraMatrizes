import math
def multiplicar_matrizes(matrizA, matrizB):

    la = len(matrizA)
    ca = len(matrizA[0])
    lb = len(matrizB)
    cb = len(matrizB[0])
    if (ca != lb):
        return []

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

def analisar_vetores(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Os vetores devem ter a mesma dimensão (R^n).")
    
    produto_escalar = sum(x * y for x, y in zip(v1, v2))
    norma_v1 = math.sqrt(sum(x**2 for x in v1))
    norma_v2 = math.sqrt(sum(x**2 for x in v2))
    
    if norma_v1 == 0 or norma_v2 == 0:
        raise ValueError("Nenhum dos vetores pode ser nulo.")
        
    cos_theta = produto_escalar / (norma_v1 * norma_v2)
    cos_theta = max(-1.0, min(1.0, cos_theta)) 
    
    angulo_rad = math.acos(cos_theta)
    angulo_graus = math.degrees(angulo_rad)
    
    if math.isclose(angulo_graus, 0.0, abs_tol=1e-5):
        classificacao = "Nulo"
    elif math.isclose(angulo_graus, 90.0, abs_tol=1e-5):
        classificacao = "Reto"
    elif math.isclose(angulo_graus, 180.0, abs_tol=1e-5):
        classificacao = "Raso"
    elif 0 < angulo_graus < 90:
        classificacao = "Agudo"
    else:
        classificacao = "Obtuso"
        
    return {
        "produto_escalar": produto_escalar,
        "norma_v1": norma_v1,
        "norma_v2": norma_v2,
        "angulo_radianos": round(angulo_rad, 4),
        "angulo_graus": round(angulo_graus, 2),
        "classificacao": classificacao
    }
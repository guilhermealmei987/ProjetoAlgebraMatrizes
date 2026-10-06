document.getElementById("btnCalcularMatriz").addEventListener("click", async () => {
    function lerMatrizTextarea(textid) {
        const texto = document.getElementById(textid).value.trim();
        return texto.split('\n').map(linha => {
            return linha.trim().split(/[\s,]+/).map(Number);
        });
    }
    const matrizA = lerMatrizTextarea("usermatrizA");
    const matrizB = lerMatrizTextarea("usermatrizB");

    const response = await fetch("/produto_matriz", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ matrizA: matrizA, matrizB: matrizB })
    });

    const data = await response.json();
    document.getElementById("matrizC").innerText = JSON.stringify(data.resultado);
});

document.getElementById("btnCalcularVetor").addEventListener("click", async () => {
    function lerVetorTextarea(textid) {
        const texto = document.getElementById(textid).value.trim();
        return texto.split(/[\s,]+/).map(Number);
    }
    
    const vetorA = lerVetorTextarea("userVetorA");
    const vetorB = lerVetorTextarea("userVetorB");

    const response = await fetch("/produto_escalar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ vetorA: vetorA, vetorB: vetorB })
    });

    const data = await response.json();
    document.getElementById("resultadoVetor").innerText = JSON.stringify(data.resultado, null, 4);
});
function introducao(value) {
    document.getElementById("resultado").value += value;
}

function limpar() {
    document.getElementById("resultado").value = "";
}

function calcular() {
    try {
        const result = eval(document.getElementById("resultado").value);
        document.getElementById("resultado").value = result;
    } catch (error) {
        document.getElementById("resultado").value = "Erro";
    }
}
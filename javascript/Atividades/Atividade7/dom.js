let objetos = ["Cadeira", "Impressora", "Garfo"];


let addButton = document.getElementById("add-button");
addButton.addEventListener("click", () => {
    let input = document.getElementById("input-text").value.trim();
    
    if (input === "") {
        alert("Por favor, insira um valor válido.");
        return;
    }
    
    if (objetos.includes(input)) {
        alert("Este objeto já foi adicionado anteriormente.");
        return;
    }
    
    objetos.push(input);
    console.log("Objetos atualizados:", objetos);
    document.getElementById("input-text").value = "";
});


let orderButton = document.getElementById("order-button");
orderButton.addEventListener("click", () => {
    objetos.sort();
    console.log("Objetos ordenados:", objetos);
});
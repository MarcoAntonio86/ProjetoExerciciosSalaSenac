var fundo = document.getElementById('fundo');
fundo.addEventListener('focus', sobre);
fundo.addEventListener('blur', fora);

function sobre(){
    fundo.style.backgroundColor = 'yellow';
}

function fora(){
    fundo.style.backgroundColor = 'white';
}

var input = document.getElementById('fundo');
input.addEventListener('input', function() {
    var valor = input.value;
    if(valor.length < 3 && valor.length >= 1){
        input.style.backgroundColor = 'red';
    } else if (valor.length > 3) {
        input.style.backgroundColor = 'green';
    } else {
        input.style.backgroundColor = 'white';
    }
});
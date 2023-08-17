function ligardesligar() {
    var imagem = document.getElementById("luz").src;
    var imagemLigada = "https://www.w3schools.com/js/pic_bulbon.gif";
    var imagemDesligada = "https://www.w3schools.com/js/pic_bulboff.gif";
  
    if (imagem == imagemLigada) {
      document.getElementById("luz").src = imagemDesligada;
    } else {
      document.getElementById("luz").src = imagemLigada;
    }
  }
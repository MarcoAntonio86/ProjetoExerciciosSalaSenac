notas = {
    "Matematica": 8.5,
    "Portugues": 7.8,
    "Historia": 9.2,
    "Ciencias": 8.0,
    "ingles": 8.6,
}


for nome, nota in notas.items():
    sun = notas["Matematica"] + notas["Portugues"] + notas["Historia"] + notas["Ciencias"] + notas["ingles"]
    media = sun / 5


print(media)


    



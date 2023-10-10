'''Crie uma classe chamada `Livro` que represente um livro em uma biblioteca. O livro deve ter 
os seguintes atributos e métodos:
- Atributos:
 - `titulo`: O título do livro.
 - `autor`: O autor do livro.
 - `ano_publicacao`: O ano de publicação do livro.
 - `disponivel`: Um valor booleano que indica se o livro está disponível na biblioteca 
(inicialmente, True).
- Métodos:
 - `emprestar(self)`: Um método que empresta o livro, definindo o atributo `disponivel` como 
False.
 - `devolver(self)`: Um método que devolve o livro, definindo o atributo `disponivel` como 
True.
Crie objetos da classe `Livro`, empreste e devolva livros, e verifique o status de disponibilidade 
de cada livro.'''

class Livros:
    def __init__(self, titulo, autor, ano_publicacao, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    '''def disponivel(self):
        self.disponivel = True'''
    
    def emprestar(self):    
        self.disponivel = False

    def devolver(self):
        self.disponivel = True


livro1 = Livros('Harry Potter', 'J.K. Rowling', 1997, True)
livro1.emprestar()
livro1.devolver()

print(livro1.titulo, livro1.autor, livro1.ano_publicacao, livro1.disponivel)

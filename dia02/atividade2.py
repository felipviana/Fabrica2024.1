#Criar uma super classe animalcom subclasses(gato e cachorro) que herdam características, mas têm funções específicas

class Animal:
    def __init__(self, nome,idade,porte,raca):
        self.nome = nome
        self.idade = idade
        self.porte = porte
        self.raca = raca
    
    def definicao(self):
        print(f"nome{self.nome}, idade{self.idade}, porte{self.porte}, raça{self.raca}")

class Gato(Animal):
    def __init__(self,nome, idade, porte, raca, bigode):
        self.nome = nome
        self.idade = idade
        self.porte = porte
        self.raca = raca
        self.bigode = bigode

    def definicao(self):
        print(f"nome{self.nome}, idade{self.idade}, porte{self.porte}, raça{self.raca}, bigode{self.bigode}")
    def grunhido(self):
        print(f"{self.nome} miou")
    
class Cachorro(Animal):
    def grunhido(self):
        print(f"{self.nome} latiu")


nick = Cachorro("Nick", 12, 15, "Viralata")
nick.grunhido()
nick.definicao()

lua = Gato("Lua", 12, 9, "Siamês", "Grande")
lua.grunhido()
lua.definicao()
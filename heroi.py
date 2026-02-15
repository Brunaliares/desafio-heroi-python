class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        # Estrutura de decisão
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            ataque = "ataque desconhecido"

        # Operador de comparação
        if self.idade < 18:
            print(f"{self.nome} é muito jovem para lutar!")
        else:
            print(f"O {self.tipo} atacou usando {ataque}")


# Criando objetos (instâncias da classe)
heroi1 = Heroi("Aragorn", 30, "guerreiro")
heroi2 = Heroi("Naruto", 16, "ninja")
heroi3 = Heroi("Merlin", 50, "mago")

# Lista (variável)
lista_herois = [heroi1, heroi2, heroi3]

# Laço de repetição
for heroi in lista_herois:
    heroi.atacar()

class Gatto:

    familia = "felini"

    def __init__(self, nome, anni):
        self.nome = nome
        self.anni = anni

class Cane:

    def __init__(self, nome, anni, razza):
        self.nome = nome
        self.anni = anni
        self.razza = razza

mio_gatto = Gatto(nome = "palla", anni = 10)
secondo_gatto = Gatto("Black", 1)
print(type(mio_gatto))

print("Nome: ", mio_gatto.nome)
print("Anni: ", mio_gatto.anni)
print("Famiglia: ", mio_gatto.familia)

print("Nome: ", secondo_gatto.nome)
print("Anni: ", secondo_gatto.anni)
print("Famiglia: ", secondo_gatto.familia)

# mio_cane = Cane("Bob", 5, "Pastore tedesco")
# print(type(mio_cane))
# print("Nome: ", mio_cane.nome)
# print("Anni: ", mio_cane.anni)
# print("Razza: ", mio_cane.razza)

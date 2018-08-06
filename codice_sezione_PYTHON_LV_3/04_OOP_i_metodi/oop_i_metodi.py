class Automobile:

    def __init__(self, produttore, modello, cilindrata, anno):
        self.produttore = produttore
        self.modello = modello
        self.cilindrata = cilindrata
        self.anno = anno

    def accelera(self):
        print(self.modello, ": sto accelerando")

    def rifornimento(self):
        print(self.modello, ": sto rifornendo...")

my_car = Automobile("Lancia", "Delta", 1600, 1980)
lambo = Automobile("Lamborghini", "Gallardo", 5000, 2013)

lambo.accelera()
my_car.rifornimento()
# print(type(my_car))
# print(type(lambo))
#
# print(my_car)
# print(lambo)

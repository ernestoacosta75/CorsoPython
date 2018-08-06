import math

def print_tre_volte():
    print("Hello world")
    print("Hello world")
    print("Hello world")

def my_max(a, b):
    print("Max value is:", max(a, b))

#La gestione dei parametri opzionali si fa inizializzando il
#parametro specifico con un valore, ad esempio, accessori = False.
def macchina_nuova(produttore, modello, accessori = False):
    print("Acquisto macchina nuova; Caratteristiche: ")
    print("Produttore: ", produttore)
    print("Modello: ", modello)

    if accessori == True:
        print("La macchina è accessoriata")

def sommatrice(x, y):
    risultato = x + y
    return risultato

# print_tre_volte()
# my_max(5, 4)
# macchina_nuova("Tesla", "Model 3", accessori = True)
print(sommatrice(3, 5))

def max_tra_due_numeri(numero_1, numero_2):
    if numero_1 > numero_2:
        print("Il valore massimo tra {} e {} è: ".format(numero_1, numero_2), numero_1)
    elif numero_2 > numero_1:
        print("Il valore massimo tra {} e {} è: ".format(numero_1, numero_2), numero_2)
    else:
        print("I numeri sono uguali")

max_tra_due_numeri(4, 4)

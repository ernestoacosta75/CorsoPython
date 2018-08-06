def membro_di(valore, lista_valori):
    if valore in lista_valori:
        print("{} è presente in {}".format(valore, lista_valori))
    else:
        print("{} non è presente in {}".format(valore, lista_valori))

membro_di("Acosta", ["Rodriguez", "Acosta"])        

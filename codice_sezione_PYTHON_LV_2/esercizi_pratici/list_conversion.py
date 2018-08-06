def list_conversion(lista_parole):
    lista_lunghezze = []

    for parola in lista_parole:
        lista_lunghezze.append(len(parola))

    print("Lista di parole: ", lista_parole)
    print("Lista lunghezza delle parole: ", lista_lunghezze)

list_conversion(['Ernesto', 'Antonio', 'Rodriguez', 'Acosta'])

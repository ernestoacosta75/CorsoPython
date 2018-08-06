def palindrome(parola):
    indice = (len(parola) - 1)
    nuova_parola = ""

    while indice >= 0:
        nuova_parola += parola[indice]
        indice -= 1

    print("Parola di origine: ", parola)
    print("Parola ricostruita: ", nuova_parola)

    if nuova_parola == parola:
        print("La parola {} è un pailndromo".format(parola))
    else:
        print("La parola {} non è un pailndromo".format(parola))

palindrome("illuminati")

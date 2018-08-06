def divisore(x, y):
    try:
        risultato = x / y
        print(risultato)
    except :
        print("I dati inseriti non sono supportati")
    finally:
        print("Questo codice verrà eseguito in ogni caso")

divisore(9, 3)

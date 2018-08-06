def custom_len(stringa_o_lista):
    lunghezza = 0

    for carattere in stringa_o_lista:
        lunghezza += 1

    return lunghezza

print(custom_len(input("Inserisce la stringa desiderata --> ")))
print(custom_len(['asd', 2,2, 66, 'Roma', 3.14]))

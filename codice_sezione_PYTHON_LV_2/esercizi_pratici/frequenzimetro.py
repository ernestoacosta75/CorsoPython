def frequenzimetro(stringa):
    dizionario_frequenze = {}

    for carattere in stringa:
        if carattere in dizionario_frequenze:
            dizionario_frequenze[carattere] += 1
        else:
            dizionario_frequenze[carattere] = 1
    print(dizionario_frequenze)

frequenzimetro("ababccaa")

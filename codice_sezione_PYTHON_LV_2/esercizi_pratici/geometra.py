def geometra():
    dizionario_aree = {"1": "Cerchio", "2": "Quadrato", "3": "Rettangolo", "4": "Triangolo"}
    for opzione in dizionario_aree.keys():
        print("Opzione {}) ".format(opzione), dizionario_aree[opzione])

    scelta = input("Quale area desidera calcolare? ")

    if scelta in dizionario_aree:
        if dizionario_aree[scelta] == "Cerchio":
            raggio = input("Inserisca il raggio del cerchio: ")
            print("La area del cerchio è {}".format(3.14 * int(raggio)**2))
        elif dizionario_aree[scelta] == "Quadrato":
            lato = input("Inserisca il valore di un lato del quadrato: ")
            print("La area del cerchio è {}".format(int(lato)**2))
        elif dizionario_aree[scelta] == "Rettangolo":
            base_rettangolo = input("Inserisca il valore di la base: ")
            altezza_rettangolo = input("Inserisca il valore di l'altezza': ")
            print("La area del rettangolo è {}".format(int(base_rettangolo) * int(altezza_rettangolo)))
        elif dizionario_aree[scelta] == "Triangolo":
            base_triangolo = input("Inserisca il valore di la base: ")
            altezza_triangolo = input("Inserisca il valore di l'altezza': ")
            print("La area del triangolo è {}".format((int(base_triangolo) * int(altezza_triangolo)) / 2))

geometra()

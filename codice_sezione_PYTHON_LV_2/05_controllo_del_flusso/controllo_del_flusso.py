eta = input("Inserisce l'età: ")
hai_patente = input("Hai la patente (True/False)? ")

if int(eta) >= 18 and bool(hai_patente) == True:
    print("Puoi noleggiare una Ferrari!")
elif int(eta) >= 18 and bool(hai_patente) == False:
    print("Niente Ferrari! Prima la patente!")
else:
    print("Ne riparleremo tra qualche anno!")

# Variabile con global scopeself.
#Resta in vita dall'avio alla chiusura dello script
x = 50

def mia_funzione():
    # global x    #Usando global diciami alla funzione che stiamo facendo riferimento ad una variabile con global scope
    z = x
    z += 50

    return z

print(mia_funzione())

# I Dizionari possono contenere parecchi elementi al loro interno. Sono l'equivalente dei Map in Java.
# e a ciascun elemento corrisponde una coppia chiave-valore.
# A differenza delle liste, si deve usare un indice per accedere ad un determinato valore, usando la chiave associata.
# Si creano usando le parentessi graffe "{}".
# del: Per cancellare un elemento in base alla chiave.
# keys(): Ci restituisce una lista contenente tutte le chiavi presenti nel dizionario
# values(): Ci restituisce una lista contenente tutti valori delle chiavi presenti nel dizionario
# items(): Ci restituisce dei tuples che rappresentano tutte le copie chiave/valore presenti nel dizionario
# get(): Ci restituisce il valore di una chiave nel dizionario. Se non la trova, visualizza il messaggio allegato alla funzione.

mio_dizionario = {"mia_chiave": "mio_valore", "età": 26, "pi_greco": 3.14, "primi": [2, 3, 5, 7]}

# mio_dizionario["nazionalità"] = "italiana"
# print(mio_dizionario)
#
# del mio_dizionario["mia_chiave"]
# print(mio_dizionario)
#
# mio_dizionario["mia_chiave"] = "mio_valore_n_2"
# print(mio_dizionario)
# print(mio_dizionario.keys())
# print(mio_dizionario.values())
# print(mio_dizionario.items())
mio_dizionario.setdefault("bacon", "eggs")
print(mio_dizionario)

# -Le Liste sono un tipo di dato che può contenere svariati valori al suo interno, anche tutti diversi tra di loro;
# -Per accedere ai valori delle Liste possiamo usare il sistema di indicizzazione della Lista;
# -L'indice parte da 0, e si possono usare numeri negativi per accedere dalla fine all'inizio;
# -Si puó inoltre impostare un intervallo utilizzando i due punti per l'inizio o la fine del range;
# -L'indice si usa inoltre per sostituire un elemento, o eliminarlo con l'istruzione DEL;

# -Utilizziamo i Metodi associati alle liste per poterle gestire nel migliore dei modi;
# -Il Metodo append() ci consente di aggiungere un elemento alla fine della lista;
# -Il Metodo extend() ci consente di "estendere" una lista, con l'aggiunta di valori provenienti da una seconda lista;
# -Il Metodo remove() invece di consente di rimuovere un elemento, a partire dal suo valore;
# -Il Metodo pop() ci consente di eliminare l'ultimo elemento della lista;
# -Il Metodo sort() ci consente di riordinare gli elementi di una lista;
# -Il Metodo reverse() ci consente di invertire l'ordine degli elementi di una lista;
# -Il Metodo index() ci permette di ottenere l'indice di un elemento passato;
# -Il Metodo insert() ci consente di aggiungere un valore in una posizione prestabilita.

# Esempi: https://www.programmareinpython.it/video-corso-python-base/16-i-metodi-delle-liste/

elenco = [2, 5, "bacon", 3.14, "eggs", "asd", 55, 23]

# print(elenco)       # Visualizzare il contenuto della lista
# print(elenco[-2])
# print(elenco[2:6])  # Usando ":" possiamo prendere delle subliste all'interno della lista
# print(elenco[:6])
# print(elenco[2:])

# for elemento in elenco:
#     print(elemento)

# mia_lista = list(range(49, 155))    # Creazione di una lista a partire di un range
# print(mia_lista)

altra_lista = [2, 5, "bacon", 3.14, ["eggs", "asd", 55, 23]]
altra_lista[1] = 6

print(altra_lista[4][1])
print(altra_lista)

# del altra_lista[1]  #Con "dell" viene eseguita la cancellazione dell'elemento che si trova a quell'indice nella Lista
# altra_lista.remove(3.14)    #Con "remove" si cancella un elemento della lista in base al suo valore
# altra_lista.append("spam")  # Con "append" si aggiunge un elemento alla fine della lista
# altra_lista.reverse()   #Con "reverse" si cambia l'ordine degli elementi della lista
# print(altra_lista)

lista_numerica = [4, 2, 6, 7, 1, 77]
lista_numerica.sort()   #Il "sort" serve ad ordinare gli elementi di una lista
print(lista_numerica)

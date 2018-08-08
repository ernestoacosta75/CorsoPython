'''
Created on 17 lug 2018

@author: Administrator
'''
class Database:
    pass

database = None

def initialize_database():
    '''Questo metoddo server a ritardare la creazione dell'oggetto Database
    fino a quando non sia strittamente necessario.
    La parola chiave 'global' indica che la variabile database all'interno
    di questo metodo è l'unica definita a livello di modulo. '''
    global database
    database = Database()
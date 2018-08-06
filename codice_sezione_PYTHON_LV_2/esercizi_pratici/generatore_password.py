import random, string

def generatore_password():
    tipo_password = input("Quale tipo di password desidera [1= Semplice, 2 = Complessa]: ")
    password_finale = ""

    if tipo_password == "1":
        x = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        print(x)
    elif tipo_password == "2":
        x = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
        print(x)

generatore_password()

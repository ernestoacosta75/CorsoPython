contatore = 0

while contatore <= 10:
    contatore += 1
    if contatore == 5:
        print("Saltato", contatore)
        continue
    print(contatore)

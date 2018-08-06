def fattoriale(n):
	if n == 1:
		return n
	else:
		result = n * fattoriale(n-1)
		return result
num = int(8))
# num = int(input('Inserisci il numero da fattorizzare  -> '))
print(fattoriale(num))

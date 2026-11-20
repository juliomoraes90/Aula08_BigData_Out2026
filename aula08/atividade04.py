numeros = []

for i in range(15):
    numero = int(input('Insira o numero: '))
    numeros.append(numero)

conjunto = set(numeros)
print(conjunto)
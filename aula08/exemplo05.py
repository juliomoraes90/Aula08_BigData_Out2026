# TUPLAS
# Coleção Imutável
# Permite elementos duplicados
# Permite acesso pelo índice
# Mantém a ordem de inserção

frutas = ('Maçã' , 'Uva' , 'Pêra' , 'Laranja')
print(frutas[2])
print(frutas)

# frutas[1] = 'Melancia'  # A tupla nao pode ser alterada
numeros = (10, 20, 50, 20, 30, 10, 400, 20)

print(numeros.count(20))
print(frutas.index('Laranja'))
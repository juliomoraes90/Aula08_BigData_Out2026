# SETS "Conjuntos"
# Coleção mutável
# Não garante ordem
# Não permite índice
# Não permite elementos duplicados

# Criar um sets vazios
dias = set()

dias.add('Segunda')
dias.add('Terça')
dias.add('Quarta')
dias.add('Quinta')
dias.add('Sexta')
print(dias)

# Conjuntos inicializados
frutas = {'Maçã' , 'Uva' , 'Pêra' , 'Laranja'}
print(type(frutas))
print(frutas)

# Remover
frutas.remove('Uva')
frutas.discard('Uva')
print(frutas)
print(len(frutas))

# Converter lista para sets
lista = [5, 7, 4, 1, 2, 8, 13, 6]
conjunto_set = set(lista)
print(conjunto_set)

numeros = [5, 7, 4, 1, 2, 8, 13, 6, 13, 8, 29, 4, 4, 5, 7]
conjunto = set(numeros) # converte lista para conjunto set
numeros = list(conjunto) # converte conjunto set para lista
print(conjunto)
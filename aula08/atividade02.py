numeros = []
contador = 0

while True:
    contador += 1
    numero = int(input('Insira novo número: '))
    continuar = input('Para encerrar Digite N. Ou aperte qualquer outra tecla para continuar: ').upper()
    numeros.append(numero)
    
    if continuar == 'N':
        print(f'Total de entradas {len(numeros)}')
        print(numeros)
        break
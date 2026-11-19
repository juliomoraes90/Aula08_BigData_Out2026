notas = []
contador = 0

while contador <= 12:
    contador += 1
    nota = int(input(f'Nota da prova matricula #{contador}: '))
    notas.append(nota)

print(f'Boletim de notas: {sorted(notas)}')
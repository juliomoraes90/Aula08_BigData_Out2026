vendas = []
contador = 0

for n in range(10):
    contador += 1
    venda = float(input(f'Digite o valor da venda #{contador}: '))
    vendas.append(venda)
    print(vendas)
    
print(f'Total de vendas: {sum(vendas)}')
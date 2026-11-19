produtos = []

for i in range(5):
    produto = input('Nome do prodto: ')
    produtos.append(produto)
    print(produtos)

# Acesso ao elemento
n = int(input('Digite a posição do elemento a acessar: '))
print(produtos[n-1])

# Alterando ma lista "nome de um elemento"
produtos[n-1] = input(f'Novo produto para substituir o anterior {n}: ')
print(produtos)

# Removendo item da lista
produto_a_remover = input('\nDigite o nome do produto a remover: ')
confirmar = input(f'Tem certeza que deseja remover {produto_a_remover}? [S/N]').upper()[0]

if produto_a_remover in produtos:
    produtos.remove(produto_a_remover)
else:
    print('Produto não encontrado')

print(f'\n{produto_a_remover} removido com sucesso\n')
print(produtos)
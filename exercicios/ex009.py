carros = ['i5', 'i9', 'c200']

car_user = input('qual carro quer: ')
disponivel = ''
for i in carros:
    if i == car_user:
        disponivel = 'disponivel'
        break
    else:
        disponivel = 'nao disponivel'

print(disponivel)
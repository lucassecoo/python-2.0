def dobro(n):
    return n * 2

def quadrado(num):
    return num ** 2

print(quadrado(dobro(2)))

ex = lambda x, y: x * y

num1 = int(input('num1:'))
num2 = int(input('num2:'))

print(ex(num1, num2))
def ponto(temp):
    if temp < 48 or 48 < temp < 54:
        print('selada')
    elif 54 < temp < 60:
        print('ao ponto para o mal')
    elif 60 < temp < 65:
        print('ao ponto')
    elif 65 < temp < 71:
        print('ao ponto para o bem')
    else:
        print('bem passada')

temperatura = int(input('qual a temp: '))

ponto(temperatura)
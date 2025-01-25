def tintas(rend, alt, larg):
    area = alt * larg
    rendimento = area / rend
    print(f'voce precisa de {rendimento} latas')

rendimento_user = float(input('rendimento:'))
altura = float(input('altura:'))
largura = float(input('largura:'))

tintas(rendimento_user, altura, largura)
funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

noite_carro = list(set(tem_carro) & set(turno_noite))
print(noite_carro)

dia_carro = list(set(tem_carro) & set(turno_dia))
print(dia_carro)

sem_carro = list(set(funcionarios) - set(tem_carro))
print(sem_carro)
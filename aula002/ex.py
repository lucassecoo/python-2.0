tarefas = []

while True:
    def comandos():
        print('Comandos: listar, desfazer, refazer')
        comando = input(print('Digite uma tarefa ou um comando: '))
        match comando:
            case 'listar':
                for i in range(tarefas):
                    print(i)

        comandos()
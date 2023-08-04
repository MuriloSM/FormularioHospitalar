print('Bem-Vindo(a)!')
print('Escolha uma opção:')

def exibir_menu():    
    print('1 - Cadastrar Paciente')
    print('0 - Sair')

def chamar_arquivo(arquivo):
    with open(arquivo, 'r') as file:
        codigo = file.read()
        exec(codigo)

exibir_menu()

def resposta_menu():
    resposta_loop = 0
    while resposta_loop == 0:
        resposta = input('Escolha uma opção: ')
        if resposta == '1':
            chamar_arquivo('ficha_entrada.py')
            exibir_menu()
          
        elif resposta == '0':
            print('Saindo...')
            break
        else:
            print('========DIGITE UMA OPÇÃO VALIDA========= ')
            exibir_menu()

resposta_menu()
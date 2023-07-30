# Menu inicial do usuario:

def menu_inicial():
    print('Bem-Vindo(a)! ')
    print('1 - Cadastrar Novo Paciente.')
    print('0 - Sair')

# Criando um loop para o usuario a escolher uma das opções apresentadas:
while True:
    menu_inicial() 
    opcao_menu_inicial = input('Escolha uma opção: ')


    if opcao_menu_inicial == '1':
        import ficha_entrada
    elif opcao_menu_inicial == '0':
        print('Saindo...')
        break
    else:
        print('DIGITE UMA OPÇÃO VALIDA')
        

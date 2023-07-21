# Sistema de Hospital - Ficha de Entrada do paciente

import datetime

#looping para cadastrar um novo paciente

resposta = 'SIM'
while resposta == 'SIM':  

#Dados do paciente:

    nome = input('Nome Completo: ').upper()
    idade = int(input('Idade: '))
    telefone = input('Telefone: ')
    doenca_infectocontagiosa = input('Suspeita de doença infectocontagiosa? ').upper()
    

# Hora atual e formatada.

    hora_atual = datetime.datetime.now()
    hora_formatada = hora_atual.strftime("%Y-%m-%d %H:%M:%S")

# Ficha (resposta ao usuario dos dados inseridos) 

    print('==========================================================')
    print('ENTRADA:', hora_formatada)
    print('Paciente:', nome, '\nIdade:', idade, '\nTelefone:', telefone)

# Atendimento prioritário (Idosos).

    if idade >= 80:
        print('Paciente', nome, 'COM Atendimento Prioritario.')
        if doenca_infectocontagiosa == 'SIM' or doenca_infectocontagiosa == 'S':
            print('Deve ser direcionado para a sala de espera reservada.' )
        else:
            print('NAO deve direcionado para a sala de espera reservada.')
    else:
        print('Paciente SEM Atendimento Prioritario.')
        if doenca_infectocontagiosa == 'SIM' or doenca_infectocontagiosa == 'S' :
            print('Deve ser direcionado para a sala de espera reservada.' )
        else:
            print('NAO deve direcionado para a sala de espera reservada.')
    print('===========================================================')
    resposta = input('Digite SIM para um novo cadastro: ').upper()














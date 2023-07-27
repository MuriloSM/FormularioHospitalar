# Sistema de Hospital - Ficha de Entrada do paciente

import datetime
import csv

#dicionario para guardar dados de paciente:

dados_pacientes = {}

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

    #salvando dados inseridos:

    dados_pacientes[nome] = {
        'Idade': idade,
        'Telefone': telefone,
        'Doença Infectocontagiosa': doenca_infectocontagiosa,
        'Data de entrada': hora_formatada
    }

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

    #salvando dados:
    resposta = input('Digite SIM para um novo cadastro ou S salvar dados: ').upper()
    if resposta == 'S':
        nome_arquivo_csv = 'dados_pacientes.csv'
        with open(nome_arquivo_csv, 'w', newline='') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            header = ['Nome', 'Idade', 'Telefone', 'Doença Infectocontagiosa', 'Data de Entrada']
            writer.writerow(header)
            for nome, dados in dados_pacientes.items():
                idade = dados['Idade']
                telefone = dados['Telefone']
                doenca_infectocontagiosa = dados['Doença Infectocontagiosa']
                data_entrada = dados['Data de entrada']
                writer.writerow([nome, idade, telefone, doenca_infectocontagiosa, data_entrada])

   















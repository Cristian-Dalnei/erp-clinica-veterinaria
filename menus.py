from cliente import pets_usuario, consultas_futuras, lista_consultas
from funcionario import cadastrar_cliente, listar_cliente, pesquisar_cliente_nome, cadastrar_pet
from gerente import quant_consulta_mes, diferenca_consultas_mes, veterinario_rank_mes, cliente_inativos_dias
from login import entrar, id_cliente
from veterinario import consultas_futuras, lista_consulta, relatorio_consulta, adicionar_relatorio_consulta


def menu_cliente(id_usuario):
    while True:
        print('1-Pets Cadastrados')
        print('2-Consultas Futuras')
        print('3-Consultas Realizadas')
        print('4- Sair')
        escolha = input('Digite a opção desejada: ')
        if escolha == 1:
            pets_usuario(id_usuario)
        elif escolha == 2:
            id_pet = int(input('Digite o id do pet: '))
            consultas_futuras(id_pet)
        elif escolha == 3:
            id_pet = int(input('Digite o id do pet: '))
            lista_consultas(id_pet)
        elif escolha == 4:
            break
        else:
            print('Opção invalida')


def menu_cadastras_pet():
    while True:
        print('Para cadastrar um pet é necessario o ID do dono.')
        print('1-Listar usuarios')
        print('2-Pesquisar usuario por nome')
        print('3-Cadastrar Pet')
        print('4-Sair')
        escolha = input('Digite a escolha desejada: ')
        if escolha == 1:
            listar_cliente()
        elif escolha == 2:
            pesquisar_cliente_nome()
        elif escolha == 3:
            cadastrar_pet()
        elif escolha == 4:
            break
        else:
            print('Valor invalido!')

def menu_funcionario():
    while True:
        print('1-Cadastrar Cliente')
        print('2-Cadastar Pet')
        print('4-Sair')
        escolha = input('Digite a opção desejada: ')
        if escolha == 1:
            cadastrar_cliente()
        elif escolha == 2:
            menu_cadastras_pet()
        elif escolha == 4:
            break
        else:
            print('Opção invalida!')





def menu_gerente():
    while True:
        print('1-Quantidade de consultas por mês')
        print('2-Comparação de consultas mês a mês')
        print('3-Quantidade de atendimentos por veterinario')
        print('4-Clientes inativos há mais de 6 meses')
        print('5- Sair')
        escolha = input('Digite a opção desejada')
        if escolha == 1:
            quant_consulta_mes()
        elif escolha == 2:
            diferenca_consultas_mes()
        elif escolha == 3:
            veterinario_rank_mes()
        elif escolha == 4:
            cliente_inativos_dias()
        elif escolha == 5:
            break
        else:
            print('Opção invalida')

def menu_veterinario(id_usuario):
    while True:
        print('1-Consultas Futuras')
        print('2-Todas as consultas')
        print('3-Relatorio Consultas')
        print('4-Adicionar relatorio para a consulta')
        print('5-Sair')
        escolha = input('Digite a opção desejada: ')
        if escolha == 1:
            consultas_futuras(id_usuario)
        elif escolha == 2:
            lista_consulta(id_usuario)
        elif escolha == 3:
            while True:
                try:
                    id_relatorio = int(input('Digite o id do relatorio: '))
                    print('Iniciando relatorio')
                    break
                except ValueError:
                    print('Valor invalido')
            relatorio_consulta(id_relatorio)
        elif escolha == 4:
            while True:
                try:
                    id_relatorio = int(input('Digite o id do relatorio: '))
                    print('Iniciando relatorio')
                    break
                except ValueError:
                    print('Valor invalido')
            adicionar_relatorio_consulta(id_relatorio)
        elif escolha == 5:
            break
        else:
            print('Valor invalido')

def menu_geral():
    id_menu = None
    id_usuario = None
    print('=====Pet SHOPCadu=====')
    email = input('Digite seu email: ')
    id_menu = entrar(email)
    id_usuario = id_cliente(email)
    if id_usuario != None and id_menu != None:
        if id_menu == 1:
            menu_cliente(id_usuario)
        elif id_menu == 2:
            menu_veterinario(id_usuario)
        elif id_menu == 3:
            menu_funcionario()
        elif id_menu == 4:
            menu_gerente()
    else:
        print('Erro ao ao carregar o sistema')




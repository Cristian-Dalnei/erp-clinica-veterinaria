from db import conectar
from queries_cliente import query_consultas_futuras, query_pets, query_lista_consultas, query_relatorio_remedios


#Consultar tras as consultas futuras do animal de extimação
def consultas_futuras(id_pet):
    conn = None
    cur = None
    tabela = None
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(query_consultas_futuras, (id_pet,))
        tabela = cur.fetchall()
    except Exception:
        print('Erro ao consultar consultas')
        return
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

    if tabela:
        for pet_nome, responsavel, descricao, data_consulta in tabela:
            print(f'Nome: {pet_nome}')
            print(f'Resposavel: {responsavel}')
            print(f'Descricao: {descricao}')
            print(f'Data Consulta: {data_consulta}')
            print('-' * 20)
    else:
        print('Nenhuma consulta encontrada')

#Lista de consultas anteriores ao dia e a hora atual
def lista_consultas(id_pet):
    conn = None
    cur = None
    tabela = None
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(query_lista_consultas, (id_pet,))
        tabela = cur.fetchall()
        if not tabela:
            print('Nenhuma consulta encontrada')
            return
    except Exception:
        print('Erro ao consultar pet')
        return
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

    for id_consulta, nome_pet, veterinario, data, descricao in tabela:
        print(f'Id: {id_consulta}')
        print(f'Nome: {nome_pet}')
        print(f'Veterinario: {veterinario}')
        print(f'Data Consulta: {data}')
        print(f'Descricao: {descricao}')
        print('-'*20)

    while True:
        print('Verificiar relatorio da consulta')
        print('1-Veificar relatorio')
        print('2- Sair')
        escolha = int(input('Digite a opção desejada: '))
        if escolha == 1:
            id_escolhido = int(input('Digite o id referente a consulta: '))
            relatorio_consulta(id_escolhido)
        elif escolha == 2:
            break

#Lista dos pets referente ao usuario
def pets_usuario(id_usuario):
    conn = None
    cur = None
    tabela = None
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(query_pets, (id_usuario,))
        tabela = cur.fetchall()
    except Exception:
        print('Erro ao consultar pet')
        return
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

    for pet_id ,pet_nome, nome_especie, _ in tabela:
        print(f'ID: {pet_id}')
        print(f'Nome: {pet_nome}')
        print(f'Especie: {nome_especie}')
        print('-'*20)

#Lista dos remedios da consulta
def relatorio_consulta(id_consulta):
    conn = None
    cur = None
    tabela = None
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(query_relatorio_remedios,(id_consulta,))
        tabela = cur.fetchall()
        if not tabela:
            print('Nenhum remedio encontrada')
            return
    except Exception:
        print('Erro ao consultar relatorio')
        return
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

    for nome_remedio, dosagem, frequencia, duracao in tabela:
        print(f'Nome: {nome_remedio}')
        print(f'Dosagem: {dosagem}')
        print(f'Frequencia: {frequencia}')
        print(f'Duracao: {duracao}')
        print('-'*20)






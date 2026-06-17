from pydoc import text

from db import conectar
from queries_veterinario import query_lista_consultas, query_consultas_futuras, query_relatorio_consulta, query_adicionar_relatorio, \
    query_relatorio_remedio

#Lista todas as consultas futuras do veterinario a partir da data atual
def consultas_futuras(id_usuario):
    conn = conectar()
    cur = conn.cursor()
    cur.execute(query_consultas_futuras,(id_usuario,))
    tabela = cur.fetchall()
    if cur:
        cur.close()
    if conn:
        conn.close()
    for id_pet, pet_nome, pet_especie, data_consulta, descricao in tabela:
        print(f'Especie: {pet_especie}')
        print(f'Nome pet: {pet_nome}')
        print(f'Data de consulta: {data_consulta}')
        print(f'Descricao: {descricao}')
        print('-' * 20)

#Lista todas as consultas do veterinario
def lista_consulta(id_veterinario):
    conn = conectar()
    cur = conn.cursor()
    cur.execute(query_lista_consultas, (id_veterinario,))
    tabela = cur.fetchall()
    if cur:
        cur.close()
    if conn:
        conn.close()
    for id_consulta, pet_nome, pet_especie, data_consulta, veterinario, descricao in tabela:
        print(f'Id: {id_consulta}')
        print(f'Nome pet: {pet_nome}')
        print(f'Especie: {pet_especie}')
        print(f'Data de consulta: {data_consulta}')
        print(f'Veterinario: {veterinario}')
        print(f'Descricao: {descricao}')
        print('-'*20)

#Retorna relatorio da consulta se existir e pergunta se deseja olhar os remedios.
def relatorio_consulta(id_consulta):
    conn = None
    cur = None
    tabela = None
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(query_relatorio_consulta, (id_consulta,))
        tabela = cur.fetchone()
    except Exception as e:
        print(f'Erro: {e}')
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

    if tabela:
        peso_pet, descricao, diagnostico = tabela
        print(f'Peso: {peso_pet}')
        print(f'Descricao: {descricao}')
        print(f'Diagnostico: {diagnostico}')
    else:
        print('ID não encontrado')
        return

    while True:
        print('Remedios receitados: ')
        print('1-Verificar')
        print('2-Sair')
        escolha = input('Escolha: ')
        if escolha == 1:
            verificar_relatorio_remedio(id_consulta)
        elif escolha == 2:
            break
        else:
            print('Opção invalida')

#Verifica se a consulta já tem um relatorio e se não tem adiciona
def adicionar_relatorio_consulta(id_consulta):
    conn = None
    cur = None
    verificacao = None
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute('select id_consulta from relatorio where id_consulta = %s', (id_consulta,))
        verificacao = cur.fetchone()
    except Exception as e:
        print(f'Erro: {e}')
        return
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
    if verificacao:
        print('Esta consulta já contém um relatório.')
        return

    try:
        conn = conectar()
        cur = conn.cursor()
        peso = float(input('Informe o peso: '))
        descricao = input('Descrição: ')
        diagnostico = input('Diagnostico: ')
        cur.execute(query_adicionar_relatorio, (id_consulta, peso, descricao, diagnostico))
        conn.commit()
        print('Relatório cadastrado com sucesso!')
    except ValueError:
        print('Valor não aceito para o peso.')
    except Exception as e:
        print(f'Erro: {e}')
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

#Verificar se consulta tem remedios receitados
def verificar_relatorio_remedio(id_consulta):
    conn = None
    cur = None
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(query_relatorio_remedio, (id_consulta,))
        tabela = cur.fetchall()
    except Exception as e:
        print(f'Erro: {e}')
        return
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

    if tabela:
        for nome_remedio, dosagem, frequencia, periodo in tabela:
            print(f'Nome do remedio: {nome_remedio}')
            print(f'Dosagem: {dosagem}')
            print(f'Frequencia: {frequencia}')
            print(f'Periodo: {periodo}')
            print('-'*20)
    else:
        print('Nenhum remedio encontrado')



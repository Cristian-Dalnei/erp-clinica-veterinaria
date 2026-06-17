from db import conectar
from queries_gerente import quant_de_atendimentos_rank, quant_atendimentos_mes, clientes_inati_mais_6_meses, \
    diferenca_mes_atendimentos


#Quantidade de atendimentos po veterinario no mes, mais rank
def veterinario_rank_mes():
    conn = None
    cur = None
    tabela = None
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(quant_de_atendimentos_rank)
        tabela = cur.fetchall()
        print('Consulta bem sucedida')
    except Exception:
        print("Erro ao ler o banco de dados")
        return
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

    data_atual = None
    for veterinario, total_atendimentos, rank, data, data2 in tabela:
        if data !=  data_atual:
            data_atual = data
            print(f'\n=== {data_atual} ===')

        print(f'Rank-{rank}  Veterinario-{veterinario} Total Atendimentos-{total_atendimentos}')
 #Lista com a quantidade de consultas por mes
def quant_consulta_mes():
    conn = None
    cur = None
    tabela = None
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(quant_atendimentos_mes)
        tabela = cur.fetchall()
        print('Consulta bem sucedida')
    except Exception:
        print("Erro ao ler o banco de dados")
        return
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

    for _, mes_formatado, quantidade_atend in tabela:
        print(
            f'Data-{mes_formatado} - {quantidade_atend} atendimentos'
        )
#Lista de clientes inativos por mais de 6 meses
def cliente_inativos_dias():
    conn = None
    cur = None
    tabela = None
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(clientes_inati_mais_6_meses)
        tabela = cur.fetchall()
        print('Consulta bem sucedida')
    except Exception:
        print("Erro ao ler o banco de dados")
        return
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
#Quantidade de consulta por mes + status comparando ao ultimo mes
def diferenca_consultas_mes():
    conn = None
    cur = None
    tabela = None
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(diferenca_mes_atendimentos)
        tabela = cur.fetchall()
        print('Consulta bem sucedida')
    except Exception:
        print("Erro ao ler o banco de dados")
        return
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
    for mes_formatado, quantidade_atendimentos, diferenca_mes, status in tabela:
        print(f'Data - {mes_formatado}')
        print(f'Quantidade - {quantidade_atendimentos}')
        print(f'Difereça - {diferenca_mes}')
        print(f'Status - {status}\n')
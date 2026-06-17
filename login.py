from db import conectar

query_burcar_email = """
select
id_usuario,
email
from usuario
where email = %s
"""

query_tipo_usuario = """
select
t.id_tipo,
t.nome_tipo
from tipo_usuario
inner join tipo t on t.id_tipo = tipo_usuario.id_tipo
where id_usuario = %s
"""

query_id_usuario = """
select
id_usuario
from usuario 
where email = %s
"""

def consultar(email):
    conn = None
    cur = None
    tabela = None
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(query_burcar_email,(email,))
        print('Consultando email...')
        tabela = cur.fetchone()
    except Exception:
        print('Erro ao consultar usuario')
        return
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
    if not tabela:
        print('Usuario não encontrado')
        return
    id_usuario, email = tabela

    return id_usuario

def verificar_tipo(id_usuario):
    conn = None
    cur = None
    tabela = None
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(query_tipo_usuario, (id_usuario,))
        tabela = cur.fetchall()
    except Exception:
        print('Erro ao consultar usuario')
        return
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
    if not tabela:
        print('Não encontrado')
        return
    return tabela

def id_cliente(email):
    conn = None
    cur = None
    tabela = None
    id_cliente = None
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(query_id_usuario,(email,))
        tabela = cur.fetchone()
    except Exception:
        print('Erro ao consultar usuario')
        return
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
    if tabela:
        id_cliente = tabela[0]
        return id_cliente
    return None

def entrar(email):
    id_usuario = consultar(email)
    if id_usuario == None:
        print('Usuario não cadastrado')
        return None
    tipo_usuario = verificar_tipo(id_usuario)
    lista_id = []
    print('Selecione o id: ')
    for id_tipo, nome in tipo_usuario:
        print(f'ID - {id_tipo}  Função:{nome}')
        lista_id.append(id_tipo)

    while True:
        try:
            escolha = int(input('Informe o ID: '))
            break
        except ValueError:
            print('Digite um ID valido.')

    if not escolha in lista_id:
        print('ID não encontrado')
        return None

    return escolha














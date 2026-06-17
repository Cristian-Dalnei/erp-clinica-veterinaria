from db import conectar
from queries_funcionario import query_cadastro_cliente, query_lista_cliente, query_pesquisar_por_nome


def input_cadastro():
    nome = input('Digite o nome do cliente: ')
    sobrenome = input('Digite o sobrenome do cliente: ')
    email = input('Digite o email do cliente: ')
    ddd = input('Digite o ddd do cliente: ')
    numero = input('Digite o numero do cliente: ')
    rua = input('Digite o rua do cliente: ')
    cidade = input('Digite o cidade do cliente: ')
    bairro = input('Digite o bairro do cliente: ')
    numero_casa = input('Digite o numero da casa do cliente: ')
    return {
        'nome': f'{nome} {sobrenome}',
        'email': email,
        'telefone': f'{ddd}{numero}',
        'rua': rua,
        'cidade': cidade,
        'bairro': bairro,
        'numero_casa': numero_casa,
    }
def cadastrar_cliente():
    dados = input_cadastro()
    conn = None
    cur = None
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(
            query_cadastro_cliente, (dados['nome'],dados['email'],dados['telefone'],
            dados['rua'],dados['cidade'],dados['bairro'],dados['numero_casa'])
        )
        conn.commit()
        print('Cliente cadastrado com sucesso!')
    except Exception:
        print('Tente novamente!')
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def listar_cliente():
    conn = None
    cur = None
    tabela = None
    print('Listando clientes...')
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(query_lista_cliente)
        tabela = cur.fetchall()
    except Exception:
        print('Tente novamente!')
        return
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
    if tabela:
        for id_cliente, nome in tabela:
            print(f'ID={id_cliente} NOME={nome}')
    else:
        print('Dados não encontrados!')
def pesquisar_cliente_nome():
    conn = None
    cur = None
    tabela = None
    nome = input('Digite o nome do cliente: ')
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(query_pesquisar_por_nome,(f"%{nome}%",))
        tabela = cur.fetchall()
    except Exception:
        print('Tente novamente!')
        return
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
    if tabela:
        for id_cliente, nome_usuario in tabela:
            print(f'ID={id_cliente} NOME={nome_usuario}')
    else:
        print('Não encontrado!')


def especie():
    conn = None
    cur = None
    tabela = None
    print('Listando especies...')
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute('select id_especie, nome_especie from especie')
        tabela = cur.fetchall()
    except Exception as e:
        print(f'Erro: {e}')
        return
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
    for id_especie, nome_especie in tabela:
        print(f'ID={id_especie} NOME={nome_especie}')
def validar_especie():
    while True:
        tabela = None
        try:
            especie()
            id_especie = int(input('Digite o ID do especie: '))
            conn = conectar()
            cur = conn.cursor()
            cur.execute('select id_especie from especie')
            tabela = cur.fetchall()
            break
        except ValueError:
            print('Somente numeros')
            continue
        except Exception as e:
            print(f'Erro: {e}')
            continue
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
    for id_es in tabela:
        if id_es[0] == id_especie:
            return id_especie
    return None

def validar_usuario():
    while True:
        conn = None
        cur = None
        tabela = None
        try:
            id_dono = int(input('Digite o ID do cliente: '))
        except ValueError:
            print('Somente numeros')
            continue
        try:
            conn = conectar()
            cur = conn.cursor()
            cur.execute('select nome_usuario, email, celular from usuario where id_usuario = %s', (id_dono,))
            tabela = cur.fetchone()
        except Exception as e:
            print(f'Erro: {e}')
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
        if tabela:
            nome, email, celular = tabela
            print('Cliente:', nome)
            print('Email:', email)
            print('Celular:', celular)
            escolha = input('Confirmar [S/N]:').lower().strip()
            if escolha == 's':
                return id_dono
            elif escolha == 'n':
                continue
            else:
                print('Valor invalido!')
                continue
        else:
            print('Cliente não encontrado!')
            continue

def cadastrar_pet():
    from datetime import date
    id_dono = validar_usuario()
    nome_pet = input('Digite o nome do pet: ')
    id_especie =  validar_especie()
    raca = input('Digite o nome do raca: ')
    while True:
        try:
            dia = int(input('Digite o dia de nascimento: '))
            mes = int(input('Digite o mes de nascimento: '))
            ano = int(input('Digite o ano de nascimento: '))
            data_fomatada = date(ano, mes, dia)
            break
        except ValueError:
            print('Somente numeros')
            continue
    conn = None
    cur = None
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute('insert into pet(pet_nome, id_especie, raca, nascimento) values (%s, %s, %s, %s) returning id_pet',(nome_pet, id_especie, raca, data_fomatada))
        tabela = cur.fetchone()
        id_pet = tabela[0]
        cur.execute('insert into usuario_pet(id_pet, id_usuario) values (%s, %s)', (id_pet, id_dono))
        conn.commit()
        print('Pet cadastrado com sucesso!')
    except Exception as e:
        print(f'Erro: {e}')
        conn.rollback()
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()




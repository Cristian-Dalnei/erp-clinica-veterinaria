query_cadastro_cliente = """
insert into usuario(nome_usuario, email, celular, rua, cidade, bairro, numero)
values(%s, %s, %s, %s, %s, %s, %s)
"""

query_lista_cliente = """
select id_usuario, nome_usuario from usuario
"""

query_pesquisar_por_nome = """
select
id_usuario,
nome_usuario
from usuario
where ilike %s
"""
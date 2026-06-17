query_lista_consultas = """
select 
c.id_consulta, 
p.pet_nome,
e.nome_especie,
c.data_consulta,
u.nome_usuario as veterinario,
c.descricao
from consulta c
inner join pet p on c.id_pet = p.id_pet
inner join especie e on p.id_especie = e.id_especie
inner join usuario u on u.id_usuario = c.id_veterinario
where u.id_usuario = %s"""

query_consultas_futuras = """
select 
c.id_consulta, 
c.id_pet, 
p.pet_nome, 
e.nome_especie, 
c.data_consulta, 
c.descricao 
from consulta
c inner join pet p on p.id_pet = c.id_pet 
inner join especie e on e.id_especie = p.id_especie 
where data_consulta >= current_date and c.id_veterinario = %s"""

query_relatorio_consulta = """
select
r.peso_pet,
r.descricao,
r.diagnostico
from relatorio r
where id_consulta = %s
"""

query_adicionar_relatorio = """
insert into relatorio (id_consulta, peso_pet, descricao, diagnostico)
values (%s, %s, %s, %s)
"""

query_relatorio_remedio = """
select 
r.nome_remedio,
re.dosagem,
re.frequencia,
re.duracao
from relatorio_remedio re
inner join remedio r on r.id_remedio = re.id_remedio
where re.id_consulta = %s
"""
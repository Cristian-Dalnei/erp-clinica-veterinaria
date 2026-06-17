query_consultas_futuras = """
select
p.pet_nome,
u.nome_usuario as responsavel,
c.descricao,
c.data_consulta
from consulta c
inner join usuario u on u.id_usuario = c.id_responsavel
inner join pet p on p.id_pet = c.id_pet
where p.id_pet = %s and c.data_consulta >= current_timestamp
order by c.data_consulta
"""

query_lista_consultas = """
select 
c.id_consulta,
p.pet_nome,
u.nome_usuario as veterinario,
c.data_consulta,
c.descricao
from consulta c
inner join pet p on p.id_pet = c.id_pet
inner join usuario u on u.id_usuario = c.id_veterinario
where p.id_pet = %s and c.data_consulta < current_timestamp
order by c.data_consulta
"""

query_pets = """
select
p.id_pet,
p.pet_nome,
e.nome_especie,
u.nome_usuario
from pet p
inner join usuario_pet up on p.id_pet = up.id_pet
inner join especie e on e.id_especie = p.id_especie
inner join usuario u on u.id_usuario = up.id_usuario
where u.id_usuario = %s
"""

query_relatorio_remedios = """
select
r.nome_remedio,
rr.dosagem,
rr.frequencia,
rr.duracao
from relatorio_remedio rr
inner join remedio r on r.id_remedio = rr.id_remedio
where rr.id_consulta = %s
"""
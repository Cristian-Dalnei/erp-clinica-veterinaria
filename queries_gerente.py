quant_de_atendimentos_rank = """
with tabela1 as(
select
u.id_usuario,
u.nome_usuario as veterinario,
date_trunc('month',c.data_consulta) as mes,
to_char(data_consulta,'MM/YYYY') as mes_formatado
from consulta c
inner join usuario u on u.id_usuario = c.id_veterinario
), tabela2 as(
select
t1.id_usuario,
count(t1.id_usuario) as total_atendimentos,
t1.veterinario,
t1.mes,
t1.mes_formatado
from tabela1 t1
group by t1.id_usuario, t1.veterinario, t1.mes, t1.mes_formatado
)select
t2.veterinario,
t2.total_atendimentos,
rank() over(partition by t2.mes order by t2.total_atendimentos desc) as rank_atendimentos,
t2.mes_formatado,
t2.mes
from tabela2 t2
order by t2.mes, t2.total_atendimentos desc
"""

quant_atendimentos_mes ="""
select
date_trunc('month', data_consulta) as mes,
to_char(data_consulta,'MM/YYYY') as mes_formatado,
count(id_consulta) as quantidade_consultas
from consulta 
group by mes, mes_formatado
order by mes
"""

clientes_inati_mais_6_meses = """
select
u.nome_usuario,
max(c.data_consulta) as ultima_consulta,
current_date - max(c.data_consulta::date) as dias_sem_marcar
from usuario u
inner join consulta c on u.id_usuario = c.id_responsavel
group by u.id_usuario, u.nome_usuario
having max(c.data_consulta) < current_date - interval '6 months'
order by dias_sem_marcar desc
"""

diferenca_mes_atendimentos = """
with tabela1 as(
select
date_trunc('month',data_consulta) as mes,
to_char(data_consulta::date, 'MM/YYYY') as mes_formatado,
count(id_consulta) as quantidade_consultas
from consulta 
group by mes, mes_formatado
), tabela2 as(
select
t1.mes,
t1.mes_formatado,
t1.quantidade_consultas,
t1.quantidade_consultas - lag(t1.quantidade_consultas) over(order by t1.mes)as diferenca_mes
from tabela1 t1
)select
t2.mes_formatado,
t2.quantidade_consultas,
diferenca_mes,
case
	when diferenca_mes > 0 then 'Aumento'
	when diferenca_mes < 0 then 'Regrediu'
	else 'Sem alteraçao'
	end as Status
from tabela2 t2
"""

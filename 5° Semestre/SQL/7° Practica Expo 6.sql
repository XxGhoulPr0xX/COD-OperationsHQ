USE VETERINARIA;

SELECT m.nombre,r.descripcion,t.descripcion from Mascotas as m
	inner join Raza as r on m.raza_id=r.id
	inner join Tamaño as t on m.tamaño_id=t.id
--Son aquellos elementos que estan en el conjunto A y B, donde solo hay una interseccion

SELECT alpha.nombre as 'Mascotas', beta.nombre as 'Cliente'
from Mascotas alpha
left join Clientes beta
on alpha.Id=beta.id

select m.nombre,r.nombre from Raza r
left join Mascotas as m
on m.id=r.id
--Intersecta las dos tablas, pero solo trae a todos los de la izquierda

Select * from Mascotas as m
right join Raza as r
on m.id=r.id

select m.nombre,r.nombre,c.nombre from Mascotas as m
right join Raza as r on m.id=r.id
right join Clientes as c on m.cliente_id=c.id
--Intersecta las tablas, pero solo trae a todos de la izquierda
--Ejercicio 1
SELECT m.nombre,r.nombre from Mascotas as m
	inner join Raza as r on m.raza_id=r.id
--Ejercicio 2
select v.nombre,e.descripcion from Veterinario as v
left join Especialidad as e on v.especialidad_id=e.id
--Ejercicio 3
select s.descripcion,ts.servicio from Servicios as s
left join TipoDeServicio as ts on s.id_tipo=ts.id
--Ejercicio 4
SELECT d.Fecha,s.descripcion,m.nombre,h.Sintomas,h.Tratamiento from Detalles as d
	inner join Mascotas as m on m.id=d.Mascota_id
	inner join Servicios as s on  s.id=d.Servicio_id
	inner join Historial as h on  h.id_signos=d.Historial_id
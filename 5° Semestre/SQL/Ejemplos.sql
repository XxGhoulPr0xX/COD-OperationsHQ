use VETERINARIA;
select * from Clientes,Mascotas where Clientes.id=cliente_id;

select m.nombre,m.edad,m.sexo,c.nombre,c.telefono+' '+c.RFC [Nombre de cliente], (select nombre from Raza where id=m.raza_id) Raza
from Mascotas m
inner join Clientes C
on c.id=m.cliente_id
where raza_id in (select id from Raza where UPPER(nombre) like '%Labrador%')
AND m.edad BETWeen 2 and 10

select SUBSTRING(rfc,12,2) [rfc],rfc from Veterinario
where SUBSTRING(rfc,12,2) ='DF'

select * from Detalles
select * from Historial
select * from Atendido
/* 
	Se requiere de una consulta que muestre los servicios generados en enero del 2023
	en los cuales participan veterinario de las especialidades de oftamalogo o anestecia
	los datos requeridos son:
	nombre de la mascota
	nombre del servicio
	fecha del servicio
	detalles del servicio, como duracion, sintomas y tratamiento,
	nombre del veterinario
*/
select 
(select m.nombre from Mascotas m where m.id=Mascota_id) [nombre mascota],
(select s.descripcion from Servicios s where s.id=Servicio_id) [Nombre Servicio],
d.fecha,
d.Duracion,
h.Sintomas,
h.Tratamiento,
v.nombre,
(select nombre from Especialidad where id=v.especialidad_id) especialidad
--(select nombre from Veterinario where rfc=a.veterinario_id) veterinario
--(select v.nombre from Veterinario v where v.rfc=(select veterinario_id from Atendido where folio_id=d.Folio)) veterinario
from Detalles d
inner join Historial h
on d.Historial_id=h.id

inner join Atendido a
on d.Folio=a.folio_id
inner join Veterinario v
on a.veterinario_id=v.rfc
where fecha between '2023-01-01' and '2023-01-30'
and v.especialidad_id in (3,9)

--Ejemplos de consultas con WHERE:
use VETERINARIA;

--WHERE con <, >, <=, >=: para buscar todas las mascotas que tengan una edad mayor o igual a 8 años: 
--se utilizan para buscar filas donde el valor de una columna sea menor que, mayor que, menor o igual a, o mayor o igual a un valor especificado. 

SELECT * FROM Mascotas WHERE edad >= 8;
select * from Mascotas where edad <10;

--WHERE con IN: para buscar todas las mascotas de color "café" o "negro": 
--se utiliza para filtrar resultados basados en un conjunto de valores.

SELECT * FROM Mascotas WHERE color IN ('café', 'negro');

--WHERE con LIKE: para buscar todas las mascotas cuyo nombre empiece con "L": 
--se utiliza para buscar patrones dentro de una columna de texto.

SELECT * FROM Clientes WHERE nombre LIKE '%J%';


--WHERE con AND: para buscar todas las mascotas que tengan más de 5 años de edad y cuyo tamaño sea el "2": 
--se utiliza para combinar múltiples condiciones en una consulta.

SELECT * FROM Mascotas WHERE edad > 5 AND tamaño_id = 2;


--WHERE con OR: para buscar todas las mascotas que tengan menos de 2 años de edad o cuyo tamaño sea "5": 
--se utiliza para buscar filas que cumplan al menos una de varias condiciones en una consulta.

SELECT * FROM Mascotas WHERE edad < 2 OR tamaño_id = 5;


--WHERE con BETWEEN: para buscar todas las citas programadas para el mes de enero: 
--se utiliza para buscar filas donde el valor de una columna esté dentro de un rango de valores. 

SELECT * FROM Detalles WHERE Fecha BETWEEN '2023-01-01' AND '2023-01-31';

alter function RegresaTablaM(@parametro int)
returns table
as
return(
	select nombre,edad from Mascotas where edad >=@parametro
)

select * from RegresaTablaM('15')
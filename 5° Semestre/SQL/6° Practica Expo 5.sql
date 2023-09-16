use VETERINARIA;
--- Columna, nombre cualquiera= (select (variable cualquier).columna de la tabla que va aparecer from 
--tabla y su variable where variable.con la llave primaria de especialidad y despues la variable 
--de la otra columna ademas de su foranea de la primeria de la primera tabla) 
--que viene de la tabla original y al final su variable de nuevo
select nombre,especialidad_id, especialidad = (select E.descripcion from Especialidad E where E.id=V.especialidad_id) from Veterinario V
select nombre from Clientes where id in (select Cliente_id from DomicilioC where Noexte='123');
----------
--Ejercicio 1
select nombre, mascota = (select alpha.nombre from Mascotas alpha where alpha.id=beta.id) from Clientes beta
select nombre, tamaño = (select E.descripcion from Tamaño E where E.id=V.id) from Mascotas V
select nombre, calle = (select alpha.Calle from DomicilioC alpha where alpha.Cliente_id=beta.id) from Clientes beta

select * from Clientes
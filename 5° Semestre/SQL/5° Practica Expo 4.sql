use VETERINARIA;
---Se crea una tabla manualmente
-----------------------------------------------------------------
-----------------------------------------------------------------
create table clientebas(
	id int,
	nombre char(35)
);

insert into clientebas(id,nombre)
select id, nombre from Clientes where id<=10;

select * from clientebas;
---Se crea una nueva tabla  nueva con un solo codigo
select id, nombre, rfc, edad into personas
from Clientes;

select * from personas;
-----------------------------------------------------------------
-----------------------------------------------------------------
---1 Ejercicio: Aplicar una copia
select id, nombre, rfc, edad, telefono, correo into ClienteDani
from Clientes;

Select id,nombre,edad,RFC,telefono,correo from ClienteDani;

---2 Ejercicio Obtener datos específicos de una tabla y hacer una nueva: minimo 3 datos nombre, edad, rfc
select nombre, rfc, edad into ClientePecas
from Clientes;

Select nombre,rfc,edad from ClientePecas;

---3 Ejercicio Obtener datos específicos de una tabla mascotas y hacer una nueva con un where
create table Mascota1(
	id int,
	nombre char(35)
);

insert into Mascota1(id,nombre)
select id, nombre from Mascotas where id<=10;
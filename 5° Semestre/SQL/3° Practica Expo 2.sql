Use VETERINARIA;
---Ejercicio 2
SELECT folio_id FROM Atendido;
select  id from Especialidad;
select id from Historial;

SELECT id,nombre FROM Clientes;
SELECT edad,rfc FROM Clientes;
SELECT telefono,correo FROM Clientes;

select * from Atendido;
select * from Clientes;
select * from Detalles;
--Ejercicio 3
SELECT folio_id FROM Atendido where folio_id= 10 ;
select  id from Especialidad where id=10 ;


--Ejercicio 2 Daniela
SELECT nombre FROM Mascotas;
select nombre from Raza;
select id from Servicios;

SELECT especialidad_id,turno_id FROM Veterinario;
SELECT nombre,rfc FROM Veterinario;
SELECT telefono,correo FROM Veterinario;

select * from Signos;
select * from Detalles;
select * from Turno;

--Ejercicio 3 Daniela
SELECT folio_id FROM Atendido where folio_id= 10 ;
select  * from Especialidad where id<=10 ;


--Ejercicio 2 Dani x2
SELECT nombre FROM Especialidad



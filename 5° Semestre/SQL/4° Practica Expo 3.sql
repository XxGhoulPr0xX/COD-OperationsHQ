use VETERINARIA;

select * from Mascotas;

update Mascotas set nombre='Laika' where id=1;
delete from Mascotas where id=10;
-----Ejercicio 1

-----Ejercicio 2
select * from Veterinario;
delete from Veterinario where rfc='HOGM880427M75';
-----Ejercicio 3
select * from Clientes;
update Clientes set nombre='Javier Marquez' where id=3

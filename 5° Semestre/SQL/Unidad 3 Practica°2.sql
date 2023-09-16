use veterinaria
Create View ClientesMascota as
	select m.id [idMascotas],m.nombre [NombreMascotas],c.id [IdClientes],c.nombre [NombreCliente]
	from Mascotas m 
	inner join clientes c on m.cliente_id=c.id

select * from ClientesMascota

select * from detalles

select mes=
	(	
	case
	when month(d.fecha)=1 then 'enero'
	when month(d.fecha)=2 then 'febrero'
	when month(d.fecha)=12 then 'diciembre'
	end
	),
	year(d.fecha) [Año],
	sum(t.costo) [VentaTotal]
from detalles d
inner join tipodeservicio t on d.servicio_id=t.id 
group by year(d.fecha),month(d.fecha)

select month(d.fecha),year(d.Fecha),sum(t.costo) from detalles d
inner join tipodeservicio t on d.servicio_id=t.id
group by d.fecha,month(d.fecha)

Alter View ReporteVentas as
	select (month(d.fecha)) [Mes],year(d.fecha) [Año],sum(t.costo) [VentaTotal]
	from detalles d
	inner join tipodeservicio t on d.servicio_id=t.id 
	group by year(d.fecha),month(d.fecha)
select * from ReporteVentas
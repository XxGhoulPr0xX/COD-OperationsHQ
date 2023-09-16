use veterinaria
/* Practica �10:
	Crear una funcion tabla que regrese las fechas que tuvieron ventas superiores al promedio diario en un determinado mes
*/
alter FUNCTION VentasSuperiores(@mes int,@dia int)
Returns table
as
Return(
		select day(d.fecha) dia,sum(t.costo) costo,dbo.VentaA�oMes(@mes,@dia) promedio
		from detalles d
		inner join tipodeservicio t on t.id=d.Servicio_id
		where t.costo>=dbo.VentaA�oMes(@mes,@dia) and day(d.fecha)=@dia
		group by DAY(d.fecha)
)

select * from VentasSuperiores('01','02')
select dbo.VentaA�oMes('01') Promedio

		select day(d.fecha) dia,sum(t.costo) costo,dbo.VentaA�oMes('01','02') promedio
		from detalles d
		inner join tipodeservicio t on t.id=d.Servicio_id
		where t.costo>=dbo.VentaA�oMes('01','02') and day(d.fecha)='01'
		group by DAY(d.fecha)
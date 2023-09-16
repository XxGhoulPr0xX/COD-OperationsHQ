use VETERINARIA
/* Practica °9:
	Crear una funcion escalar que
	regrese el promedio venta diaria en un determinado mes
*/
ALTER FUNCTION VentaAñoMes(@mes int,@dia int,@año int)
RETURNS int
AS
BEGIN
	declare @ventas int
	set @ventas=(select AVG(t.costo) Promedio from Detalles d
				inner join TipoDeServicio t on t.id=d.Servicio_id
				where MONTH(d.Fecha)=@mes and DAY(d.fecha)=@dia)
	return @ventas
END

select dbo.VentaAñoMes('01','02') Promedio
select * from Detalles
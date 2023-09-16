----P9.Generar una funcion que reciba una fecha y
----que regrese la fecha en formato siguiente:
----ej: 01/01/2023 ----------> '01 de enero del 2023'
alter FUNCTION Fecha(@fecha date)
returns varchar(max)
as
BEGIN
	declare @fechan varchar(MAX)= ''
	set @fechan= CONCAT(DATENAME(DAY,@fecha),' de ',DATENAME(MONTH,@fecha),' del ',DATENAME(YEAR,@FECHA))
	return @fechan
END

select dbo.Fecha('2023-10-01') Fecha

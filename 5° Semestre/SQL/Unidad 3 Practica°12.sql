----P10.Generar una funcion que reciba una fecha y
----que regrese la fecha en formato siguiente:
----ej: 01/01/2023 ----------> '01 de enero del 2023'
ALTER FUNCTION A�os(@fechaNa date)
returns varchar(max)
as
BEGIN
	DECLARE @A�OS INT, @MESES INT, @EDAD Nvarchar(max)
	select @A�OS= (DATEDIFF(YEAR,@fechaNa,GETDATE()))-CASE WHEN DATEADD(YEAR,DATEDIFF(YEAR,@fechaNa,GetDate()),@fechaNa)>GETDATE() then 1 else 0 end
	select @MESES = DATEDIFF(MONTH,DATEADD(YEAR,@A�OS,@fechaNa),getDate())
	set @EDAD= CONVERT(nvarchar(MAX),@A�OS)+' A�os y '+CONVERT(nvarchar(MAX),@MESES)+' MESES'
	return @edad
END
select dbo.A�os('2001-06-01') Fecha_Nacimiento
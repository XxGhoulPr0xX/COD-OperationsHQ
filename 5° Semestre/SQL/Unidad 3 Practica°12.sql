----P10.Generar una funcion que reciba una fecha y
----que regrese la fecha en formato siguiente:
----ej: 01/01/2023 ----------> '01 de enero del 2023'
ALTER FUNCTION Años(@fechaNa date)
returns varchar(max)
as
BEGIN
	DECLARE @AÑOS INT, @MESES INT, @EDAD Nvarchar(max)
	select @AÑOS= (DATEDIFF(YEAR,@fechaNa,GETDATE()))-CASE WHEN DATEADD(YEAR,DATEDIFF(YEAR,@fechaNa,GetDate()),@fechaNa)>GETDATE() then 1 else 0 end
	select @MESES = DATEDIFF(MONTH,DATEADD(YEAR,@AÑOS,@fechaNa),getDate())
	set @EDAD= CONVERT(nvarchar(MAX),@AÑOS)+' Años y '+CONVERT(nvarchar(MAX),@MESES)+' MESES'
	return @edad
END
select dbo.Años('2001-06-01') Fecha_Nacimiento
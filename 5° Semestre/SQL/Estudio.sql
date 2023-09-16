create function sexo()
returns table
as
return(
	select * from Detalles where YEAR(fecha)='2023'
)

select * from dbo.sexo()
use veterinaria
alter function examen1Prome(@numeroa int,@numerob int,@numeroc int,@numerod int,@numerof int)
returns int
as
begin
	declare @suma int
	set @suma=@numeroa+@numerob+@numeroc+@numerod+@numerof
	declare @promedio float
	set @promedio=@suma/5
	return @promedio
end

select dbo.examen1Prome('1','2','3','4','5')

create function examen2()
returns table
as
return(
	select m.id,m.nombre nombreMascota,c.nombre nombreCliente,c.telefono,c.correo from Mascotas m
	inner join Clientes c on c.id=m.cliente_id
)
select * from dbo.examen2()
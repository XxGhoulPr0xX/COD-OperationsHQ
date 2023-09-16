use veterinaria;
select * from veterinario where especialidad_id=11
select	(select m.nombre from Mascotas m where m.id=d.Mascota_id),
		v.nombre,
		e.nombre,
		d.fecha
from detalles d
inner join Atendido a on a.folio_id=d.Folio
inner join Veterinario v on v.rfc=a.veterinario_id
inner join Especialidad e on v.especialidad_id=e.id
where e.id=11
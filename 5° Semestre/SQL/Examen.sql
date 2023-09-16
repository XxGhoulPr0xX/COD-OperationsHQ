use veterinaria;
select * from Veterinario where especialidad_id=11
select	(select m.nombre from Mascotas m where m.id=d.Mascota_id),
		(select v.nombre from Veterinario v	where v.rfc=a.veterinario_id),
		(select e.nombre from Especialidad e where e.id=11),
		d.fecha
from detalles d
inner join Atendido a on a.folio_id=d.Folio
inner join Veterinario v on v.rfc=a.veterinario_id
use VETERINARIA;
INSERT INTO raza (nombre, descripcion) 
VALUES ('Labrador Retriever', 'Raza de perro originaria de Terranova, en Canad�'),
		('Pastor Alem�n', 'Raza de perro originaria de Alemania'),
		('Golden Retriever', 'Raza de perro originaria de Escocia'),
		('Bulldog', 'Raza de perro originaria de Inglaterra'),
		('Poodle', 'Raza de perro originaria de Francia'),
		('D�lmata', 'Raza de perro originaria de Croacia'),
		('Chihuahua', 'Raza de perro originaria de M�xico'),
		('Doberman', 'Raza de perro originaria de Alemania'),
		('Beagle', 'Raza de perro originaria de Inglaterra'),
		('Schnauzer', 'Raza de perro originaria de Alemania'),
		('Yorkshire Terrier', 'Raza de perro originaria de Inglaterra'),
		('Boxer', 'Raza de perro originaria de Alemania'),
		('Shar Pei', 'Raza de perro originaria de China'),
		('Bich�n Fris�', 'Raza de perro originaria de Espa�a'),
		('Husky Siberiano', 'Raza de perro originaria de Rusia'),
		('B�xer', 'Raza de perro originaria de Alemania'),
		('Collie', 'Raza de perro originaria de Escocia'),
		('Terrier Escoc�s', 'Raza de perro originaria de Escocia'),
		('Gran Dan�s', 'Raza de perro originaria de Alemania'),
		('Cocker Spaniel', 'Raza de perro originaria de Inglaterra');
select * from raza;

INSERT INTO tama�o (descripcion) 
VALUES ('Peque�o'),
		('Mediano'),
		('Grande'),
		('Extra Grande'),
		('Toy'),
		('Miniatura'),
		('Standard'),
		('Peque�o-Mediano'),
		('Mediano-Grande'),
		('Muy Peque�o'),
		('Muy Grande'),
		('Peque�o-Grande'),
		('Gigante'),
		('Muy Peque�o-Mediano'),
		('Muy Grande-Mediano'),
		('Peque�o-Extra Grande'),
		('Mediano-Extra Grande'),
		('Muy Peque�o-Grande'),
		('Muy Grande-Extra Grande'),
		('Extra Peque�o');
select * from Tama�o;

INSERT INTO TipoDeServicio (servicio, costo) 
VALUES ('Consulta', 20000),
		('Vacunaci�n', 150.00),
		('Desparasitaci�n', 100.00),
		('Examen de sangre', 350.00),
		('Cirug�a', 8000.0),
		('Radiograf�a', 4500.0),
		('Ecosonograma', 7000.0),
		('An�lisis de orina', 2500.0),
		('Control de peso', 1200.0),
		('Ba�o y peluquer�a', 3500.0),
		('Limpieza dental', 6000.0),
		('Tratamiento de heridas', 300.00),
		('Ultrasonido', 500.00),
		('Consulta especializada', 300.00),
		('Prueba de alergias', 550.00),
		('Revisi�n general', 250.00),
		('Chequeo anual', 4500.0),
		('Cuidados post-operatorios', 35000),
		('Tratamiento para pulgas y garrapatas', 2000.0),
		('Control de enfermedades cr�nicas', 500.00);
select * from TipoDeServicio;

Insert into Servicios(descripcion,id_tipo)
Values ('Consulta',10),
		('Vacunaci�n',20),
		('Desparacitaci�n',9),
		('Examen de sangre',19),
		('Cirug�a',8),
		('Radiograf�a',18),
		('Ecosonograma',7),
		('An�lisis de orina',17),
		('Control de peso',7),
		('Ba�o y peluquer�a',16),
		('Limpieza dental',6),
		('Tratamiento de heridas',16),
		('Ultrasonido',5),
		('Consulta especializada',15),
		('Prueba de alerg�as',4),
		('Revisi�n general',14),
		('Chequeo anual',3),
		('Cuidados post-operatorios',13),
		('Tratamientos para pulgas',12),
		('Control de enfermedades cr�nicas',2);
select * from Servicios;


INSERT INTO turno (nombre, descripcion) 
VALUES ('Ma�ana', 'Turno de 8am a 2pm'),
		('Tarde', 'Turno de 2pm a 8pm'),
		('Noche', 'Turno de 8pm a 8am'),
		('24 horas', 'Turno continuo de 24 horas'),
		('Fines de semana', 'Turno los s�bados y domingos'),
		('D�as feriados', 'Turno en d�as festivos'),
		('Nocturno', 'Turno desde las 10pm hasta las 6am'),
		('Diurno', 'Turno de 6am a 10pm'),
		('Festivos', 'Turno los d�as festivos'),
		('Fin de semana', 'Turno los s�bados y domingos'),
		('Lunes a viernes', 'Turno de lunes a viernes'),
		('D�a', 'Turno de 8am a 6pm'),
		('Noche larga', 'Turno de 10pm a 8am'),
		('24 horas fines de semana', 'Turno continuo de 24 horas los s�bados y domingos'),
		('Feriados y fines de semana', 'Turno los d�as festivos y los s�bados y domingos'),
		('Ma�ana y tarde', 'Turno de 8am a 8pm'),
		('Tarde y noche', 'Turno de 2pm a 8am'),
		('Fin de semana y feriados', 'Turno los s�bados, domingos y d�as festivos'),
		('Feriados', 'Turno en d�as festivos'),
		('Noche corta', 'Turno de 10pm a 6am');
select * from Turno;

INSERT INTO especialidad (nombre, descripcion) 
VALUES ('Dermatolog�a', 'Especialidad encargada del cuidado de la piel y pelaje de las mascotas.'),
		('Oftalmolog�a', 'Especialidad encargada del cuidado de los ojos de las mascotas.'),
		('Cardiolog�a', 'Especialidad encargada del cuidado del coraz�n y sistema circulatorio de las mascotas.'),
		('Odontolog�a', 'Especialidad encargada del cuidado dental de las mascotas.'),
		('Cirug�a', 'Especialidad encargada de realizar operaciones quir�rgicas en mascotas.'),
		('Neurolog�a', 'Especialidad encargada del cuidado del sistema nervioso de las mascotas.'),
		('Nutrici�n', 'Especialidad encargada de recomendar una dieta adecuada para cada mascota seg�n sus necesidades.'),
		('Reproducci�n', 'Especialidad encargada del cuidado y manejo reproductivo de las mascotas.'),
		('Ortopedia', 'Especialidad encargada del cuidado y tratamiento de las lesiones musculoesquel�ticas de las mascotas.'),
		('Endocrinolog�a', 'Especialidad encargada del cuidado de los sistemas hormonales de las mascotas.'),
		('Oncolog�a', 'Especialidad encargada del diagn�stico y tratamiento de los tumores en las mascotas.'),
		('Infectolog�a', 'Especialidad encargada del diagn�stico y tratamiento de enfermedades infecciosas en mascotas.'),
		('Anestesiolog�a', 'Especialidad encargada del manejo y control del dolor en mascotas durante procedimientos m�dicos y quir�rgicos.'),
		('Traumatolog�a', 'Especialidad encargada del cuidado y tratamiento de lesiones traum�ticas en mascotas.'),
		('Terapia f�sica', 'Especialidad encargada del tratamiento y recuperaci�n de mascotas con problemas f�sicos.'),
		('Geriatr�a', 'Especialidad encargada del cuidado y tratamiento de mascotas de edad avanzada'),
		('Urolog�a', 'Especialidad encargada de estudiar las enfermedades relacionadas con el sistema urinario'),
		('Gastroenterolog�a', 'Especialidad encargada de estudiar las enfermedades relacionadas con el aparato digestivo'),
		('Endocrinolog�a', 'Especialidad encargada de estudiar las enfermedades relacionadas con las gl�ndulas endocrinas'),
		('Pediatr�a', 'Especialidad encargada de estudiar las enfermedades en ni�os y adolescentes');
select * from Especialidad;

INSERT INTO Veterinario (rfc,nombre,telefono,correo,turno_id,especialidad_id)
VALUES ('PEGI900823XX','Ivan','5525342779','ivan@gmail.com',1,1),
       ('LOAA870416SM5','Luis','5576453889','Luis@gmail.com',2,1),
	   ('GOMM9504278W0','Francisco','5526354792','Francisco@gmail.com',3,1),
       ('MOLM920427HI2','Carlos','5562341769','Carlos@gmail.com',4,1),
       ('CAMJ861215DF9','Mar�a','5562481062','Mar�a@gmail.com',5,1),
	   ('GUTA900426GG5','Jos�e','5578653428','Jos�e@gmail.com',6,2),
       ('MELG850902I44','Jonathan','5575291889','Jonhy@gmail.com',7,3),
	   ('NIGJ840427LH7','Javier','552686542','Javier@gmail.com',1,4),
       ('JENJ900427TG1','Paola','5562347629','Pao@gmail.com',1,5),
	   ('HOGM880427M75','Cinthya','5597992779','Cinthy@gmail.com',2,1),
       ('GALM790427D32','Ver�nica','5567542679','Vero@gmail.com',3,2),
	   ('FERM830427LH6','Gloria','5598753762','Goya@gmail.com',4,3),
       ('DURJ800427K86','Julieta','5567513506','July@gmail.com',5,4),
       ('CENM920427ML8','Daniel','5573528469','Leinad@gmail.com',8,1),
       ('BANM840427TQ2','Fernando','5556382917','Fercho@gmail.com',9,11),
	   ('ZAGA9004279H9','Fredy','5533662745','Fredy@gmail.com',15,19),
	   ('YEPJ810427M54','Gabriel','5597130756','Gabo@gmail.com',14,16),
       ('VIAJ920427F33','Andrea','5578452645','Andie@gmail.com',12,11),
       ('TORC830426QD9','Diego','5575372890','Diegolin@gmail.com',15,18),
       ('ROAM900427LK2','Jennifer','5578372546','Jenny@gmail.com',17,18);
select * from Veterinario

INSERT INTO DomicilioV(Veterinario_rfc, calle, Nexte, Ninte, cp, municipio) 
VALUES  ('PEGI900823XX', 'Calle de la Amistad', '123', '4A', '01010', 'Coyoac�n'),
		('LOAA870416SM5', 'Avenida de la Reforma', '456', 'B10', '06200', 'Cuauht�moc'),
		('GOMM9504278W0', 'Calle Insurgentes Sur', '789', '3C', '14000', 'Benito Ju�rez'),
		('MOLM920427HI2', 'Calle de la Felicidad', '321', '2B', '01100', '�lvaro Obreg�n'),
		('CAMJ861215DF9', 'Avenida Revoluci�n', '567', 'A8', '01020', 'Tlalpan'),
		('GUTA900426GG5', 'Calle del Progreso', '890', '5D', '09400', 'Iztapalapa'),
		('MELG850902I44', 'Avenida Patriotismo', '432', '1F', '03800', 'Cuauht�moc'),
		('NIGJ840427LH7', 'Calle de la Libertad', '765', '4E', '01210', 'Azcapotzalco'),
		('ROAM900427LK2', 'Calle de la Paz', '098', '6G', '15000', 'Milpa Alta'),
		('TORC830426QD9', 'Calle del Trabajo', '543', '9H', '13100', 'Tl�huac'),
		('VIAJ920427F33', 'Avenida de los Insurgentes', '876', '7I', '08000', 'Gustavo A. Madero'),
		('YEPJ810427M54', 'Calle de la Esperanza', '210', '2J', '09250', 'Iztacalco'),
		('ZAGA9004279H9', 'Avenida Ju�rez', '543', '3K', '06000', 'Cuauht�moc'),
		('BANM840427TQ2', 'Av. Insurgentes Norte', '567', '1', '07000', 'Gustavo A. Madero'),
		('CENM920427ML8', 'Calle Sur 16', '123', '3B', '08000', 'Iztacalco'),
		('DURJ800427K86', 'Calle Oriente 11', '456', '2A', '09000', 'Iztapalapa'),
		('FERM830427LH6', 'Calle Tierra y Libertad', '321', '', '10200', 'La Magdalena Contreras'),
		('GALM790427D32', 'Calle Principal', '12', '', '12000', 'Milpa Alta'),
		('HOGM880427M75', 'Av. Toluca', '5678', '', '01760', '�lvaro Obreg�n'),
		('JENJ900427TG1', 'Av. Tl�huac', '789', '4', '13000', 'Tl�huac');
select * from DomicilioV;


INSERT INTO Clientes(nombre, edad, RFC, telefono, correo)
VALUES ('Juan P�rez', 35, 'PEJL890321', '551234567', 'juan.perez@email.com'),
		('Ana Garc�a', 28, 'GARA920405', '552345678', 'ana.garcia@email.com'),
		('Pedro Hern�ndez', 42, 'HEPP750818', '553456789', 'pedro.hernandez@email.com'),
		('Mar�a Torres', 50, 'TOMM690716', '554567890', 'maria.torres@email.com'),
		('Sergio M�ndez', 37, 'MEPS831014', '555678901', 'sergio.mendez@email.com'),
		('Luisa Garc�a', 42, 'GALM790625', '556789012', 'luisa.garcia@email.com'),
		('Jorge Morales', 29, 'MORJ911105', '557890123', 'jorge.morales@email.com'),
		('Martha G�mez', 46, 'GOMM750929', '558901234', 'martha.gomez@email.com'),
		('Ricardo S�nchez', 38, 'SARJ831219', '559012345', 'ricardo.sanchez@email.com'),
		('Laura Ju�rez', 25, 'JUAL960831', '550123456', 'laura.juarez@email.com'),
		('Oscar Mart�nez', 33, 'MAOO890615', '551234567', 'oscar.martinez@email.com'),
		('Carla Flores', 31, 'FOCC900510', '552345678', 'carla.flores@email.com'),
		('Ra�l P�rez', 48, 'PERA730315', '553456789', 'raul.perez@email.com'),
		('Ana Gonz�lez', 32, 'GOZA870101345', '551234567', 'ana.gonzalez@example.com'),
		('Miguel Hern�ndez', 45, 'HEMM751212123', '552345678', 'miguel.hernandez@example.com'),
		('Mar�a L�pez', 27, 'LOMM940203876', '553456789', 'maria.lopez@example.com'),
		('Carlos S�nchez', 50, 'SACO700321423', '554567890', 'carlos.sanchez@example.com'),
		('Ver�nica Rodr�guez', 38, 'ROVV810627923', '555678901', 'veronica.rodriguez@example.com'),
		('Javier Ram�rez', 29, 'RAJJ920219765', '556789012', 'javier.ramirez@example.com'),
		('Sof�a G�mez', 43, 'GOSS780724123', '557890123', 'sofia.gomez@example.com');
select * from Clientes;

Insert into Mascotas(nombre,edad,peso,color,sexo,raza_id,cliente_id,tama�o_id)
Values ('Laika',13,25,'caf�',1,1,2,3),
	   ('Pechuga',7,25,'blanco',0,2,3,4),
   	   ('Rito',9,23,'miel',1,3,4,5),
	   ('Max',15,27,'miel',1,4,5,6),
	   ('Peluchina',11,15,'gris',0,5,6,7),
	   ('Shoulder',12,25,'blanco',0,6,7,8),
	   ('Ram�n',15,30,'amarillo',1,7,8,9),
	   ('Firulais',14,27,'negro',1,8,9,10),
	   ('Benito',13,20,'gris',1,9,10,11),
	   ('Duque',14,22,'negro',1,10,11,12),
	   ('Princesa',15,25,'blanco',0,11,12,13),
	   ('Zoe',13,25,'caf�',0,12,13,14),
	   ('Kiara',13,27,'gris',0,13,14,15),
	   ('Goofy',12,22,'amarillo',1,14,15,16),
	   ('Gary',17,21,'caf�',1,15,16,17),
	   ('Scooby',10,15,'caf�',1,16,17,18),
	   ('Chocolate',9,24,'caf�',0,17,18,19),
	   ('Loki',12,23,'negro',1,18,19,20),
	   ('Mila',11,20,'blanco',0,19,20,1),
	   ('Mike',14,20,'caf�',1,20,1,2);
select * from Mascotas;

INSERT INTO Signos (peso, temperatura) 
VALUES  ('4.5 kg', '37.2 �C'),
		('12.3 kg', '38.1 �C'),
		('6.8 kg', '39.5 �C'),
		('3.2 kg', '36.9 �C'),
		('9.1 kg', '37.8 �C'),
		('15.6 kg', '36.5 �C'),
		('7.8 kg', '38.7 �C'),
		('2.9 kg', '39.3 �C'),
		('5.4 kg', '37.1 �C'),
		('11.7 kg', '38.5 �C'),
		('13.8 kg', '39.8 �C'),
		('8.2 kg', '37.4 �C'),
		('4.6 kg', '38.9 �C'),
		('10.5 kg', '36.7 �C'),
		('6.3 kg', '39.1 �C'),
		('2.1 kg', '37.9 �C'),
		('14.2 kg', '38.3 �C'),
		('9.8 kg', '36.8 �C'),
		('5.9 kg', '39.4 �C'),
		('11.3 kg', '37.6 �C');
select * from Signos;

INSERT INTO DomicilioC(cliente_id, calle, noexte, nointe, cp, municipio) 
VALUES (1, 'Calle de la Amistad', '123', '4A', '01010', 'Coyoac�n'),
		(2, 'Avenida de la Reforma', '456', 'B10', '06200', 'Cuauht�moc'),
		(3, 'Calle Insurgentes Sur', '789', '3C', '14000', 'Benito Ju�rez'),
		(4, 'Calle de la Felicidad', '321', '2B', '01100', '�lvaro Obreg�n'),
		(5, 'Avenida Revoluci�n', '567', 'A8', '01020', 'Tlalpan'),
		(6, 'Calle del Progreso', '890', '5D', '09400', 'Iztapalapa'),
		(7, 'Avenida Patriotismo', '432', '1F', '03800', 'Cuauht�moc'),
		(8, 'Calle de la Libertad', '765', '4E', '01210', 'Azcapotzalco'),
		(9, 'Calle de la Paz', '098', '6G', '15000', 'Milpa Alta'),
		(10, 'Calle del Trabajo', '543', '9H', '13100', 'Tl�huac'),
		(11, 'Avenida de los Insurgentes', '876', '7I', '08000', 'Gustavo A. Madero'),
		(12, 'Calle de la Esperanza', '210', '2J', '09250', 'Iztacalco'),
		(13, 'Avenida Ju�rez', '543', '3K', '06000', 'Cuauht�moc'),
		(14, 'Av. Insurgentes Norte', '567', '1', '07000', 'Gustavo A. Madero'),
		(15, 'Calle Sur 16', '123', '3B', '08000', 'Iztacalco'),
		(16, 'Calle Oriente 11', '456', '2A', '09000', 'Iztapalapa'),
		(17, 'Calle Tierra y Libertad', '321', '', '10200', 'La Magdalena Contreras'),
		(18, 'Calle Principal', '12', '', '12000', 'Milpa Alta'),
		(19, 'Av. Toluca', '5678', '', '01760', '�lvaro Obreg�n'),
		(20, 'Av. Tl�huac', '789', '4', '13000', 'Tl�huac');
select * from DomicilioC;

insert into Historial(Sintomas, Tratamiento,id_signos)
values ('infeccion oral','extraccion',5),
		('infeccion de oidos','limpieza',2),
		('dermatitis','suero de piel',1),
		('parvovirus','desparasitante',1),
		('obesidad','hacer ejercicio',3),
		('vomito rojo','inyecciones',5),
		('tos cronica','polvos',4),
		('demasiada sed','suero',3),
		('mal peaje','ba�o constante',1),
		('patita rota','vendaje yeso',2),
		('dermatitis','suero de piel',3),
		('vomito','inyecciones',5),
		('mucha cera en oidos','limpieza',4),
		('epilapsia','inyecciones',1),
		('infeccion oral','extraccion',3),
		('demasiada sed','suero',1),
		('parvovirus','desparasitante',2),
		('rabia','vacuna',5),
		('gusanos en el estomago','desparasitante',4),
		('ataques de epilepsia','inyecciones',1);
select * from Historial;

insert into Detalles(mascota_id,servicio_id,Historial_id,Duracion, fecha, descripcion)
values  (1,2,1,'1 horas','2022-12-08','cirugia para remover la matriz'),
		(2,4,2,'10 minutos','2023-02-15','vacuna contra la rabia'),
		(3,5,3,'1 hora','2023-02-14','castracion'),
		(4,1,4,'2 horas','2023-02-13','estetica canina'),
		(5,2,5,'40 minutos','2023-02-12','cirugia para remover la matriz'),
		(6,4,6,'10 minutos','2023-02-11','vacuna contra la rabia'),
		(7,5,7,'2 horas','2023-02-10','castracion'),
		(8,3,8,'25 minutos','2023-02-09','examen medico'),
		(9,3,9,'25 minutos','2023-02-08','examen medico'),
		(10,2,10,'50 minutos','2023-01-27','cirugia para remover la matriz'),
		(2,4,11,'15 minutos','2023-01-28','vacuna contra la rabia'),
		(4,5,12,'1 hora','2023-01-29','castracion'),
		(6,1,13,'2 horas','2023-01-30','estetica canina'),
		(7,2,14,'1 hora','2023-02-02','cirugia para remover la matriz'),
		(2,4,15,'10 minutos','2023-02-03','vacuna contra la rabia'),
		(1,5,16,'1 hora','2023-02-05','castracion'),
		(6,1,17,'2 horas','2023-02-04','estetica canina'),
		(8,3,18,'30 minutos','2023-02-01','examen medico'),
		(10,5,19,'1 hora','2023-02-01','castracion'),
		(4,1,20,'2 horas','2023-01-31','estetica canina');
select * from Detalles;

insert into Atendido(folio_id,veterinario_id)
values (1,'PEGI900823XX'),
	   (2,'LOAA870416SM5'),
	   (3,'GOMM9504278W0'),
	   (4,'MOLM920427HI2'),
	   (5,'CAMJ861215DF9'),
	   (6,'GUTA900426GG5'),
	   (7,'MELG850902I44'),
	   (8,'NIGJ840427LH7'),
	   (9,'JENJ900427TG1'),
	   (10,'HOGM880427M75'),
	   (11,'GALM790427D32'),
	   (12,'FERM830427LH6'),
	   (13,'DURJ800427K86'),
	   (14,'CENM920427ML8'),
	   (15,'BANM840427TQ2'),
	   (16,'ZAGA9004279H9'),
	   (17,'YEPJ810427M54'),
	   (18,'VIAJ920427F33'),
	   (19,'TORC830426QD9'),
	   (20,'ROAM900427LK2');
select * from Atendido;

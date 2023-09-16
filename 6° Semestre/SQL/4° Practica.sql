CREATE VIEW DatosPelicula AS
	SELECT p.IdPeliculas, p.Nombre, d.Nombre AS NombreDirector, p.FechaEstreno
	FROM Peliculas p
	INNER JOIN DirePelicula dp ON dp.IdPeliculas = p.IdPeliculas
	INNER JOIN Director d ON dp.IdDirector = d.IdDirector;

CREATE FUNCTION DirectorPeliculas(@iddirector tinyint)
RETURNS TABLE
AS
RETURN (
	SELECT p.Nombre, d.Nombre AS NombreDirector
	FROM Peliculas p 
	INNER JOIN DirePelicula dp ON dp.IdPeliculas = p.IdPeliculas
	INNER JOIN Director d ON dp.IdDirector = d.IdDirector
	where d.IdDirector=@iddirector
)

-- Inserciones para la tabla Clasificacion
INSERT INTO Clasificacion (IdClasificacion, Clasificacion) VALUES
(1, 'A'),
(2, 'B'),
(3, 'C'),
(4, 'D'),
(5, 'E'),
(6, 'F'),
(7, 'G'),
(8, 'H'),
(9, 'I'),
(10, 'J');

-- Inserciones para la tabla Actores
INSERT INTO Actores (IdActor, Nombre, ApellidoP, ApellidoM) VALUES
(1, 'Juan', 'Garc�a', 'L�pez'),
(2, 'Mar�a', 'Mart�nez', 'P�rez'),
(3, 'Carlos', 'Rodr�guez', 'Ram�rez'),
(4, 'Ana', 'Hern�ndez', 'G�mez'),
(5, 'David', 'Gonz�lez', 'Fern�ndez'),
(6, 'Laura', 'D�az', 'Torres'),
(7, 'Jos�', 'L�pez', 'S�nchez'),
(8, 'Paula', 'P�rez', 'Mart�nez'),
(9, 'Miguel', 'Ram�rez', 'Garc�a'),
(10, 'Sof�a', 'G�mez', 'Hern�ndez');

-- Inserciones para la tabla Director
INSERT INTO Director (IdDirector, Nombre, ApellidoPa, ApellidoMa) VALUES
(1, 'Alejandro', 'G�mez', 'L�pez'),
(2, 'Isabel', 'Mart�nez', 'P�rez'),
(3, 'Luis', 'Rodr�guez', 'Ram�rez'),
(4, 'Elena', 'Hern�ndez', 'G�mez'),
(5, 'Pablo', 'Gonz�lez', 'Fern�ndez'),
(6, 'Carmen', 'D�az', 'Torres'),
(7, 'Andr�s', 'L�pez', 'S�nchez'),
(8, 'Ana', 'P�rez', 'Mart�nez'),
(9, 'Juan', 'Ram�rez', 'Garc�a'),
(10, 'Mar�a', 'G�mez', 'Hern�ndez');

-- Inserciones para la tabla Genero
INSERT INTO Genero (IdGenero, Nombre) VALUES
(1, 'Acci�n'),
(2, 'Comedia'),
(3, 'Drama'),
(4, 'Fantas�a'),
(5, 'Ciencia Ficci�n'),
(6, 'Aventura'),
(7, 'Romance'),
(8, 'Suspenso'),
(9, 'Terror'),
(10, 'Animaci�n');

-- Inserciones para la tabla Peliculas
INSERT INTO Peliculas (IdPeliculas, Nombre, FechaSalida, FechaEstreno, Clasificacion) VALUES
(1, 'Pelicula 1', '2023-05-01', '2023-05-15', 1),
(2, 'Pelicula 2', '2023-05-02', '2023-05-16', 2),
(3, 'Pelicula 3', '2023-05-03', '2023-05-17', 3),
(4, 'Pelicula 4', '2023-05-04', '2023-05-18', 4),
(5, 'Pelicula 5', '2023-05-05', '2023-05-19', 5),
(6, 'Pelicula 6', '2023-05-06', '2023-05-20', 6),
(7, 'Pelicula 7', '2023-05-07', '2023-05-21', 7),
(8, 'Pelicula 8', '2023-05-08', '2023-05-22', 8),
(9, 'Pelicula 9', '2023-05-09', '2023-05-23', 9),
(10, 'Pelicula 10', '2023-05-10', '2023-05-24', 10);

-- Inserciones para la tabla Sala
INSERT INTO Sala (IdSala, Sala) VALUES
(1, 'Sala 1'),
(2, 'Sala 2'),
(3, 'Sala 3'),
(4, 'Sala 4'),
(5, 'Sala 5'),
(6, 'Sala 6'),
(7, 'Sala 7'),
(8, 'Sala 8'),
(9, 'Sala 9'),
(10, 'Sala 10');

-- Inserciones para la tabla SalaPeli
INSERT INTO SalaPeli (IdPeliculas, IdSala) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);

-- Inserciones para la tabla GeneroPeli
INSERT INTO GeneroPeli (IdPeliculas, IdGenero) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);

-- Inserciones para la tabla ActorPeli
INSERT INTO ActorPeli (IdActor, IdPelicula) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);

-- Inserciones para la tabla DirePelicula
INSERT INTO DirePelicula (IdPeliculas, IdDirector) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);

select * from dbo.DirectorPeliculas(1) 
select * from dbo.DatosPelicula
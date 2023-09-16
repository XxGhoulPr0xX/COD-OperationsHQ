CREATE DATABASE CINE;
USE CINE

Create table Clasificacion(
	IdClasificacion tinyint primary key not null,
	Clasificacion varchar(max) not null
)
Create table Actores(
	IdActor tinyint primary key not null,
	Nombre varchar(max) not null,
	ApellidoP varchar(max) not null,
	ApellidoM varchar(max) not null
)
Create table Director(
	IdDirector tinyint primary key not null,
	Nombre varchar(max) not null,
	ApellidoPa varchar(max) not null,
	ApellidoMa varchar(max) not null
)
Create table Genero(
	IdGenero tinyint primary key not null,
	Nombre varchar(max) not null
)
Create table Peliculas(
	IdPeliculas tinyint primary key not null,
	Nombre varchar(max) not null,
	FechaSalida date not null,
	FechaEstreno date not null,
	Clasificacion tinyint not null,
	FOREIGN KEY (Clasificacion) references Clasificacion(IdClasificacion)
)
Create table Sala(
	IdSala tinyint primary key not null,
	Sala varchar(max) not null
)
Create table SalaPeli(
	IdPeliculas tinyint not null,
	IdSala tinyint not null,
	FOREIGN KEY (IdSala) references Sala(IdSala),
	FOREIGN KEY (IdPeliculas) references Peliculas(IdPeliculas)
)
Create table GeneroPeli(
	IdPeliculas tinyint not null,
	IdGenero tinyint not null,
	FOREIGN KEY (IdGenero) references Genero(IdGenero),
	FOREIGN KEY (IdPeliculas) references Peliculas(IdPeliculas)
)
Create table ActorPeli(
	IdActor tinyint not null,
	IdPelicula tinyint not null,
	FOREIGN KEY (IdActor) references Actores(IdActor),
	FOREIGN KEY (IdPelicula) references Peliculas(IdPeliculas)
)
Create table DirePelicula(
	IdPeliculas tinyint not null,
	IdDirector tinyint not null,
	FOREIGN KEY (IdDirector) references Director(IdDirector),
	FOREIGN KEY (IdPeliculas) references Peliculas(IdPeliculas)
)
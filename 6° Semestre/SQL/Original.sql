CREATE DATABASE CINE;
USE CINE
CREATE TABLE Sala(
	IdSala int identity(1,1) primary key,
	Descripcion varchar(max) not null
)
CREATE TABLE Productores(
	IdProductor int identity(1,1) primary key,
	Nombre varchar(Max) NOT NULL,
	Nacionalidad varchar(Max) NOT NULL
)
CREATE TABLE Clasificacion(
	IdClasificacion int identity(1,1) primary key,
	Nombre varchar(MAX) NOT NULL,
	Descripcion varchar(MAX) NOT NULL,
	EdadMin INT NOT NULL
)
CREATE TABLE Genero(
	IdGenero int identity(1,1) primary key,
	Nombre varchar(max) NOT NULL,
	Descripcion varchar(max) NOT NULL,
	Clasificacion INT NOT NULL,
	FOREIGN KEY (Clasificacion) references Clasificacion(IdClasificacion)
)
CREATE TABLE Peliculas(
	IdPelicula int identity(1,1) primary key,
	Titutlo varchar(Max) NOT NULL,
	Duracion Decimal(4,2) NOT NULL,
	Genero INT NOT NULL,
	Productores INT NOT NULL,
	FOREIGN KEY (Productores) references Productores(IdProductor),
	FOREIGN KEY (Genero) REFERENCES Genero(IdGenero)
)
CREATE TABLE DatellesSala(
	Id_Sala INT NOT NULL,
	Id_Pelicula INT NOT NULL,
	Horario Decimal(4,2) NOT NULL,
    FOREIGN KEY (Id_Sala) REFERENCES Sala(IdSala),
	FOREIGN KEY (Id_Pelicula) REFERENCES Peliculas(IdPelicula)
)
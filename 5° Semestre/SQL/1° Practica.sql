CREATE DATABASE VETERINARIA;

USE veterinaria;

CREATE TABLE Clientes (
  id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
  nombre char(32) NOT NULL,
  edad TINYINT NOT NULL,
  RFC VARCHAR(18) NOT NULL,
  telefono char(10) NOT NULL,
  correo VARCHAR(30) NOT NULL
);

CREATE TABLE DomicilioC (
  Cliente_id INT NOT NULL,
  Calle char(32) NOT NULL,
  Noexte char(16) NOT NULL,
  Nointe char(16) NOT NULL,
  Cp char(5) NOT NULL,
  Municipio char(32) NOT NULL,
  FOREIGN KEY (Cliente_id) REFERENCES Clientes(id)
);

CREATE TABLE Tamaño (
 id INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
  descripcion char(64) NOT NULL
);

CREATE TABLE Raza (
  id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
  nombre char(32) NOT NULL,
  descripcion char(64) NOT NULL
);

CREATE TABLE Signos (
  id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
  peso char(20) NOT NULL,
  temperatura char(10) NOT NULL
);

CREATE TABLE TipoDeServicio (
  id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
  servicio varchar(64) NOT NULL,
  costo DECIMAL(8,2) NOT NULL
);

CREATE TABLE Especialidad (
  id INT IDENTITY(1,1) NOT NULL  PRIMARY KEY,
  nombre char(64) NOT NULL,
  descripcion varchar(128) NOT NULL
);

CREATE TABLE Turno (
  id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
  nombre char(64) NOT NULL,
  descripcion varchar(128) NOT NULL
);

CREATE TABLE Veterinario (
  rfc varchar(13) NOT NULL PRIMARY KEY,
  nombre char(35) NOT NULL,
  telefono char(10) NOT NULL,
  correo VARCHAR(35) NOT NULL,
  turno_id INT NOT NULL,
  especialidad_id INT NOT NULL
  FOREIGN KEY (especialidad_id) REFERENCES Especialidad(id),
  FOREIGN KEY (turno_id) REFERENCES Turno(id)
);
CREATE TABLE DomicilioV (
  Veterinario_rfc varchar(13),
  Calle char(32) NOT NULL,
  Nexte char(16) NOT NULL,
  Ninte char(16) NOT NULL,
  Cp char(5) NOT NULL,
  Municipio VARCHAR(35) NOT NULL,
  FOREIGN KEY (Veterinario_rfc) REFERENCES Veterinario(rfc)
);


CREATE TABLE Servicios (
  id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
  descripcion varchar(35) NOT NULL,
  id_tipo INT NOT NULL,
  FOREIGN KEY (id_tipo) REFERENCES TipodeServicio(id)
);

CREATE TABLE Historial (
  id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
  Sintomas VARCHAR(60) NOT NULL,
  Tratamiento char(25) NOT NULL,
  id_signos INT NOT NULL,
  FOREIGN KEY (id_signos) REFERENCES Signos(id)
);

CREATE TABLE Mascotas (
  id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
  nombre char(35) NOT NULL,
   edad TINYINT NOT NULL,
  peso char(15) NOT NULL,
  color char(10) NOT NULL,
  sexo BIT NOT NULL,
  raza_id INT NOT NULL,
  cliente_id INT NOT NULL,
  tamaño_id INT NOT NULL,
  FOREIGN KEY (tamaño_id) REFERENCES Tamaño(id),
  FOREIGN KEY (raza_id) REFERENCES Raza(id),
  FOREIGN KEY (cliente_id) REFERENCES Clientes(id)
);

CREATE TABLE Detalles (
  Folio INT IDENTITY(1,1) NOT NULL  PRIMARY KEY,
  Mascota_id INT NOT NULL,
  Servicio_id INT NOT NULL,
  Historial_id INT NOT NULL,
  Duracion varchar(64) NOT NULL,
  Fecha date NOT NULL,
  descripcion VARCHAR(64) NOT NULL,
  FOREIGN KEY (Mascota_id) REFERENCES Mascotas(id),
  FOREIGN KEY (Servicio_id) REFERENCES Servicios(id),
  FOREIGN KEY (Historial_id) REFERENCES Historial(id)
);

CREATE TABLE Atendido (
  folio_id INT NOT NULL,
  veterinario_id varchar(13) NOT NULL,
  FOREIGN KEY (folio_id) REFERENCES Detalles(Folio),
  FOREIGN KEY (veterinario_id) REFERENCES Veterinario(rfc)
);
use VETERINARIA
/* Practica °4:
	Generar una funcion escalar que reciba un curp valida y retorne la entidad de nacimiento:
	Ejemplo: TOAO860920H'PL'RLC04 retorna puebla
*/ 
ALTER FUNCTION obtenerEntidadNacimiento(@curp CHAR(18))
RETURNS NVARCHAR(50)
AS
BEGIN
	DECLARE @Estados TABLE (id int,code varchar(2),Nombre varchar(50))
	DECLARE @i int =0
    DECLARE @codigoEntidad CHAR(2) = SUBSTRING(@curp, 12, 2);
    DECLARE @entidadNacimiento NVARCHAR(50);

	Insert into @Estados (id,code,nombre)
	VALUES	(1,'AS','AGUASCALIENTES'),(2,'BC','BAJA CALIFORNIA'),(3,'BS','BAJA CALIFORNIA SUR'),(4,'CC','CAMPECHE'),
			(5,'CL','COAHUILA DE ZARAGOZA'),(6,'CM','COLIMA'),(7,'CS','CHIAPAS'),(8,'CH','CHIHUAHUA'),
			(9,'DF','CIUDAD DE MÉXICO'),(10,'DG','DURANGO'),(11,'GT','GUANAJUATO'),(12,'GR','GUERRERO'),
			(13,'HG','HIDALGO'),(14,'JC','JALISCO'),(15,'MC','MÉXICO'),(16,'MN','MICHOACÁN DE OCAMPO'),
			(17,'MS','MORELOS'),(18,'NT','NAYARIT'),(19,'NL','NUEVO LEÓN'),(20,'OC','OAXACA'),
			(21,'PL','PUEBLA'),(22,'QT','QUERÉTARO'),(23,'QR','QUINTANA ROO'),(24,'SP','SAN LUIS POTOSÍ'),
			(25,'SL','SINALOA'),(26,'SR','SONORA'),(27,'TC','TABASCO'),(28,'TS','TAMAULIPAS'),
			(29,'TL','TLAXCALA'),(30,'VZ','VERACRUZ DE IGNACIO DE LA LLAVE'),(31,'YN','YUCATÁN'),(32,'ZS','ZACATECAS')
	While @i<= (select COUNT(*) FROM @Estados)
	BEGIN
	    IF @codigoEntidad = (select code from @Estados where id=@i)
			SET @entidadNacimiento = (select nombre from @Estados where id=@i)
		set @i= @i+1
	END
	RETURN @entidadNacimiento
END

SELECT dbo.obtenerEntidadNacimiento('MACM790720MYNRRR00') Estado;




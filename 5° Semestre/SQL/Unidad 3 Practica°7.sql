Use Veterinaria
/* Practica °7:
	Generar una función escalar que regrese en una cadena
	la tabla de multiplicar del parámetro indica
*/ 
IF OBJECT_ID('MultiplicarEscalar', 'FN') IS NOT NULL
    DROP FUNCTION MultiplicarEscalar;
GO
CREATE FUNCTION MultiplicarEscalar(@numero int)
RETURNS VARCHAR(MAX)
AS
BEGIN
	declare @total varchar(MAX)= ''
	declare @i int=1
	while (@i<=10)
	begin
		SET @total = @total + CAST(@numero AS VARCHAR) + ' x ' + CAST(@i AS VARCHAR) + ' = ' + CAST(@numero*@i AS VARCHAR) + CHAR(13) + CHAR(10)
		set @i=@i+1
	end
	return @total
END

SELECT dbo.MultiplicarEscalar('5') Total

use VETERINARIA
/* Practica �6:
	Crear una funcion escalar que reciba el a�o y el mes
	y regrese la venta de ese a�o y mes
*/ 
IF OBJECT_ID('VentaA�oMes', 'FN') IS NOT NULL
    DROP FUNCTION VentaA�oMes;
GO
CREATE FUNCTION VentaA�oMes(@a�o int,@mes int)
RETURNS decimal(18,2)
AS
BEGIN
	declare @total decimal(18,2)
	set @total = (select VentaTotal from ReporteVentas where mes=@mes and a�o=@a�o)
	return @total
END

SELECT dbo.VentaA�oMes('2022','12') Total;

DECLARE @valor int 
set @valor = 4
if @valor %2 =0
	print 'valor par'
else
	print 'Valor impar'
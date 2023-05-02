use VETERINARIA
/* Practica °6:
	Crear una funcion escalar que reciba el año y el mes
	y regrese la venta de ese año y mes
*/ 
IF OBJECT_ID('VentaAñoMes', 'FN') IS NOT NULL
    DROP FUNCTION VentaAñoMes;
GO
CREATE FUNCTION VentaAñoMes(@año int,@mes int)
RETURNS decimal(18,2)
AS
BEGIN
	declare @total decimal(18,2)
	set @total = (select VentaTotal from ReporteVentas where mes=@mes and año=@año)
	return @total
END

SELECT dbo.VentaAñoMes('2022','12') Total;

DECLARE @valor int 
set @valor = 4
if @valor %2 =0
	print 'valor par'
else
	print 'Valor impar'
use VETERINARIA
/* Practica °8:
	Generar una función tabla que regrese en una cadena
	la tabla de multiplicar del parámetro indica
*/ 
CREATE FUNCTION MultiT(@numero int)
RETURNS TABLE
AS
RETURN (
    SELECT CAST(@numero AS VARCHAR) + ' x ' + CAST(numero AS VARCHAR) + ' = ' + CAST(@numero*numero AS VARCHAR) resultado
    FROM (
        SELECT 1 AS numero UNION ALL
        SELECT 2 AS numero UNION ALL
        SELECT 3 AS numero UNION ALL
        SELECT 4 AS numero UNION ALL
        SELECT 5 AS numero UNION ALL
        SELECT 6 AS numero UNION ALL
        SELECT 7 AS numero UNION ALL
        SELECT 8 AS numero UNION ALL
        SELECT 9 AS numero UNION ALL
        SELECT 10 AS numero
    ) numeros
)
SELECT * from MultiT('5') Total;


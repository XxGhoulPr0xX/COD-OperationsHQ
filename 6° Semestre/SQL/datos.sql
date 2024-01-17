INSERT INTO Ingredientes (ID_Ingredientes,Nombre)
VALUES	(1,'Chocolate'),
		(2,'Plátano'),
		(3,'Fresa'),
		(4,'Glaseado'),
		(5,'Vainilla'),
		(6,'Avena'),
		(7,'Zanahoria'),
		(8,'Limón');
Select * from Ingredientes
INSERT INTO Producto (ID_Producto,Nombre,Precio,Stock,ID_Ingredientes)
Values	(1,'Galletas de chocolate', 2.5, 100, 1),
		(2,'Pan de plátano', 3.0, 80, 2),
		(3,'Paletas de fresa', 1.0, 150, 3),
		(4,'Donas de glaseado', 2.0, 120, 4),
		(5,'Vizcocho de vainilla', 4.0, 90, 5),
		(6,'Galletas de avena', 2.0, 110, 6),
		(7,'Pan de zanahoria', 3.5, 70, 7),
		(8,'Paletas de limón', 1.5, 130, 8),
		(9,'Donas de chocolate', 2.5, 100, 1),
		(10,'Vizcocho de chocolate', 4.5, 80, 1);
Insert Into Tienda( ID_Tienda, Nombre, Teléfono, Dirección)
Values	(1,'Tienda Tulyehualco', '5512762662', 'Oriente 44c Mz 134 Lt 11'),
		(2, 'Tienda XYZ', '5555555555', 'Calle Principal 123'),
		(3, 'Tienda ABC', '5551234567', 'Avenida Central 789'),
		(4, 'Tienda ZYX', '5567890123', 'Calle Secundaria 456'),
		(5, 'Otra Tienda', '5543219876', 'Avenida Norte 101'),
		(6, 'Super Tienda', '5512345678', 'Calle del Centro 222'),
		(7, 'Tienda Rápida', '5577777777', 'Avenida Sur 333'),
		(8, 'Tienda Express', '5511111111', 'Calle Este 444'),
		(9, 'Tienda Online', '5599999999', 'Avenida Oeste 555'),
		(10, 'Tienda de Prueba', '5500000000', 'Calle de Ejemplo 666');

INSERT INTO Categorias (ID_Categoria, Nombre) 
VALUES	(1, 'Postres'),
		(2, 'Bebidas');

INSERT INTO Categorias (ID_Categoria, Nombre) 
VALUES	(3, 'Ensaladas'),
		(4, 'Pasteles'),
		(5, 'Desayunos'),
		(6, 'Aperitivos'),
		(7, 'Platos Principales'),
		(8, 'Bocadillos'),
		(9, 'Sopas'),
		(10, 'Vegetariano'),
		(11, 'Sin Gluten'),
		(12, 'Sin Lactosa');

INSERT INTO Proveedor (ID_Proveedor, Nombre, Dirección, Teléfono) 
VALUES	(1, 'Proveedor1', 'Dirección1', '1234567890'),
		(2, 'Proveedor2', 'Dirección2', '0987654321');

INSERT INTO Proveedor (ID_Proveedor, Nombre, Dirección, Teléfono) 
VALUES	(3, 'Proveedor3', 'Dirección3', '1112233445'),
		(4, 'Proveedor4', 'Dirección4', '5556677889'),
		(5, 'Proveedor5', 'Dirección5', '9876543210'),
		(6, 'Proveedor6', 'Dirección6', '1110009999'),
		(7, 'Proveedor7', 'Dirección7', '7778889999'),
		(8, 'Proveedor8', 'Dirección8', '4443332222'),
		(9, 'Proveedor9', 'Dirección9', '9998887777'),
		(10, 'Proveedor10', 'Dirección10', '6665554444'),
		(11, 'Proveedor11', 'Dirección11', '3332221111'),
		(12, 'Proveedor12', 'Dirección12', '0009998888');

-- ... Otras inserciones ...
Select * from Producto
Select * from Tienda
SELECT * FROM Domicilio_Cliente
select * from Cliente
select * from Pedido
select * from Proveedor
select * from Categorias
select * from Ingredientes
select * from CarritoCompras
select * from DetallesCarrito
select * from RegistroPedido

DELETE FROM Pedido;
DELETE FROM CarritoCompras
Delete from DetallesCarrito
delete from RegistroPedido

CREATE PROCEDURE RealizarPedido
	@p_idPedido int,
    @p_fechaPedido DATETIME,
    @p_idTienda INT,
    @p_idCliente INT,
    @p_idProducto INT,
    @p_cantidadPedido INT
AS
BEGIN
    DECLARE @mensaje NVARCHAR(255)
    BEGIN TRY
        BEGIN TRANSACTION;
        -- Insertar en la tabla de pedidos
        INSERT INTO Pedido (ID_Pedido, Fecha_Pedido, ID_Tienda, ID_Cliente, ID_Producto)
        VALUES (@p_idPedido, @p_fechaPedido, @p_idTienda, @p_idCliente, @p_idProducto);
        -- Restar la cantidad pedida al stock en la tabla de productos
        UPDATE Producto
        SET Stock = Stock - @p_cantidadPedido
        WHERE ID_Producto = @p_idProducto;
        -- Confirmar la transacción
        COMMIT;
        SET @mensaje = 'Transacción realizada con éxito';
        SELECT @mensaje AS Resultado; -- Puedes imprimir o seleccionar el mensaje
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
            ROLLBACK;
        SET @mensaje = 'Error en la transacción';
        SELECT @mensaje AS Resultado;
    END CATCH
END;
DECLARE @p_idPedido int
select @p_idPedido = ISNULL(MAX(ID_Cliente),0) + 1 FROM Pedido
print @p_idPedido
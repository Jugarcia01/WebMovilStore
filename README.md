# WebMovilStore
Aplicación Movil y Web que simula una Tienda de Articulos con: Descripción, Cantidad, Precio y más atributos. La aplicación esta desarrollada empleando el framework Django 2.1 en lenguaje Python 3.7 para el backend y para el frontend se empleó Ionic 4.0, la información es almacenada y administrada en una Base de Datos relacional creada con MySQL Workbench 8.0 por lo anterior es necesario también integrar la libreria de base de datos: mysql-client.
Se emplea plantilla para la vista/interfaz de usuario web mediante Bootstrap 4.4.1 con Responsive Design es necesario integrar esta librería para su correcta visualización y/o poseer buena conexion a internet.

El Modelo Relacional plantea las siguiente tablas:

- Item(PRODUCTO)
id
nombreProd
descripcion
precio
OrderItem(CompraProducto)

- Order(COMPRA)
id
estadoCompra (Exitosa, Pendiente, Fallida)
idCliente
idProducto
idPago
fechaCompra

- User(CLIENTE se usará como pruebas el usuario de acceso a mySql-backend)
id
nombre
identif
direccion
email

- PAGO
id
metodoPago
idMetodoPago
entidadPago

TO DO / Pendiente: integrar con SandBox API para Pay-Out -> Para lo referente a pagos.

Att: Julian Garcia eMail: jugarcia01@hotmail.com

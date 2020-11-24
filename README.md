# WebMovilStore
Aplicación Movil y Web que simula una Tienda de Articulos con: Descripción, Cantidad, Precio y más atributos. La aplicación esta desarrollada empleando el framework Django 2.0 en lenguaje Python 3.7 para el backend y para el frontend se empleó Ionic 4.0

WebStore
Acerca de Aplicación WebStore:

Desarrollo creado con el IDE VisualStudioCode en lenguaje Python3,7 empleando el framework Django 2.1. Base de Datos creada con MySQL, por lo cual es necesario integrar la libreria de base de datos: mysql-client Se emplea bootstrap4.4.1 con Responsive Design para la interfaz de usuario web, por lo cual es necesario integrar esta librería para su correcta visualización o poseer buena conexion a internet.

La BD será Relacional con las siguiente tablas:

Item(PRODUCTO)

id
nombreProd
descripcion
precio
OrderItem(CompraProducto)

Order(COMPRA)

id
estadoCompra (Exitosa, Pendiente, Fallida)
idCliente
idProducto
idPago
fechaCompra
User(CLIENTE se usará como pruebas el usuario de acceso a mySql-backend)

id
nombre
identif
direccion
email
PAGO

id
metodoPago
idMetodoPago
entidadPago
Pendiente: integrar con SandBox API para Pay-Out -> Para lo referente a pagos.

Att: Julian Garcia eMail: jugarcia01@hotmail.com

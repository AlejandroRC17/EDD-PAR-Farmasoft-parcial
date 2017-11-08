# Flujo de programa

El sitio cuenta con una pagina de bienvenida el cual sugiere que inicies sesion para poder utilizar el sistema o en caso de no tener usuario, poder registrarse. Una vez ingresado se accedera a una nueva pagina de bienvenida la cual tendra un menu donde se podra seleccionar las distintas acciones (consultas) a realizar, las mismas tambien estaran disponibles en la barra de navegacion, ademas de un boton para cerrar sesion.
# Estructura 

El programa cuenta con un archivo principal denominado app.py y los modulos classyforms.py, list_csv.py,y vldr_csv.py:
+ classyforms = Modulo en el cual se encuentran los formularios de Logueo, Registro y Busqueda. Ademas la clase csv donde se genera una lista de objetos con los registros del 'listado.csv'.
+ list_csv = Aqui se encuentran las distintas funciones que se usan para satisfacer las consultas pedidas(ultimas ventas, productos mas vendidos, etc...).
+ vldr_csv = Valida y maneja los errores que puede tener la importacion del CSV.
+ app.py =  Archivo principal, en el se importan los mencionados modulos y los trabaja para que pueda renderizarse su funcionamiento en sus respectivos HTML.
Los archivos CSV que se utilizaron fueron, 'users.csv' donde estan los usuarios registrados, y 'listado.csv' en el cual se encuentra los datos de producto, cliente, cantidad, precio, codigo.
# Como usar el programa

Al iniciar tendra una pagina de bienvenida y las opciones de iniciar sesion y registrarse, para registrarse debera rellenar los campos con un usuario y una contraseña la cual tendra que vericarla en otro campo. Una vez creada la cuenta podra iniciar sesion con los datos que se proporcionaron. Ya logueado se redireccionara a una segunda pagina de bienvenida que tendra las siguientes opciones: buscar clientes, buscar producto, mas vendidos, clientes que mas gastaron, y ultimas ventas.
Selecciona la opcion que desea consultar.
+ Buscar clientes = Cuenta con un campo donde se escribe el nombre de cliente que desea ver, el campo debe constar de al menos 3 caracteres para que realize la busqueda. En caso de que se encuentren resultados similares, tendra a disposicion una lista donde podra seleccionar que opcion es la que esta buscando. Una vez seleccionado aparecera una tabla con todos los datos del cliente.
+ Buscar productos = su funcionamiento es similar al de 'buscar cliente', cuenta con el campo donde podra ingresar su busqueda, no menos de 3 caracteres, y saldra la tabla del respectivo producto.
+ Mas vendidos, ultimas ventas, clientes que mas gastaron = Basta con seleccionar la opcion deseada y ya se podra ver las tablas que contienen cada consulta. Solo se mostraran 5 registros en cada tabla. La pagina cuenta con una barra de navegacion donde podra seleccionar todas las opciones sin necesidad de volver a la pagina principal.
Una vez finalizado su consulta podra cerrar sesion con el boton que se encuentra en la barra de navegacion.
# Clases creadas
+ En el archivo classyforms.py se crearon las clases de Ingreso, Registro, BusquedaClientes, BusquedaProductos, el cual importa los formularios que se necesita para poder realizar las operaciones de busqueda, logueo y registro.
Ademas se encuentra la clase Csv, donde se cataloga el archivo 'listado.csv' en una lista llamada listaregistros dependiendo su respectivo campo(codigo, cliente, precio, producto, cantidad).
+ En vldr_csv.py estan las clases donde se valida y se manejan los distintos errores del CSV

Para crear la aplicacion se utilizo las siguientes herramientas:
+ python3
+ Flask
+ Manager (Flask script)
+ Bootstrap

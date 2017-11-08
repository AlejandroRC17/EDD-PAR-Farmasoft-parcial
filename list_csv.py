# ULTIMAS VENTAS
# Devuelve una lista con las ultimas ventas
# La cantidad de registro que devuelve es la
# que se especifica en app.py
def ultimas_ventas(registros, cantidadregistro):
    ultimasventas = []
    ultimosreg = registros.reverse()
    while cantidadregistro > len(registros):
        cantidadregistro = cantidadregistro - 1
    for i in range(cantidadregistro):
        ultimasventas.append(registros[i])
    return ultimasventas

# BUSQUEDA CLIENTE
# Busca en lista registros, un cliente que contenga los caracteres ingresados
# del formulario BusquedaCliente y devuelve una lista con las coincidencias

def buscar_cliente(registros, nombre):
    cliente = []
    for i in range(len(registros)):
        if nombre in registros[i].cliente:
            if registros[i].cliente in cliente:
                pass
            else:
                cliente.append(registros[i].cliente)
        else:
            pass
    return cliente
# Devuelve en una lista todos los productos que compro el cliente
def productos_cliente(registros, cliente):
    nombre_cliente = cliente.upper()
    productos = []
    for i in range(len(registros)):
        if nombre_cliente in registros[i].cliente:
            productos.append(registros[i])
    return productos


# BUSQUEDAPRODUCTO
# Busca en lista registros, un producto con los mismos caracteres ingresados en el
# BusquedaProductos y devuelve las coincidencias en una lista

def buscar_productos(registros, nombre):
    producto = []
    for i in range(len(registros)):
        if nombre in registros[i].producto:
            if registros[i].producto in producto:
                pass
            else:
                producto.append(registros[i].producto)
        else:
            pass
    return producto
# Devuelve en una lista el producto y lo clientes que lo compraron
def lista_producto(registros, producto):
    nombre_producto = producto.upper()
    cliente = []
    for i in range(len(registros)):
        if nombre_producto in registros[i].producto:
            cliente.append(registros[i])
    return cliente

# MAS VENDIDOS
# Lista los productos que mas se vendieron

def masvendidos(registros, cantidad):
    producto = []
    cantidad_produc = []
    colunna = 0
    for i in range(len(registros)):
        if i == 0:
            producto.append(registros[i].producto)
            cantidad_produc.append([])
            cantidad_produc[colunna] = [0, registros[i]]
        else:
            if registros[i].producto in producto:
                pass
            else:
                colunna = colunna + 1
                producto.append(registros[i].producto)
                cantidad_produc.append([])
                cantidad_produc[colunna] = [0, registros[i]]
    for i in range(len(producto)):
        for x in range(len(registros)):
            if producto[i] in registros[x].producto:
                cantidad_produc[i][0] = cantidad_produc[i][0] + registros[x].cantidad
            else:
                pass
# Se ordena de menor a mayor
    cantidad_produc.sort(reverse = True)
    while cantidad > len(producto):
        cantidad = cantidad - 1
    lista_producto = []
    for i in range(cantidad):
        lista_producto.append([0] * 2)
        lista_producto[i][0] = cantidad_produc[i][0]
        lista_producto[i][1] = cantidad_produc[i][1]
    return lista_producto

# CLIENTES QUE MAS GASTARON
# Lista los clientes que mas gastaron y los ordena de mayor a menor
# se multiplica la cantidad y el precio para obtener el total que gastaron

def clientes_regulares(registros, cantidad):
    clientes = []
    cantidadclientes = []
    colunna = 0
    for i in range(len(registros)):
        if i == 0:
            clientes.append(registros[i].cliente)
            cantidadclientes.append([])
            cantidadclientes[colunna] = [0, registros[i]]
        else:
            if registros[i].cliente in clientes:
                pass
            else:
                clientes.append(registros[i].cliente)
                colunna = colunna + 1
                cantidadclientes.append([])
                cantidadclientes[colunna] = [0, registros[i]]
    for i in range(len(clientes)):
        for x in range(len(registros)):
            if clientes[i] in registros[x].cliente:
                cantidadclientes[i][0] = cantidadclientes[i][0] + (registros[x].cantidad * registros[x].precio)
            else:
                pass
    cantidadclientes.sort(reverse = True)
    while cantidad > len(clientes):
        cantidad = cantidad - 1
    lista_clientes = []
    for i in range(cantidad):
        lista_clientes.append([0] * 2)
        lista_clientes[i][0] = cantidadclientes[i][0]
        lista_clientes[i][1] = cantidadclientes[i][1]
    return lista_clientes

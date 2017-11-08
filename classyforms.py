import csv
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required


class Ingreso(FlaskForm):
	username = StringField('Nombre de usuario', validators = [Required()])
	password = PasswordField('Contraseña', validators = [Required()])
	enviar = SubmitField('Ingresar')


class Registro(Ingreso):
	re_password = PasswordField('Verificar Contraseña', validators = [Required()])
	enviar = SubmitField('Registrarse')

class BusquedaCliente(FlaskForm):
	campocliente = StringField('Ingrese un cliente', validators = [Required()])
	buscar = SubmitField('Buscar')

class BusquedaProducto(FlaskForm):
	campoproducto = StringField('Ingrese producto', validators = [Required()])
	buscar = SubmitField('Buscar')

class Csv:
    def __init__ (self, codigo, cliente, producto, cantidad, precio):
        self.codigo = codigo
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio
    def __str__ (self):
        return '{}, {}, {}, {}, {}'.format(self.codigo, self.cliente, self.producto, self.cantidad, self.precio)
    def __gt__ (self, otro):
        return self.cantidad > otro.cantidad
    def compra (self):
        return self.cantidad * self.precio

def catcsv(archivocsv):
    listaregistros = []
    with open(archivocsv) as archivo:
        archivo_csv = csv.reader(archivo)
        x = 0
        for linea in archivo_csv:
            if x == 0:
                y = 0
                for y in range(5):
                    campo = linea[y]
                    if campo == 'CODIGO':
                        campo_codigo = y
                    elif campo == 'CLIENTE':
                        campo_cliente = y
                    elif campo == 'PRODUCTO':
                        campo_producto = y
                    elif campo == 'CANTIDAD':
                        campo_cantidad = y
                    else:
                        campo_precio = y
                    y = y + 1
                x = x + 1
            else:
                listaregistros.append(Csv(codigo = linea[campo_codigo], cliente = linea[campo_cliente].upper(), producto = linea[campo_producto].upper(), cantidad = float(linea[campo_cantidad]), precio = float(linea[campo_precio])))
    return (listaregistros)
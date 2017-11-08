#!/usr/bin/env python
from flask import Flask, render_template, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap
from flask_script import Manager
from classyforms import Ingreso, Registro, BusquedaCliente, BusquedaProducto
import csv
import vldr_csv
import classyforms
import list_csv

app = Flask(__name__)
bootstrap = Bootstrap(app)
manager = Manager(app)

app.config['SECRET_KEY'] = 'un string que funcione como llave'

# PAGINA INICIAL

@app.route("/")
def index():
	return render_template("index.html")

# LOGIN, REGISTRO Y LOGOUT

@app.route("/login", methods = ["GET", "POST"])
def login():
	form = Ingreso()
	if form.validate_on_submit():
		with open('users') as archivo:
			archivo_csv = csv.reader(archivo)
			registro = next(archivo_csv)
			while registro:
				if form.username.data == registro[0] and form.password.data == registro[1]:
					flash("Sesion iniciada como " + form.username.data)
					session['username'] = form.username.data
					return render_template('home.html')
				registro = next(archivo_csv, None)
			else:
				flash("Usuario o contraseña incorrectos")
				return redirect(url_for('login'))
	return render_template('ingresar.html', form = form)

@app.route("/register", methods = ['GET', 'POST'])
def registrarse():
	form = Registro()
	if form.validate_on_submit():
		if form.password.data == form.re_password.data:
			with open ('users', 'a+') as archivo:
				archivo_csv = csv.writer(archivo)
				registro = [form.username.data, form.password.data]
				archivo_csv.writerow(registro)
			flash('Usuario creado correctamente')
			return redirect(url_for('login'))
		else:
			flash('Las contraseñas deben ser iguales')
	return render_template('registro.html', formrg=form)


@app.route("/logout", methods = ['GET'])
def logout():
	if 'username' in session:
		session.pop('username')
		return render_template("index.html")
	else:
		flash('Salio correctamente')
		return redirect(url_for('index'))

# PAGINA INICIAL LOGUEADO

@app.route("/home", methods = ['GET','POST'])
def home():
	if 'username' in session:
		return render_template("home.html")
	else:
		flash('Primero inicia sesion')
		return redirect(url_for('login'))

# PAGINAS CONSULTAS(ULTIMAS VENTAS, BUSQUEDAS CLIENTES PRODUCTOS, MAS VENDIDOS, CLIENTES QUE MAS GASTARON) 

abrir_archivo = 'listado.csv'
vldr_csv.validarcampos(abrir_archivo)
registros = classyforms.catcsv(abrir_archivo)


@app.route("/ultventas", methods = ['GET', 'POST'])
def show():
	if 'username' in session:
		cantidadregistros = 5
		listaventas = []
		listaventas = list_csv.ultimas_ventas(registros, cantidadregistros)
		return render_template('ultimasventas.html', listarventas = listaventas)
	else:
		flash('Primero inicia sesion')
		return redirect(url_for('login'))

@app.route("/busquedaclientes", methods = ['GET', 'POST'])
def busquedaclientes():
	if 'username' in session:
		formcliente = BusquedaCliente()
		if formcliente.validate_on_submit():
			cliente = formcliente.campocliente.data.upper()
			if len(cliente) < 3:
				flash('La busqueda debe tener al menos 3 caracteres')
				return render_template('busquedaclientes.html', form = formcliente)
			else:
				buscarclientes = list_csv.buscar_cliente(registros, cliente)
				if len(buscarclientes) == 0:
					flash('No hay resultados')
				elif len(buscarclientes) == 1:
					listar = list_csv.productos_cliente(registros, cliente)
					return render_template('busquedaclientes.html', form = formcliente, listar = listar, cliente = formcliente.campocliente.data.upper())
				else:
					return render_template('busquedaclientes.html', form = formcliente, clientes = buscarclientes)
		return render_template('busquedaclientes.html', form = formcliente)
	else:
		flash('Primero inicia sesion')
		return redirect(url_for('login'))

@app.route("/busquedaclientes/<clientes>", methods = ['GET', 'POST'])
def busquedaclientes1(clientes):
	if 'username' in session:
		formcliente = BusquedaCliente()
		if formcliente.validate_on_submit():
			cliente = formcliente.campocliente.data.upper()
			if len(cliente) < 3:
				flash('La busqueda debe al menos 3 caracteres')
				return render_template('busquedaclientes.html', form = formcliente)
			else:
				buscarclientes = list_csv.buscar_cliente(registros, cliente)
				if len(buscarclientes) == 0:
					flash('No hay resultados')
					return redirect(url_for(busquedaclientes))
				elif len(buscarclientes) == 1:
					listar = list_csv.productos_cliente(registros, cliente)
					return render_template('busquedaclientes.html', form = formcliente, listar = listar, cliente = formcliente.campocliente.data.upper())
				else:
					return render_template('busquedaclientes.html', form = formcliente, clientes = buscarclientes)
		else:
			cliente = clientes
			clientenc = list_csv.buscar_cliente(registros, cliente)
			listar = list_csv.productos_cliente(registros, cliente)
			return render_template('busquedaclientes.html', form = formcliente, listar = listar, cliente = clientenc)
	else:
		flash('Primero inicia sesion')
		return redirect(url_for('login'))

@app.route("/busquedaproductos", methods = ['GET', 'POST'])
def buscarproductos():
	if 'username' in session:
		formproducto = BusquedaProducto()
		if formproducto.validate_on_submit():
			producto = formproducto.campoproducto.data.upper()
			if len(producto) < 3:
				flash('La busqueda debe tener al menos 3 caracteres')
				return render_template('busquedaproducto.html', form = formproducto)
			else:
				res_pr = list_csv.buscar_productos(registros, producto)
				if len(res_pr) == 0:
					flash('No se encontraron productos')
				elif len(res_pr) == 1:
					listar = list_csv.lista_producto(registros, producto)
					return render_template('busquedaproducto.html', form = formproducto, listar = listar, producto= formproducto.campoproducto.data.upper())
		return render_template('busquedaproducto.html', form = formproducto)
	else:
		flash ('Primero inicia sesion')
		return redirect(url_for('login'))


@app.route("/masvendidos", methods = ['GET', 'POST'])
def masvendidos():
	if 'username' in session:
		productos = [] 
		cantidad = 5
		productos = list_csv.masvendidos(registros = registros, cantidad = cantidad)
		return render_template('masvendidos.html', masvendidos = productos)
	else:
		flash('Primero inicia sesion')
		return redirect(url_for('login'))

@app.route("/clientesregulares", methods = ['GET', 'POST'])
def clientesregulares():
	if 'username' in session:
		clientes = []
		cantidad = 5
		clientes = list_csv.clientes_regulares(registros = registros, cantidad = cantidad)
		return render_template('clientesregulares.html', listarclientes = clientes)
	else:
		flash('Primero inicia sesion')
		return redirect(url_for('login'))

# ERRORES

@app.errorhandler(404)
def no_encontrado(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_interno(e):
    return render_template('500.html'), 500



if __name__ == "__main__":
	manager.run()


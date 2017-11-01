#!/usr/bin/env python
import csv
from flask import Flask, render_template, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap
from clases import Ingreso, Registro

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'noerror'

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
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
					return render_template("ultimasventas.html")
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

@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/logout")
def logout():
	return render_template("logout.html")

@app.route("/ult_ventas")
def show():
	return render_template("ultimasventas.html")

if __name__ == "__main__":
	app.run(debug=True)
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required


class Ingreso(FlaskForm):
    username = StringField('Nombre de usuario', validators=[Required()])
    password = PasswordField('Contraseña', validators=[Required()])
    enviar = SubmitField('Ingresar')


class Registro(Ingreso):
    re_password = PasswordField('Verificar Contraseña', validators=[Required()])
    enviar = SubmitField('Registrarse')
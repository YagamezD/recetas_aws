from flask_app.config.mysqlconnection import connectToMySQL

import re #Importamos expresiones regulares
#crear una expresión regular para verificar que tengamos el email con formato correcto
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask import jsonify #mandar mensajes a la plantilla

class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO users(first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        result = connectToMySQL('recetas').query_db(query, formulario) #1 - Insert recibe id
        return result #result = Identificador del nuevo registro

    @staticmethod
    def valida_usuario(formulario):
        #formulario = {
        #    first_name:    "Elena",
        #    last_name:     "De Troya",
        #    email:         "elena@codingdojo.com",
        #    password:      "password123",
        #confirm_password:      "password123",
        #}
        mensaje = ""
        es_valido = True
        
        #Validar que mi nombre tenga más de 2 caracteres
        if len(formulario['first_name']) < 3:
            mensaje+='Nombre debe de tener al menos 3 caracteres'
            es_valido = False
        
        if len(formulario['last_name']) < 3:
            mensaje+='Apellido debe de tener al menos 3 caracteres'
            es_valido = False
        
        #Valido email con expresiones regulares
        if not EMAIL_REGEX.match(formulario['email']): 
            mensaje+='E-mail invalido'
            es_valido = False

        if len(formulario['password']) < 6:
            mensaje+='Contraseña debe de tener al menos 6 caracteres'
            es_valido = False
        
        if formulario['password'] != formulario['confirm_password']:
            mensaje+='Contraseñas no coinciden'
            es_valido = False
        
        #Consultar si YA existe el correo
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('recetas').query_db(query, formulario)
        if len(results) >= 1:
            mensaje+='E-mail registrado previamente'
            es_valido = False

        return es_valido

    @classmethod
    def get_by_email(cls, formulario):
        #formulario = {
        #   "email": "elena@cd.com"
        #   "password": "1234"
        #}
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL('recetas').query_db(query, formulario)
        if len(result) < 1:
            return False
        else:
            #result = [ {first_name: Elena, last_name: De Troya.....} ]
            user = cls(result[0]) #Haciendo una instancia de User -> CON los datos que recibimos de la base de datos
            return user

    @classmethod
    def get_by_id(cls, formulario):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('recetas').query_db(query, formulario) #Select recibe lista
        user = cls(result[0])
        return user

    

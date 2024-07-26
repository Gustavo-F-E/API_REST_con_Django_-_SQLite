# api_veoveo/models.py
from django.db import models

class Consulta(models.Model):
    nombre_y_apellido = models.CharField(max_length=100)
    tipo_consulta = models.CharField(max_length=100)
    URL_captura_problema = models.TextField()
    descripcion_problema = models.TextField()

    def __str__(self):
        return self.nombre_y_apellido

class Pelicula(models.Model):
    ruta_img_peliculas = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    link = models.TextField()
    categoria = models.CharField(max_length=100)
    apto_menores = models.CharField(max_length=10)

    def __str__(self):
        return self.titulo

class Serie(models.Model):
    ruta_img_series = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    link = models.TextField()
    categoria = models.CharField(max_length=100)
    apto_menores = models.CharField(max_length=10)

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    apto_menores = models.CharField(max_length=10)

    def __str__(self):
        return self.username


# Guía para crear esta API REST con Django:
Esta es la guía para crear una API REST en Django basado en una base de datos SQLite (configurada por defecto en Django).
## Crear entorno virtual para la API:
```
py -m venv venv_django_rest_framework
source venv_django_rest_framework/Scripts/activate
```
## Crear proyecto Django:
```
django-admin startproject veoveo
cd veoveo
```
## Verificar que el servidor esté corriendo:
```
py manage.py runserver
```
## Crear superusuario:
```
py manage.py createsuperuser
Username (leave blank to use 'gustavo'): 
Email address: eichhorn.gustavof@gmail.com
Password: 
Password (again):
Superuser created successfully.
```
## Crear 'requirements.txt':
```
touch requirements.txt
pip install -r requirements.txt 
py -m pip freeze > requirements.txt
```
## Instalar algunas dependencias para hacer una API REST con Django:
```
pip install djangorestframework
pip install markdown
pip install django-filter
pip freeze > requirements.txt
```
## Crear APP de nuestra API:
```
py manage.py startapp api_veoveo
```
## Configurar los diferentes archivos:
- veoveo/settings.py
 ``` python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'veoveo',
    'api_veoveo',
]
```
- veoveo/urls.py
 ``` python
# veoveo/urls.py
from django.contrib import admin
from django.urls import include, path
from api_veoveo.views import root_view  # Asegúrate de importar la vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_veoveo.urls')),
    path('', root_view),  # Redirige la raíz a la API
]
```
- api_veoveo/urls.py
 ``` python
# api_veoveo/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConsultaViewSet, PeliculaViewSet, SerieViewSet, UsuarioViewSet

router = DefaultRouter()
router.register(r'consultas', ConsultaViewSet)
router.register(r'peliculas', PeliculaViewSet)
router.register(r'series', SerieViewSet)
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```
- api_veoveo/views.py
 ``` python
# api_veoveo/views.py
from rest_framework import viewsets
from .models import Consulta, Pelicula, Serie, Usuario
from .serializers import ConsultaSerializer, PeliculaSerializer, SerieSerializer, UsuarioSerializer
from django.shortcuts import redirect

def root_view(request):
    return redirect('/api/')

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer

class SerieViewSet(viewsets.ModelViewSet):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
```
- api_veoveo/models.py
 ``` python
# api_veoveo/models.py
from django.db import models

class Consulta(models.Model):
    nombre_y_apellido = models.CharField(max_length=100)
    tipo_consulta = models.CharField(max_length=100)
    URL_captura_problema = models.URLField()
    descripcion_problema = models.TextField()

    def __str__(self):
        return self.nombre_y_apellido

class Pelicula(models.Model):
    ruta_img_peliculas = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    link = models.URLField()
    categoria = models.CharField(max_length=100)
    apto_menores = models.CharField(max_length=10)

    def __str__(self):
        return self.titulo

class Serie(models.Model):
    ruta_img_series = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    link = models.URLField()
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
```
- api_veoveo/serializers.py
 ``` python
# api_veoveo/serializers.py
from rest_framework import serializers
from .models import Consulta, Pelicula, Serie, Usuario

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = '__all__'

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
```
## Comandos para migrar datos a la base de datos:
```
py manage.py makemigrations
py manage.py migrate
```

## Cargar datos a partir de un json:
A la misma altura que 'manage.py' colocamos diferentes archivos JSON con la data que queremos inyectar a nuestra base de datos SQLite y además creamos un archivo llamado 'load_data.py':
``` python
import json
import os
import django
from django.core.exceptions import ValidationError

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'veoveo.settings')
django.setup()

from api_veoveo.models import Consulta, Pelicula, Serie, Usuario

# Función para cargar datos desde un archivo JSON
def load_data_from_json(file_path, model_class):
    try:
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
        for record in data:
            try:
                model_class.objects.create(**record)
            except ValidationError as e:
                print(f"Error loading {model_class.__name__}: {e}")
    except FileNotFoundError as e:
        print(f"File {file_path} not found: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {file_path}: {e}")

# Cargar datos en las tablas
load_data_from_json('consultas.json', Consulta)
load_data_from_json('peliculas.json', Pelicula)
load_data_from_json('series.json', Serie)
load_data_from_json('usuarios.json', Usuario)

print("Data loaded successfully")
```
Luego ejecutamos el siguiente comando y se carga nuestra base de datos:
```
python load_data.py
```
## Ejecutar servidor de la API REST con Django:
```
py manage.py runserver
```
## Verificar el funcionamiento de la api con 'POSTMAN' o similar:
Ejemplo realizado en los archivos .rest de vscode:
``` js
GET http://127.0.0.1:8000/consultas
###
GET http://127.0.0.1:8000/consultas/9/
###
POST http://127.0.0.1:8000/consultas/
Content-Type: application/json

{
    "nombre_y_apellido": "Sory not sory",
    "tipo_consulta": "Nada",
    "URL_captura_problema": "http://127.0.0.1:8000/consultas",
    "descripcion_problema": "###"
}
###

PUT http://127.0.0.1:8000/consultas/9/
Content-Type: application/json

{
    "nombre_y_apellido": "Sory not sory",
    "tipo_consulta": "Técnica",
    "URL_captura_problema": "URL66",
    "descripcion_problema": "Esto es Postman"
}
###

PATCH http://127.0.0.1:8000/consultas/9/
Content-Type: application/json

{
    "descripcion_problema": "Se me apagó la matrix"
}
###
DELETE http://127.0.0.1:8000/consultas/9/
```
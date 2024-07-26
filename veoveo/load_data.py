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
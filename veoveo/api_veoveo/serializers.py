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
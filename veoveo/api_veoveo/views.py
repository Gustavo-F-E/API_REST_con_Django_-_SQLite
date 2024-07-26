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


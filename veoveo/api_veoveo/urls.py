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

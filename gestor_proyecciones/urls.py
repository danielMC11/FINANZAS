from django.urls import path
from . import views

urlpatterns = [
    path('crear/proyeccion/', views.CrearProyeccion.as_view(), name='crear_proyeccion')
]
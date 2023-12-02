from django.urls import path
from . import views

urlpatterns = [
    path('crear/proyeccion/<str:u_id>/', views.CrearProyeccion.as_view(), name='crear_proyeccion')
]
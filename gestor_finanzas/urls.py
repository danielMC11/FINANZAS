from django.urls import path
from . import views

urlpatterns = [
	path('crear/cartera', views.CrearCartera.as_view(), name='crear_cartera'),
]
 
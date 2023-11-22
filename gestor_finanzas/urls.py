from django.urls import path
from . import views

urlpatterns = [
	path('crear/cartera', views.CrearCartera.as_view(), name='crear_cartera'),
    path('registrar/ingreso', views.RegistrarOperacionIngreso.as_view(), name='registrar_ingreso'),
    path('registrar/gasto', views.RegistrarOperacionGasto.as_view(), name='registrar_gasto'),
    path('visualizar/extractos', views.VisualizarExtractos.as_view(), name='visualizar_extractos'),

]
 
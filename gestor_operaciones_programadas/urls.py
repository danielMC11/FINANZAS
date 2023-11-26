from django.urls import path
from . import views

urlpatterns = [
    path('registrar/ingreso', views.RegistrarOperacionProgramadaIngreso.as_view(), name='registrar_ingreso_programado'),
    path('registrar/gasto', views.RegistrarOperacionProgramadaGasto.as_view(), name='registrar_gasto_programado'),
    path('visualizar/habilitadas', views.VisualizarOperacionesHabilitadas.as_view(), name='visualizar_operaciones_habilitadas'),

]
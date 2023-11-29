from django.urls import path
from . import views

urlpatterns = [
    path('registrar/ingreso/<str:u_id>/', views.RegistrarOperacionProgramadaIngreso.as_view(), name='registrar_ingreso_programado'),
    path('registrar/gasto/<str:u_id>/', views.RegistrarOperacionProgramadaGasto.as_view(), name='registrar_gasto_programado'),
    path('visualizar/habilitadas/<str:u_id>/', views.VisualizarOperacionesHabilitadas.as_view(), name='visualizar_operaciones_habilitadas'),
    path('confirmar/<str:op_id>/<str:u_id>/', views.ConfirmarOperacionProgramada.as_view(), name='confirmar_operacion_programada'),
    path('visualizar/listado/<str:u_id>/', views.VisualizarOperacionesProgramadas.as_view(), name='visualizar_operaciones_programdas'),
]
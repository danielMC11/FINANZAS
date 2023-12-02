from django.urls import path
from . import views

urlpatterns = [
    path('visualizar/categorias/ingreso', views.VisualizarCategoriasIngreso.as_view(), name='visualizar_categorias_ingreso'),
    path('visualizar/subcategorias/ingreso', views.VisualizarSubcategoriasIngreso.as_view(), name='visualizar_subcategorias_ingreso'),
    path('visualizar/categorias/gasto', views.VisualizarCategoriasGasto.as_view(), name='visualizar_categorias_gasto'),
    path('visualizar/subcategorias/gasto', views.VisualizarSubcategoriasGasto.as_view(), name='visualizar_subcategorias_gasto'),
    path('registrar/ingreso/', views.RegistrarOperacionIngreso.as_view(), name='registrar_ingreso'),
    path('registrar/gasto/', views.RegistrarOperacionGasto.as_view(), name='registrar_gasto'),
    path('visualizar/extractos/', views.VisualizarExtractos.as_view(), name='visualizar_extractos'),
    path('visualizar/extracto/ingreso/<str:o_id>/', views.VisualizarExtractoDetalleIngreso.as_view(), name='visualizar_extracto_ingreso'),
    path('visualizar/extracto/gasto/<str:o_id>/', views.VisualizarExtractoDetalleGasto.as_view(), name='visualizar_extracto_gasto'),
]
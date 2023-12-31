
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usr/', include('usuarios.urls')),
    path('cartera/', include('gestor_cartera.urls')),
    path('operaciones/', include('gestor_operaciones.urls')),
    path('operaciones/programadas/', include('gestor_operaciones_programadas.urls')),
    path('proyecciones/', include('gestor_proyecciones.urls'))
]

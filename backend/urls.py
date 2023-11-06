
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('usr/', include('usuarios.urls')),
    path('finanzas/', include('gestor_finanzas.urls'))
]

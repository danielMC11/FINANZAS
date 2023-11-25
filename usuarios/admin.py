from django.contrib import admin
from .models import Usuario


@admin.register(Usuario)
class AdminUsuario(admin.ModelAdmin):
    fields = ['email', 'nombres', 'apellidos', "password"]

    def save_model(self, request, obj, form, change):
        password_text = form.cleaned_data.get('password')  
        obj.set_password(password_text)
        super().save_model(request, obj, form, change)
        
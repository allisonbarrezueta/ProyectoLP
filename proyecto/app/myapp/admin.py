from django.contrib import admin

from .models import animal, direccion, usuario

admin.site.register(animal)
admin.site.register(direccion)
admin.site.register(usuario)

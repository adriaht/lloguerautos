from django.contrib import admin
from lloguer.models import Automobil,Reserva



# Register your models here.





class AutomobilAdmin(admin.ModelAdmin):
    list_display = ( 'matricula','marca', 'model')  # Campos visibles en la lista
    search_fields = ('marca', 'model', 'matricula')  # Campos de búsqueda


class ReservaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'automobil', 'fecha_inicio', 'fecha_fin', 'creado_en')
    search_fields = ('usuario__username', 'automobil__marca', 'automobil__model', 'automobil__matricula')
    list_filter = ('fecha_inicio', 'fecha_fin', 'automobil')

admin.site.register(Automobil, AutomobilAdmin)
admin.site.register(Reserva, ReservaAdmin)
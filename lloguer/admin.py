from django.contrib import admin
from lloguer.models import Automobil



# Register your models here.





class AutomobilAdmin(admin.ModelAdmin):
    list_display = ( 'matricula','marca', 'model')  # Campos visibles en la lista
    search_fields = ('marca', 'model', 'matricula')  # Campos de búsqueda


admin.site.register(Automobil, AutomobilAdmin) 
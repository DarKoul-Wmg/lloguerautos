from django.contrib import admin
from lloguer.models import *

# Register your models here.

from django.contrib import admin
from lloguer.models import Automobil

class AutomobilAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'marca', 'model')  
    search_fields = ('matricula', 'marca', 'model')

admin.site.register(Automobil, AutomobilAdmin)

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('user', 'automobil', 'data_inicio', 'data_fi')
    search_fields = ('user__username', 'automobil__matricula')
    list_filter = ('data_inicio', 'data_fi')

admin.site.register(Reserva, ReservaAdmin)
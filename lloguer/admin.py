from django.contrib import admin
from lloguer.models import *

# Register your models here.

from django.contrib import admin
from lloguer.models import Automobil

class AutomobilAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'marca', 'model')  
    search_fields = ('matricula', 'marca', 'model')

admin.site.register(Automobil, AutomobilAdmin)
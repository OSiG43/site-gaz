from django.contrib import admin

# Register your models here.
from .models import Data


class DataAdmin(admin.ModelAdmin):
    list_display = ('date', 'value')
    list_filter = ['date']
    search_fields = ['date']

admin.site.register(Data, DataAdmin)


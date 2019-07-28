from django.contrib import admin
from .models import Input

class InputAdmin(admin.ModelAdmin):
    list_display = ['pk','gender','age','category']

admin.site.register(Input, InputAdmin)
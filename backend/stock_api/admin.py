from django.contrib import admin
from .models import Animal

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'owner')  # Specify the fields you want to display

admin.site.register(Animal, AnimalAdmin)

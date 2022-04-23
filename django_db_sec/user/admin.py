from django.contrib import admin
from .models import person

# Register your models here.
@admin.register(person)
class personAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

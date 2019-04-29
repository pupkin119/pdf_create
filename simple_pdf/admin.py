from django.contrib import admin


from django import forms
from django.contrib import admin
from .models import Sertificates

@admin.register(Sertificates)
class FacesAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment',)

from django.urls import path
from . import views

app_name = 'simple_pdf'

urlpatterns = [
    path('', views.start, name = 'start'),
]
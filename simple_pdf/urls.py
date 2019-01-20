from django.urls import path
from . import views

app_name = 'simple_pdf'

urlpatterns = [
    path('', views.start, name = 'start'),
    path('generate_pdf/', views.generate_pdf, name = 'generate_pdf'),
]
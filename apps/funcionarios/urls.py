from django.urls import path
from .views import home

urlpatterns = [
    path('', home),
    path('funcionarios', home, name='list_funcionarios'),
]
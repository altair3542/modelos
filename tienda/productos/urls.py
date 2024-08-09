from django.urls import path
from .views import listar_clientes, listar_productos

urlpatterns = [
    path('productos/', listar_productos, name='listar_productos'),
    path('clientes/', listar_clientes, name='listar_clientes'),
]

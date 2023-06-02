from django.urls import path
from apps.usuarios.views import login, cadastro, logout
from apps.calendario.views import index, calendario, cadastro_eventos


urlpatterns = [
    path('', index, name='index'),
    path('calendario/<int:dia>', calendario, name='calendario'),
    path('cadastro_eventos', cadastro_eventos, name='cadastro_eventos'),
]
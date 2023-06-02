from django.urls import path
from apps.usuarios.views import login, cadastro, logout, perfil, editar_perfil, apagar_conta


urlpatterns = [
    path('login', login, name='login'),
    path('cadastro',cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
    path('perfil', perfil, name='perfil'),
    path('editar_perfil', editar_perfil, name='editar_perfil'),
    path('apagar_conta', apagar_conta, name='apagar_conta')
]
from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    OPCOES_PERIODO = [
        ("Primeiro","1º"),
        ("Segundo","2º"),
        ("Terceiro","3º"),
        ("Quarto","4º"),
        ("Quinto","5º"),
        ("Sexto","6º"),
        ("Sétimo","7º"),
        ("Oitavo","8º")
    ]
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    periodo = models.CharField(max_length=100, choices=OPCOES_PERIODO, default='')
    curso = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=128)
    is_moderator = models.BooleanField(default=False)
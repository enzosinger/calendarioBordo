from datetime import datetime
from django.db import models

class Calendario(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null = False, blank=False)
    disciplina = models.TextField(null = True, blank=False)
    publicada = models.BooleanField(default=False)
    data = models.DateTimeField(default = datetime.now, blank=False)
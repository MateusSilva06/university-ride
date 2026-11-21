from django.db import models
from django.contrib.auth.models import User

class Carona(models.Model):
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    data = models.DateField()
    horario_saida = models.TimeField()
    vagas_disponiveis = models.IntegerField()
    ponto_encontro = models.CharField(max_length=200, default='A combinar') # Nova linha aqui
    passageiros = models.ManyToManyField(User, blank=True, related_name='caronas_reservadas')

    def __str__(self):
        return f"{self.origem} para {self.destino} ({self.data} às {self.horario_saida})"
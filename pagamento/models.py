from django.db import models
from django.contrib.auth.models import User
from busca_match.models import Carona


class Pagamento(models.Model):
    METODO_CHOICES = [
        ('PIX', 'Pix'),
        ('CARTAO', 'Cartão de Crédito'),
        ('DINHEIRO', 'Dinheiro na Hora'),
    ]

    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('PAGO', 'Pago'),
    ]

    carona = models.ForeignKey(Carona, on_delete=models.CASCADE, related_name='pagamentos')
    passageiro = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    nome_pagador = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=6, decimal_places=2, default=15.00)
    metodo = models.CharField(max_length=20, choices=METODO_CHOICES, default='PIX')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PAGO')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pagamento #{self.id} - {self.nome_pagador} ({self.get_status_display()})"
from django.db import models

from .cor import Cor
from .modelo import Modelo


class Veiculo(models.Model):
    nome = models.CharField(max_length=100)
    cor = models.ForeignKey(Cor, on_delete=models.RESTRICT, related_name="Veiculo", blank=True, null=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.RESTRICT, related_name="Veiculo", blank=True, null=True)

    def __str__(self):
        return f"Nome: {self.nome} | Cor: {self.cor} | Modelo: {self.modelo}"

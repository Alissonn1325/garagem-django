from django.db import models

from .categoria import Categoria
from .marca import Marca


class Modelo(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="Modelo", blank=True, null=True)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="Modelo", blank=True, null=True)

    def __str__(self):
        return f"Nome: {self.nome} | ID: {self.id} | Categoria: {self.categoria} | Marca: {self.marca} |"

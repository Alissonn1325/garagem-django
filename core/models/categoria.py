from django.db import models


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f" Categoria: {self.descricao} | ID: {self.id}"

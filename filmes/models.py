from django.db import models


class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    ano = models.IntegerField()
    sinopse = models.TextField()

    def __str__(self):
        return f"{self.titulo} ({self.ano})"

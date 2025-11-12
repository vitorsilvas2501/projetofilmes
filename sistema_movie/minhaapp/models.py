from django.db import models

# Create your models here.

class Filme(models.Model):
    titulo = models.CharField(
        max_length=100,
        help_text="Digite o titulo do filme")
    comentario = models.TextField(
        max_length=1000,
        help_text="Digite um comentario")
    nota = models.IntegerField()
    imagem_url = models.URLField(
        blank=True)




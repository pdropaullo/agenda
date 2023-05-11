from distutils.command.upload import upload
from pyexpat import model
from django.db import models


class Contatos(models.Model):
    nome = models.CharField(max_length=255)
    imagem = models.ImageField()
    cpf = models.CharField(max_length=14)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    altura = models.DecimalField(max_digits=3, decimal_places=2)
    descricao = models.TextField()
    data_nascimento = models.DateField()
    ativo = models.BooleanField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Contatos'

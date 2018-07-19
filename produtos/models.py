from django.db import models

# Create your models here.
class Produtos(models.Model):
    nome_produto = models.CharField(max_length=30)
    quantidade = models.IntegerField()
    preço = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome_produto
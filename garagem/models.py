from django.db import models

# Create your models here.

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.nacionalidade}"
    
    class Meta:
        verbose_name_plural = "Marcas"
    
class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
from django.db import models
from .marca import Marca
from .cor import Cor
from .categoria import Categoria
from .modelos import Modelos



class Veiculo(models.Model):
    modelo = models.ForeignKey(Modelos, on_delete=models.PROTECT, related_name="Veiculo")
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="Veiculo")
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="Veiculo"
    )
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="Veiculo")
    ano = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)

    def __str__(self):
        return f"{self.marca} {self.categoria} {self.ano} {self.cor}"

    class Meta:
        verbose_name = "Veículo"
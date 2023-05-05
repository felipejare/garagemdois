from django.contrib import admin

from garagem.models import Acessorio, Categoria, Cor, Marca, Modelo, Veiculo

# Register your models here.


admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Veiculo)
admin.site.register(Cor)
admin.site.register(Acessorio)
admin.site.register(Modelo)

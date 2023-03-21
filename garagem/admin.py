from django.contrib import admin

# Register your models here.

from garagem.models import Marca, Categoria, Veiculo, Cor, Acessorio

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Veiculo)
admin.site.register(Cor)
admin.site.register(Acessorio)
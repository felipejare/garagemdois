from rest_framework.serializers import ModelSerializer

from garagem.serializers import ModeloSerializer

from garagem.models import Veiculo

class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"


class VeiculoDetailSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"
        depth = 1


class VeiculoListSerializer(ModeloSerializer):
    class Meta:
        model = Veiculo
        fields = ["id", "cor", "preco"]

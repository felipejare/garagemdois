from rest_framework.serializers import ModelSerializer

from garagem.models import Modelos


class ModelosSerializer(ModelSerializer):
    class Meta:
        model = Modelos
        fields = "__all__"
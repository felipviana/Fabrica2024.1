from rest_framework.serializers import ModelSerializer
from ..models import BancoDeDados

class Serializer(ModelSerializer):
    class Meta: 
        model = BancoDeDados
        fields = ['id','nome','cep','bairro','logradouro','complemento','uf']
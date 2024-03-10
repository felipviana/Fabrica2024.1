from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from ..models import BancoDeDados
from .serializers import Serializer
import requests

class AppViewSet(ModelViewSet):
    queryset=BancoDeDados.objects.all()
    serializer_class = Serializer

    def create(self, request):
        cep= request.data.get('cep','0000000')
        site = f'https://viacep.com.br/ws/{cep}/json/'
        requisicao= requests.get(site)
        json = requisicao.json()

        cep = json.get('cep','')
        logradouro = json.get('logradouro','')
        complemento = json.get('complemento','')
        bairro =json.get('bairro','')
        localidade = json.get('localidade','')
        uf = json.get('uf','')


        dadosRecebidos={
            "cep":f'{cep}',
            "logradouro":f'{logradouro}',
            "complemento":f'{complemento}',
            "bairro":f'{bairro}',
            "localidade":f'{localidade}',
            "uf": f'{uf}'
        }

        meuserializer = Serializer(data=dadosRecebidos)

        if meuserializer.is_valid():

            cep_pesquisado = BancoDeDados.objects.filter(cep=cep)

            cep_pesquisado_existe = cep_pesquisado.exists()

            if cep_pesquisado_existe:
                return Response({"aviso! Seu cep já existe no banco"})
            meuserializer.save()
            return Response(meuserializer.data)
        else:
            return Response({"Aviso:"f"{NameError}"})
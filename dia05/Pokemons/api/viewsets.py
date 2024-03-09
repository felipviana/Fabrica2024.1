from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from ..models import Pokemon
from .serializers import Serializer
import requests

class AppViewSet(ModelViewSet):
    queryset=Pokemon.objects.all()
    serializer_class = Serializer

    #As habilidades e tipagens dos pokemons retornam no json separados por listas/dicionários, para conseguir guardar essas 
    #informaçoes em variáveis foi necessário criar funções que percorrecem essas estruturas 
    
    def create(self, request):
        def pegarHabilidades(Pokemon):
            listaDeHabilidades = [i['ability']['name'] for i in Pokemon['abilities']]
            return listaDeHabilidades
        
        def pegarTipagem(Pokemon):
            listaDeTipagens = [i['type']['name'] for i in Pokemon['types']]
            return listaDeTipagens
        
        pokemon= (request.data.get('nomePokemon')).lower()
        site = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
        requisicao= requests.get(site)
        json = requisicao.json()

        nomePokemon = json.get('name','')
        tipagem = ', '.join(pegarTipagem(json))
        habilidade = ', '.join(pegarHabilidades(json))
        altura = json.get('height','')
        peso =json.get('weight','')
        idNaPokedex = json.get('id','')
        

        dadosRecebidos={
            "nomePokemon":f'{nomePokemon}',
            "tipagem":f'{tipagem}',
            "habilidade":f'{habilidade}',
            "altura":f'{altura}',
            "peso":f'{peso}',
            "pokedexId":f'{idNaPokedex}'
        }

        meuserializer = Serializer(data=dadosRecebidos)

        if meuserializer.is_valid():

            pokemonPesquisado = Pokemon.objects.filter(nomePokemon=nomePokemon)

            pokemonPesquisadoExiste = pokemonPesquisado.exists()

            if pokemonPesquisadoExiste:
                return Response({"aviso! Seu Pokemon já existe no banco"})
            meuserializer.save()
            return Response(meuserializer.data)
        else:
            return Response({"Erro de validação! Consulte o suporte"})
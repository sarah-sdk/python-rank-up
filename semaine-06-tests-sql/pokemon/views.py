from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pokemon
from .serializers import PokemonSerializer

# Create your views here.
class PokemonList(APIView):
  def get(self, response):
    pokemons = Pokemon.objects.all()
    serializer = PokemonSerializer(pokemons, many=True)
    return Response(serializer.data)

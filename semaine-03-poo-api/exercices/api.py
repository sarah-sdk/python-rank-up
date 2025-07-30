import requests

class Pokemon:
  def __init__(self, name, type1, type2):
    self.name = name
    self.type1 = type1
    self.type2 = type2
  
  def __str__(self):
    return f"{self.name} is a Pokémon of type {self.type1}" + \
    (f" and {self.type2}" if self.type2 else "")

url = 'https://pokeapi.co/api/v2/pokemon'

search_pokemon = input('Enter a Pokemon name: ')
response = requests.get(f'{url}/{search_pokemon.lower()}').json()

pokemon = Pokemon(response['name'], response['types'][0]['type']['name'], response['types'][1]['type']['name'] if len(response['types']) > 1 else None)

print(pokemon)
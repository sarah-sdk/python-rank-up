import requests

class Pokemon:
  def __init__(self, name, type1, type2):
    self.name = name
    self.type1 = type1
    self.type2 = type2

  def __str__(self):
    return f"{self.name} is a Pokémon of type {self.type1}" + \
    (f" and {self.type2}" if self.type2 else "")

def search_pokemon():
  asked_pokemon = input('Enter a Pokemon name: ')

  url = f'https://pokeapi.co/api/v2/pokemon/{asked_pokemon.lower()}'

  response = requests.get(url)
  
  if response.status_code == 404:
    return "This Pokémon doesn't exist."
  
  else:
    decoded_response = response.json()

    pokemon = Pokemon(decoded_response['name'].capitalize(), decoded_response['types'][0]['type']['name'], decoded_response['types'][1]['type']['name'] if len(decoded_response['types']) > 1 else None)
    return pokemon

def main():
  print(search_pokemon())

if __name__ == '__main__':
  main()
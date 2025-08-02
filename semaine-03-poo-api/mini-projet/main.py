import requests
from IPython.display import Image, display

class Pokemon:
  def __init__(self, name, type1, type2, hp, attack, defense, sprite):
    self.name = name
    self.type1 = type1
    self.type2 = type2
    self.hp = hp
    self.attack = attack
    self.defense = defense
    self.sprite = sprite

  def __str__(self):
    description = f"{self.name} is a Pokémon of type {self.type1}"
    if self.type2:
      description += f" and {self.type2}"
    description += f"\nHP: {self.hp} - Attack: {self.attack} - Defense: {self.defense}"
    return description

  def show_pokemon_sprite(self):
    display(Image(url=self.sprite))

def search_pokemon():
  asked_pokemon = input('Enter a Pokemon name: ')

  url = f'https://pokeapi.co/api/v2/pokemon/{asked_pokemon.lower()}'

  response = requests.get(url)
  
  if response.status_code == 404:
    return "This Pokémon doesn't exist."
  
  else:
    decoded_response = response.json()

    types = decoded_response['types']
    type1 = types[0]['type']['name']
    type2 = types[1]['type']['name'] if len(types) > 1 else None

    stats = decoded_response['stats']
    stat_map = {stat['stat']['name']: stat['base_stat'] for stat in stats}
    hp = stat_map.get('hp', 0)
    attack = stat_map.get('attack', 0)
    defense = stat_map.get('defense', 0)

    sprites = decoded_response['sprites']
    sprite = sprites['front_default']

    pokemon = Pokemon(
      decoded_response['name'].capitalize(),
      type1,
      type2,
      hp,
      attack,
      defense,
      sprite
    )

    pokemon.show_pokemon_sprite()
    
    return pokemon

def main():
  print(search_pokemon())

if __name__ == '__main__':
  main()
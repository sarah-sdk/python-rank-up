import requests
from models import Pokemon

def fetch_pokemon(name: str) -> Pokemon | str:
  url= f'https://pokeapi.co/api/v2/pokemon/{name.lower()}'
  response = requests.get(url)

  if response.status_code == 404:
    return "This Pokémon doesn't exist."
  
  data = response.json()

  types = data['types']
  type1 = types[0]['type']['name']
  type2 = types[1]['type']['name'] if len(types) > 1 else None

  stats = data['stats']
  stat_map = {stat['stat']['name']: stat['base_stat'] for stat in stats}
  hp = stat_map.get('hp', 0)
  attack = stat_map.get('attack', 0)
  defense = stat_map.get('defense', 0)

  sprites = data['sprites']
  sprite = sprites['front_default']

  pokemon = Pokemon(
    name=data['name'].capitalize(),
    type1=type1,
    type2=type2,
    hp=hp,
    attack=attack,
    defense=defense,
    sprite=sprite,
  )

  return pokemon
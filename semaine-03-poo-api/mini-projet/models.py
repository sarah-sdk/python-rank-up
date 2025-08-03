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
class Animal:
  def __init__(self, name, specie, sound, emoji):
    self.name = name
    self.specie = specie
    self.sound = sound
    self.emoji = emoji

  def make_sound(self):
    print(f'{self.name} makes {self.sound} {self.emoji}')

class Dog(Animal):
  def __init__(self, name):
    super().__init__(name, 'Dog', 'Woof', '🐶')

my_dog = Dog('Chien')
my_dog.make_sound()

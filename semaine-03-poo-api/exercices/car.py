class Car:
  def __init__(self, brand, color):
    self.brand = brand
    self.color = color
    self.speed = 0

  def speed_up(self):
    self.speed += 10
    print(f'The {self.color} car accelerates at a speed of {self.speed} km/h.')

my_car = Car('Mustang', 'grey')
print(my_car.brand)
my_car.speed_up()
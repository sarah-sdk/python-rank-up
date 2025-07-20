# MINI PROJET :
# Créer un programme en ligne permettant à un utilisateur de convertir différentes unités:
# - Température (Celsius ↔ Fahrenheit)
# - Distance (Kilomètres ↔ Miles)
# - Devise (Euros ↔ Dollars US)

def convert_temperature(way_choice, value):
  if way_choice == 1:
    return (value * 9/5)+32
  else:
    return (value-32)*5/9

def convert_distance(way_choice, value):
  if way_choice == 1:
    return value / 1.609
  else:
    return value * 1.609

def convert_currency(way_choice, value):
  if way_choice == 1:
    return value * 1.16
  else:
    return value / 1.16
      

available_units = ["Temperature", "Distance", "Currency"]

available_ways = {
  1: ['Celsius → Fahrenheit', 'Fahrenheit → Celsius'],
  2: ['km → miles', 'miles → km'],
  3: ['euros → US dollars', 'US dollars → euros'],
}

def select_unit(unit_choice):
  print('Which way would you like to convert?')
  ways = available_ways[unit_choice]

  for index, way in enumerate(ways, 1):
    print(f'{index}- {way}')
  print(f'{len(ways)+1}- Back')

  while True:
    try:
      way_choice = int(input("Your choice: "))
      if 1 <= way_choice <= len(ways):
        return way_choice
      elif way_choice == len(ways)+1:
        return None
      else:
        print("Invalid choice.")
    except ValueError:
      print("Please enter a valid number.")

def get_value():
  while True:
    try:
      return float(input("Enter the value to convert: "))
    except ValueError:
      print("Please enter a valid number.")

def show_main_menu():
    print("Which kind of unit you want to convert?")

    for index, unit in enumerate(available_units, 1):
      print(f"{index}- {unit}")
    print(f"{len(available_units)+1}- Exit")
    
    while True:
      try:
        unit_choice = int(input("Your choice: "))
        if 1 <= unit_choice <= len(available_units)+1:
          return unit_choice
        else:
          print("Please choose a valid number.")
      except ValueError:
        print("Please enter a valid number.")

print("Welcome to the converter!")
while True:
  unit_choice = show_main_menu()

  if unit_choice == 4:
    print('Goodbye!')
    break

  way_choice = select_unit(unit_choice)
  if way_choice is None:
    continue

  print(f"You chose to convert: {available_ways[unit_choice][way_choice - 1]}")

  value = get_value()

  if unit_choice == 1:
    result = convert_temperature(way_choice, value)
  elif unit_choice == 2:
    result = convert_distance(way_choice, value)
  elif unit_choice == 3:
    result = convert_currency(way_choice, value)

  print(f"Result: {round(result, 2)}")

  again = input("Do you want to do another conversion? (y/n): ").strip().lower()
  if again != "y":
    print("Goodbye!")
    break
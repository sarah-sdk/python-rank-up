# Objectifs :
# Déclarer et utiliser des variables de type str, int, float et bool
# Afficher les infos sous forme de phrases complètes

name = input('Enter your name: ')
age = int(input('Enter your age: '))
height = float(input('Enter your height: '))
is_adult = age > 18

print(f'Your name is {name}.')
print(f"Are you an adult? {'Yes' if is_adult else 'No'}.")
print(f'You are {height:.2f} meters tall.')
# EXERCICE 1 : Compter à rebours à partir d'un nombre
start = int(input("Enter a number: "))

while start > 0:
  print(start)
  start -= 1
print("0... Ignition 🚀")

# EXERCICE 2 : Parcours une liste de prénoms
names = ["Michel", "Jean-Michel", "Jean-Michel-Michel", "Jean-Jean-Michel"]

for name in names:
  print(f'Hello, {name}!')

# EXERCICE 3 : Somme de nombres pairs
n = int(input("Enter a number: "))
sum = 0
i = 0

while i <= n:
  if i % 2 == 0:
    sum += i
    i+=2

print(f'The sum of even numbers between 0 and {n} is {sum}')

# EXERCICE 4 : Générateur de table de multiplication
x = int(input("Enter a number: "))
i = 1

while i <= 10:
  print(f'{x} x {i} = {x*i}')
  i+=1
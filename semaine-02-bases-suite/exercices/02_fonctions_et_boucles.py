#EXERCICE 1:
def is_even(n):
  return n % 2 == 0

#EXERCICE 2:
def average(grades):
  # total = 0
  # for grade in grades:
  #   total += grade

  if sum(grades)/len(grades) >= 10:
    return "✅ Admis"
  else:
    return "❌ Echec"

#EXERCICE 3:
def reverse(word):
  return word[::-1]

#EXERCICE 4:
def main():
  print(is_even(132456))
  print(is_even(3))

  print(average([9,10,12,11,8]))
  print(average([3,2,6,14]))

  print(reverse('kayak'))
  print(reverse('pouet'))
  print(reverse('engage le jeu que je le gagne'))
  print(reverse('Kaer Morhen'))

if __name__ == '__main__':
  main()
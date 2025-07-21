# EXERCICE 1: Addition simple
# -> x + y
def sum(a, b=0):
  return a+b

# EXERCICE 2: Factorielle
# -> n! = n x (n-1) x ... x 1
def factorial(x):
  if x == 0:
    return 1
  else:
    result = 1
    for i in range(2, x+1):
      result *= i
    return result


# EXERCICE 3: Fonction main()
# Crée une fonction main() qui appelle tes deux fonctions avec des exemples de ton choix, puis exécute-la à la fin
def main():
  print(sum(1))
  print(factorial(5))

if __name__ == '__main__':
  main()
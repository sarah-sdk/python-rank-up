from random import randint

# EXERCICE 1 
age = int(input("Enter your age: "))

if age < 18:
  print("You're underage.")
elif age == 18:
  print("You've just come of age !")
else :
  print("You're an adult.")

# EXERCICE 2
number = int(input("Enter an integer: "))

if number % 2 == 0:
  print("Your number is even.")
else :
  print("Your number is odd.")

# EXERCICE 3
secret = randint(1,100)

print("🔍 Guess the secret number between 1 and 100!")

while True:
  guess = int(input("Your guess: "))

  if guess < 1 or guess > 100:
    print("⚠️ Number must be between 1 and 100.")
    continue
  
  if secret > guess: 
    print("Too low !")
  elif secret < guess:
    print("Too high !")
  else:
    print(f"🎉 Correct ! The number was {secret}")
    break

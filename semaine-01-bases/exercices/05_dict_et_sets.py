# EXERCICE 1:
user = {}

user['name'] = input("What's your name? ")
user['age'] = int(input("How old are you? "))
user['email'] = input("What's your email? ")

print(user)

user['age'] += 10
user['is_verified'] = True

if user['age'] >= 18:
  user['status'] = 'adult'
else:
  user['status'] = 'minor'

print(user)

for key in user:
  print(f'{key}: {user[key]}')

# EXERCICE 2:
user1 = {'coding', 'traveling', 'gaming'}
user2 = {'gaming', 'music', 'coding'}

common_hobbies = user1 & user2

if not common_hobbies:
  print('The 2 users have no hobbies in common.')
else:
  hobbies_list = list(common_hobbies)
  if len(hobbies_list) == 1:
    print(f'The common hobby of the 2 users is {hobbies_list[0]}')
  else:
    *all_but_last, last = hobbies_list
    formatted = ", ".join(all_but_last) + f" and {last}"
    print(f"The common hobbies of the two users are {formatted}.")

# EXERCICE 3:
numbers = [1, 2, 2, 3, 4, 4]
print(set(numbers))

# add_contact()
def add_contact(doc):
  contact = ''

  print("What's the informations of the person you want to add?")
  lastname = input("Lastname: ")
  firstname = input("Firstname: ")
  email = input("Email: ")
  phone_number = input("Phone number: ")

  contact += f'{lastname},{firstname},{email},{phone_number}\n'

  with open(doc, "a") as file:
    file.write(contact)

  print('✅ Contact added successfully with the following informations:')
  print(f"Lastname: {lastname} - Firstname: {firstname} - Email: {email} - Phone number: {phone_number}")

# search_contact()

#all_contacts()
def all_contacts(doc):
  with open(doc, "r") as file:
    content = file.read()
    print(content)

choices = ["Add a new contact", "Search a contact", "See all of your contacts"]

def show_main_menu():
  print("What do you want to do ?")

  for index, choice in enumerate(choices, 1):
    print(f'{index}- {choice}')
  print(f'{len(choices)+1}- Exit')

  while True:
    try:
      choice = int(input("Your choice: "))
      if 1 <= choice <= len(choices)+1:
        return choice
      else:
        print("Please choose a valid number.")
    except ValueError:
      print("Please enter a valid number.")

while True:
  link = './semaine-02-bases-suite/mini-projet/contacts.csv'
  choice = show_main_menu()

  if choice == 4:
    print('Goodbye!')
    break

  if choice == 1:
    result = add_contact(link)
  # elif choice == 2:
  #   result = search_contact(link)
  elif choice == 3:
    result = all_contacts(link)

  again = input('Do you want to do anything else? (y/n):').strip().lower()
  if again != 'y':
    print('Goodbye!')
    break
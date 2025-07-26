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
def search_contacts(doc):
  with open(doc, 'r') as file:
    lines = file.readlines()
  
  headers = lines[0].strip().split(', ')
  contacts = lines[1:]

  contacts_list = []

  for contact in contacts:
    data = contact.strip().split(', ')
    person = dict(zip(headers, data))
    contacts_list.append(person)
  
  firstname = input("What's the firstname of the person you're looking for? ")

  for person in contacts_list:
    if person["firstname"].lower() == firstname.lower():
      print(f'✅ Contact found: ', person)
      break
    else:
      print('No contact found')

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
  elif choice == 2:
    # print("How do you want to search a contact?")
    # print('1- By firstname')
    # print('2- By lastname')
    # print('3- By email')
    # print('4- By phone number')
    result = search_contacts(link)
  elif choice == 3:
    result = all_contacts(link)

  again = input('Do you want to do anything else? (y/n):').strip().lower()
  if again != 'y':
    print('Goodbye!')
    break
# add_contact()
def add_contact(doc):
  print("📇 What are the details of the person you want to add?")
  lastname = input("Last name: ")
  firstname = input("First name: ")
  email = input("Email: ")
  phone_number = input("Phone number: ")

  contact = f'{lastname}, {firstname}, {email}, {phone_number}\n'

  with open(doc, "a") as file:
    file.write(contact)

  print('✅ Contact added successfully:')
  print(f"{lastname} {firstname} - Email: {email} - Phone: {phone_number}")

# search_contact()
def search_contacts(doc, filter_index):
  filters = ["firstname", "lastname", "email", "phone number"]
  selected_filter = filters[filter_index - 1]

  with open(doc, 'r') as file:
    lines = file.readlines()
  
  headers = lines[0].strip().split(', ')
  contacts = lines[1:]

  contacts_list = []
  for contact in contacts:
    data = contact.strip().split(', ')
    person = dict(zip(headers, data))
    contacts_list.append(person)
  
  answer = input(f"What's the {selected_filter} of the person you're looking for? ")

  matches = [
    person for person in contacts_list
    if person[selected_filter].strip().lower() == answer.strip().lower()
  ]

  if matches:
    print(f"✅ {len(matches)} contact(s) found:")
    for person in matches:
      print(f"{person['firstname']} {person['lastname']} - {person['email']} - {person['phone number']}")
  else:
    print("❌ No contact found.")

#view_all_contacts()
def view_all_contacts(doc):
  with open(doc, 'r') as file:
    lines = file.readlines()
  
  headers = lines[0].strip().split(', ')
  contacts = lines[1:]

  contacts_list = []

  for contact in contacts:
    data = contact.strip().split(', ')
    person = dict(zip(headers, data))
    contacts_list.append(person)

  print("📒 Your contact list:")
  for contact in contacts_list:
      print(f"{contact['firstname']} {contact['lastname']}, {contact['email']}, {contact['phone number']}")

#select_search_filter()
def select_search_filter():
  while True:
    print("🔍 How would you like to search for a contact?")
    print("1- By first name")
    print("2- By last name")
    print("3- By email")
    print("4- By phone number")
    try:
      selected_choice = int(input("Your choice: "))
      if 1 <= selected_choice <= 4:
        return selected_choice
      else:
        print("Please enter a number between 1 and 4.")
    except ValueError:
      print("Please enter a valid number.")

def show_main_menu():
  choices = ["Add a new contact", "Search a contact", "See all of your contacts"]
  print("\n📘 What would you like to do?")

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


def main():
    print("📇 Welcome to the Contact Manager!")
    file_path = "./semaine-02-bases-suite/mini-projet/contacts.csv"

    while True:
        choice = show_main_menu()

        if choice == 1:
            add_contact(file_path)
        elif choice == 2:
            filter_index = select_search_filter()
            search_contacts(file_path, filter_index)
        elif choice == 3:
            view_all_contacts(file_path)
        elif choice == 4:
            print("👋 Goodbye!")
            break

        again = input("Would you like to do something else? (y/n): ").strip().lower()
        if again != 'y':
            print("👋 Goodbye!")
            break


if __name__ == "__main__":
    main()
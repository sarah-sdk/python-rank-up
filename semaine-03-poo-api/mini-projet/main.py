from api import fetch_pokemon

def run():
  print('Welcome to the Pokemon Finder 🔍')

  while True:
    name = input("\nEnter a Pokémon name (or 'q' to quit): ")
    if name.lower() == 'q':
      print('Goodbye Trainer! 👋')
      break
    
    result = fetch_pokemon(name)
    print(result)

if __name__ == '__main__':
  run()
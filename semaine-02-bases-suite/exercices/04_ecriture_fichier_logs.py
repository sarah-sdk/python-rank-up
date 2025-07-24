import datetime

def log_event(doc, message):
  today = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

  print('🔓 Ouverture du fichier')
  with open(doc, 'a') as file:
    content = f'[{today}] {message}\n'

    file.write(content)
  print(f'✅ Log enregistré : {message}')

def main():
  doc = './semaine-02-bases-suite/exercices/fichiers_annexes/logs.txt'
  log_event(doc, 'pouet')

if __name__ == '__main__':
  main()

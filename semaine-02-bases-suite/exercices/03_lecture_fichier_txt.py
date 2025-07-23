def count_lines(doc):
  with open(doc, 'r') as file:
    lines = len(file.readlines())
    print('Total number of lines:', lines)

def print_uppercase_lines(doc):
  with open(doc, 'r') as file:
    content = file.read()
    print(content.upper())

def main():
  doc = './semaine-02-bases-suite/exercices/fichiers_annexes/data.txt'

  count_lines(doc)
  print_uppercase_lines(doc)

if __name__ == '__main__':
  main()
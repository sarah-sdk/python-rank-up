import argparse

parser = argparse.ArgumentParser(description='Add txt to file')

parser.add_argument('txt', type=str, help='Text to add')
parser.add_argument('-f', '--file', type=str, help='The file')
args = parser.parse_args()

if args.file:
  with open(args.file, 'a') as file:
    file.write(args.txt + '\n')
  
  print(f'Text add: {args.txt}')
else:
  print(args.txt)
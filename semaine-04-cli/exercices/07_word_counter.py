import argparse
import os

parser = argparse.ArgumentParser(description='Word counter')

parser.add_argument('file', type=str, help='File')
parser.add_argument('-l', '--lines', action='store_true', help='Lines counter')
args = parser.parse_args()

if not os.path.exists(args.file):
  parser.error(f'The file {args.file} does not exist.')

with open(args.file, 'r') as file:
  content = file.read().replace('\n', ' ')
  print(content)
  print(f'Number of words: {len(content.split(' '))}')

if args.lines:
    with open(args.file, 'r') as file:
      lines = file.readlines()
      print(f'Number of lines: {len(lines)}')
  

import argparse
import os

parser = argparse.ArgumentParser(description='File summary')
parser.add_argument('file', type=str, help='Path to the file')
arg = parser.parse_arg()

if not os.path.exists(arg.file):
  parser.error(f"The file {arg.file} does not exist.")

with open(arg.file, 'r') as file:
  content = file.read()

lines = content.splitlines()
words = [w for w in content.split() if w.strip()]
chars = [c for c in content if c.strip()]

print(f'Number of lines: {len(lines)}')
print(f'Number of words: {len(words)}')
print(f'Number of characters: {len(chars)}')
print(f'Average word length: {int(len(chars)/len(words)) if words else 0}')
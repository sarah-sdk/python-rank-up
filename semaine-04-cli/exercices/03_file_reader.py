import argparse
import os

parser = argparse.ArgumentParser(description='File Reader')

parser.add_argument('filepath', type=str, help='Path to the input file.')
parser.add_argument('-l', '--lines', type=int, help='The line you want to stop at')
args = parser.parse_args()

if not os.path.exists(args.filepath):
  parser.error(f"The file {args.filepath} does not exist.")

with open(args.filepath, 'r') as file:
  if args.lines:
    lines = file.readlines()

    for i in range(min(args.lines, len(lines))):
        print(lines[i])
  else:
    content = file.read()

    print(content)
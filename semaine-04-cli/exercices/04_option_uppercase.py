import argparse

parser = argparse.ArgumentParser(description='Sentence printer')

parser.add_argument('txt', type=str, help='The text you want to print')
parser.add_argument('-u', '--uppercase', action='store_true', help='If you want to see it in uppercase')
args = parser.parse_args()

if args.uppercase:
  print(args.txt.upper())
else:
  print(args.txt)
import argparse

parser = argparse.ArgumentParser(description='Repeat please')

parser.add_argument('txt', type=str, help='The text you want to repeat')
parser.add_argument('-t', '--times', type=int, help='The time you want to say it')
args = parser.parse_args()

if args.times:
  for _ in range(args.times):
    print(args.txt)
else:
  print(args.txt)
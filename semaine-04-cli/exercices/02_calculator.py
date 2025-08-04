import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('num1', type=int, help='The first number.')
parser.add_argument('num2', type=int, help='The second number.')
parser.add_argument('operator', choices=['+', '-', '*', '/'], help='The operation to perform: +, -, * or /')
args = parser.parse_args()

if args.operator == '+':
  operator = 'sum'
  result = args.num1 + args.num2
elif args.operator == '-':
  operator = 'substraction'
  result = args.num1 - args.num2
elif args.operator == '*':
  operator = 'multiplication'
  result = args.num1 * args.num2
else:
  operator = 'division'
  result = args.num1 / args.num2

print('The {} of {} and {} is {}'.format(operator, args.num1, args.num2, result))

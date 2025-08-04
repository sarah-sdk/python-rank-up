import argparse

parser = argparse.ArgumentParser(description='Hello to user')
parser.add_argument('name', type=str, help='The name to say hello with.')
args = parser.parse_args()

print('👋 Hello, {}!'.format(args.name))
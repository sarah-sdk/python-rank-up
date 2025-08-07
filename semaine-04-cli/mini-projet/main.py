import argparse
from todo import add_task, list_tasks

parser = argparse.ArgumentParser(description='TODO List')

parser.add_argument('action', choices=['add', 'list'], help='Actions you can do with the TODO list.')
parser.add_argument('task', nargs='?', help='Name of the task you want to add.')
args = parser.parse_args()

if args.action == 'add':
  if args.task is None:
    parser.error('Entrez le nom de la tâche à ajouter.')
  else:
    print(f"Tâche ajoutée: {args.task}")
    add_task(args.task)
elif args.action == 'list':
  list_tasks()

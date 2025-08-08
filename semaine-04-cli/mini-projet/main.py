import argparse
from todo import add_task, list_tasks, task_done, delete_task

parser = argparse.ArgumentParser(description='TODO List')

parser.add_argument('action', choices=['add', 'list', 'done', 'delete'], help='Actions you can do with the TODO list.')
parser.add_argument('value', nargs='?', help='Task name or ID depending on the action.')
args = parser.parse_args()

if args.action == 'add':
  if args.value is None:
    parser.error('Entrez le nom de la tâche à ajouter.')
  else:
    print(f"Tâche ajoutée: {args.value}")
    add_task(args.value)

elif args.action == 'list':
  list_tasks()

elif args.action == 'done':
  if args.value is None:
    parser.error('Entrez un ID.')
  else:
    try:
      task_id = int(args.value)
    except ValueError:
      parser.error("L'ID doit être un nombre.")
    task_done(task_id)
    print(f'Tâche {task_id} marquée comme terminée ✅')

elif args.action == 'delete':
    if args.value is None:
      parser.error('Entrez un ID.')
    else:
      try:
        task_id = int(args.value)
      except ValueError:
        parser.error("L'ID doit être un nombre.")
      delete_task(task_id)
      print(f'Tâche {task_id} supprimée 🗑️')

import json

doc = "semaine-04-cli/mini-projet/todo.json"

def add_task(description):
  with open(doc, 'r') as file:
    tasks = json.load(file)

    if not tasks:
      max_id = 0
    else:
      max_id = 0
      for task in tasks:
        if int(task['id']) >= max_id:
          max_id = int(task['id'])

    max_id += 1
      
    new_task = {
      'id': max_id,
      'description': description,
      'done': False,
    }

    if not tasks:
      tasks = [new_task]
    else:
      tasks.append(new_task)

  with open(doc, 'w') as file:
    json.dump(tasks, file, indent=2)

def list_tasks():
  with open(doc, 'r') as file:
    tasks = json.load(file)

    if not tasks:
      print("Aucune tâche enregitrée")
    else:
      for task in tasks:
        print(f"{task['id']} - {task['description']} - {'Fait' if task['done'] else 'A faire' }")

def task_done(task_id):
  with open(doc, 'r') as file:
    tasks = json.load(file)

    for task in tasks:
      if task['id'] == task_id:
        task['done'] = True

  with open(doc, 'w') as file:
    json.dump(tasks, file, indent=2)

def delete_task(task_id):
  with open(doc, 'r') as file:
    tasks = json.load(file)

  filtered_tasks = [task for task in tasks if task['id'] != task_id]

  with open(doc, 'w') as file:
    json.dump(filtered_tasks, file, indent=2)
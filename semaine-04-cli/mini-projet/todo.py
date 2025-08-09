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
  
  return new_task

def list_tasks():
  with open(doc, 'r') as file:
    tasks = json.load(file)
    return tasks

def task_done(task_id):
  with open(doc, 'r') as file:
    tasks = json.load(file)

    task_done = None
    for task in tasks:
      if task['id'] == task_id:
        task['done'] = True
        task_done = task

  with open(doc, 'w') as file:
    json.dump(tasks, file, indent=2)
  
  return task_done

def delete_task(task_id):
  with open(doc, 'r') as file:
    tasks = json.load(file)

  filtered_tasks = [task for task in tasks if task['id'] != task_id]
  if len(filtered_tasks) == len(tasks):
    return False

  with open(doc, 'w') as file:
    json.dump(filtered_tasks, file, indent=2)

  return True
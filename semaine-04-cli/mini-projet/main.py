import argparse
from todo import add_task, list_tasks, task_done, delete_task
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

console = Console()

parser = argparse.ArgumentParser(description='TODO List')

parser.add_argument('action', choices=['add', 'list', 'done', 'delete'], help='Actions you can do with the TODO list.')
parser.add_argument('value', nargs='?', help='Task name or ID depending on the action.')
args = parser.parse_args()

if args.action == 'add':
  if args.value is None:
    parser.error('Entrez le nom de la tâche à ajouter.')
  else:
    new_task = add_task(args.value)
    console.print(
      Panel(
        f"☕️ Tâche [bold dark_orange3]#{new_task['id']}[/bold dark_orange3] : [italic #DEB887]{new_task['description']}[/italic #DEB887]",
        border_style="#A0522D",
        style="on grey11",
        title="Tâche ajoutée",
        title_align="left"
      )
    )

elif args.action == 'list':
  tasks = list_tasks()
  if not tasks:
          console.print(
        Panel(
          "[italic #DEB887]Aucune tâche enregistrer.[/italic #DEB887]",
          border_style="#A0522D",
          style="on grey11",
          title="Information",
          title_align="left"
        )
      )
  else:
    table = Table(box=box.ROUNDED)
    table.add_column("ID", style="dark_orange3", justify="center")
    table.add_column("Description", style="#DEB887")
    table.add_column("Statut", justify="center")

    for task in tasks:
      status = "✅" if task['done'] else "❌"
      table.add_row(str(task['id']), task['description'], status)
    
    console.print(
      Panel(
        table,
        border_style="#A0522D",
        style="on grey11",
        title="Liste des tâches",
        title_align='left',
      )
    )

elif args.action == 'done':
  if args.value is None:
    parser.error('Entrez un ID.')
  else:
    try:
      task_id = int(args.value)
    except ValueError:
      parser.error("L'ID doit être un nombre.")
    task = task_done(task_id)

    if not task:
      console.print(
        Panel(
          "[italic #DEB887]Aucune tâche ne possède cet ID.[/italic #DEB887]",
          border_style="#A0522D",
          style="on grey11",
          title="Information",
          title_align="left"
        )
      )
    else:
      console.print(
        Panel(
          f"✅ Tâche [bold dark_orange3]#{task['id']}[/bold dark_orange3] : [italic #DEB887]{task['description']}[/italic #DEB887]",
          border_style="#A0522D",
          style="on grey11",
          title="Tâche complétée",
          title_align="left"
        )
      )

elif args.action == 'delete':
  if args.value is None:
    parser.error('Entrez un ID.')

  try:
    task_id = int(args.value)
  except ValueError:
    parser.error("L'ID doit être un nombre.")

  confirmation = console.input(
    Panel(
      "[#DEB887]Êtes-vous sûr de vouloir supprimer cette tâche ? [bold](o/n)[/bold][/#DEB887]",
      border_style="#A0522D",
      style="on grey11",
    )
  ).lower()

  while confirmation != 'n' and confirmation != 'o':
    confirmation = console.input(
    Panel(
      "[#DEB887]Veuillez choisir une entrée valide : [bold](o/n)[/bold][/#DEB887]",
      border_style="#A0522D",
      style="on grey11",
    )
  ).lower()

  if confirmation == 'n':
    console.print(
      Panel(
        "[italic #DEB887]Aucune tâche ne sera supprimée.[/italic #DEB887]",
        border_style="#A0522D",
        style= "on grey11",
      )
    )
    
  else:
    deletion_confirmation = delete_task(task_id)
    if deletion_confirmation:
      console.print(
        Panel(
          f"[italic #DEB887]Tâche [bold dark_orange3]#{task_id}[/bold dark_orange3] supprimée[/italic #DEB887]",
          border_style="#A0522D",
          style="on grey11",
          title="Information",
          title_align="left"
        )
      )
    else:
      console.print(
        Panel(
          f"[italic #DEB887]Aucune tâche ne possède cet ID.[/italic #DEB887]",
          border_style="#A0522D",
          style="on grey11",
          title="Information",
          title_align="left"
        )
      )

# CLI To-Do List Manager
A simple command-line application to manage your tasks.
Built with Python, using `argparse` for argument parsing and `rich` for styled output.

---

## Features
- Add tasks with an auto-incremented ID
- List all tasks with a clear, styled table
- Mark tasks as done ✅
- Delete tasks with confirmation prompt
- Data stored in JSON format

---

## Installation
### 1. Clone this repository:
```bash
git clone git@github.com:sarah-sdk/python-rank-up.git
cd python-rank-up/semaine-04-cli/mini-projet
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Usage
### Add task
```bash
python main.py add "Buy coffee"
```

### List tasks
```bash
python main.py list
```

### Mark as done
```bash
python main.py done 1
```

### Delete a task
```bash
python main.py delete 1
```

---

## Project structure
```markdown
mini-projet/
│
├── data/
│   └── todo.json         # Stores all tasks
│
├── main.py               # CLI logic and argument parsing
├── todo.py               # Task management functions
├── README.md
└── requirements.txt

---

## Requirements
- Python 3.8+
- [`rich`](https://rich.readthedocs.io/en/stable/)
```
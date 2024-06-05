# todolist.py

import json
import os

# Chemin du fichier où les tâches seront sauvegardées
FILE_PATH = 'tasks.json'

def load_tasks():
    """Charge les tâches à partir du fichier JSON."""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Sauvegarde les tâches dans le fichier JSON."""
    with open(FILE_PATH, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    """Ajoute une nouvelle tâche."""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"Tâche '{task}' ajoutée.")

def list_tasks():
    """Liste toutes les tâches."""
    tasks = load_tasks()
    if not tasks:
        print("Aucune tâche trouvée.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. [{status}] {task['task']}")

def mark_task_done(task_number):
    """Marque une tâche comme terminée."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        print(f"Tâche {task_number} marquée comme terminée.")
    else:
        print("Numéro de tâche invalide.")
# main.py

from todolist import add_task, list_tasks, mark_task_done

def main():
    """Boucle principale de l'application."""
    while True:
        print("\nOptions:")
        print("1. Ajouter une tâche")
        print("2. Lister les tâches")
        print("3. Marquer une tâche comme terminée")
        print("4. Quitter")
        choice = input("Choisissez une option: ")
        if choice == '1':
            task = input("Entrez la tâche: ")
            add_task(task)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            try:
                task_number = int(input("Entrez le numéro de la tâche à marquer comme terminée: "))
                mark_task_done(task_number)
            except ValueError:
                print("Veuillez entrer un numéro valide.")
        elif choice == '4':
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()

import json
import os

# Функция для загрузки задач из файла
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        return tasks
    else:
        return []

# Функция для сохранения задач в файл
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)

# Функция для добавления новой задачи
def add_task(tasks, task):
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Задача добавлена!")

# Функция для вывода списка задач
def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
    else:
        print("Список задач:")
        for index, task in enumerate(tasks, start=1):
            status = "Готово" if task["completed"] else "В процессе"
            print(f"{index}. {task['task']} - {status}")

# Функция для отметки задачи как выполненной
def complete_task(tasks, index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]["completed"] = True
        save_tasks(tasks)
        print("Задача отмечена как выполненная!")
    else:
        print("Некорректный номер задачи.")

# Основная функция приложения
def main():
    tasks = load_tasks()

    while True:
        print("\n1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Отметить задачу как выполненную")
        print("4. Выйти")

        choice = input("Выберите действие (1/2/3/4): ")
        os.system('clear')

        if choice == "1":
            task = input("Введите новую задачу: ")
            add_task(tasks, task)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            index = int(input("Введите номер задачи, которую хотите отметить как выполненную: "))
            complete_task(tasks, index)
        elif choice == "4":
            print("Выход из приложения. До свидания!")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие снова.")

if __name__ == "__main__":
    main()

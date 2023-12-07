import json
import os
import tkinter as tk
from tkinter import messagebox


# Функція для завантаження задач з файлу
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        return tasks
    else:
        return []


# Функція для збереження задач у файл
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)


# Функція для додавання задачі
def add_task(entry, listbox, tasks):
    task = entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        save_tasks(tasks)
        messagebox.showinfo("Успішно", "Задачу додано!")
        entry.delete(0, tk.END)
        show_tasks(listbox, tasks)
    else:
        messagebox.showwarning("Увага", "Будь ласка, введить задачу.")


# Функция для вывода списка задач
def show_tasks(listbox, tasks):
    listbox.delete(0, tk.END)
    if not tasks:
        listbox.insert(tk.END, "Список задач пустий.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "Готово" if task["completed"] else "В процесі"
            listbox.insert(tk.END, f"{index}. {task['task']} - {status}")


# Функція для позначенния задачі як виконаної
def complete_task(listbox, tasks):
    selected_index = listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            save_tasks(tasks)
            messagebox.showinfo("Успішно", "Задачу позначено як виконану!")
            show_tasks(listbox, tasks)
        else:
            messagebox.showwarning("Увага", "Невірний номер задачи.")
    else:
        messagebox.showwarning("Увага", "Будь ласка, виберіть задачу для позначення.")


def delete_task(listbox, tasks):
    selected_index = listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        if 0 <= index < len(tasks):
            tasks.pop(index)
            save_tasks(tasks)
            messagebox.showinfo("Успішно", "Задачу видалено!")
            show_tasks(listbox, tasks)
        else:
            messagebox.showwarning("Увага", "Невірний номер задачи.")
    else:
        messagebox.showwarning("Увага", "Будь ласка, виберіть задачу для видалення.")


# Основная функция приложения
def main():
    tasks = load_tasks()

    root = tk.Tk()
    root.title("Менеджер задач")

    label = tk.Label(root, text="Введіть нову задачу:")
    label.pack(pady=10)

    entry = tk.Entry(root, width=50)
    entry.pack(pady=10)

    add_button = tk.Button(root, text="Додати задачу", command=lambda: add_task(entry, listbox, tasks))
    add_button.pack(pady=10)

    listbox = tk.Listbox(root, width=60, height=15)
    listbox.pack(pady=10)

    show_tasks(listbox, tasks)

    complete_button = tk.Button(root, text="Позначити як виконану", command=lambda: complete_task(listbox, tasks))
    complete_button.pack(pady=10)

    delete_button = tk.Button(root, text="Видалити задачу", command=lambda: delete_task(listbox, tasks))
    delete_button.pack(pady=10)

    exit_button = tk.Button(root, text="Вийти", command=root.destroy)
    exit_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()

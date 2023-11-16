import json
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ToDo List")
        self.root.geometry("400x400")

        # Загрузка задач из файла
        self.tasks = self.load_tasks()

        # Создание стиля для кнопок
        self.style = ttk.Style()
        self.style.configure("TButton", padding=5, font=("Helvetica", 12))

        # Создание виджетов
        self.task_entry = tk.Entry(root, width=40, font=("Helvetica", 12))
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, font=("Helvetica", 12))
        self.task_listbox.bind("<Delete>", self.delete_task)
        self.task_listbox.bind("<Return>", self.toggle_completion)
        self.add_button = ttk.Button(root, text="Добавить", command=self.add_task, style="TButton")
        self.show_button = ttk.Button(root, text="Показать задачи", command=self.show_tasks, style="TButton")
        self.exit_button = ttk.Button(root, text="Выйти", command=root.quit, style="TButton")

        # Размещение виджетов
        self.task_entry.pack(pady=10)
        self.add_button.pack()
        self.show_button.pack()
        self.task_listbox.pack()
        self.exit_button.pack()

    def load_tasks(self):
        if not tk.messagebox.askyesno("Загрузка задач", "Хотите ли вы загрузить предыдущие задачи?"):
            return []
        try:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
            return tasks
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            messagebox.showerror("Ошибка", "Ошибка при загрузке задач из файла.")
            return []

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=2)

    def add_task(self):
        new_task = self.task_entry.get()
        if new_task:
            self.tasks.append({"task": new_task, "completed": False})
            self.save_tasks()
            self.task_entry.delete(0, tk.END)  # Очистить поле ввода
            messagebox.showinfo("Успех", "Задача добавлена успешно!")
        else:
            messagebox.showwarning("Внимание", "Введите текст задачи.")

    def show_tasks(self):
        self.task_listbox.delete(0, tk.END)
        if not self.tasks:
            messagebox.showinfo("Список задач", "Список задач пуст.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                status = "Готово" if task["completed"] else "В процессе"
                self.task_listbox.insert(tk.END, f"{index}. {task['task']} - {status}")

    def delete_task(self, event):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            confirmed = messagebox.askyesno("Удаление задачи", "Вы уверены, что хотите удалить эту задачу?")
            if confirmed:
                del self.tasks[selected_index[0]]
                self.save_tasks()
                self.show_tasks()

    def toggle_completion(self, event):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            task["completed"] = not task["completed"]
            self.save_tasks()
            self.show_tasks()

if __name__ == "__main__":
    root = ThemedTk(theme="arc")  # Выберите тему: "arc", "plastik", "adapta", и другие
    app = TodoApp(root)
    root.mainloop()

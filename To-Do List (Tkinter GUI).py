import tkinter as tk
from tkinter import messagebox


def add_task():
    task = task_entry.get().strip()

    # Check if task is empty
    if task == "":
        messagebox.showerror("Error", "Task cannot be empty!")
        return

    # Add task to Listbox
    task_listbox.insert(tk.END, task)

    # Clear the Entry box
    task_entry.delete(0, tk.END)



def delete_task():
    selected = task_listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Please select a task to delete.")
        return

    task_listbox.delete(selected)



def clear_tasks():
    answer = messagebox.askyesno(
        "Confirm",
        "Are you sure you want to clear all tasks?"
    )

    if answer:
        task_listbox.delete(0, tk.END)



root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.resizable(False, False)


title_label = tk.Label(
    root,
    text="My To-Do List",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=10)


task_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 12)
)
task_entry.pack(pady=10)


add_button = tk.Button(
    root,
    text="Add Task",
    width=20,
    command=add_task
)
add_button.pack(pady=5)


task_listbox = tk.Listbox(
    root,
    width=40,
    height=12,
    font=("Arial", 12),
    selectbackground="lightblue"
)
task_listbox.pack(pady=15)


delete_button = tk.Button(
    root,
    text="Delete Selected Task",
    width=20,
    command=delete_task
)
delete_button.pack(pady=5)


clear_button = tk.Button(
    root,
    text="Clear All Tasks",
    width=20,
    command=clear_tasks
)
clear_button.pack(pady=5)


root.mainloop()
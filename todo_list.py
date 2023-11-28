from tkinter import *
from tkinter import messagebox


def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(END, task)
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


def edit_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        selected_task_index = int(selected_task_index[0])
        edited_task = task_entry.get()
        if edited_task:
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index, edited_task)
            task_entry.delete(0, END)
            btn_edit.config(state=DISABLED)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    else:
        messagebox.showwarning("Warning", "Please select a task to edit.")



def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")


def enable_edit_button(event):
    btn_edit.config(state=NORMAL)


root = Tk()
root.title("To-Do List")
label1 = Label(root, text="To-Do List", width=22, height=2, font=("arial", 15), bg="light Green")
label1.grid(row=0, column=0, columnspan=6)

task_entry = Entry(root, width=15)
task_entry.grid(row=2, column=0, columnspan=3)

btn_add = Button(root, text="Add Task", width=10, command=add_task)
btn_add.grid(row=2, column=3, columnspan=3)

listbox = Listbox(root, width=40, bg="light blue")
listbox.grid(row=3, column=0, columnspan=6)

btn_edit = Button(root, text="Edit Task", width=10, command=edit_task, state=DISABLED)
btn_edit.grid(row=4, column=0, columnspan=3)

btn_del = Button(root, text="Delete Task", width=10, command=delete_task)
btn_del.grid(row=4, column=3, columnspan=3)

listbox.bind("<<ListboxSelect>>", enable_edit_button)

btn_quit = Button(root, text="Quit", width=10, relief="sunken", bd=2.5)
btn_quit.grid(row=6, column=0, columnspan=6)
btn_quit.bind('<Double-1>', quit)


root.mainloop()

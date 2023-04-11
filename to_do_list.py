from  tkinter import *
import ttkbootstrap as ttk
from tkinter import messagebox


#button functions
do_list = []
def add(todo_text):
    if(todo_text == ""):
        print("please enter text")
    else:
        do_list.append(todo_text)
        entry_box.delete(0, END)
        for i in range(len(do_list)):
            if i+1 ==len(do_list):
                list_box.insert(END, do_list[i])

def done():
    if list_box.curselection():
        current_task = list_box.get(ANCHOR)
        if current_task in do_list:
            do_list.remove(current_task)
            list_box.delete(ANCHOR)
    else:
        return print("Select a Task")   

def info():
    messagebox.showinfo("ToDo List", "This ToDo List App v1.0\nCreated by Tunao2den\nPython Project", icon="info")

#main window
main_window = ttk.Window(themename="darkly")
main_window.title("To Do List")
main_window.resizable(0,0)

#label
typetask_label = Label(text="Type a task!", font="calibri 20 bold")    
todo_label = Label(text="To Do List", font="calibri 20 bold")

typetask_label.grid(row=0,column=0)
todo_label.grid(row=3,column=0)

#listbox
entry_box = Entry(master=main_window, width=35, font = ("Bold"))    
list_box = Listbox(master=main_window, width=35, height=10 , font = ("Bold"))

entry_box.grid(row=1,column=0)
list_box.grid(row=4,column=0)

#button
add_button = Button(master=main_window, text="Add", width = 15, font="bold", command = lambda: add(entry_box.get()))
done_button = Button(master=main_window, text="Done",width=15,font="bold", command=done)
info_button = Button(master=main_window, text="Info",width=15, font="bold", command=info)

add_button.grid(row=2,column=0)
done_button.grid(row=5,column=0)
info_button.grid(row=6,column=0)

#run
main_window.mainloop()
from tkinter import *
from backend import Database

db=Database()

def view_command():
    list1.delete(0, END)
    for row in Database.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in  Database.search(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get()):
        list1.insert(END,row)

def add_command():
    Database.insert(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get())
    list1.delete(0,END)
    list1.insert(END,(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get()))

def get_selected_row(event):
    global selected_row
    index=list1.curselection()[0]
    selected_row=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_row[1])

    e2.delete(0, END)
    e2.insert(END, selected_row[2])

    e3.delete(0, END)
    e3.insert(END, selected_row[3])

    e4.delete(0, END)
    e4.insert(END, selected_row[4])


def delete_command():
    id=selected_row[0]
    Database.delete(id)

def update_command():
    Database.update(selected_row[0],e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get())


window=Tk()

window.wm_title('BookStore')
l1=Label(window,text='Title')
l1.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

l2=Label(window,text='Author')
l2.grid(row=0,column=2)

e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=0,column=3)

l3=Label(window,text='Year')
l3.grid(row=1,column=0)

e3_value=StringVar()
e3=Entry(window,textvariable=e3_value)
e3.grid(row=1,column=1)

l4=Label(window,text='ISBN')
l4.grid(row=1,column=2)

e4_value=StringVar()
e4=Entry(window,textvariable=e4_value)
e4.grid(row=1,column=3)

list1=Listbox(window,height=10,width=30)
list1.grid(row=2,column=0,rowspan=10,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=10)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1=Button(window,text='View all',width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text='Search',width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text='Delete Selected',width=12,command=delete_command)
b3.grid(row=4,column=3)

b4=Button(window,text='Add Entry',width=12,command=add_command)
b4.grid(row=5,column=3)

b5=Button(window,text='Update Selected',width=12,command=update_command)
b5.grid(row=6,column=3)

b6=Button(window,text='Close',width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
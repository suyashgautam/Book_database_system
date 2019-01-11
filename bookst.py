
from tkinter import *
import sqlite3
import backend

def get_selected_index(event):
    global selected_index
    index=t1.curselection()[0]
    selected_index=t1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_index[1])
    e2.delete(0,END)
    e2.insert(END,selected_index[2])
    e3.delete(0,END)
    e3.insert(END,selected_index[3])
    e4.delete(0,END)
    e4.insert(END,selected_index[4])

def delete_command():
    backend.deleteselected(selected_index[0])

def view_command():
    t1.delete(0,END)
    for row in backend.viewall():
        t1.insert(END,row)

def search_command():
    t1.delete(0,END)
    for row in backend.search_entry(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        t1.insert(END,row)

def add_command():
    backend.add_entry(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    t1.delete(0,END)
    t1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def update_command():
    backend.updateselected(selected_index[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())



window=Tk()

window.wm_title("Book Database")

title_text=StringVar()
author_text=StringVar()
year_text=StringVar()
isbn_text=StringVar()


l1=Label(window,text="Title")
l1.grid(row=0,column=0)
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

t1=Listbox(window,height=6,width=35)
t1.grid(row=2,column=0,rowspan=6,columnspan=2)

sbi=Scrollbar(window)
sbi.grid(row=2,column=2,rowspan=6)

t1.configure(yscrollcommand=sbi.set)
sbi.configure(command=t1.yview)

t1.bind('<<ListboxSelect>>',get_selected_index)

b1=Button(window,text="View all",width=12,command=view_command)
b1.grid(row=2,column=3,columnspan=1)

b2=Button(window,text="Search entry",width=12,command=search_command)
b2.grid(row=3,column=3,columnspan=1)

b3=Button(window,text="Add entry",width=12,command=add_command)
b3.grid(row=4,column=3,columnspan=1)

b4=Button(window,text="Update",width=12,command=update_command)
b4.grid(row=5,column=3,columnspan=1)

b5=Button(window,text="Delete",width=12,command=delete_command)
b5.grid(row=6,column=3,columnspan=1)

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3,columnspan=1)

window.mainloop()

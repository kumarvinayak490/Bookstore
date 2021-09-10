from tkinter import *

window=Tk()
def miles_to_km():
    print(e1_value.get())
    kms=float(e1_value.get())*1.6
    t1.insert(END,kms)

b1=Button(window,text="Execute",command=miles_to_km)
b1.grid(row=0,column=0)
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)


window.mainloop()


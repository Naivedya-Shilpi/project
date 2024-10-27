from customtkinter import *
from tkinter import *

app = CTk()
app.geometry("500x400")
app.title("The Brewers")

count1=0
def cost1():
    global count1
    count1 += 70
    return count1

l=[]
l.append(count1)

count2 = 0
def cost2():
    global count2
    count2 += 150
    return count2

m=[]
m.append(count2)

Icon = PhotoImage(file="edited.png")
label = Label(app, relief=RAISED, bd=10, image = Icon)
label.place(x=0, y=0)

entry = CTkEntry(master=app, placeholder_text="What are you craving?...", width=250)
entry.pack()


Sw= PhotoImage(file="sandwich.png")
app.iconphoto(True, Sw)
Item1 = Label(app, relief=RAISED, bd=10, image=Sw)
Item1.place(x=120, y=350)
btn1= CTkButton(master=app, text="Add to cart", corner_radius=32, fg_color="#C850C0", hover_color="#4158D0",
                    border_color="#FFCC70", border_width=2, command=cost1)
btn1.place(x=120, y=510)

coffee = PhotoImage(file="coffee.png")
app.iconphoto(True, coffee)
Item2 = Label(app, relief=RAISED, bd=10, image=coffee)
Item2.place(x=500, y=350)
btn2= CTkButton(master=app, text="Add to cart", corner_radius=32, fg_color="#C850C0", hover_color="#4158D0",
                    border_color="#FFCC70", border_width=2, command=cost2)
btn2.place(x=460, y=508)


app.mainloop()

print(l)
print(m)
from tkinter import *

window = Tk()

window.geometry("420x420")
window.title("Bill")

Head = Label(window, text="BILL", font=("Arial", 40, "bold"))
Head.pack()

items_ordered = Label(window, text="Items ordered", font=("Arial", 20, "bold"))
items_ordered.place(x=120, y=120)

listbox = Listbox(window, bg="black", height=10, width=31)
listbox.place(x=120, y=158)

items_price = Label(window, text="Price", font=("Arial", 20, "bold"))
items_price.place(x=500, y=120)

price = Listbox(window, bg="black", height=10, width=31)
price.place(x=500, y=158)

window.mainloop()
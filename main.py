from tkinter import *
import requests
from tkinter import messagebox

root = Tk()
root.title("Currency Converter")
root.geometry('600x400')
root.config(bg='gray')


def convert():
    try:
        currency = box2.get(ACTIVE)
        # exchange stuff
        r = requests.get(' https://v6.exchangerate-api.com/v6/70ffe6a16e8d1feb0dcea85a/latest/'+currency)
        rj = r.json()
        x = rj['conversion_rates']['USD']
        mylist = rj['conversion_rates'].keys()

        selected = box.get(ACTIVE)
        value = round(rj['conversion_rates'][selected], 2)
        converted_amount = round(float(user.get())*value, 2)

        display_lbl['text'] = converted_amount
    except Exception as e:
        messagebox.showerror("error", "Enter a Number")


def clear():
    user.delete(0, END)


# exchange stuff
r = requests.get(' https://v6.exchangerate-api.com/v6/70ffe6a16e8d1feb0dcea85a/latest/USD')
rj = r.json()
x = rj['conversion_rates']['USD']
mylist = rj['conversion_rates'].keys()


# T stuff
box = Listbox(root, fg='green')
box2 = Listbox(root, fg='green')
for items in mylist:
    box.insert(END, items)
    box2.insert(END, items)
# buttons
btn = Button(root, text='convert', bg='green', command=convert)
clear_btn = Button(root, text='clear', bg='red', command=clear)
user = Entry(root)
display_lbl = Label(root)
slct_lbl1 = Label(root, text="Select a currency:")
slct_lbl2 = Label(root, text="Select a currency:")


# placements
box.place(x=410, y=40)
box2.place(x=20, y=40)
btn.place(x=265, y=100)
clear_btn.place(x=275, y=200)
user.place(x=220, y=150)
display_lbl.place(x=280, y=300)
slct_lbl1.place(x=20, y=5)
slct_lbl2.place(x=410, y=5)

root.mainloop()

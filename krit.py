from tkinter import *
from tkinter import ttk

root = Tk()
root.title("โปรแกรมแปลงสกุลเงิน")

# currencies conversion rates
EUR = 0.028
JPY = 3.91
USD = 0.030
GBP = 0.025

# input
money = DoubleVar()
Label(root, text="จำนวนเงิน(THB)", padx=10, font=30).grid(row=0, sticky=W)
et1 = Entry(root, font=30, width=30, textvariable=money)
et1.grid(row=0, column=1)

choice = StringVar(value="โปรดเลือกสกุลเงิน")
Label(root, text="เลือกสกุลเงิน", padx=10, font=30).grid(row=1, sticky=W)
Combo = ttk.Combobox(root, width=30, font=30, textvariable=choice)
Combo["values"] = ("EUR", "JPY", "USD", "GBP")
Combo.grid(row=1, column=1)

# output
Label(root, text="ผลการคำนวน", padx=10, font=30).grid(row=2, sticky=W)
et2 = Entry(root, font=30, width=30,)
et2.grid(row=2, column=1)


def calculate():
    amount = money.get()
    currency = choice.get()
    if currency == "EUR":
        et2.delete(0, END)
        result = round(amount * EUR, 2), "EUR(ยูโร)"
        et2.insert(0, result)
    elif currency == "JPY":
        et2.delete(0, END)
        result = round(amount * JPY, 2), "JPY(เยน)"
        et2.insert(0, result)
    elif currency == "USD":
        et2.delete(0, END)
        result = round(amount * USD, 2), "USD(ดอลล่า)"
        et2.insert(0, result)
    elif currency == "GBP":
        et2.delete(0, END)
        result = round(amount * GBP, 2), "GBP(ปอนด์)"
        et2.insert(0, result)
    else:
        et2.delete(0, END)
        result = "ไม่พบข้อมูล"
        et2.insert(0, result)


def clear():
    et1.delete(0, END)
    et2.delete(0, END)


Button(root, text="คำนวน", font=30, width=15, command=calculate).grid(row=3, column=1, sticky=W)
Button(root, text="ล้าง", font=30, width=15, command=clear).grid(row=3, column=1, sticky=E)

root.mainloop()

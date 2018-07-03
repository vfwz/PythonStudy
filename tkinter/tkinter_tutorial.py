import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


def click_me(btn, label):
    btn.configure(text='Clicked')
    btn.configure(state='disabled')
    label.configure(foreground='red')


def welcome(btn, label):
    btn.configure(text='Welcomed')
    # btn.configure(state='disabled')
    label.configure(text='Welcome, ' + name.get() + '!')
    label.configure(foreground='red')
    label.grid(column=1, row=3)
    print(multi_text.get("0.0", "end"))
    print("kkkk")


if __name__ == '__main__':
    jm = tk.Tk()
    jm.title("第一个图形界面")
    jm.resizable(True, True)

    row = 0
    first_label = ttk.Label(jm, text="First Label")
    first_label.grid(column=0, row=row)

    row += 1
    txt = ttk.Label(jm, text='Please Note The Label Color')
    txt.grid(column=0, row=row)

    click_btn = ttk.Button(jm, text='Click', command=lambda: click_me(btn=click_btn, label=txt))
    click_btn.grid(column=1, row=row)

    row += 1
    name = tk.StringVar()
    name_input = ttk.Entry(jm, width=12, textvariable=name)
    name_input.grid(column=0, row=row)

    welcome_label = ttk.Label(jm, text='')
    welcome_label.grid_forget()

    welcome_btn = ttk.Button(jm, text='Welcome', command=lambda: welcome(btn=welcome_btn, label=welcome_label))
    welcome_btn.grid(column=1, row=row)

    row += 1
    multi_text = tk.Text(jm, width=20, height=15)
    multi_text.grid(column=0, row=row)

    jm.mainloop()

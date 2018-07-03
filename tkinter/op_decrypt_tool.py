import tkinter as tk
from tkinter import ttk


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
    mframe = tk.Tk()
    mframe.title("开放支付解密工具")
    mframe.geometry('400x400+400+200')
    mframe.resizable(False, False)

    row = 0
    first_label = tk.Label(mframe, text="数据类型")
    first_label.grid(column=0, row=row, ipady="8")

    rframe = tk.Frame(mframe)
    rv = tk.IntVar()
    rv.set(1)
    tk.Radiobutton(rframe, variable=rv, text='Pin', value=1).pack(side=tk.LEFT)
    tk.Radiobutton(rframe, variable=rv, text='icData', value=2).pack(side=tk.LEFT)
    tk.Radiobutton(rframe, variable=rv, text='track2', value=3).pack(side=tk.LEFT)
    rframe.grid(column=1, row=row)

    row += 1
    txt = tk.Label(mframe, text='加密数据')
    txt.grid(column=0, row=row)

    encrypt_data = tk.StringVar()
    encrypt_data_text = tk.Text(mframe, width=20, height=6)
    encrypt_data_text.grid(column=1, row=row)

    welcome_label = ttk.Label(mframe, text='')
    welcome_label.grid_forget()

    click_btn = ttk.Button(mframe, text='Click', command=lambda: click_me(btn=click_btn, label=txt))
    click_btn.grid(column=1, row=row)

    row += 1
    name = tk.StringVar()
    name_input = ttk.Entry(mframe, width=12, textvariable=name)
    name_input.grid(column=0, row=row)

    welcome_label = ttk.Label(mframe, text='')
    welcome_label.grid_forget()

    welcome_btn = ttk.Button(mframe, text='Welcome', command=lambda: welcome(btn=welcome_btn, label=welcome_label))
    welcome_btn.grid(column=1, row=row)

    row += 1
    multi_text = tk.Text(mframe, width=20, height=15)
    multi_text.grid(column=0, row=row)

    mframe.mainloop()

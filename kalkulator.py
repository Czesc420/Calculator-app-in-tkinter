import tkinter as tk

def button_click(value):
    current = wys.get()
    wys.delete(0, tk.END)
    wys.insert(tk.END, current + str(value))

def button_del():
    wys.delete(0, tk.END)

def button_equal():
    try:
        result = eval(wys.get())
        wys.delete(0, tk.END)
        wys.insert(tk.END, result)
    except:
        wys.delete(0, tk.END)
        wys.insert(tk.END, "Error")

root = tk.Tk()
root.title("Kalkulator")

wys = tk.Entry(root, font=("Arial", 18), justify="right")
wys.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

padx, pady = 20, 10
sticky = "nsew"

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("/", 4, 2), ("=", 4, 3)
]

for (text, row, col) in buttons:
    if text == "=":
        cmd = button_equal
    elif text == "C":
        cmd = button_del
    else:
        cmd = lambda t=text: button_click(t)

    tk.Button(root, text=text, padx=padx, pady=pady, command=cmd)\
        .grid(row=row, column=col, sticky=sticky)

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()

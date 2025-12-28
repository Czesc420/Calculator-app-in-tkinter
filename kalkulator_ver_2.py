import tkinter as tk
class Calc:

    def __init__(self):
        #configuration
        self.root = tk.Tk()
        self.root.title("Kalkulator")
        self.wys = tk.Entry(self.root, font=("Arial", 18), justify="right")
        self.wys.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        self.buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
            ("C", 4, 0), ("0", 4, 1), ("/", 4, 2), ("=", 4, 3)
        ]

        self.padx, self.pady = 20, 10
        self.sticky = "nsew"

    def button_click(self,value):
        current = self.wys.get()
        self.wys.delete(0, tk.END)
        self.wys.insert(tk.END, current + str(value))

    def button_del(self):
        self.wys.delete(0, tk.END)

    def button_equal(self):
        try:
            result = eval(self.wys.get())
            self.wys.delete(0, tk.END)
            self.wys.insert(tk.END, result)
        except:
            self.wys.delete(0, tk.END)
            self.wys.insert(tk.END, "Error")


    def run(self):
        for (text, row, col) in self.buttons:
            if text == "=":
                cmd = self.button_equal
            elif text == "C":
                cmd = self.button_del
            else:
                cmd = lambda t=text: self.button_click(t)

            tk.Button(self.root, text=text, padx=self.padx, pady=self.pady, command=cmd) \
                .grid(row=row, column=col, sticky=self.sticky)

        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

        self.root.mainloop()

    @classmethod
    def run_calc(cls):
        calc = Calc()
        calc.run()
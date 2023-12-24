import tkinter as tk
from tkinter import font as tkf

# Counter Project

class Counter(tk.Tk):
    def __init__(self):
        super(Counter, self).__init__()
        self.title("Counter Project")
        self.font = tkf.Font(name='Arial', size=20, weight="bold")
        self.components()


    def components(self):
        self.btnPlus = tk.Button(command=self.increase, text="+", font=self.font, relief=tk.GROOVE, padx=20, pady=20)
        self.btnPlus.pack(side=tk.LEFT)

        self.label = tk.Label(text="0", font=self.font, padx=20, pady=20)
        self.label.pack(side=tk.LEFT)

        self.btnMinus = tk.Button(command=self.decrease, text="-", font=self.font, relief=tk.GROOVE, padx=20, pady=20)
        self.btnMinus.pack(side=tk.LEFT)

        self.reset = tk.Button(command=self.reset, text="Reset", font=self.font, relief=tk.GROOVE, padx=20, pady=20)
        self.reset.pack(side=tk.LEFT)

        self.entry = tk.Entry(font=self.font, relief=tk.GROOVE)
        self.entry.pack(side=tk.LEFT)

        self.btncustom = tk.Button(command=self.custom, text="Apply", font=self.font, relief=tk.GROOVE, padx=20, pady=20)
        self.btncustom.pack(side=tk.LEFT)

    def increase(self):
        num = int(self.label['text'])
        num += 1
        self.label.configure(text=num)

    def decrease(self):
        num = int(self.label['text'])
        if num > 0:  # Check if the number is greater than zero before decrementing
            num -= 1
            self.label.configure(text=num)

    def reset(self):
        self.label.configure(text="0")


    def custom(self):
        try:
            custom_value = int(self.entry.get())
            current_value = int(self.label['text'])
            result = current_value + custom_value
            if result >= 0:
                self.label.configure(text=str(result))
        except ValueError:
            pass

cnt = Counter()
cnt.mainloop()
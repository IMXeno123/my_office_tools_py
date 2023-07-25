import tkinter as tk
from tkinter import messagebox


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.createWidget()
        
    def createWidget(self):
        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()
        self.var1.set("admin")
        self.var2.set("123456")
        self.lb1 = tk.Label(self, text="User name")
        self.lb2 = tk.Label(self, text="Password")
        self.et1 = tk.Entry(self, textvariable=self.var1)
        self.et2 = tk.Entry(self, textvariable=self.var2, show="*")
        self.bt1 = tk.Button(self, text="login", command=self.login)
        self.bt1.config(anchor=tk.CENTER, width=5, height=1)
        
        self.lb1.pack()
        self.et1.pack()
        self.lb2.pack()
        self.et2.pack()
        self.bt1.pack()

    def login(self):
        if self.var2.get() == "131313" and self.var1.get() == "jjj":
            messagebox.showinfo(title="seccess", message="Welcome!")
        else:
            messagebox.showwarning(title="error", message="This is an user\'s info:\n"
                +f"User\'s name: {self.var1.get()}\nUser\'s password: {self.var2.get()}")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x150+500+500")
    app = App()
    app.mainloop()
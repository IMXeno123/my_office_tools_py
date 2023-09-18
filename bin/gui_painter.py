import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.createWidget()
       
    def createWidget(self):
        pass
    







if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x150+500+500")
    app = App()
    app.mainloop()
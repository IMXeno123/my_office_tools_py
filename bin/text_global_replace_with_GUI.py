import text_global_replace as tgr
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.text_box = None
        self.pack()
        self.createWidget()
       
    def createWidget(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("900x350+200+300")
    root.title("painter")
    app = App()
    app.mainloop()

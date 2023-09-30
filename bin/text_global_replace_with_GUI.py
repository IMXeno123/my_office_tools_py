import text_global_replace as tgr
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.text_box = None
        self.createWidget()

    def createWidget(self):
        bt_fileIn = tk.Button(root, text="File Path", name="path")
        bt_fileIn.config(width=10,height=1)
        textBox_fileIn = tk.Text(root, width=10, height=1)



        bt_fileIn.place(x=10, y=10)
        textBox_fileIn.place(x=100, y=10)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("900x350+200+300")
    root.title("Text Global Replace GUI")
    app = App(master=root)
    app.mainloop()

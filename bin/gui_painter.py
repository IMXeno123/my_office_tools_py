import tkinter as tk




class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.win_width = 900
        self.win_height = 280
        self.x = 0
        self.y = 0
        self.fgcolor = "#ff0000"
        self.bgcolor = "#ffffff"
        self.canvas_ = None
        self.bt_list = []
        self.bt_name = ["start", "pen", "rect", "clear", "eraser", "strline", "arrow", "color"]
        self.pack()
        self.createWidget()
       
    def createWidget(self):
        self.canvas_ = tk.Canvas(root, width=self.win_width, height=self.win_height, bg=self.bgcolor)
        self.canvas_.pack()
        for i in self.bt_name:
            bt = tk.Button(root, text=i, name=i)
            bt.pack(side="left", padx="10")
            bt.bind_class("Button","<1>",self.eventManager)
            self.bt_list.append(bt)
            
    def eventManager(self, event):
        # for a in self.bt_list:
        name = event.widget.winfo_name()
        if name == "strline":
            self.canvas_.bind("<B1-Motion>", self.drawStrLine)
            
        else:
            print(name)
            
    def drawStrLine(self, event):
        self.canvas_.create_line(self.x,self.y,event.x,event.y,fill=self.fgcolor)





if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("900x310+200+300")
    root.title("painter")
    app = App()
    app.mainloop()
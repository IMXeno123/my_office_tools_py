import tkinter as tk
from tkinter.colorchooser import askcolor
from turtle import width

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.text_box = None
        self.win_width = 900
        self.win_height = 280
        self.x = 0
        self.y = 0
        self.pen_size = 5
        self.eraser_size = 10
        self.fgcolor = "#ff0000"
        self.bgcolor = "#ffffff"
        self.canvas_ = None
        self.startStrLine = False
        self.lastStrLine = None
        self.bt_list = []
        self.bt_name = ["start", "pen", "rect", "oval", "clear", "eraser", "strline", "arrow", "color", "new size","exit"]
        self.pack()
        self.createWidget()
       
    def createWidget(self):
        self.canvas_ = tk.Canvas(root, width=self.win_width, height=self.win_height, bg=self.bgcolor)
        self.canvas_.bind("<ButtonRelease-1>", self.stopDraw)
        self.canvas_.pack()
        root.bind("<KeyPress-r>", self.shortcuts)
        # self.text_box.config(x=10,y=10)
        
        for i in self.bt_name:
            bt = tk.Button(root, text=i, name=i)
            bt.pack(side="left", padx="10")
            bt.bind_class("Button","<1>",self.eventManager)
            if i == "new size":
                self.text_box = tk.Text(root, width=2, height=1)
                self.text_box.pack(side="left", padx="10")
            self.bt_list.append(bt)
            
    def eventManager(self, event):
        # for a in self.bt_list:
        name = event.widget.winfo_name()
        if name == "strline":
            self.canvas_.bind("<B1-Motion>", self.drawStrLine)
            
        elif name == "arrow":
            self.canvas_.bind("<B1-Motion>", self.drawArrow)
            
        elif name == "rect":
            self.canvas_.bind("<B1-Motion>", self.drawRect)
            
        elif name == "oval":
            self.canvas_.bind("<B1-Motion>", self.drawOval)
            
        elif name == "pen":
            self.canvas_.bind("<B1-Motion>", self.drawCurve)
            
        elif name == "eraser":
            self.canvas_.bind("<B1-Motion>", self.eraser)
            
        elif name == "clear":
            self.canvas_.delete("all")
            
        elif name == "new size":
            self.getPenSize()
            
        elif name == "color":
            color_ = askcolor(color=self.fgcolor, title="change color")
            self.fgcolor = color_[1]
            
        elif name == "exit":
            exit()
            
        else:
            print(name)
            
    def startDraw(self, event):
        self.canvas_.delete(self.lastStrLine)
        if not self.startStrLine:
            self.startStrLine = True
            self.x = event.x
            self.y = event.y
        
    def drawStrLine(self, event):
        self.startDraw(event)
        self.lastStrLine = self.canvas_.create_line(self.x,self.y,event.x,event.y,fill=self.fgcolor,width=self.pen_size)
        
    def drawArrow(self, event):
        self.startDraw(event)
        self.lastStrLine = self.canvas_.create_line(self.x,self.y,event.x,event.y,fill=self.fgcolor,arrow="last",width=self.pen_size)
    
    def drawRect(self, event):
        self.startDraw(event)
        self.lastStrLine = self.canvas_.create_rectangle(self.x,self.y,event.x,event.y,outline=self.fgcolor,width=self.pen_size)
        
    def drawOval(self, event):
        self.startDraw(event)
        self.lastStrLine = self.canvas_.create_oval(self.x,self.y,event.x,event.y,outline=self.fgcolor)
        
    def drawCurve(self, event):
        self.startDraw(event)
        self.canvas_.create_line(self.x,self.y,event.x,event.y,fill=self.fgcolor,width=self.pen_size)
        self.x = event.x
        self.y = event.y

    def eraser(self, event):
        self.startDraw(event)
        self.canvas_.create_line(self.x,self.y,event.x,event.y,fill=self.bgcolor,width=self.eraser_size)
        self.x = event.x
        self.y = event.y

    def stopDraw(self, event):
        self.startStrLine = False
        self.lastStrLine = False

    def shortcuts(self, event):
        if event.char == "r":
            self.fgcolor = "#ff0000"
            
    def getPenSize(self):
        self.pen_size = int(self.text_box.get(1.0,"end"))



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("900x350+200+300")
    root.title("painter")
    app = App()
    app.mainloop()

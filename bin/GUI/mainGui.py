from pathlib import Path
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

PATH = Path(__file__).parent

class mainGui(ttk.Frame):
    
    def __init__(self, master):
        super().__init__(master, padding=(10))
        self.pack(fill=BOTH, expand=YES)
        self.style = ttk.Style()
        self.createWidget()
        
    def createWidget(self):
        

        self.left_frame = ttk.Frame(self)
        self.left_frame.pack(side=LEFT)
        self.right_frame = ttk.Frame(self)
        self.right_frame.pack(side=LEFT)
        self.leftFrame()
        self.rightFrame()
        
    def themeSelection(self):
        theme_names = self.style.theme_names()
        theme_selection = ttk.Frame(self.right_frame, padding=(10, 10, 10, 0))
        theme_selection.pack(fill=X, expand=YES)
        lbl = ttk.Label(theme_selection, text="Select a theme:")
        self.theme_cbo = ttk.Combobox(
            master=theme_selection,
            text=self.style.theme.name,
            values=theme_names,
        )
        self.theme_cbo.pack(padx=10, side=RIGHT)
        self.theme_cbo.current(theme_names.index(self.style.theme.name))
        lbl.pack(side=RIGHT)
        self.cbo = ttk.Combobox(
            self,
            text=self.style.theme.name,
            values=theme_names,
            exportselection=False
        )
        self.theme_cbo.bind('<<ComboboxSelected>>', self.change_theme)

    def change_theme(self, event):
            t = self.cbo.get()
            self.style.theme_use(t)
            self.theme_cbo.selection_clear()    

    def leftFrame(self):
        ttk.Label(self.left_frame, text="Path to walk: ").pack(anchor=N)
        ttk.Entry(self.left_frame, textvariable="")
        ttk.Button(self.left_frame, bootstyle="outline", text="text").pack()
        ttk.Separator(self.left_frame, orient="vertical").pack()

    def rightFrame(self):
        self.themeSelection()






















if __name__ == "__main__":
    app = ttk.Window(
        title = "Data Entry", 
        themename = "flatly", 
        size=(1000,600),
        resizable = (False, False)
        )
    mainGui(app)
    app.mainloop()

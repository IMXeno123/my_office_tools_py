import ttkbootstrap as ttk
from logs import *
from pathlib import Path
from ttkbootstrap.dialogs import Messagebox
from tkinter.filedialog import askdirectory
from ttkbootstrap.constants import *

env_path = Path(__file__).parent

class mainGui(ttk.Frame):
    
    def __init__(self, master):
        super().__init__(master, padding=(10))
        self.pack(fill=BOTH, expand=YES)
        self.style = ttk.Style()
        _path = Path().absolute().as_posix()
        self.path_var = ttk.StringVar(value=_path)
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
        self.theme_cbo.bind('<<ComboboxSelected>>', self.changeTheme)

    def changeTheme(self, event):
            t = self.cbo.get()
            self.style.theme_use(t)
            self.theme_cbo.selection_clear()    

    def leftFrame(self):
        ttk.Label(self.left_frame, text="Path to walk: ").pack(fill=X, anchor=N)
        self.createFormEntry(self.path_var)
        ttk.Label(self.left_frame, text="Search of contents: ").pack(fill=X, anchor=N)

    def rightFrame(self):
        ttk.Separator(self.left_frame, orient="vertical").pack()
        self.themeSelection()
        
    def createFormEntry(self, variable):
        container = ttk.Frame(self.left_frame)
        container.pack(fill=X, expand=YES, pady=5)
        ent = ttk.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)
        btn = ttk.Button(master=container, text="Browse", command=self.onBrowse)
        btn.pack(side=LEFT, padx=5)

    def onBrowse(self):
        path = askdirectory(title="Browse directory")
        if path:
            self.path_var.set(path)
            creat_log(f"[info] path: {self.path_var.get()}", env_path)
            




















if __name__ == "__main__":
    app = ttk.Window(
        title = "Data Entry", 
        themename = "flatly", 
        size=(1000,600),
        resizable = (False, False)
        )
    mainGui(app)
    app.mainloop()

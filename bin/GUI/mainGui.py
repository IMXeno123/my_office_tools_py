from pathlib import Path
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

PATH = Path(__file__).parent

class mainGui(ttk.Frame):
    
    def __init__(self, master):
        super().__init__(master, padding=(10))
        self.pack(fill=BOTH, expand=YES)
        btn = ttk.Button(self, text="test")
        btn.pack()
        print(PATH)

























if __name__ == "__main__":
    app = ttk.Window(
        title = "Data Entry", 
        themename = "flatly", 
        size=(1000,600),
        resizable = (False, False)
        )
    mainGui(app)
    app.mainloop()

from pathlib import Path
import ttkbootstrap as ttk


class mainGui(ttk.Frame):
    def __init__(self):
        pass


























if __name__ == "__main__":
    app = ttk.Window(
        title = "Data Entry", 
        themename = "flatly", 
        size=(1000,600),
        resizable = (False, False)
        )
    app.mainloop()

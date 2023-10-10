import ttkbootstrap as ttk
import json
import re
import os
from logs import *
from pathlib import Path
from ttkbootstrap.dialogs import Messagebox
from tkinter.filedialog import askdirectory
from ttkbootstrap.constants import *

env_path = Path(__file__).parent

class mainGui(ttk.Frame):
    
    def __init__(self, master):
        super().__init__(master, padding=(10))
        self.creat_settings()
        self.pack(fill=BOTH, expand=YES)
        self.style = ttk.Style()
        self.path_var = ttk.StringVar(value="")
        self.find_txt_var = ttk.StringVar(value="") # find
        self.repalce_txt_var = ttk.StringVar(value="") # replace
        _content = get_log(env_path)
        self.log_txt_var = ttk.StringVar(value=_content)
        self.createWidget()
        
    def createWidget(self):
        self.left_frame = ttk.Frame(self)
        self.left_frame.pack(side=LEFT)
        seprator_ = ttk.Separator(self, orient="vertical")
        seprator_.pack(side=LEFT, fill=Y, expand=YES, anchor=W, padx=5)
        self.mid_frame = ttk.Frame(self)
        self.mid_frame.pack(side=LEFT)
        self.right_frame = ttk.Frame(self)
        self.right_frame.pack(side=LEFT)
        self.leftFrame()
        self.rightFrame()
        
    def themeSelection(self):
        theme_names = self.style.theme_names()
        theme_selection = ttk.Frame(self.right_frame, padding=(10, 10, 10, 0))
        theme_selection.pack(fill=X, expand=YES, anchor=N)
        lbl = ttk.Label(theme_selection, text="Select a theme : ")
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
        ttk.Label(self.left_frame, text="Path to walk : ").pack(fill=X, anchor=N)
        self.createFormEntry(self.path_var)
        ttk.Label(self.left_frame, text="Find : ").pack(fill=X, anchor=N)
        find_txt = ttk.Text(
            master=self.left_frame,
            height=6,
            width=50,
            wrap='none'
            )
        find_txt.insert(END, self.find_txt_var.get())
        find_txt.pack(
            anchor=N,
            pady=5,
            padx=5,
            fill=BOTH,
            expand=YES
            )
        
        ttk.Label(self.left_frame, text="Replace : ").pack(fill=X, anchor=N)
        
        repalce_txt = ttk.Text(
            master=self.left_frame,
            height=8,
            width=50,
            wrap='none'
            )
        repalce_txt.insert(END, self.repalce_txt_var.get())
        repalce_txt.pack(
            anchor=N,
            pady=5,
            padx=5,
            fill=BOTH,
            expand=YES
            )
        
        btn_replace = ttk.Button(self.left_frame, 
                                 text="Replace", 
                                 command=lambda:self.subByDir(self.path_var.get(), 
                                                              self.find_txt_var.get(), 
                                                              self.repalce_txt_var.get()))
        btn_replace.pack(side=RIGHT, padx=5)

    def rightFrame(self):
        self.themeSelection()
        self.log_txt = ttk.Text(
            master=self.right_frame,
            width=60,
            wrap='word'
            )
        self.log_txt.insert(END, self.log_txt_var.get())
        self.log_txt.pack(
            side=LEFT,
            anchor=N,
            pady=5,
            padx=5,
            fill=BOTH,
            expand=YES
            )
        
    def createFormEntry(self, variable):
        container = ttk.Frame(self.left_frame)
        container.pack(fill=X, expand=YES, pady=5)
        ent = ttk.Entry(master=container, textvariable=variable, width=50)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)
        btn = ttk.Button(master=container, text="Browse", command=self.onBrowse)
        btn.pack(side=LEFT, padx=5)

    def onBrowse(self):
        path = askdirectory(title="Browse directory")
        if path:
            self.path_var.set(path)
            # log
            log_ = creat_log(f'[info] Set path: "{self.path_var.get()}"', env_path)
            self.log_txt.insert(END, log_)
       
    def subByDir(self, directory:str, old_text:str, new_text:str):
        """
        Need import re and os modules!
        Only support txt md.
        """
        try:       
            # sub context
            isMatch = 0
            counts = 0
            for root, dirs, files in os.walk(directory):
                for filename in files:
                    if filename.endswith(".md") or filename.endswith(".txt"):
                        filepath = os.path.join(root, filename)
                        with open(filepath, "r", encoding="utf-8") as f:
                            content = f.read()
                        if re.search(old_text, content, flags=re.M|re.S):
                            isMatch = 1
                            # log
                            log_ = creat_log(f"[info] \"{filepath}\"", directory)
                            self.log_txt.insert(END, log_)
                            counts += 1
                            content = re.sub(old_text, new_text, content, flags=re.M|re.S)
                            with open(filepath, "w", encoding="utf-8") as f:
                                f.write(content)
            if isMatch:
                # log
                log_ = creat_log(f"[info] 有{counts}個檔案替換成功!", directory)
                self.log_txt.insert(END, log_)
                isMatch = 0
            else:
                # log
                log_ = creat_log(f"[info] **未匹配到內容**", directory)
                self.log_txt.insert(END, log_)
                
        except Exception as error:
            # log
            log_ = creat_log(f"[error] 遇到錯誤：{error}", directory)
            self.log_txt.insert(END, log_)
            
    def creat_settings(self, path):
        if not Path(f"{env_path}/config/config.ini").exists():
            with open(f"{env_path}/config/config.ini", mode="a", encoding="UTF-8") as f:
                f.write(f"path_m={path}")
                
    def get_settings(self):
        

if __name__ == "__main__":
    app = ttk.Window(
        title = "Global Text Replace Tool v0.0.1", 
        themename = "flatly", 
        size=(800,405),
        resizable = (False, False)
        )
    mainGui(app)
    app.mainloop()

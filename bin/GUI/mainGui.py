from os import replace
import ttkbootstrap as ttk
from db import MySqlDatabases
from SubByDir import subByDir
from logs import *
from pathlib import Path
from ttkbootstrap.dialogs import Messagebox
from tkinter.filedialog import askdirectory
from ttkbootstrap.constants import *

env_path = Path(__file__).parent
db = MySqlDatabases(env_path)

class mainGui(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master, padding=(10))
        image_files = {
            "help_icon":"help_icon_16px.png",
            }
        self.photoimages = []
        imgpath = Path(__file__).parent / 'assets'
        for key, val in image_files.items():
            path_1 = imgpath / val
            self.photoimages.append(ttk.PhotoImage(name=key, file=path_1))
        db.creat_settings()
        self.all_settings = db.all_data()
        path_2 = self.all_settings[0]["path"]
        self.pack(fill=BOTH, expand=YES)
        self.style = ttk.Style()
        self.path_var = ttk.StringVar(value=path_2)
        self.find_txt_var = ttk.StringVar(value="") # find
        self.repalce_txt_var = ttk.StringVar(value="") # replace
        _content = ""
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
        theme_selection = ttk.Frame(self.right_frame, padding=(10, 10, 0, 0))
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
        find_frame = ttk.Frame(self.left_frame)
        find_frame.pack(fill=X, anchor=N)
        ttk.Label(find_frame, text="Find : ").pack(side=LEFT, anchor=W)
        ttk.Button(find_frame, image="help_icon", bootstyle=LINK, command=self.createHelpMessage).pack(side=RIGHT, anchor=E, padx=5)
        self.find_txt = ttk.Text(
            master=self.left_frame,
            height=6,
            width=50,
            wrap='none'
            )
        self.find_txt.insert(END, self.find_txt_var.get())
        self.find_txt.pack(
            anchor=N,
            pady=5,
            padx=5,
            fill=BOTH,
            expand=YES
            )
        
        ttk.Label(self.left_frame, text="Replace : ").pack(fill=X, anchor=N)
        
        self.repalce_txt = ttk.Text(
            master=self.left_frame,
            height=8,
            width=50,
            wrap="char"
            )
        self.repalce_txt.insert(END, self.repalce_txt_var.get())
        self.repalce_txt.pack(
            anchor=N,
            pady=5,
            padx=5,
            fill=BOTH,
            expand=YES
            )
        # replaced content
        btn_replace = ttk.Button(
            self.left_frame, 
            text="Replace", 
            command=self.replace_text)
        btn_replace.pack(side=RIGHT, padx=5)

    def rightFrame(self):
        self.themeSelection()
        ttk.Label(self.right_frame, text="Logs in here: ").pack(fill=X, anchor=N)
        self.log_txt = ttk.Text(
            master=self.right_frame,
            width=60,
            wrap="char"
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
    
    def replace_text(self):
        # print(self.find_txt.get(1.0,END))
        # print(self.repalce_txt.get(1.0,END))
        # print(self.path_var.get())
        ot = self.find_txt.get(1.0,END)[:-1]
        ot = ot.replace("\n", "\\n")
        nt = self.repalce_txt.get(1.0,END)[:-1]
        # print(ot)
        # print(nt)
        # return None
        bool_ = subByDir(
                old_text=ot,
                new_text=nt,
                path=self.path_var.get(),
                log_path=env_path
            )
        if bool_:
            self.loger_(f'[info] 替換成功!', env_path)
        else:
            self.loger_(f'[info] 未找到可替換的內容!', env_path)
            
        return bool_
    
    def createFormEntry(self, variable):
        container = ttk.Frame(self.left_frame)
        container.pack(fill=X, expand=YES, pady=5)
        ent = ttk.Entry(master=container, textvariable=variable, width=50)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)
        btn = ttk.Button(master=container, text="Browse", command=self.onBrowse)
        btn.pack(side=LEFT, padx=5)
        
    def createHelpMessage(self):
        Messagebox.ok(title="使用提示", 
                      alert=True,
                      message="""Tip: 
支持正則表達式搜尋喔 :)
正則表達式的開頭可以加(?sm)等, 以修改匹配行為!
注意：因為是正則模式，所以有特殊符號記得要用"\"轉譯!
                      """)

    def onBrowse(self):
        path = askdirectory(title="Browse directory")
        if path:
            self.path_var.set(path)
            db.change_settings(self.all_settings, path, 0, "path")
            # log
            self.loger_(f'[info] Set path: "{self.path_var.get()}"', env_path)
       
    def loger_(self, log, path:str|bool=False):
        if not path:
            path = env_path
        log_ = creat_log(log, path)
        self.log_txt.insert(END, log_)
            

if __name__ == "__main__":
    app = ttk.Window(
        title = "Global Text Replace Tool v0.0.1", 
        themename = "darkly", 
        position=(200,200),
        size=(800,430),
        resizable = (False, False)
        )
    mainGui(app)
    app.iconbitmap(f"{env_path}/assets/dora.ico")
    app.mainloop()

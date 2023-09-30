import tkinter as tk

def menu_add_command_1(master, label_:str):
    if label_ == "Exit":
        master.add_command(label=label_, command=root.quit)
    else:
        master.add_command(label=label_)
def menu_add_command(master, label_):
    master.add_command(label=label_)
    
root = tk.Tk()
root.title("Notepad")
root.geometry("800x500+100+100")

# main menu
menu = tk.Menu(root, tearoff=False)

# file
file_menu = tk.Menu(menu, tearoff=False)
for i in ["New", "Open", "Save", "Exit"]:
    menu_add_command_1(file_menu, i)
    if i == "Save":
        t_menu = tk.Menu(file_menu, tearoff=False)
        for j in ["Save as .txt","Save as .md", "Save as .*"]:
            menu_add_command(t_menu, j)
        file_menu.add_cascade(label="Save as", menu=t_menu)

menu.add_cascade(label="Files", menu=file_menu)

# edit
edit_menu = tk.Menu(menu, tearoff=False)
for i in ["Undo", "Redo", "Copy", "Paste", "Cut"]:
    menu_add_command(edit_menu, i)
    if i == "Redo":
        edit_menu.add_separator()
        
menu.add_cascade(label="Edit", menu=edit_menu)

# about
about_menu = tk.Menu(menu, tearoff=False)
for i in ["About me", "About software", "License"]:
    menu_add_command(about_menu, i)
    if i == "About software":
        about_menu.add_separator()

menu.add_cascade(label="About", menu=about_menu)

# status_label
status_str_var = tk.StringVar()
status_str_var.set("Strings: {}".format(0))
status_label = tk.Label(root, textvariable=status_str_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_label.pack(side=tk.BOTTOM, fill=tk.X)

line_var = tk.StringVar()
line_label = tk.Label(root, textvariable=line_var, width=2, bg="#faebd7", anchor=tk.N, font=18)
line_label.pack(side=tk.LEFT, fill=tk.Y)

# text_pad
text_pad = tk.Text(root, font=18)
text_pad.pack(fill=tk.BOTH, expand=True)

# scroller
scroller = tk.Scrollbar(text_pad)
scroller.pack(side=tk.RIGHT, fill=tk.Y)
text_pad.config(yscrollcommand=scroller.set)
scroller.config(command=text_pad.yview)




root.config(menu=menu)
root.mainloop()
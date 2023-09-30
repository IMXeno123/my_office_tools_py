import tkinter as tk
from tkinter import messagebox
from random import random


def on_exit():
    messagebox.showwarning(title="Tips", message="How dare you!!!!")

def move(event):
    bt_no.place(relx=random(), rely=random(), anchor=tk.CENTER)

def fine():
    frame1.pack_forget()
    frame2.pack(fill="both", expand=True)


root = tk.Tk()
root.geometry("500x300+100+100")
root.title("TEST")
# frame 1
frame1 = tk.Frame(root)
frame1.pack(fill="both", expand=True)

lb1 = tk.Label(frame1, text="Hi guys what's up!", font=("Arial", 10), padx=10, pady=10)
lb1.pack(side=tk.LEFT, anchor=tk.N)

img1 = tk.PhotoImage(file="./Untitled.png")
lb2 = tk.Label(frame1, image=img1, bd=0)
lb2.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=40)

lb3 = tk.Label(frame1, text="fork you!", font=("Arial", 10), padx=10)
lb3.pack(side=tk.BOTTOM, anchor=tk.SE)

bt_yes = tk.Button(frame1, text="YES!!!", name="yes", width=10, bd=1)
bt_no = tk.Button(frame1, text="Noooo", name="no", width=10, bd=1)
bt_yes.place(relx=0.3, rely=0.8, anchor=tk.CENTER)
bt_no.place(relx=0.7, rely=0.8, anchor=tk.CENTER)
bt_no.bind("<Enter>", move)
bt_yes.config(command=fine)

# frame 2

frame2 = tk.Frame(root)

lb4 = tk.Label(frame2, text="heyyayayayayayaheyayayayaya\nAnd I say hey!\nWhat's going on!", 
               font=("Arial", 10), padx=10, pady=10, fg="red",
               justify=tk.LEFT, bg="green")
lb4.pack(anchor=tk.CENTER, pady=80)

bt_exit = tk.Button(frame2, text="Exit", name="exit", width=10, command=root.quit)
bt_exit.pack(side=tk.BOTTOM, anchor=tk.NE, pady=10, padx=10)


root.protocol("WM_DELETE_WINDOW", on_exit)
root.mainloop()
import tkinter as tk

root = tk.Tk()
root.geometry("500x300+100+100")
root.title("TEST")

frame1 = tk.Frame(root)
frame1.pack(fill="both", expand=True)

lb1 = tk.Label(frame1, text="Hi guys what's up!", font=("Arial", 10), bg="#FF0000")
lb1.pack(side=tk.TOP, fill=tk.X)

img1 = tk.PhotoImage(file="E:/Documents/My project/Repos/IMXeno123/my_office_tools_py/bin/Untitled.png")
lb2 = tk.Label(frame1, image=img1, bd=0)
lb2.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

lb3 = tk.Label(frame1, text="fork you!", font=("Arial", 10), bg="#FF0000")
lb3.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()

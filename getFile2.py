import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

from tkfilebrowser import askopendirname, askopenfilenames, asksaveasfilename

root = tk.Tk()


style = ttk.Style(root)
style.theme_use("clam")

def c_open_file_old():
    rep = filedialog.askopenfilenames(parent=root,initialdir='/',initialfile='tmp',filetypes=[("PNG", "*.png"),("JPEG", "*.jpg"),("All files", "*")])
    #f = open(rep, "rt")
    #print(f.readline())
    st=str(rep)
    splitter=st.split("/")
    file_name=splitter[len(splitter)-1]
    file_name=file_name.split("'")
    file_name=file_name[0]
    f=open(file_name,"rt")
    for x in f:
        print(x[0])

ttk.Label(root, text='Default dialogs').grid(row=0, column=0,padx=4, pady=4,sticky='ew')
ttk.Label(root, text='tkfilebrowser dialogs').grid(row=0, column=1,padx=4, pady=4,sticky='ew')
ttk.Button(root, text="Open files", command=c_open_file_old).grid(row=1, column=0,padx=4, pady=4,sticky='ew')

root.mainloop()
import tkinter as tk
from tkinter import ttk
import webbrowser

def openYoutube():
    webbrowser.open("https://youtube.com/@aidexe.mp4")

root = tk.Tk()
root.title("SimpleComputeTools")

links = ttk.Frame(root)
links.pack()

ytLink = ttk.Label(links)
ytLink.configure(text="Youtube")
ytLink.configure(foreground="#0000ff")
ytLink.configure(cursor="hand")
ytLink.grid(row=0, column=0)
ytLink.bind("<Button-1>", openYoutube)

root.mainloop()

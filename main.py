import tkinter as tk
from tkinter import ttk
import webbrowser
from QrCodeGenerator import openQrCodeGenerator

def openYoutube():
    webbrowser.open("https://youtube.com/@aidexe.mp4")

def openGitHub():
    webbrowser.open("https://github.com/bzeizinger")

root = tk.Tk()
root.title("SimpleComputeTools")
root.geometry("500x250")

tools = ttk.Frame(root)
tools.pack()

qrCodeGenerator = ttk.Button(tools)
qrCodeGenerator.configure(text="QR Code generator")
qrCodeGenerator.configure(command=openQrCodeGenerator)
qrCodeGenerator.grid(row=0, column=0)

links = ttk.Frame(root)
links.pack()

ytLink = ttk.Label(links)
ytLink.configure(text="Youtube ")
ytLink.configure(foreground="#0000ff")
ytLink.configure(cursor="hand")
ytLink.grid(row=0, column=0)
ytLink.bind("<Button-1>", openYoutube)

ghLink = ttk.Label(links)
ghLink.configure(text=" GitHub")
ghLink.configure(foreground="#0000ff")
ghLink.configure(cursor="hand")
ghLink.grid(row=0, column=1)
ghLink.bind("<Button-1>", openGitHub)

root.mainloop()

import tkinter as tk
from tkinter import ttk
import qrcode

def openQrCodeGenerator():
    qrCodeGeneratorWindow = tk.Tk()
    qrCodeGeneratorWindow.title("QR Code generator")
    qrCodeGeneratorWindow.geometry("500x250")

    contentEntry = ttk.Entry(qrCodeGeneratorWindow)
    contentEntry.configure(width=100)
    contentEntry.pack()
    contentEntry.insert(0, "Your content!")

    qrCodeGeneratorWindow.mainloop()
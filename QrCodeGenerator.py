import tkinter as tk
from tkinter import ttk
import qrcode
from PIL import Image, ImageTk

def openQrCodeGenerator():
    qrCodeGeneratorWindow = tk.Tk()
    qrCodeGeneratorWindow.title("QR Code generator")
    qrCodeGeneratorWindow.geometry("500x250")

    directions = ttk.Label(qrCodeGeneratorWindow)
    directions.configure(text="Enter the content here:")
    directions.pack()

    contentEntry = ttk.Entry(qrCodeGeneratorWindow)
    contentEntry.configure(width=100)
    contentEntry.pack()

    def createQrCode():
        qrcodeData = contentEntry.get()

        if qrcodeData:
            qrcode.make(qrcodeData)
            qrcode.save("qrcode.png")

            image = Image.open("qrcode.png")
            photo = ImageTk.PhotoImage(image)

            displayQrcode = ttk.Label(qrCodeGeneratorWindow)
            displayQrcode.configure(image=photo)

            contentEntry.delete(0, tk.END)

    createQrcodeButton = ttk.Button(qrCodeGeneratorWindow)
    createQrcodeButton.configure(text="Create QR Code")
    createQrcodeButton.configure(command=createQrCode)
    createQrcodeButton.pack()

    qrCodeGeneratorWindow.mainloop()

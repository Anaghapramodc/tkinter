from tkinter import *
import qrcode
from PIL import Image, ImageTk
class QRCode:
    def __init__(self,master):
        self.master=master
        master.title("QR code generat")
        self.label=Label(master,text="Enter text or URL")
        self.label.pack()
        self.entry=Entry(master)
        self.entry.pack()
        self.btn=Button(master,text="Generate QR code",command=self.generator)
        self.btn.pack()
        self.qrcode_label=Label(master)
        self.qrcode_label.pack()
    def generator(self):
        text=self.entry.get()
        if text:
            qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,)
            qr.add_data(text)
            qr.make(fit=True)
            img=qr.make_image(fill_color="black",back_color="white")
            img=ImageTk.PhotoImage(img)
            self.qrcode_label.configure(image=img)
            self.qrcode_label.image=img
        else:
            self.qrcode_label.configure(image=None)
            self.qrcode_label.image =None

root = Tk()
app=QRCode(root)
root.mainloop()

from tkinter import *
import qrcode
from PIL import Image, ImageTk

class QRCodeGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("QR Code Generator")

        self.label = Label(master, text="Enter text or URL:")
        self.label.pack()

        self.entry = Entry(master)
        self.entry.pack()

        self.generate_button = Button(master, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack()

        self.qr_code_label = Label(master)
        self.qr_code_label.pack()

    def generate_qr_code(self):
        text = self.entry.get()
        if text:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            # Convert PIL Image to Tkinter PhotoImage
            img = ImageTk.PhotoImage(img)

            # Update the label with the QR code image
            self.qr_code_label.configure(image=img)
            self.qr_code_label.image = img
        else:
            self.qr_code_label.configure(image=None)
            self.qr_code_label.image = None

root =Tk()
app = QRCodeGeneratorApp(root)
root.mainloop()

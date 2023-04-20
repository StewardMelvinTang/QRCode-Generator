import pyqrcode
from pyqrcode import QRCode
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk

TITLE_FONT_STYLE = ("Arial", 22, "bold")
DEF_FONT_STYLE = ("Arial", 12)

def setScreensize(window, res):
    window.geometry(res)
    window.resizable(False,False)
    #split the resolution string from "500x500" to ["500", "500"]
    split_res = res.split("x")
    #set to center of screen
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_pos = int(screen_width / 2 - int(split_res[0]) / 2)
    y_pos = int(screen_height / 2 - int(split_res[1]) / 2)
    window.geometry("+{}+{}".format(x_pos, y_pos))

def generateQRCode(url):
    if len(url.get()) <= 0:
        messagebox.showerror(title="Error", message="Please input a valid URL")
    else:
        url = url.get()
        qr = pyqrcode.create(url)
        file_path = filedialog.asksaveasfilename(initialfile = "qr_code",defaultextension=".png",
                                                filetypes=(("Image files", "*.png"), ("All files", "*.*")))
        qr.png(file_path, scale=20)
        qr.show()
        
        if qr:
            qr_canvas = Canvas(window, width=200, height=200)
            qr_canvas.pack()
            
            qr_image = ImageTk.PhotoImage(qr.make_image(fill_color="black", back_color="white"))
            qr_canvas.create_image(100, 100, image=qr_image)
        

window = Tk()
window.title("QR Code Generator")
setScreensize(window, "400x250")

frame = Frame(window)
frame.pack(expand=False, fill="both")

title_label = Label(frame, text="QR Code Generator", font=TITLE_FONT_STYLE, fg="black")
title_label.pack(pady=(25,0))

url_label = Label(frame, text="Input URL Here:", font=("Arial", 10))
url_label.pack(side=LEFT, padx=(10,0), pady=(10,0))

URL_ENTRY = StringVar()
url_entry = Entry(frame, font=DEF_FONT_STYLE, textvariable=URL_ENTRY)
url_entry.pack(side=LEFT, padx=(10,20), pady=(12,0), fill="x", expand=True)

btn_generate = ttk.Button(window, text="Generate", padding=(35,10,35,10), command=lambda url=URL_ENTRY:generateQRCode(url))
btn_generate.pack(pady=(20,0))

window.mainloop()
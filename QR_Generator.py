import qrcode
from tkinter import *
from tkinter import filedialog
import os

def get_code():
    data_var = data.get()
    qr = qrcode.make(str(data_var))
    save_directory = filedialog.askdirectory()
    if not save_directory:
        return
    os.chdir(save_directory)
    save_as = name_to_save.get()
    if not save_as:
        save_as = "qr_code"
    qr.save(f"{save_as}.png")
    label_done = Label(base, text="Done", bg="red")
    label_done.place(x=80, y=150)

def main():
    print("------------------Ceated By Mahesh Pawar-----------------")
    
    global base, data, name_to_save
    base = Tk()
    base.geometry("400x200")
    base.title("QR Code Generator")
    data = StringVar()
    name_to_save = StringVar()
    Label(base, text="SAVE AS").place(x=80, y=10)
    Entry(base, textvariable=name_to_save, width=30).place(x=80, y=30)
    Label(base, text="INSIDE QRCODE").place(x=80, y=50)
    Entry(base, textvariable=data, width=30).place(x=80, y=70)
    Button(base, text="Get Code", command=get_code, width=30, height=2, bg="grey").place(x=80, y=100)
    base.mainloop()

if __name__ == "__main__":
    main()

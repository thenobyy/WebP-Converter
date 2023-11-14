import subprocess, tkinter, os
from tkinter import filedialog
from tkinter import *
import shutil

##Try to copy cwebp-Files to System

#if not os.path.exists(os.getenv('ProgramFiles')+"\cwebp\cwebp.exe"):
#    shutil.copytree("cwebp", os.getenv('ProgramFiles')+"\cwebp")
#    print("Installation failed")
#    os.system("pause")
#    exit()
    
def ende():
    fenster.destroy()

def checkData():
    pfad = entEingabe.get()
    pfad = pfad.strip()
    if not os.path.exists(pfad):
        lbAusgabe["text"] = "This file does not exist"

    else:
        output = '"'+pfad+'"'
        pfad = '"'+pfad+'"'
        print(pfad)
        if pfad.find(".jpg") > 0:
            output = output.replace(".jpg",".webp")
            convert(pfad,output)
        elif pfad.find(".jpeg") > 0:
            output = output.replace(".jpeg",".webp")
            convert(pfad,output)
        elif pfad.find(".png") > 0:
            output = output.replace(".png",".webp")
            convert(pfad,output)
        else:
            lbAusgabe["text"] = "Invalid file format (allowed formats: jpg,jpeg,png)"
            
        
def convert(p,o):
    try:
        subprocess.call(f"cwebp -quiet {p} -o {o}" ,shell=False)
        lbAusgabe["text"] = "Conversion successful"
    except:
        lbAusgabe["text"] = "An error has occurred"

def openFile():
    entEingabe.delete(0,"end")
    filename =  filedialog.askopenfilename(title = "Choose a file",filetypes = (("jpeg,png,jpg",["*.jpeg","*.png","*.jpg"]),("all files","*.*")))
    entEingabe.insert(0, filename)
    
fenster = tkinter.Tk()
fenster.title("WebP - Converter")
fenster.iconbitmap('icon.ico')

window_width = 450
window_height = 350

# get the screen dimension
screen_width = fenster.winfo_screenwidth()
screen_height = fenster.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

fenster.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
fenster.resizable(0, 0)


imBrand = tkinter.PhotoImage(file="logo.png")
lbBrand = tkinter.Label(fenster)
lbBrand["image"] = imBrand
lbBrand.grid(row=0, column=1, padx= 10, pady = 10)

lbEingabe = tkinter.Label(fenster, text="Choose a file to convert", font=('Helvetica', 16))
lbEingabe.grid(row=1,column=0, columnspan=2, padx=10, pady = 10)


entEingabe = tkinter.Entry(fenster)
entEingabe.grid(row=2,column=0,sticky="w", padx= 10, pady = 20 ,ipadx=40 ,ipady=5)

buFile = tkinter.Button(fenster, text="Datei auswählen", command=openFile, width= 20)
buFile.grid(row=2, column=1,padx=50, pady=50)

lbAusgabe = tkinter.Label(fenster, text="", fg = "red")
lbAusgabe.grid(row=3,column=0, sticky="w", padx= 10, pady = 10)

buConv = tkinter.Button(fenster, text="Konvertieren", command=checkData, width= 10)
buConv.grid(row=4, column=0,padx=0, pady=0)

buEnde = tkinter.Button(fenster, text="Ende", command=ende, width= 10)
buEnde.grid(row=4, column=1,padx=10, pady=10)



fenster.mainloop()


#setx variable_name variable_value

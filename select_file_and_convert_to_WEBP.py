from tkinter import *
from tkinter import filedialog
from PIL import Image

def conversie(fisier, ext):
    nume = fisier.split(ext)
    if len(nume) == 2:
        img = nume[0]+ext
        image = Image.open(img)
        image = image.convert('RGB')
        img_webp = nume[0]+'.webp'
        image.save(img_webp, 'webp')

def browseFiles():
    global Selectie_fisiere
    Selectie_fisiere = filedialog.askopenfilenames(initialdir = "/",title = "Selecte a file")

def convertWebP():
    for fisier in Selectie_fisiere:
        if fisier.find(".jpg"):
            conversie(fisier, '.jpg')
            label_file_explorer.configure(text = "File converted: " + fisier + " to webP")
        if fisier.find(".jpeg"):
            conversie(fisier, '.jpeg')
            label_file_explorer.configure(text = "File converted: " + fisier + " to webP")
        if fisier.find(".png"):
            conversie(fisier, '.png')
            label_file_explorer.configure(text = "File converted: " + fisier + " to webP")
        
window = Tk()
window.title('File Convertor to WebP')
window.geometry("500x200")
window.config(background = "white")
label_file_explorer = Label(window, text = "Convert to WEBP", width = 50, height = 4, fg ="blue")
button_explore = Button(window, text = "Browse Files", command = browseFiles)
button_convert = Button(window, text = "Convert to WEBP", command = convertWebP)
button_exit = Button(window, text = "Exit", command = exit)
label_file_explorer.grid(column = 1, row = 1)
button_explore.place(x = 395, y = 110)
button_convert.place(x = 370, y = 140)
button_exit.place(x = 441, y = 170)
window.mainloop()

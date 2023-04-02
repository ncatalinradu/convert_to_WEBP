from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps
import PIL, tkinter

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
    Selectie_fisiere = filedialog.askopenfilenames(initialdir = "C:\python\Scripts\webp",title = "Selecte a file")
    for fisier in Selectie_fisiere:
        img = Image.open(fisier)
        img = img.resize((250,int(float(img.size[1])*250/float(img.size[0]))))
        test = ImageTk.PhotoImage(img)
        label1 = tkinter.Label(image=test, borderwidth = 1, relief = "solid")
        label1.image = test
        label1.place(x=1,y=10)

def convertWebP():
    for fisier in Selectie_fisiere:
        if fisier.find(".jpg"):
            conversie(fisier, '.jpg')
#            label_file_explorer.configure(text = "File converted: " + fisier + " to webP")
        if fisier.find(".jpeg"):
            conversie(fisier, '.jpeg')
#            label_file_explorer.configure(text = "File converted: " + fisier + " to webP")
        if fisier.find(".png"):
            conversie(fisier, '.png')
#            label_file_explorer.configure(text = "File converted: " + fisier + " to webP")

def resize(x,y):
    for fisier in Selectie_fisiere:
        print(fisier)
        nume = fisier.split('.')[0]
        print(nume)
        img = Image.open(fisier)
        width, height = img.size
        ratioW = width/x
        ratioH = height/y
        if ratioW >= ratioH :
            new_width = int(width/ratioH)
            crop_stg = int((new_width - x)/2)
            print('ajunstari pe W: ',crop_stg)
            new_img = img.resize((new_width,y))
            crop_img = new_img.crop((crop_stg,0,x+crop_stg,y))
            name_jpg = nume + str(x) + 'x' + str(y) +'.jpg'
            name_webp = nume + str(x) + 'x' + str(y) +'.webp'
            crop_img.save(name_webp, 'webp')
            jpg = crop_img.convert('RGB')
            jpg.save(name_jpg, 'JPEG')
        if ratioW < ratioH :
            new_height = int(height/ratioW)
            crop_sus = int((new_height - y)/2)
            print('ajustari pe H: ', crop_sus)
            new_img = img.resize((x,new_height))
            crop_img = new_img.crop((0, crop_sus, x, y+crop_sus))
            name_jpg = nume + str(x) + 'x' + str(y) +'.jpg'
            name_webp = nume + str(x) + 'x' + str(y) +'.webp'
            crop_img.save(name_webp, 'webp')
            jpg = crop_img.convert('RGB')
            jpg.save(name_jpg, 'JPEG')

def WhiteBorder():
    for fisier in Selectie_fisiere:
        color = "white"
        nume = fisier.split('.')[0] + 'w'
        img = Image.open(fisier)
        width, height = img.size
        BorderLeft = int((600 - width)/2)
        BorderRight = 600 - width - BorderLeft
        BorderUp = int((650 - height)/2)
        BorderDown = 650 - height - BorderUp
        border = (BorderUp, BorderRight, BorderDown, BorderLeft)
        new_img = ImageOps.expand(img, border = border, fill = color)
        name_jpg = nume + '.jpg'
        name_webp = nume + '.webp'
        new_img.save(name_webp, 'webp')
        jpg = new_img.convert('RGB')
        jpg.save(name_jpg, 'JPEG')

def close():
   window.destroy()

window = Tk()
window.title('File Convertor to WebP')
window.geometry("500x400")
window.config(background = "white")
label_file_explorer = Label(window, text = "Convert to WEBP", width = 20, height = 4, fg ="blue")
button_explore = Button(window, text = "Browse Files", command = browseFiles)
button_resize260 = Button(window, text = "Resize 240x260", command = lambda : resize(240,260))
button_resize600 = Button(window, text = "Resize 600x650", command = lambda : resize(600,650))
button_resize250 = Button(window, text = "Resize 250x300", command = lambda : resize(250,300))
button_resize500 = Button(window, text = "Resize 500x600", command = lambda : resize(500,600))
button_white = Button(window, text = "White Border", command = WhiteBorder)
button_convert = Button(window, text = "Convert to WEBP", command = convertWebP)
button_exit = Button(window, text = "Exit", command = close)
label_file_explorer.place(x = 300, y = 0)
button_explore.place(x = 370, y = 70)
button_resize260.place(x = 370, y = 100)
button_resize600.place(x = 370, y = 130)
button_resize250.place(x = 370, y = 160)
button_resize500.place(x = 370, y = 190)
button_white.place(x = 370, y = 220)
button_convert.place(x = 370, y = 250)
button_exit.place(x = 370, y = 280)
window.mainloop()

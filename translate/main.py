from tkinter import *
from googletrans import Translator 
from PIL import Image, ImageTk



app = Tk()
app.resizable(height=False,width=False)
app.title("Google Translate")
app.geometry("500x600")
app.iconbitmap("logo.ico")

img = ImageTk.PhotoImage(Image.open("./Background-clouds.jpeg"))
background = Label(app,image=img)
background.pack()

text_title = Label(app,text="Translator",bg="#8c86c1",font=("Times",30))
text_title.place(x=180,y=10)

text_box1 =  Text(app,width=28,height=8,font=("ROBOTO",20),relief="sunken")
text_box1.place(x=60,y=100)

text_box2 =  Text(app,width=28,height=8,font=("ROBOTO",20),relief="sunken")
text_box2.place(x=60,y=370)

def clear_action():
    text_box1.delete(1.0,END)
    text_box2.delete(1.0,END)


def translate_action():
    txt = text_box1.get(1.0,END)
    trans = Translator()
    trans_txt  = trans.translate(txt,dest="en",src="vi")
    if text_box2.get(1.0,END) != "":
        text_box2.delete(1.0,END)
    text_box2.insert(END,trans_txt.text)

   


        



button_frame = Frame(app).pack(side=BOTTOM)
clear_button = Button(app,text="Clear text",font=("arial",16,"bold"),bg="black",fg='green',command=clear_action)
clear_button.place(x=250,y=320)
trans_button = Button(app,text="Translate",font=("arial",16,"bold"),bg="black",fg='green',command=translate_action)
trans_button.place(x=150,y=320)

app.mainloop()
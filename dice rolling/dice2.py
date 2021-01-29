import tkinter
from PIL import Image, ImageTk
import random

root = tkinter.Tk()
root.geometry('400x550')
root.title('Roll Two Dice')

l0 = tkinter.Label(root, text="")
l0.pack()

l1 = tkinter.Label(root, text="ROLL TWO DICE", fg = "light blue",
        bg = "white",
        font = "Helvetica 16 bold italic")
l1.pack()

dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tkinter.Label(root, image=image1)
label1.image = image1
label2 = tkinter.Label(root, image=image2)

label1.pack( expand=True)
label2.pack( expand=True)

def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image = image1
    label2.configure(image=image2)
    label2.image = image2


button = tkinter.Button(root, text='Roll Two Dice', fg='black', command=rolling_dice)

button.pack( expand=True)

root.mainloop()

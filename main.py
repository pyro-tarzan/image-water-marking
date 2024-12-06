from tkinter import Tk, Canvas, Label, Button
from PIL import Image, ImageTk

# CREATE TK WINDOW
window = Tk()
window.title("Image Watermarking")

#CREATE A IMAGE OBJECT IN PIL
image = Image.open("./images/GangsterGanesh.jpeg")
width, height = image.size

#CONVERT PIL IMAGE INTO TK IMAGE
tk_image = ImageTk.PhotoImage(image)

# CREATE CANVAS FOR IMAGE
img_cnv = Canvas(window, width=width, height=height, bg="white")
img_cnv.grid()

# #CREATE IMAGE INSIDE THE CANVAS
img_cnv.create_image(width / 2, height / 2, image=tk_image)

button = Button(window, text="Submit")
button.grid()

window.mainloop()


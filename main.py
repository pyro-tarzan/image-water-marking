import tkinter
from tkinter import Tk, Canvas, Label, Button, Entry, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

# ----------------------------------
# LOGIC
# ----------------------------------

filename = "GangsterGanesh.jpeg"

def terminate():
    window.destroy()

def submit_value():
    text = text_entry.get()

    if text:
        original_image = Image.open(f"./images/{filename}").convert("RGBA")
        z_index = Image.new("RGBA", original_image.size, (255, 255, 255, 0))

        draw = ImageDraw.Draw(z_index)

        w, h = original_image.size
        w, h = w // 2, h - 20

        font = ImageFont.truetype("/DejaVuSans-Bold.ttf" ,size=12)
        draw.text((w, h), text, font=font)

        final = Image.alpha_composite(original_image, z_index)

        f = filename.split(".")[0]
        new_path = f"/home/vicky/Pictures/{f}_WaterMarked.png"
        final.save(new_path)
        final.show("GangsterGanesh")

        text_entry.delete(0, tkinter.END)
    else:
        messagebox.showinfo("Note", "Text Field can't be empty.")
    window.destroy()


# --------------------------------------
# UI
#---------------------------------------

# CREATE TK WINDOW
window = Tk()
window.title("Image Watermarking")
window.config(pady=10)

for i in range(5):
    window.grid_columnconfigure(i, weight=0, uniform="equal")

# CREATE A IMAGE OBJECT IN PIL
image = Image.open(f"./images/{filename}")
width, height = image.size

# CONVERT PIL IMAGE INTO TK IMAGE
tk_image = ImageTk.PhotoImage(image)

# CREATE CANVAS FOR IMAGE
img_cnv = Canvas(window, width=width, height=height)
img_cnv.grid(row=0, column=0, columnspan=6, rowspan=5)

# #CREATE IMAGE INSIDE THE CANVAS
img_cnv.create_image(width / 2, height / 2, image=tk_image)

text_label = Label(window, text="Name:")
text_label.grid(row=6, column=2, sticky="e")

text_entry = Entry(window, width=10)
text_entry.grid(row=6, column=3, sticky="e")

cancel_button = Button(text="Cancel", command=terminate)
submit_button = Button(text="Submit", command=submit_value)
cancel_button.grid(row=6, column=4, sticky="e")
submit_button.grid(row=6, column=5, sticky="e")

window.mainloop()

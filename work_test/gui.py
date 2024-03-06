# import csv
import pandas as pd
from tkinter import *
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import numpy as np
import tkinter as tk
from tkinter import Tk, Frame
import Ensemble

def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

def end_fullscreen(event=None):
    root.attributes("-fullscreen", False)

root = Tk()
root.title('No.1 APP')
root.attributes("-fullscreen", True)
root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", end_fullscreen)
frame = Frame(root)
frame.pack()

canvas = Canvas(frame, bg="white", width=960, height=560)
canvas.pack()

header = Label(canvas, text="ตาราง", bg="white", fg="black", font="Inter 20 bold").place(x=450, y=20)

body = PhotoImage(file="pic/form.png")
canvas.create_image(200, 260, image=body)
form_header = canvas.create_text(200, 55, text="ใส่ข้อมูล", font="Inter 30 bold", fill="black")
temp = canvas.create_text(130, 115, text="Date", font="Inter 22 bold", fill="black")
lowest = canvas.create_text(130, 185, text="Age", font="Inter 22 bold", fill="black")
moisture = canvas.create_text(105, 255, text="Team", font="Inter 22 bold", fill="black")
Pressure = canvas.create_text(105, 325, text="Opp", font="Inter 22 bold", fill="black")
Rainfall = canvas.create_text(105, 375, text="Mp", font="Inter 22 bold", fill="black")

table = PhotoImage(file="pic/table.png")
canvas.create_image(665, 235, image=table)

Input_image_box = PhotoImage(file="pic/input.png")
temp = IntVar()
canvas.create_image(290, 120, image=Input_image_box)
input_temp = Entry(canvas, width=5, font="Inter 20 bold", border=0, textvariable=temp).place(x=220, y=100)

lowest = IntVar()
canvas.create_image(290, 190, image=Input_image_box)
input_lowest = Entry(canvas, width=5, font="Inter 20 bold", border=0, textvariable=lowest).place(x=220, y=170)

moisture = IntVar()
canvas.create_image(290, 260, image=Input_image_box)
input_moisture = Entry(canvas, width=5, font="Inter 20 bold", border=0, textvariable=moisture).place(x=220, y=240)

Pressure = IntVar()
canvas.create_image(290, 323, image=Input_image_box)
input_Pressure = Entry(canvas, width=5, font="Inter 20 bold", border=0, textvariable=Pressure).place(x=220, y=310)

Rainfall = IntVar()
canvas.create_image(290, 385, image=Input_image_box)
input_Rainfall = Entry(canvas, width=5, font="Inter 20 bold", border=0, textvariable=Rainfall).place(x=220, y=365)

under = PhotoImage(file="pic/mother_result.png")
canvas.create_image(485, 470, image=under)
result = PhotoImage(file="pic/under_result.png")
canvas.create_image(485, 500, image=result)

output = PhotoImage(file="pic/result.png")
canvas.create_image(650, 495, image=output)

txt = StringVar()
print(txt)
txt.set("Initial Value")

out_put = Label(canvas, width=15, font="Inter 12 bold", background="#ffffff", border=0, textvariable=txt).place(x=652, y=480)

# Get data from beta.py
data = Ensemble.Voting.data

def predict_quality(entry_boxes):
    print(entry_boxes)

def open_image():
    file_path = filedialog.askopenfilename(initialdir="/", title="Select Image",
                                           filetypes=(("Image files", "*.png;*.jpg;*.jpeg;*.gif"), ("all files", "*.*")))

    if file_path:
        image = Image.open(file_path)
        image = image.resize((300, 300))
        tk_image = ImageTk.PhotoImage(image)

        image_window = Toplevel(root)
        image_window.title("รูปภาพ")

        image_label = Label(image_window, image=tk_image)
        image_label.image = tk_image
        image_label.pack()


def open_csv():
    file_path = filedialog.askopenfilename(
        initialdir="/",
        title="Select CSV File",
        filetypes=(("CSV files", "*.csv"), ("all files", "*.*"))
    )

    if file_path:
        try:
            df = pd.read_csv(file_path)
            show_table(df)
        except pd.errors.EmptyDataError:
            print("The selected CSV file is empty.")


def show_table(dataframe):
    table_window = Toplevel(root)
    table_window.title("CSV Table")

    tree = ttk.Treeview(table_window, columns=list(dataframe.columns), show='headings')
    for col in dataframe.columns:
        tree.heading(col, text=col)
    tree.pack()

    for i, row in dataframe.iterrows():
        tree.insert("", "end", values=list(row))


button_image = PhotoImage(file="pic/button.PNG")
click_label = Label(canvas, image=button_image)
button = Button(canvas, image=button_image, command=predict_quality(temp), border=0, background="white", cursor="hand2")
button.place(x=250, y=460)

CSVButton = Button(canvas, text="เปิดไฟล์ CSV", command=open_csv, border=1, background="white", cursor="hand2")
CSVButton.place(x=890, y=100)

ImageButton = Button(canvas, text="เปิดรูป", command=open_image, border=1, background="white", cursor="hand2")
ImageButton.place(x=890, y=50)

root.mainloop()
from tkinter import *
from tkinter import filedialog
from PIL import Image
import time
import math

print("Welcome! This is the image-array-generator for javascript (specifically for hack club's blot). \nWarning: this script will copy the image array to your clipboard.")
time.sleep(1)

root = Tk()
filepath = filedialog.askopenfilename(initialdir = "/", title = "Upload an image", filetypes = [("Image files", ".png .jpg")])

image = Image.open(filepath)

original_w, original_h = image.size

width = int(input("Input a width for your image array: "))
height = math.floor(original_h * width / original_w)
image = image.resize((width, height), Image.LANCZOS)

pixels = image.load()

brightnesses = []

for y in range(height):
    brightnesses.append([])
    for x in range(width):
        R, G, B = pixels[x, y][:3]
        brightnesses[y].append(round((R + G + B) / 3))


string_print = "var image = ["

for row in brightnesses:
    string_print += "["
    for value in row:
        string_print += str(int(value)) + ", "
    string_print = string_print[:-2]
    string_print += "], "

string_print = string_print[:-2]
string_print += "]"

print(string_print)

import pyperclip
pyperclip.copy(string_print)

print("Copied to clipboard.")

brightness_image = Image.new('L', (width, height))
brightness_list = []
for sublist in brightnesses:
    brightness_list.extend(sublist)

brightness_image.putdata(brightness_list)

brightness_image.show()

root.mainloop()
# Batch File Renamer for easier processing for Plex
# Made by Rasmus Bremholm 2020
# Good starting point https://www.geeksforgeeks.org/rename-multiple-files-using-python/


# Here we are importing OS library
import os
import tkinter as tk
import requests

height = 600
width = 800

input_dir = ""
output_dir = ""
count = 1
directory = ""
suffix = ""

# Setting up the root window
root = tk.Tk()

# main container
canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

# content container
frame = tk.Frame(root)
frame.place(relx=0.05, rely=0.05, relwidth=0.95, relheight=0.95)

root.mainloop()

os.chdir(directory)


def increment():
    global count
    count = count + 1


for file in os.listdir():
    file_name, file_ext = os.path.split(file)
    file_name = suffix + str(count)
    increment()

    new_name = "{} {}".format(file_name, file_ext)
    os.rename(file, new_name)

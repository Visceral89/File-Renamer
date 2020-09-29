# Batch File Renamer for easier processing for Plex
# Made by Rasmus Bremholm 2020
# Good starting point https://www.geeksforgeeks.org/rename-multiple-files-using-python/

import os #Here we are importing OS library
import tkinter as tk
import requests

input_dir = ""
output_dir = ""
count = 1
directory = ""
suffix = ""

#Setting up the root window.
root = tk.TK()


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
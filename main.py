# Batch File Renamer for easier processing for Plex
# Made by Rasmus Bremholm 2020
# Good starting point https://www.geeksforgeeks.org/rename-all-file-names-in-your-directory-using-python/?ref=lbp
# http://timgolden.me.uk/python/win32_how_do_i/browse-for-a-folder.html


# Here we are importing OS library
import os
import tkinter as tk

height = 600
width = 800

input_dir = ""
output_dir = ""
count = 1
prefix = ""
index = 0

# Setting up the root window
root = tk.Tk()
root.title("File Renamer by Rasmus")

# main grid
e = tk.Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# content container
frame = tk.Frame(root)
frame.place(relx=0.05, rely=0.05, relwidth=0.95, relheight=0.95)

root.mainloop()

os.chdir("G://3D")
print(os.getcwd())

for file in os.listdir():
    file_name, file_ext = os.path.split(file)
    file_name = prefix + str(index)

    new_name = "{} {}".format(file_name, file_ext)
    os.rename(file, new_name)
    print(file_name)

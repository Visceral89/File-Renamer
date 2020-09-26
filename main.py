# Batch File Renamer for easier processing for Plex
# Made by Rasmus Bremholm 2020
# Good starting point https://www.geeksforgeeks.org/rename-multiple-files-using-python/

import os #Here we are importing OS library

def main():

    for count, filename in enumerate(os.listdir("xyz")): #getting the files in specified directory
        dst = prefix + str(count) + ".jpg"
        src = xyz + filename
        dst = xyz + dst

        os.rename(src, dst)

if __name__ =="__main__":
    main()
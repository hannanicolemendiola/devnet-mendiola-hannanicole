"""
Module 2 — Activity: File Sorting with os and shutil
Student: Mendiola, Hanna Nicole L.
Date: September 27, 2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
This is a file sorter, where files will be
sorted according to their extension. The
user pastes a directory he or she wants to
be organized.

============================================
KEY VOCABULARY
============================================
- os module: a module used to interact with
the user's operating system.
- shutil module: a module used for modifying
or handling files and directories.
- file path: a path linking to a certain
file location.
- directory: a destination folder. 

============================================
YOUR SCRIPT
============================================
"""

import os
import shutil

while True:
    path = input("Enter folder path to organize: ")
    if os.path.exists(path):
        break   
    else:
        print("Folder path does not exist.")

print("Getting files...")
files = os.listdir(path)

categories = {
              "Images" : [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
              "Documents" : [".docx", ".pdf", ".pptx", ".xlsx"],
              "Videos" : [".mp4", ".mov"],
              "Others" : [".txt", ".zip"]
              }

for category in categories.keys():
    if os.path.exists(category):
        print(f"{category} folder already created.")
    else:
        os.mkdir(f"{category}")
        print(f"{category} folder created!")

for file in files:
    if os.path.isdir(file):
        continue
    else:
        for category, type_list in categories.items():
            for type in type_list:
                if file.endswith(type):
                    shutil.move(file, os.path.join(path, category))
                    print(f"{file} successfully moved to {category}.")
images = 0
documents = 0
videos = 0
others = 0

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
Using dictionaries is quite tricky since
keys and values are used. I was so
confused strategizing to use it here, but I
know it is a big help here.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
This made me thought of more projects that
would probably need more automation in my
operating system like some sort of trash bin
where unimportant files are deleted.
"""

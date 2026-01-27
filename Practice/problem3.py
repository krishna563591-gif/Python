import os

path = "/New Folder"

for item in os.listdir(path):
    print(os.path.join(path, item))
#Write a program to list all files in a directory
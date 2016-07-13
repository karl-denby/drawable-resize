import sys
import os

def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        print("Folder", folder_name, "created.")
    except:
        print("Unable to create folder")


def folder_check():
    android_sizes = ['mdpi', 'hdpi', 'xhdpi', 'xxhdpi', 'xxxhdpi']
    android_folder = 'drawable-'

    # check folders exist
    print("Pre-check: looking for folders")

    for size in android_sizes:
        folder_name = android_folder + size
        if os.path.exists(folder_name):
            print("Folder", folder_name, "exists")
        else:
            create_folder(folder_name)


print("Filename provided is", sys.argv[1])
source_image = sys.argv[1]

android_pixel = [192, 180, 96, 72, 48]
folder_check()

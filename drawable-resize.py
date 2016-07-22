from __future__ import print_function  # in case user is using python 2.7
from PIL import Image  # for manipulating the image
import sys, os  # cli arguments and path functions for folder check/create


def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        print("Folder", folder_name, "created.")
    except:
        print("Unable to create folder")


def folder_check():
    android_sizes = ['mdpi', 'hdpi', 'xhdpi', 'xxhdpi', 'xxxhdpi']


    # check folders exist
    android_folder = 'drawable-'
    print("Pre-check: looking for drawable folders")

    for size in android_sizes:
        folder_name = android_folder + size
        if os.path.isdir(folder_name):
            print("Folder", folder_name, "exists")
        else:
            create_folder(folder_name)

    android_folder = 'mipmap-'
    print("Pre-check: looking for mipmap folders")

    for size in android_sizes:
        folder_name = android_folder + size
        if os.path.isdir(folder_name):
            print("Folder", folder_name, "exists")
        else:
            create_folder(folder_name)


def output_images(source_image, image_type):

    icon_sizes = {
        'mdpi': (48, 48),
        'hdpi': (72, 72),
        'xhdpi': (96, 96),
        'xxhdpi': (180, 180),
        'xxxhdpi': (192, 192)
    }

    image_sizes = {
        'mdpi': (480, 480),
        'hdpi': (720, 720),
        'xhdpi': (960, 960),
        'xxhdpi': (1800, 1800),
        'xxxhdpi': (1920, 1920)
    }

    if image_type == 'icon':
        folder_to_pixel = icon_sizes
        android_prefix = 'mipmap-'
    elif image_type == 'image':
        folder_to_pixel = image_sizes
        android_prefix = 'drawable-'
    else:
        print("USAGE:", sys.argv[0], "icon|image", "filename.png")
        exit()

    for folder in folder_to_pixel:
        outfile = android_prefix + folder + os.path.sep + source_image
        size = folder_to_pixel[folder]
        print ("Write:", source_image, size, "in folder", folder)

        try:
            im = Image.open(source_image)
            im.thumbnail(folder_to_pixel[folder], Image.ANTIALIAS)
            im.save(outfile, "PNG")
        except IOError:
            print ("cannot create thumbnail for '%s'" % source_image)


# ---- Main ----
script_name = sys.argv[0]
image_type = sys.argv[1]
source_images = sys.argv[2:]
folder_check()  # Check folders exist and create if needed

for image in source_images:
    output_images(image, image_type)  # Output Images

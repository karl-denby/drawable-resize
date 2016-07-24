from __future__ import print_function  # in case user is using python 2.7
from PIL import Image  # for manipulating the image
import sys  # sys
import os  # cli arguments and path functions for folder check/create


def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        print("Folder", folder_name, "created.")
    except:
        print("Unable to create folder")


def folder_check(folder_prefix):
    android_sizes = ['ldpi', 'mdpi', 'hdpi', 'xhdpi', 'xxhdpi', 'xxxhdpi']

    # check folders exist and call create code if they don't
    print("Pre-check: looking for", folder_prefix, "folders")

    for size in android_sizes:
        folder_name = folder_prefix + '-' + size
        if os.path.isdir(folder_name):
            print("Folder", folder_name, "exists")
        else:
            create_folder(folder_name)


def output_images(source_image, folder_prefix, image_sizes):

    for resolution in image_sizes:
        outfile = folder_prefix + '-' + resolution + os.path.sep + source_image
        size = image_sizes[resolution]
        print ("Write:", source_image, size, "in folder", resolution)

        try:
            im = Image.open(source_image)
            im.thumbnail(image_sizes[resolution], Image.ANTIALIAS)
            im.save(outfile, "PNG")

        except IOError:
            print ("cannot create thumbnail for '%s'" % source_image)


# ---- Main ----
# scriptname.py mipmap|drawable filename1.png filename2.png
script_name = sys.argv[0]
image_type = sys.argv[1]
source_images = sys.argv[2:]

# Sizes for mipmap launcher icons
mipmap_sizes = {
    'ldpi': (36, 36),
    'mdpi': (48, 48),
    'hdpi': (72, 72),
    'xhdpi': (96, 96),
    'xxhdpi': (144, 144),
    'xxxhdpi': (192, 192)
}

# Sizes for drawable image resource
drawable_sizes = {
    'ldpi': (360, 360),
    'mdpi': (480, 480),
    'hdpi': (720, 720),
    'xhdpi': (960, 960),
    'xxhdpi': (1440, 1440),
    'xxxhdpi': (1920, 1920)
}

# based on input provided in parameters
# check for folders (create if needed)
# for each image provided "2:" create an image at multiple densities
# no valid input show the user an error message

if image_type == 'mipmap':
    folder_check(image_type)  # Check folders exist. Create if needed.
    for image in source_images:
        output_images(image, image_type, mipmap_sizes)  # Output Images

elif image_type == 'drawable':
    folder_check(image_type)  # Check folders exist. Create if needed.
    for image in source_images:
        output_images(image, image_type, drawable_sizes)  # Output Images

else:
    print("USAGE:", sys.argv[0], "mipmap|drawable", "filename.png")

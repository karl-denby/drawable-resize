import sys, os
from PIL import Image

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


def output_images(source_image):
    android_prefix = 'drawable-'
    folder_to_pixel = {
        'mdpi': (48, 48),
        'hdpi': (72, 72),
        'xhdpi': (96, 96),
        'xxhdpi': (180, 180),
        'xxxhdpi': (192, 192)
    }

    for folder in folder_to_pixel:
        outfile = android_prefix + folder + '\\' + source_image

        print ("Writing", outfile, folder_to_pixel[folder])
        try:
            im = Image.open(source_image)
            im.thumbnail(folder_to_pixel[folder], Image.ANTIALIAS)
            im.save(outfile, "PNG")
        except IOError:
            print ("cannot create thumbnail for '%s'" % source_image)

# ---- Main ----
source_image = sys.argv[1]
print("Filename provided is", source_image)
folder_check()  # Check folders exist and create if needed
output_images(source_image)  # Output Images

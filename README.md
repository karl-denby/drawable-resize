# py-drawable-resize

### Problem
When working with and Android project you may need to create a number of sizes of images for use in your project.  Doing this by hand can be painful as you need to resize and save many resolutions in a number of folders.

### Solution
This script aims to give you a quick easy way to take a source image and resize and deploy it to your application, it aims to be small, cross platform and error free and easy to maintain.

### Usage
* Place this file in your project res folder something like __MyApplication/app/src/main/res/drawable-resize.py__ or in its own location if you plan to copy across the images later.
* Place the source image you want to scale in the same location
* Change to this directory on the command line
* run the script and provide either the image or icon keyword and file names

### Example
> python drawable-resize.py __icon__ _myimage1.png_ _myimage2.png_

> python drawable-resize.py __image__ _myimage1.png_ _myimage2.png_

This should create 5 copies of each image in the following __folders__ at these __resolutions__
* drawable-xxxhdpi - 192x192 (icon) or 1920x1920 (image)
* drawable-xxxhdpi - 144x144 (icon) or 1440x1440 (image)
* drawable-xhdpi - 96x96 (icon) or 960x960 (image)
* drawable-hdpi - 72x72 (icon) or 720x720 (image)
* drawable-mdpi - 48x48 (icon) or 480x480 (image)
* drawable-ldpi - 36x36 (icon) or 360x360 (image)

### Features
Script will check if folders exist and create if needed.

### Limitations
* Aspect ratio is maintained so source images should have a 1:1 aspect ratio if you wish for final image to also have a 1:1 aspect ratio
* Wild cards (\*) are not supported at this time

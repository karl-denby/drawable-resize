# py-drawable-resize

## Problem
When working with Android you may need to create a number of sizes of images for use in your project.  Doing this by hand can be painful as you need to resize and save many resolutions in a number of folders.

## Usage
* Place this file in your project res folder something like __MyApplication\app\src\main\res__
* Place the source image you want to scale in the same location
* Change to this directory on the command line then run
* python drawable-resize.py myimage.png

This should create 5 copies of myimage.png in the following __folders__ at these __resolutions__
* drawable-xxxhdpi - 192x192
* drawable-xxxhdpi - 180x180
* drawable-xhdpi - 96x96
* drawable-hdpi - 72x72
* drawable-mdpi - 48x48

## Features
Script will check if folders exist and create if needed.

## Limitations
Source image needs to have a 1:1 aspect ratio.

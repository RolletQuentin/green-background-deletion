from os import listdir, mkdir, path
from PIL import Image, ImageDraw
from tqdm import tqdm
import numpy as np

FOLDER_DIR = "/home/cytech/Pictures/BDA"  # the folder with images
BACKGOUND_IMAGE_ROUTE = "./pexels-david-bartus-1166209.jpg"

if not path.exists("images"):
    mkdir("images")

bg_image = Image.open(BACKGOUND_IMAGE_ROUTE)

for image_str in tqdm(listdir(FOLDER_DIR)):

    image_route = FOLDER_DIR + "/" + image_str

    image = Image.open(image_route)
    bg_image_copy = bg_image.copy()

    # check the size of the background and resize it to fit to the image
    image_width, image_height = image.size
    bg_width, bg_height = bg_image_copy.size

    if image_width > bg_width:
        width_ratio = image_width / bg_width
        bg_image_copy = bg_image_copy.resize(
            (image_width, int(bg_height*width_ratio)), Image.ADAPTIVE)
        bg_width, bg_height = bg_image_copy.size

    if image_height > bg_height:
        height_ratio = image_height / bg_height
        bg_image_copy = bg_image_copy.resize(
            (int(bg_width*height_ratio), image_height), Image.ADAPTIVE)
        bg_width, bg_height = bg_image_copy.size

    # now, the background image is greater than foreground image
    bg_width, bg_height = bg_image_copy.size
    if image_width < bg_width or image_height < bg_height:
        left = (bg_width - image_width) // 2
        top = (bg_height - image_height) // 2
        right = left + image_width
        bottom = top + image_height
        bg_image_copy = bg_image_copy.crop((left, top, right, bottom))

    # convert RGB to HSV
    image = image.convert("HSV")
    bg_image_copy = bg_image_copy.convert("HSV")

    # transform image to np array
    image = np.asarray(image)
    bg_image_copy = np.asarray(bg_image_copy)

    # find green pixels
    mask = (image[..., 0] < 130) & (
        image[..., 0] > 70) & (image[..., 1] > 0.70)

    image_with_bg = image.copy()
    image_with_bg[mask] = bg_image_copy[mask]

    Image.fromarray(image_with_bg.astype(np.uint8), "HSV").convert("RGB").save(
        "images/" + image_str)

# red ball assignment

# import PIL module
from PIL import Image

# opens the image
redball = Image.open("redball.jpeg").load()
redball_image = Image.open("redball.jpeg")

# variables for the width and height of the image
width = redball_image.width
height = redball_image.height

# check red pixels


def is_red(r, g, b):
    if r <= 255 and r >= 160 and g <= 90 and g >= 0 and b <= 104 and b >= 0:
        return True


# counter for red pixels
red_counter = 0

for i in range(width):
    for j in range(height):
        # adds 1 to the counter for every red pixel detected
        if is_red(redball[i, j][0], redball[i, j][1], redball[i, j][2]):
            red_counter += 1
            # replaces the middle red pixel with white if the counter is 840
            if red_counter == 840:
                redball_image.putpixel((i, j), (255, 255, 255))

# saves the image
redball_image.save("output1.png")

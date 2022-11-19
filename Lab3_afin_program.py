from PIL import Image, ImageDraw
import math

img = Image.new('RGBA', (960, 960), (255, 255, 255))
paint = ImageDraw.Draw(img)
with open("DS8.txt", "r") as f:
    for line in f:
        coords_list = line.split()
        i = int(coords_list[1]) - 480
        j = int(coords_list[0]) - 480
        x = math.cos(1.57079) * i - math.sin(1.57079) * j
        y = math.sin(1.57079) * i + math.cos(1.57079) * j
        paint.point((x + 480, y + 480), (0, 190, 255))
img.show()
img.save('Final.jpg')

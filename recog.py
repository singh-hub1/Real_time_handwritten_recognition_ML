import easyocr

#Language Hindi 'hi', English 'en', Marathi 'mr'

#Download the model.

reader= easyocr.Reader(["en", 'en'], gpu=False)

import PIL

from PIL import ImageDraw

im = PIL.Image.open("C:\\Users\\HP\\Desktop\\air-writing-recognition-master\\final\\num.jpg")
im

#OCR & Get bounding boxes.

bounds=reader.readtext("C:\\Users\\HP\\Desktop\\air-writing-recognition-master\\final\\num.jpg")
bounds

#Dran
# bounding boxes

def draw_boxes(image, bounds, color='yellow', width=8):
    draw = ImageDraw.Draw(image) 
    for bound in bounds: 
        p0, p1, p2, p3= bound[0] 
        draw.line([*p0, *p1, *p2, *p3], fill=color, width=width)
    return image

draw_boxes(im, bounds)

im.save("C:\\Users\\HP\\Desktop\\air-writing-recognition-master\\final\\num.jpg")
len(bounds)
for i in bounds:
     print(i[1])

f= open("C:\\Users\\HP\\Desktop\\recognition\\recognize.jpg.jpg.txt", mode='a', encoding="utf-8")

for i in bounds:
     print(i[1])
     f.write(i[1])

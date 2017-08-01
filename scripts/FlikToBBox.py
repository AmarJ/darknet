import sys
import os
from os import walk, getcwd
from PIL import Image

annot = sys.argv[1]
imgPath = sys.argv[2]

with open(annot) as f:
    line = f.readlines()

line = [x.strip() for x in line]

#|Nike_1579|
#|Nike|
#|Nike_n70n33n69n32_2461146507.jpg|
#|logo|
#|1|
#|323|
#|10|
#|353|
#|29|

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

for i in range(0, len(line)):
    content = line[i].split()
    img = imgPath + content[2]
    x1 = content[5]
    y1 = content[6]
    x2 = content[7]
    y2 = content[8]

    im = Image.open(img)
    w=int(im.size[0])
    h=int(im.size[1])
    
    b = (float(x1), float(x2), float(y1), float(y2))
    yoloFormat = convert((w,h), b)
    
    outputFormat = os.path.splitext(content[2])[0]+".txt"

    outFile = open(imgPath+outputFormat, "w+")

    outFile.write("1 ")
    
    for numb in yoloFormat:
        outFile.write(str(numb)+" ")
    outFile.close


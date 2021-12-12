import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage.color import rgb2hsv
from skimage.measure import label, regionprops

def color_diap(h):
    return {
               h < 0.16: 'Red',
        0.16 <= h < 0.33: 'Yellow',
        0.33 <= h < 0.5:  'Green',
        0.5 <= h < 0.83:  'Blue',
        0.83 <= h:       'Purple'
    }[True]

def processing(image):
    binary = np.mean(image,2)
    binary[binary > 0] = 1
    labeled = label(binary)
    return labeled

image = plt.imread("balls_and_rects.png")
labeled = processing(image)
regions = regionprops(labeled)

circle_num = 0
rect_num = 0
color_figures = {
    'circle':{},
    'rect':{}
    }
for region in regions:
    edge = region.bbox
    
    colorful = image[edge[0]:edge[2],edge[1]:edge[3]]
    hsv = rgb2hsv(colorful)
    a = hsv.shape[0]//2
    b = hsv.shape[1]//2
    color = color_diap(hsv[a,b,0])
    
    if hsv[1,1,2] == 0:
        circle_num+=1
        if color in color_figures['circle']:
            color_figures['circle'][color]+=1
        else:
            color_figures['circle'][color] = 1
    else:
        rect_num+=1
        if color in color_figures['rect']:
            color_figures['rect'][color]+=1
        else:
            color_figures['rect'][color] = 1
 
print("number of circles: ", circle_num)    
print("number of rectangles: ", rect_num)
print("COLORS")            
print(color_figures)
   
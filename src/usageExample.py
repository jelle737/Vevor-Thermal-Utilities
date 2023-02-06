import numpy as np
import cv2
from pathlib import Path
from matplotlib import pyplot as plt
import os

filepath_irg = "examples/samples\\230201152910.irg"

filename, file_extension = os.path.splitext(filepath_irg)
filepath_jpg = filename + ".jpg"
path_irg = Path(filepath_irg)



img_metadata = np.fromfile(path_irg, dtype='uint16')
img_metadata = img_metadata[:128]
width_180 = img_metadata[5]
height_240 = img_metadata[4]

fig = plt.figure()
#Camera Preview:
img_jpg = cv2.imread(filepath_jpg)
ax1 = fig.add_subplot(1,6,1)
ax1.imshow(img_jpg[...,::-1])
ax1.title.set_text('Camera')

#Histogram corrected image in inferno colours:
img_sample = np.fromfile(path_irg, dtype='uint8')
img_sample = img_sample[128:]
img_sample = img_sample[:width_180*height_240].reshape(height_240,width_180)
ax2 = fig.add_subplot(1,6,2)
ax2.imshow(img_sample, cmap='inferno')
ax2.title.set_text('Inferno')
ax3 = fig.add_subplot(1,6,3)
#Histogram corrected image in grayscale colours:
ax3.imshow(img_sample, cmap='gray')
ax3.title.set_text('Gray')

#Thermal data in K
img_thermal = np.fromfile(path_irg, dtype='uint16')
img_thermal = img_thermal[int(width_180*height_240*0.5)+64:]
img_thermal = img_thermal[:width_180*height_240].reshape(height_240,width_180)
ax4 = fig.add_subplot(1,6,4)
ax4.imshow(img_thermal, cmap='gray')
ax4.title.set_text('*10 °K')

#Thermal data in °C
f = lambda x: np.add(np.multiply(x,0.1),-273.15)
img_degrees = f(img_thermal)
ax5 = fig.add_subplot(1,6,5)
ax5.imshow(img_degrees, cmap='gray')
ax5.title.set_text('°C')

#RGB Image in jpg format
img_rgb = np.fromfile(path_irg, dtype='uint8')
img_rgb = img_rgb[128+width_180*height_240+width_180*height_240*2:]
img_rgb = cv2.imdecode(img_rgb, cv2.IMREAD_COLOR)
ax6 = fig.add_subplot(1,6,6)
ax6.imshow(img_rgb[...,::-1])
ax6.title.set_text('RGB')
plt.show()

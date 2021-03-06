import numpy as np
import cv2
from matplotlib import pyplot as plt


# Load an color image in grayscale
img = cv2.imread('image.png',0)

#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#img = cv2.imread('image.png',0)

#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.show()



img = cv2.imread('image.png',0)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()



#cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF #for 64-bit machine
#k = cv2.waitKey(0) #for 32-bit machine
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('image_gray.png',img)
    cv2.destroyAllWindows()

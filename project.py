'''Welcome to my program. This program is about processing the image of a tarred road to remove out the unnecessary things 
in the background to reduce the information fed to the device for lane detection. While using grabCut function on the entire image,
I noticed some distinct changes. The road had become extra dark,its pixel color values had become 0. This meant that if I could 
transform the processed image into grayscale, I could apply threshold function for which any pixel color value greater than 0 would 
be converted to white.'''
import cv2
import numpy as np


img=cv2.imread('road.jpg')
img=cv2.resize(img,(800,800))
img[0:200,0:800]=[255,255,255]#Converting the top part white because clouds are black in colour
cv2.imshow('g',img)
mask=np.zeros(img.shape[:2],np.uint8)


bgdModel=np.zeros((1,65), np.float64)
fgdModel=np.zeros((1,65),np.float64)

rect=(0,0,799,799)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,20,cv2.GC_INIT_WITH_RECT)#Using grabCut on the entire image
mask2=np.where((mask==2)|(mask==0),0,1).astype('uint8')
img=img*mask2[:,:,np.newaxis]
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)#Converting the BGR image into a RGB Image
cv2.imwrite('temp.png',img)#Storing the image
imgnew=cv2.imread('temp.png',cv2.IMREAD_GRAYSCALE)#Reading the image as a grayscale
th, res=cv2.threshold(imgnew,1,255,cv2.THRESH_BINARY)#Thresholding all pixel values greater than 0

cv2.imshow('Final',res)

cv2.waitKey(0)
cv2.destroyAllWindows()
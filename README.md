
# Lane Marking and Background Isolation for Image Processing
This project is done by Gopesh Srinivasan



## Overview
This project aims to develop a computer vision pipeline that processes a given image of a lane and produces a clear output where the area between the lanes is marked black and the surrounding regions are marked white

## Working of the code 
The program first reads the image and resizes it a size of 800x800 pixels. The program then converts an area of 200x800 pixels from the top because there can be dark shaded clouds that might interfere with the program

We create two variables, namely 'bgdModel' and 'fgdModel' which are temporary arrays used by grabCUt while modelling the background and the foreground respectively.
 
A variable called 'mask' is created. It is a mask image where we specify which areas are background, foreground or probable background/foreground etc.

We then create a rectangle and specify the coordinates. Since there was some compiler error while using grabCut on the entire image, I applied it to a 799x799 pixels area. 

grabCut is a function that is used to remove the background from a specified area. But in this program, it serves a different purpose. It was noticed that on applying grabCut, a BGR image was obtained where the roads had become extra dark, approaching pixel colour values of [0,0,0]

This gave the idea that by converting this image to a grayscale image where the road would have pixel colour values approaching 0, we could apply threshold function which would convert all pixel values greater than 1 to white and the only dark portion remaining would be the road
## Limitations and Problems:-
This program has its own limitations. For instance, if there is a dark noise in the image like roadside barriers, clouds etc which are not taken care of, they are also considered as a road and are displayed in black. 

On giving an image of a road which was not dark enough, it also thresholded certain parts of the road to white because it did not detect it to be a dark shade
## References
[GrabCut function](https://docs.opencv.org/3.4/d8/d83/tutorial_py_grabcut.html)

[Threshold function](https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html)





## Input Image
![alt text](road.jpg)

## Processed Output
![alt text](<Screenshot 2024-09-08 162654.png>)

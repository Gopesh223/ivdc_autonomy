# ivdc_autonomy
Welcome to my program. This program is about processing the image of a tarred road to remove out the unnecessary things 
in the background to reduce the information fed to the device for lane detection. While using grabCut function on the entire image,
I noticed some distinct changes. The road had become extra dark,its pixel color values had become 0. This meant that if I could 
transform the processed image into grayscale, I could apply threshold function for which any pixel color value greater than 0 would 
be converted to white.
Like any other program, it has its own limitations. There are certain pictures of roads where it doesn't detect the road due to high grayscale values and some non-road part where it considers it as black due to noise or some unusual dark features like clouds. This can be minimalized by opting for a picture which has road in the lower portion of image so that the upper part can be directly converted to white
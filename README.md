# ivdc_autonomy
Welcome to my program. This program is about processing the image of a tarred road to remove the unnecessary things in the background to reduce the information fed to the device for lane detection. While using the grabCut function on the entire image, I noticed some distinct changes. The road had become extra dark,  and its pixel color values had become 0. This meant that if I could transform the processed image into a grayscale, I could apply a threshold function for which any pixel color value greater than 0 would be converted to white. Like any other program, it has its limitations. There are certain pictures of roads where it doesn't detect the road due to high grayscale values and some non-road parts where it considers it as black due to noise or some unusual dark features like clouds. This can be minimalized by opting for a picture that has a a road in the lower portion of the image so that the upper part can be directly converted to white. If there other objects in the image like road barriers, mountains, it will also portions of them to be a path.

Original Image
![road](https://github.com/user-attachments/assets/36f6a74f-765b-49fc-a07c-f66d40c27186)


Processed Image
![Screenshot 2024-09-08 162654](https://github.com/user-attachments/assets/ade7ef29-6e9b-4d79-91a6-7c05fbec41b7)

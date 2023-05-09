import numpy as np;
import cv2 as c;
image=c.imread('image/demo.jpeg');
width,height=480,540;


point1=np.float32([[12,229],[16,870],[452,241],[452,844]]);
point2=np.float32([[0,0],[0,width],[height,0],[height,width]]);

#join the points with original width and heigth
matrix=c.getPerspectiveTransform(point1,point2)
image1=c.warpPerspective(image,matrix,(width,height))
print('hello')



c.imshow("Demo",image1)
while True:
    if c.waitKey(1) & 0xFF == ord('z'):
     break;
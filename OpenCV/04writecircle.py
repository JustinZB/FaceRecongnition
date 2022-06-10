import cv2 as cv
img = cv.imread('03.jpg')
#画矩形
x,y,w,h=50,50,80,80
cv.rectangle(img,(x,y,x+w,y+h),color=(0,255,1),thickness=2)
cv.circle(img,center=(x+w//2,y+h//2),radius=w//2,color=(0,0,255),thickness=2)
cv.imshow("output_image",img)
cv.waitKey(0)
cv.destroyAllWindows()
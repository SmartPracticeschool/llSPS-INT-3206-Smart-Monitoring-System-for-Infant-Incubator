import cv2
img=cv2.imread("daisy.jpg",1)
print(img)
cv2.imshow("human",img)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()


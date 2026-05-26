import cv2
print(cv2.__version__)
img = cv2.imread('../assets/lena.png')
cv2.imshow('Lena', img)
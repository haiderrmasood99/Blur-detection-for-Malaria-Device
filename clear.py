import cv2
import numpy as np
import time
start = time.time()
print("Processing")
img = cv2.imread("9.JPG", cv2.IMREAD_GRAYSCALE)
laplacian_var = cv2.Laplacian(img, cv2.CV_64F).var()
#if laplacian_var < 5:
#    print("Image blurry")
print(laplacian_var)
end = time.time()
print("Time take in seconds is :")
print(end - start)
#cv2.imshow("Img", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

import cv2
import matplotlib.pyplot as plt
im = cv2.imread("flower.jpeg")
edges = cv2.Canny(im, 100, 1)
plt.imshow(edges)
plt.show()
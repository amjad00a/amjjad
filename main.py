import matplotlib.pyplot as plt
import numpy as np
image=plt.imread("123.jpg")
plt.figure(figsize=(10,10))
for i in range(20):
    plt.subplot(10,2,i+1)
    plt.title("image1")
    plt.axis("off")
    plt.imshow(image)
plt.show()
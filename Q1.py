import matplotlib.pyplot as plt
image=plt.imread("123.jpg")
print(type(image))
plt.subplot(121)
plt.title("image1")
plt.imshow(image)
image2=plt.imread("456.jpg")
plt.subplot(122)
plt.imshow(image2)
plt.title("image2")
plt.axis("on")
plt.show()

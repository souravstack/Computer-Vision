import cv2

### 1. Convert color image to gray image
# img = cv2.imread("resources/lena.png")
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(img.shape)
# print(img_gray.shape)


# cv2.imshow("Original image",img)
# cv2.imshow("Grayscale image",img_gray)

# cv2.waitKey(0)



### convert  to blur image


# img = cv2.imread("resources/lena.png")
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_blur = cv2.GaussianBlur(img_gray, (7,7),0)

# print(img.shape)
# print(img_gray.shape)
# print(img_blur.shape)


# cv2.imshow("Original image",img)
# cv2.imshow("Grayscale image",img_gray)
# cv2.imshow("Blur image", img_blur)
# cv2.waitKey(0)


### convert to canny image


# img = cv2.imread("resources/CV_image.png")
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_blur = cv2.GaussianBlur(img_gray, (7,7),0)
# img_canny = cv2.Canny(img_blur,100,100)


# print(img.shape)
# print(img_gray.shape)
# print(img_blur.shape)
# print(img_canny.shape)



# cv2.imshow("Original image",img)
# cv2.imshow("Grayscale image",img_gray)
# cv2.imshow("Blur image", img_blur)
# cv2.imshow("Canny image",img_canny)
# cv2.waitKey(0)



import cv2

img = cv2.imread("resources/CV_image.png")
img = cv2.resize(img, (600, 800))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7,7),0)
img_canny = cv2.Canny(img_blur,100,100)

print(img.shape)
print(img_gray.shape)
print(img_blur.shape)
print(img_canny.shape)

cv2.imshow("Original image",img)
cv2.imshow("Grayscale image",img_gray)
cv2.imshow("Blur image", img_blur)
cv2.imshow("Canny image",img_canny)
cv2.waitKey(0)







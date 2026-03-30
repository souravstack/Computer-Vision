import cv2


# #Reading an image
# img = cv2.imread("resources/lena.png")
# # print(img.shape)
# print(img)
# cv2.imshow("Output", img)
# cv2.waitKey(0)




# Reading a video
# cap = cv2.VideoCapture("resources/elon.mp4")
# # print(cap)


# while True:
#     success, img = cap.read()

#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

 


 # Reading from webcam
cap = cv2.VideoCapture(0)

cap.set(3,640) 
cap.set(4,480)

# while True:
#     success, img = cap.read()

#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

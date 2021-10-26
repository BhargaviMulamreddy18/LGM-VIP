import cv2
video=cv2.VideoCapture(0)
while True:
    success,vid=video.read()
    gray_image=cv2.cvtColor(vid,cv2.COLOR_BGR2GRAY)
    inverted_image=255-gray_image
    blurred=cv2.GaussianBlur(inverted_image,(15,25),0)
    inverted_blurred=255-blurred
    pencil_sketch=cv2.divide(gray_image,inverted_blurred,scale=255)
    cv2.imshow("original image",vid)
    cv2.imshow("blurred sketch",pencil_sketch)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.waitKey(0)
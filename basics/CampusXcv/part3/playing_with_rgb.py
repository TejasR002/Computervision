# extracting each channel and showing image
import cv2
import numpy as np

#converting from RGB to grayscale image
image = cv2.imread("D:/cmputerVisionSimform/Images/Screenshot 2025-06-26 162615.jpg")
grey_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("bus", grey_image)
cv2.waitKey(0)

# extracting each channel and showing image using hstack() function
imgBlue = image[:,:,0]
imgGreen = image[:,:,1]
imgRed = image[:,:,2]


# cv2.imshow("bus", imgGreen)
# cv2.waitKey(0)

new_image = np.hstack((imgBlue,imgGreen,imgRed))

cv2.imshow("bus", new_image)

cv2.waitKey(0)


# cv2.imshow("bus", original)

# cv2.waitKey(0)








# comparing the original image with extracted channel images,
imgBlue = image.copy()
imgGreen = image.copy()
imgRed = image.copy()

# Zeroing out other channels
imgBlue[:, :, 1] = 0  # Green channel
imgBlue[:, :, 2] = 0  # Red channel

imgGreen[:, :, 0] = 0  # Blue channel
imgGreen[:, :, 2] = 0  # Red channel

imgRed[:, :, 0] = 0  # Blue channel
imgRed[:, :, 1] = 0  # Green channel
new_image_with_original = np.hstack((image,imgBlue,imgGreen,imgRed))

cv2.imshow("bus",new_image )
cv2.waitKey(0)
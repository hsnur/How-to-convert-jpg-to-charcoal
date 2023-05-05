import cv2

# Load the image of Iron Man
img = cv2.imread('ironman.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Increase the contrast of the image
gray = cv2.equalizeHist(gray)

# Create a black and white image using adaptive thresholding
bw = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Invert the image to get a white background and black lines
bw = cv2.bitwise_not(bw)

# Save the black and white image
cv2.imwrite('ironman_bw.jpg', bw)

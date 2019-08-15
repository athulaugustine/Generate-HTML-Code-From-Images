import cv2
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import numpy as np
def inverter(name):
    # Read the image
    img = cv2.imread(name, 0)
    # Thresholding the image
    (thresh, img_bin) = cv2.threshold(img, 128, 255,cv2.THRESH_BINARY| cv2.THRESH_OTSU)
    # Invert the image
    img_bin = 255-img_bin 
    cv2.imwrite(name,img_bin)
def sort_contours(cnts, method="left-to-right"):
	# initialize the reverse flag and sort index
	reverse = False
	i = 0
	# handle if we need to sort in reverse
	if method == "right-to-left" or method == "bottom-to-top":
		reverse = True
 
	# handle if we are sorting against the y-coordinate rather than
	# the x-coordinate of the bounding box
	if method == "top-to-bottom" or method == "bottom-to-top":
		i = 1
 
	# construct the list of bounding boxes and sort them from top to
	# bottom
	boundingBoxes = [cv2.boundingRect(c) for c in cnts]
	(cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
		key=lambda b:b[1][i], reverse=reverse))
 
	# return the list of sorted contours and bounding boxes
	return (cnts, boundingBoxes)
def slice(img_for_box_extraction_path):
	# Read the image"
	img = cv2.imread(img_for_box_extraction_path, 0)
	width=img.shape[1]
	height=img.shape[0]
	img = cv2.bitwise_not(img)
	(thresh, img_bin) = cv2.threshold(img, 1100, 255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
	#print len(img_bin)

	img_bin =255-img_bin 
	#cv2.imwrite("Image_bin.jpg",img_bin)
	# Defining a kernel length
	kernel_length = np.array(img).shape[1]/80
	#print kernel_length
	verticle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))

	# A horizontal kernel of (kernel_length X 1), which will help to detect all the horizontal line from the image.
	hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))

	# A kernel of (3 X 3) ones.
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

	# Morphological operation to detect vertical lines from an image
	img_temp1 = cv2.erode(img_bin, verticle_kernel, iterations=7)
	verticle_lines_img = cv2.dilate(img_temp1, verticle_kernel, iterations=7)
	#cv2.imwrite("verticle_lines.jpg",verticle_lines_img)
	# Morphological operation to detect horizontal lines from an image
	img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=7)
	horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=7)
	#cv2.imwrite("horizontal_lines.jpg",horizontal_lines_img)

	# Weighting parameters, this will decide the quantity of an image to be added to make a new image.
	alpha = 0.6
	beta = 1.0 - alpha


	# This function helps to add two image with specific weight parameter to get a third image as summation of two image.
	img_final_bin = cv2.addWeighted(verticle_lines_img, alpha, horizontal_lines_img, beta, 0.0)
	img_final_bin = cv2.erode(~img_final_bin, kernel, iterations=2)
	(thresh, img_final_bin) = cv2.threshold(img_final_bin, 1100, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

	#cv2.imwrite("blahhh.jpg",img_final_bin)

	# Find contours for image, which will detect all the boxes
	im2, contours, hierarchy = cv2.findContours(img_final_bin, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	# Sort all the contours by top to bottom.
	#(contours, boundingBoxes) = sort_contours(contours, method="top-to-bottom")
	'''for r in range(len(hierarchy)):
		if(hierarchy)
	#print hierarchy[0][0][3]'''
#-----------------------------------------------------------------------------------------------------
	#print hierarchy
	#Load Neural Network
	for c in contours:
		if True:
			#print hierarchy[0][index]
			# Returns the location and width,height for every contour
			x, y, w, h = cv2.boundingRect(c)
			#print index
			#if (w > 80 and h > 20) and index !=0:
			if True:
				new_img = img[y-20:y+h+10, x-35:x+w+35]
				cv2.imwrite(img_for_box_extraction_path, new_img)
                inverter(img_for_box_extraction_path)
				
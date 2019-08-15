import nn
import cv2
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import numpy as np
import csv
import random
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a=nn.NeuralNetwork(784,200,len(letters))
a.load("scratchpad/wih_mnist.txt","scratchpad/who_mnist.txt")
def inverter(name):
	# Read the image
	img = cv2.imread(name, 0)
	# Thresholding the image
	(thresh, img_bin) = cv2.threshold(img, 128, 255,cv2.THRESH_BINARY|     cv2.THRESH_OTSU)
	# Invert the image
	img_bin = 255-img_bin 
	cv2.imwrite(name,img_bin)

#inverter("testitem.png")
def detect(data)
	data=(np.asfarray(data)/255.0*0.99)+0.01
	output=a.guess(data)
	print "THE LETTER IS "+letters[np.argmax(output)]
	#inverter("testitem.png")



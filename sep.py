import numpy as np
from scipy.misc import imread,imsave
import random
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import cv2
import nn
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a=nn.NeuralNetwork(784,200,2)
a.load("scratchpad/wih_sep.txt","scratchpad/who_sep.txt")
for z in range(1):
	image = Image.open('stretched.jpg').convert('RGB')
	# initialise the drawing context with
	# the image object as background
	draw = ImageDraw.Draw(image)
	# desired size		 
	font = ImageFont.truetype('Arial.ttf', size=380)		 
	# starting position of the message
	#message = str(your_list[i][0]+" "+your_list[i][1])
	message=""
	for i in range(7):
		message=message+random.choice(letters)
	color = 'rgb(255,255,255)' # black color
	# draw the message on the background
	draw.text((0,50), message, fill=color, font=font)
	i=400
	j=0
	while i<=1500:
		print i
		area = (j,0, i, 400)
		cropped_img = image.crop(area)
		#cropped_img.save("pics/"+str(z)+str(i)+".jpg")
		cropped_img=cropped_img.resize((28,28),Image.ANTIALIAS)
		cropped_img=cropped_img.convert('1')
		cropped_img.save("pics/"+str(z)+str(i)+".jpg")
		data=list(cropped_img.getdata())
		data=(np.asfarray(data)/255.0*0.99)+0.01
		i=i+30
		j=j+30
		output=a.guess(data)
		if output[0]>output[1]:
			cropped_img.save("sep/"+str(z)+str(i)+".jpg")
			color = 'rgb(255,255,255)'
			#draw.line((j+15,0,j+15,400),fill=color)
		else:
			cropped_img.save("let/"+str(z)+str(i)+".jpg")
	image.save("FINAL.jpg")
#image.save("yayyy.jpg")

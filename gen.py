from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import random
import string
import nn
import numpy as np
import sys
import os
import io
import slicer
iterations=10000
def draw_button():
	source_img = Image.open("white.jpg")
	#start=random.randint(0,150)
	start=85
	chars = "".join( [random.choice(string.letters[:26]) for i in xrange(random.randint(1,10))] )
	draw = ImageDraw.Draw(source_img)
	draw.rectangle(((120, 150), (120+random.randint(100,350), 150+random.randint(50,150))), fill="black")
	draw.text((120+random.randint(10,40),150+random.randint(20,30)),chars, font=ImageFont.truetype("Arial.ttf",20))
	source_img.save("temp.jpg")
	source_img = Image.open("temp.jpg")
	slicer.slice("temp.jpg")
	source_img = Image.open("temp.jpg")
	source_img=source_img.resize((28,28),Image.ANTIALIAS)
	source_img=source_img.convert('1')
	#os.remove("temp.jpg")
	data=list(source_img.getdata())
	data=(np.asfarray(data)/255.0*0.99)+0.01
	return data


def draw_table():
	source_img = Image.open("white.jpg")
	#start=random.randint(0,150)
	start=85
	draw = ImageDraw.Draw(source_img)
	a=start+random.randint(100,300)
	b=start+random.randint(50,300)
	columns=random.randint(2,5)
	rows=columns+random.randint(2,5)
	draw.rectangle(((start, start), (a,b)),outline="black")
	increment=(b-start)/rows
	for i in range(rows):
		draw.line((start,start+(i*increment),a,start+(i*increment)), fill="black",width=3)
	increment=(a-start)/columns
	for i in range(columns):
		draw.line((start+(i*increment),start,start+(i*increment),b),fill="black",width=3)
	source_img.save("temp.jpg")
	source_img = Image.open("temp.jpg")
	source_img=source_img.resize((28,28),Image.ANTIALIAS)
	source_img=source_img.convert('1')
	#os.remove("temp.jpg")
	data=list(source_img.getdata())
	data=(np.asfarray(data)/255.0*0.99)+0.01
	return data


def draw_text():
	source_img = Image.open("white.jpg")
	draw = ImageDraw.Draw(source_img)
	start=random.randint(0,150)
	draw = ImageDraw.Draw(source_img)
	draw.rectangle(((start, start), (start+random.randint(100,350), start+random.randint(50,150))), outline="black")
	for j in range(random.randint(0,3)):
		chars = "".join( [random.choice(string.letters[:26]) for i in xrange(random.randint(1,40))] )
		draw.text((start,start+(j*10)),chars,font=ImageFont.truetype("Arial.ttf",10),fill=(0,0,0,255))
	source_img.save("temp.jpg")
	source_img = Image.open("temp.jpg")
	#slicer.slice("temp.jpg")
	source_img=source_img.resize((28,28),Image.ANTIALIAS)
	#source_img.show()
	source_img=source_img.convert('1')
	os.remove("temp.jpg")
	data=list(source_img.getdata())
	data=(np.asfarray(data)/255.0*0.99)+0.01
	return data
max=-1

for h in range(100):
	a=nn.NeuralNetwork(784,100,3)
	print a.wih.shape[0]
	print a.wih.shape[1]
	print "Starting"

	for i in range(iterations):
		 print i
		 l=random.randint(0,2)
		 if l==0:
			array=draw_button()
			a.feedforward(array,[1,0.01,0.01])

		 if l==1:
			array=draw_table()
			a.feedforward(array,[0.01,1,0.01])
		 if l==2:
			array=draw_text()
			a.feedforward(array,[0.01,0.01,1])
		 print i

	correct=0
	but=0
	tab=0
	txt=0
	for i in range(iterations):
		l=random.randint(0,2)
		print "Hey"+str(i)
		if l==0:
			array=draw_button()
			r=a.guess(array)
			if r.argmax()==0:
				correct=correct+1
				but=but+1
		if l==1:
			array=draw_table()
			r=a.guess(array)
			if r.argmax()==1:
				correct=correct+1
				tab=tab+1
		if l==2:
			array=draw_text()
			r=a.guess(array)
			if r.argmax()==2:
				correct=correct+1
				txt=txt+1
		print i
	print "Testing Done"
	print str(correct)+"for "+str(h)
	if correct>max:
		max=correct
		print "writing!"
		if correct>9000:
			a.save("wih.txt","who.txt")
#b=nn.NeuralNetwork(10000,100,3)
#b.load()
for i in range(iterations):
		l=random.randint(0,2)
		if l==0:
			array=draw_button()
			r=b.guess(array)
			if r.argmax()==0:
				correct=correct+1
				but=but+1
		if l==1:
			array=draw_table()
			r=b.guess(array)
			if r.argmax()==1:
				correct=correct+1
				tab=tab+1
		if l==2:
			array=draw_text()
			r=b.guess(array)
			if r.argmax()==2:
				correct=correct+1
				txt=txt+1
		print i
print "Final correct"+str(correct)


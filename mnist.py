
import random
import nn
import numpy as np
import csv
iteration=10000
letters="ABCDEFGHHIJKLMNOPQRSTUVWXYZ"
a=nn.NeuralNetwork(784,200,len(letters))
def inverter(data):
	data=np.asfarray(data)
	for i in range(len(data)):
		data[i]=255-data[i]
	return data
def listmaker(temp):
	target=[]
	for i in range(len(letters)):
		if i==temp:
			target.append(0.99)
		else:
			target.append(0.01)
	return target
with open("data2.csv", "r") as f:
		datareader = csv.reader(f)
		main_list=list(datareader)

print "starting"

for j in range(60000):
	print j
	row=random.randint(0,372000)
	data=main_list[row][1:]
	#data=inverter(data)
	data=((np.asfarray(data)/255.0)*0.99)+0.01
	targets=listmaker(int(main_list[row][0]))
	a.feedforward(data,targets)

print "Testing"

correct=0
for j in range(iteration):
	print j
	row=random.randint(0,372000)
	data=main_list[row][1:]
	#data=inverter(data)
	data=((np.asfarray(data)/255.0)*0.99)+0.01
	output=a.guess(data)
	big=np.argmax(output)
	if big==int(main_list[row][0]):
		correct=correct+1
print "final result "+str(correct)
a.save("scratchpad/wih_mnist.txt","scratchpad/who_mnist.txt")
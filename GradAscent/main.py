import numpy as np
import csv

def sigmoid(inX):
	return 1.0/(1+exp(-inX))

def gradAscent(dataMatIn, classLabels):
	dataMatrix = np.mat(dataMatIn)
	labelMat = np.mat(classLabels).transpose()
	m,n = shape(dataMatrix)
	alpha = 0.001
	maxCyclass = 500
	weights = np.ones((n,1))
	for k in range(maxCyclass):
		h = sigmoid(dataMatrix*weight)
		error = (label - h)
		weights = weights + alpha * dataMatrix.transpose() * error

	return weights

def getData(filePath):
	csvfile = open(filePath, 'rb')
	reader = csv.reader(csvfile)
	for row in reader:
		print row

def gradDescent(x, y, theta, alpha, m, maxIter):
	a = 1


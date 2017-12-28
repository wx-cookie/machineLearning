import numpy as np


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

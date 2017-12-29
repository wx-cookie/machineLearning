import numpy as np
import csv
import pandas as pd
def sigmoid(inX):
	return 1.0/(1+exp(-inX))

def gradAscent_1(dataMatIn, classLabels):
	dataMatrix = np.mat(dataMatIn)
	labelMat = np.mat(classLabels).transpose()
	m,n = np.shape(dataMatrix)
	alpha = 0.001
	maxCyclass = 500
	weights = np.ones((n,1))
	for k in range(maxCyclass):
		h = sigmoid(dataMatrix*weights)
		error = (labelMat - h)
		weights = weights + alpha * dataMatrix.transpose() * error
	return weights

def sigmoid(x):
	return 1.0/(1+np.exp(-x))

def gradAscent(x, y, theta, alpha, maxIter):
	for i in range(maxIter):
		h = sigmoid(np.dot(x, theta))
		error = y.T - h
		theta = theta + alpha * np.dot(x.T, error)
	return theta

#get datas and insert x
def getDataAndX(filePath, column, num):
	data = pd.read_csv(filePath, header=None)
	x = data.iloc[:,0:column]
	y = data.iloc[:,-1]
	x.insert(0,3,num)
	x.columns = range(0,column+1)
	return x, y

def getData(filePath, column):
	data = pd.read_csv(filePath, header=None)
	return data.iloc[:,0:column], data.iloc[:,-1]

def gradDescent(x, y, theta, alpha, maxIter):
	xTrain = x.T
	for i in range(maxIter):
		hypoth = np.dot(x, theta)
		theta = theta - alpha*(np.dot(xTrain, hypoth-y))
	return theta


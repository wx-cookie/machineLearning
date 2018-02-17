from numpy as np
import time

def calcKernelValue(matrix_x, sample_x, option):
	if option == 'linear':
		kernelValue = matrix_x * sample_x.T

	return kernelValue


def calcKernelMatrix(train_x, option):
	m = train_x.shape[0]
	kernelMatrix = np.zeros((m.m))
	for i in range(m):
		kernelMtrix[:,i] = calcKernelValue(train_x, train_x[i,:], option)
	return kernelMatrix

class SVMStruct:
	def __init__(self, dataSet, labels, C, toler, option):
		self.train_x = dataSet
		self.train_y = labels
		self.C = C
		self.toler = toler
		self.numSamples = dataSet.shape[0]
		self.alphas = np.zeros((self.numSamples, 1))
		self.b = 0
		self.errorCache = np.zeros((self.numSamples, 2))
		self.kernelOpt = option
		self.kernelMat = calcKernelMatrix(self.train_x, option)

# output_k ???
def calcError(svm, alpha_k):
	output_k = float()
	error_k = output_k - float(svm.train_y[alpha_k])
	return error_k


def updateError(svm, alpha_k):
	error = calcError(svm, alpha_k)
	svm.errorCache[alpha_k] = error


# alpha_i ?? error_i ??
def selectAlpha_j(svm, alpha_i, error_i):


import csv
import random
import math
from sklearn.naive_bayes import GaussianNB
def loadCsv(filename):
  lines = csv.reader(open(filename,"rb"))
  dataset = list(lines)
  for i in range(len(dataset)):
    dataset[i] = [float(x) for x in dataset[i]]

  return dataset

def splitDataset(dataset, splitRatio):
  trainSize = int(len(dataset)*splitRatio)
  trainSet = []
  copy = list(dataset)
  while len(trainSet)<trainSize:
    index = random.randrange(len(copy))
    trainSet.append(copy.pop(index))

  return [trainSet, copy]

def seperateByClass(dataset):
  seperated = {}
  for i in range(len(dataset)):
    vector = dataset[i]
    if(vector[-1] not in seperated):
      seperated[vector[-1]] = []
    seperated[vector[-1]].append(vector)
  return seperated

def mean(numbers):
  return sum(numbers)/float(len(numbers))

def stdev(nums):
  avg = mean(nums)
  variance = sum([pow(x-avg, 2)for x in nums])/float(len(nums)-1)
  return math.sqrt(variance)

def summarize(dataset):
  summ = [(mean(att), stdev(att)) for att in zip(*dataset)]
  del summ[-1]
  return summ

def summByClass(dataset):
  seperated = seperateByClass(dataset)
  summ = {}
  for classValue,params in seperated.iteritems():
    summ[classValue] = summarize(params)
  return summ

def calculateProbability(x, mean, stdev):
  exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
  return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent

def calculateClassProbabilities(summaries, inputVector):
  probabilities = {}
  for classValue, classSummaries in summaries.iteritems():
    probabilities[classValue] = 1
    for i in range(len(classSummaries)):
      mean, stdev = classSummaries[i]
      x = inputVector[i]
      probabilities[classValue] *= calculateProbability(x, mean, stdev)
  return probabilities

def predit(summaries, inputVector):
  probs = calculateClassProbabilities(summaries, inputVector)
  print probs
  bestLabel = None;
  bestPro = -1;
  for classValue, prob in probs.iteritems():
    if bestLabel is None or prob > bestPro:
      print classValue
      bestLabel = classValue
      bestPro = prob
  return bestLabel

def getPredictions(summaries, dataset):
  res = []
  for i in range(len(dataset)):
    res.append(predit(summaries, dataset[i])) 
  return res

def getAccuracy(testset, prediction):
  count = 0
  for i in range(len(testset)):
    if testset[i][-1] == prediction[i]:
      count +=1
  return count/float(len(testset))*100

#use sklearn naiveBayes
def skearn_bayes(trainset, testset):
  trainData = [data[0:-1] for data in trainset]
  trainLabel = [data[-1] for data in trainset]
  testData = [data[0:-1] for data in testset]
  testLabel = [data[-1] for data in testset]
  gnb = GaussianNB()
  y_pred = gnb.fit(trainData, trainLabel).predict(testData)
  print (y_pred != testLabel).sum()

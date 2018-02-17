from math import log
import operator
def createDataSet():
    dataSet=[[1.,1.,1.,'yes'],[1.,1.,1.,'yes'],[1.,0.,1.,'no'],[0.,1.,0.,'no'],[0.,1.,0.,'no'],[0.,0.,0.,'yes'],[0.,0.,1.,'no'],[1.,0.,1.,'no'],[1.,0.,0.,'no']]
    labels = ['no surfaceing','flippers','test']
    return dataSet, labels

def calcShannonEnt(dataset):
    num = len(dataset)
    labelCount = {}
    for data in dataset:
        label = data[-1]
        if(label not in labelCount):
            labelCount[label] = 0
        labelCount[label] +=1
    res = 0.0
    for key in labelCount:
        p = float(labelCount[key])/num
        res -=p*log(p,2)
    return res

def splitDataSet(dataset, axis, value):
    resData = []
    for data in dataset:
        if(data[axis] == value):
            temp = data[:axis]
            temp.extend(data[axis+1:])
            resData.append(temp)
    return resData

def splitContinueDataSet(dataset, axis, value, direction):
    resData = []
    for data in dataset:
        if direction==0:
            if data[axis] > value:
                temp = data[:axis]
                temp.extend(data[axis+1:])
                resData.append(temp)
        if direction == 1:
            if data[axis] <= value:
                temp = data[:axis]
                temp.extend(data[axis+1:])
                resData.append(temp)
    return resData
    

def chooseBestFeatureToSplit(dataset):
    p = calcShannonEnt(dataset)
    numFeature = len(dataset[0])-1
    bestIndex = -1
    bestRes = 0.0
    for i in range(numFeature):
        featList = [example[i] for example in dataset]
        featSet = set(featList)
        tempEnt = 0.0
        for feat in featSet:
            subData = splitDataSet(dataset, i, feat)
            subP = calcShannonEnt(subData)
            tempEnt +=  len(subData)/float(len(dataset))*subP;
        tempRes = p - tempEnt
        if tempRes > bestRes:
            bestRes = tempRes
            bestIndex = i
    return bestIndex

def chooseBestFeatToSplit(dataset):
    H = calcShannonEnt(dataset)
    numFeat = len(dataset[0])-1
    bestIndex = -1
    bestRes = 0.0
    for i in range(numFeat):
        featList = [example[i] for example in dataset]
        if type(featList[0]).__name__=='float' or type(featList[0]).__name__=='int':
            sortFeatList =sorted(featList)
            splitList = []
            splitListIndex = -1
            bestSplitEnt = 1000
            for j in range(len(sortFeatList)-1):
                splitList.append((sortFeatList[j]+sortFeatList[j+1])/2.0)
            print splitList
            for j in range(len(splitList)):
                print '----------'+str(j)
                tempEnt = 0.0
                split0 = splitContinueDataSet(dataset, i, splitList[j], 0)
                print split0
                split1 = splitContinueDataSet(dataset, i, splitList[j], 1)
                print split1
                pro0 = calcShannonEnt(split0)
                pro1 = calcShannonEnt(split1)
                tempEnt -=(len(split0))/float(len(dataset))*pro0
                tempEnt -=(len(split1))/float(len(dataset))*pro1
                if tempEnt < bestSplitEnt:
                    bestSplitEnt = tempEnt
                    splitListIndex = j
            tempRes = H - bestSplitEnt
            if tempRes > bestRes:
                bestRes = tempRes
                bestIndex = i
    return bestIndex

def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    return max(classCount)

def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel : {}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree


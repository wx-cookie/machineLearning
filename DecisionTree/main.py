import trees

dataset, labels = trees.createDataSet()
res = trees.calcShannonEnt(dataset)
splitData = trees.splitDataSet(dataset, 0, 1)
bestIndex = trees.chooseBestFeatureToSplit(dataset)
bestContinueIndex = trees.chooseBestFeatToSplit(dataset)

myTree = trees.createTree(dataset, labels);
print myTree

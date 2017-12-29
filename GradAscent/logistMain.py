import main
import logRegres as lg
import numpy as np
a, b = main.getDataAndX('test.csv', 2, 1)
data, label = lg.loadDataSet()
weight = lg.gradAscent(data, label)
print weight

theta = np.ones(3)
theta = main.gradAscent(a,b,theta, 0.001,500)
print theta

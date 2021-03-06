from numpy import *
import logRegres

dataArr, labelMat = logRegres.loadDataSet()
weights = logRegres.gradAscent(dataArr, labelMat)
logRegres.plotBestFit(weights.getA())

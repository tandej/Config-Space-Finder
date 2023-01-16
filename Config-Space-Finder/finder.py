import constraints
import kinematics

import matplotlib.pyplot as plt
import numpy as np

import math

samplingDensity = 200 # how many samples should be made per linear distance unit
xDimensionAngular = True
yDimensionAngular = True

spatialPoints = []
configPoints = []

rects = constraints.getConstrainedAreas()

for rect in rects:
    for x in np.arange(rect[0], rect[1], 1 / samplingDensity):
        for y in np.arange(rect[2], rect[3], 1 / samplingDensity):
            spatialPoints.append([x,y])

for point in spatialPoints:
    ikSols = kinematics.inverseKinematics(point[0], point[1])

    for sol in ikSols:
        if sol[2]:
            configPoints.append([sol[0], sol[1]])

pointXs = []
pointYs = []

for point in configPoints:
    if (xDimensionAngular):
        pointXs.append(((point[0] + math.pi) % (2 * math.pi)) - math.pi)
    else:
        pointXs.append(point[0])
    if (yDimensionAngular):
        pointYs.append(((point[1] + math.pi) % (2 * math.pi)) - math.pi)
    else:
        pointYs.append(point[1])

fig = plt.figure()
fig.add_subplot().scatter(pointXs, pointYs)

plt.show()
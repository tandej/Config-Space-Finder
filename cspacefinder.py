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

for rect in constraints.getConstrainedSpatialAreas():
    for x in np.arange(rect[0], rect[1], 1 / samplingDensity):
        for y in np.arange(rect[2], rect[3], 1 / samplingDensity):
            spatialPoints.append([x,y])

for point in spatialPoints:
    ikSols = kinematics.inverseKinematics(point[0], point[1])

    for sol in ikSols:
        if sol[2]:
            configPoints.append([sol[0], sol[1]])

for rect in constraints.getConstrainedConfigAreas():
    for x in np.arange(rect[0], rect[1], 1 / samplingDensity):
        for y in np.arange(rect[2], rect[3], 1 / samplingDensity):
            configPoints.append([x,y])

pointXs = []
pointYs = []

for point in configPoints:
    if (xDimensionAngular):
        ang = ((point[0] + math.pi) % (2 * math.pi)) - math.pi
        if (ang < -math.pi / 2):
            ang += 2 * math.pi
        pointXs.append(ang)
    else:
        pointXs.append(point[0])
    if (yDimensionAngular):
        ang = ((point[1] + math.pi) % (2 * math.pi)) - math.pi
        pointYs.append(ang)
    else:
        pointYs.append(point[1])

fig = plt.figure()
fig.add_subplot().scatter(pointXs, pointYs)

plt.show()
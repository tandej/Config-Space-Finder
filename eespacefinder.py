import kinematics
import constraints

import math

import numpy as np
import matplotlib.pyplot as plt

def inRange(a: float, b: float, check: float) -> bool:
    return ((a < check and b > check) or (a > check and b < check))

samplingDensity = 20

vectorSamplingDensity = 20

xPoints = []
yPoints = []

prevPercent = -1

for x in np.arange(0, 2 * math.pi, 1 / samplingDensity):
    percent = round((x / (2 * math.pi)) * 100)
    if (percent != prevPercent):
        print(str(percent) + "%")
        prevPercent = percent

    for y in np.arange(-math.pi, math.pi, 1 / samplingDensity):
        point = kinematics.forwardKinematics(x,y)

        goodSoFar = True

        for rect in constraints.getConstrainedConfigAreas():
            if goodSoFar:
                if (inRange(rect[0], rect[1], x) and inRange(rect[2], rect[3], y)):
                    goodSoFar = False
                        
        for rect in constraints.getConstrainedSpatialAreas(): 
            for i in range(vectorSamplingDensity):
                if goodSoFar:
                    svx = (i / vectorSamplingDensity) * point[0]
                    svy = (i / vectorSamplingDensity) * point[1]
                    evx = (i / vectorSamplingDensity) * (point[2] - point[0]) + point[0]
                    evy = (i / vectorSamplingDensity) * (point[3] - point[1]) + point[1]
                    if inRange(rect[0], rect[1], svx) and inRange(rect[2], rect[3], svy):
                        goodSoFar = False
                    elif inRange(rect[0], rect[1], evx) and inRange(rect[2], rect[3], evy):
                        goodSoFar = False

        if goodSoFar:
            xPoints.append(point[2])
            yPoints.append(point[3])

if (prevPercent != 100):
    print("100%")

fig = plt.figure()
fig.add_subplot().scatter(xPoints, yPoints)

plt.show()
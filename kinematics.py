import math

segALength = 0.9
segBLength = 0.7

# must return a list of [elbowX, elbowY, endX, endY]
def forwardKinematics(thetaA: float, thetaB: float) -> list: # keep this method!
    cThetaA = thetaA % (2*math.pi)
    cThetaB = thetaB % (2*math.pi)

    elbowX = segALength * math.cos(cThetaA)
    elbowY = segALength * math.sin(cThetaA)

    eeX = (segBLength * math.cos(cThetaB)) + elbowX
    eeY = (segBLength * math.sin(cThetaB)) + elbowY

    return [elbowX, elbowY, eeX, eeY]
    
# must return a list of lists in format: [[dimensionAValue: float, dimensionBValue: float, isDefined: boolean], ...]
def inverseKinematics(x: float, y: float) -> list: # keep this method!
    if (segALength + segBLength < math.sqrt(x**2 + y**2)):
        return [[0,0,False]]
    elif (abs(segALength - segBLength) > math.sqrt(x**2 + y**2)):
        return [[0,0,False]]
    elif (x == 0 and y == 0):
        return [[0,0,False]]
    else:
        gamma = math.atan2(y, x)
        cosAlpha = (x**2 + y**2 + segALength**2 - segBLength**2) / (2 * segALength * math.sqrt(x**2 + y**2))
        cosBeta = (segALength**2 + segBLength**2 - x**2 - y**2) / (2 * segALength * segBLength)

        if (abs(cosAlpha) > 1 or abs(cosBeta) > 1):
            return [[0,0,False]]

        alpha = math.acos(cosAlpha)
        beta = math.acos(cosBeta)

        return [[gamma - alpha,math.pi - beta, True], [gamma + alpha, beta - math.pi, True]]

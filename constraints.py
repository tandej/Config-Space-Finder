import math

# Constrained areas should be represented as a list of rectangles, in format [[x_0, x_1, y_0, y_1],[x_2, x_3, y_2, y_3],...]

groundLimit = [[-2, 2, -5, -0.18]]
robotChassisLimit = [[-0.5, 0.5, -0.18, 0]]
heightLimit = [[-2, 2, 1.8, 5]]
plusExtensionLimit = [[1.45,3,-2,2]]
minusExtensionLimit = [[-1.9,-3,-2,2]]

def getConstrainedSpatialAreas() -> list:  # keep this method!
    return groundLimit + robotChassisLimit + heightLimit + plusExtensionLimit + minusExtensionLimit
    
armInterferencePlusLimit = [[-4,4,3,math.pi]]
armInterferenceMinusLimit = [[-4,4,-math.pi,-3]]

def getConstrainedConfigAreas() -> list: # keep this method!
    return armInterferencePlusLimit + armInterferenceMinusLimit
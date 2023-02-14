import math

# Constrained areas should be represented as a list of rectangles, in format [[x_0, x_1, y_0, y_1],[x_2, x_3, y_2, y_3],...]

groundLimit = [[-3, 3, -3, -0.225]]
superstructureLimit = [[-0.32, 0.21, -3, 0]]
robotChassisLimit = [[-0.625, 0.3, -3, -0.1]]
heightLimit = [[-2, 2, 1.75, 3]]
plusExtensionLimit = [[1.51,3,-3,3]]
minusExtensionLimit = [[-1.87,-3,-3,3]]

# intakeRetractedInterferenceLimit = [[-0.8,-0.5,0,0.5]]
# intakeExtendedInterferenceLimit = [[-1.2, -0.8, -0.18, 0]]

def getConstrainedSpatialAreas() -> list:  # keep this method!
    return groundLimit + superstructureLimit + robotChassisLimit + heightLimit + plusExtensionLimit + minusExtensionLimit # + intakeRetractedInterferenceLimit
    
armInterferencePlusLimit = [[-math.pi,math.pi,3,math.pi]]
armInterferenceMinusLimit = [[-math.pi,math.pi,-math.pi,-3]]

def getConstrainedConfigAreas() -> list: # keep this method!
    return armInterferencePlusLimit + armInterferenceMinusLimit
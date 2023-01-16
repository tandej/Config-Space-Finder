# Constrained areas should be represented as a list of rectangles, in format [[x_0, x_1, y_0, y_1],[x_2, x_3, y_2, y_3],...]

groundLimit = [[-2, 2, -5, -0.2]]
robotChassisLimit = [[-0.5, 0.5, -0.2, 0]]
heightLimit = [[-2, 2, 1.5, 5]]

def getConstrainedAreas() -> list:  # keep this method!
    return groundLimit + robotChassisLimit + heightLimit
    
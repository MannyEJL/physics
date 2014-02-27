# Ex input: N 30 E
# Ex output: 60
import math
a = raw_input('magnitude n direction pls, k thanks: ')
b = a.split()

b[0] = float(b[0])
b[2] = float(b[2])
def directionToDegree(dir1, angle, dir2):
    directions = 'enws'
    plus = 'nw se en ws'
    minus = 'ne sw wn es'
    newAngle = 0
    newDir = dir1 + dir2
    newAngle = (directions.index(dir1)*90)
    if newDir in plus:
        newAngle = newAngle + angle
    else:
        newAngle = newAngle - angle
    print newAngle
    return newAngle
    
c = math.radians(directionToDegree(b[1], b[2], b[3]))
xcomp = math.cos(c) * b[0]
ycomp = math.sin(c) * b[0]
print 'xcomp: {0:.2f}'.format(xcomp)
print 'ycomp: {0:.2f}'.format(ycomp)
# Ex input: N 30 E
# Ex output: 60
import math
a = raw_input('direction pls: ')
b = a.split()
print b
b[1] = float(b[1])
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
    
c = math.radians(directionToDegree(b[0], b[1], b[2]))
#Just some random vector with a magnitude of 10
xcomp = math.cos(c) * 10
ycomp = math.sin(c) * 10
print xcomp
print ycomp
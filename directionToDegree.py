import math

b = raw_input('Enter a vector: ').split()
xcomp, ycomp = 0,0

try:
	b[0] = float(b[0])
	b[2] = float(b[2])
except IndexError:
	pass
except ValueError:
	b = 'b'
	
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
    #return newAngle
    newAngle = math.radians(newAngle)
    return math.cos(newAngle) * b[0], math.sin(newAngle) * b[0]

if len(b) == 2:
	xcomp, ycomp = directionToDegree(b[1], 0, '')
elif len(b) == 4:
	xcomp, ycomp = directionToDegree(b[1], b[2], b[3])
else:
	print "You didn't enter a valid vector."
	print "Expected: Magtinude, Direction 1, Angle, Direction 2"

print 'xcomp: {0:.2f}'.format(xcomp)
print 'ycomp: {0:.2f}'.format(ycomp)

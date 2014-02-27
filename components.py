import math

def vectorToComponents(hypo, dir1, angle, dir2):
	#Splits a vector into its two x,y components
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
    newAngle = math.radians(newAngle)
    return math.cos(newAngle) * hypo, math.sin(newAngle) * hypo


def getVectorInput():
	#Stores vectors as list
	#[Vector Number][Magtinude, Direction 1, Angle, Direction 2]
	b = []
	count = 0
	print "Example input> Magtinude, Direction 1, Angle, Direction 2"
	print "Example input> 10 n 60 e \n"
	while True:
		b.append(raw_input('Enter a vector or press enter to calculate: ').split())
		if len(b[count]) == 0:
			b.pop()
			return b
		try:
			#French support. Ouest=West
			for i in range(len(b[count])):
				if b[count][i] == 'o':
					b[count][i] = 'w'
			b[count][0] = float(b[count][0])
			b[count][2] = float(b[count][2])
		except IndexError:
			pass
		except ValueError:
			b.pop()
		count = count + 1
		
def componentToVector(xcomp, ycomp):
	#Gets list of components and finds the sum
	#Returns new vectors length and angle
	x = 0
	y = 0
	for i in xcomp:
		x = x + i
	for i in ycomp:
		y = y + i
	d = math.sqrt(x**2+y**2)
	theta = math.degrees(math.atan(abs(y)/abs(x)))
	return d, theta, x, y

def componentToDirection(x,y):
	a = ''
	b = ''
	if x > 0:
		a = 'E'
	else:
		a = 'W'
	if y > 0:
		b = 'N'
	else:
		b = 'S'
	return a,b

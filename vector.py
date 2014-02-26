'''
Created on 2014-02-25

@author: Emanuel
'''
from sympy import *
import math

inputVectors = []
singleVectors = []
ysteps = []
xsteps = []
#singleVectors[vector number][spot]
# 0 - number
# 1 - unit
# 2 - first direction
# 3 - angle
# 4 - second direction
count = 0
xcomponent = 0
ycomponent = 0
xtemp = 0
ytemp = 0
ns = 'n s'
ew = 'e w o'

def plusorminus(number, direction):
	if direction == 'n':
		ysteps.append(number)
		return number
	elif direction == 's':
		ysteps.append(number*-1)
		return number * -1
	elif direction == 'e':
		xsteps.append(number)
		return number
	elif direction == 'w' or direction == 'o':
		xsteps.append(number*-1)
		return number * -1


def componentToVector(x, y):
	x = abs(x)
	y = abs(y)
	d = sqrt(x**2+y**2)
	theta = math.degrees(math.atan(y/x))
	return d, theta
	
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
		
while True:
	inputVectors.append(raw_input('Enter a vector or press enter to quit: '))
	if len(inputVectors[count]) < 1:
		inputVectors.pop()
		break
	else:
		singleVectors.append(inputVectors[count].split())
	
	count = count + 1

for i in range(len(singleVectors)):
	singleVectors[i][0] = float(singleVectors[i][0])
	if len(singleVectors[i]) == 3:
		if singleVectors[i][2] in ns:
			ycomponent = ycomponent + plusorminus(singleVectors[i][0], singleVectors[i][2])
		else:
			xcomponent = xcomponent + plusorminus(singleVectors[i][0], singleVectors[i][2])
	elif len(singleVectors[i]) == 5:
		singleVectors[i][3] = math.radians(float(singleVectors[i][3]))
		if singleVectors[i][2] in  ns:
			ytemp = math.cos(singleVectors[i][3]) * singleVectors[i][0]
			ycomponent = ycomponent + plusorminus(ytemp, singleVectors[i][2])
			xtemp = math.sin(singleVectors[i][3]) * singleVectors[i][0]
			xcomponent = xcomponent + plusorminus(xtemp, singleVectors[i][4])
		else:

			ytemp = math.sin(singleVectors[i][3]) * singleVectors[i][0]
			ycomponent = ycomponent + plusorminus(ytemp, singleVectors[i][4])
			xtemp = math.cos(singleVectors[i][3]) * singleVectors[i][0]
			xcomponent = xcomponent + plusorminus(xtemp, singleVectors[i][2])
	else:
		pass
print
print "Y components:"
for i in ysteps:
	print i
print '----------'
print ycomponent
print
print "X components:"
for i in xsteps:
	print i
print '----------'
print xcomponent
print
d, theta = componentToVector(xcomponent, ycomponent)
dir1, dir2 = componentToDirection(xcomponent, ycomponent)
print "The resulting vector is: {0:.2f} {1} [{2} {3:.2f} {4}]".format(float(d), singleVectors[0][1], dir1, float(theta), dir2)
print "It can also be expressed as : {0:.2f} {1} [{2} {3:.2f} {4}]".format(float(d), singleVectors[0][1], dir2, (90-float(theta)), dir1)

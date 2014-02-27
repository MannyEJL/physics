from components import getVectorInput, vectorToComponents, componentToVector, componentToDirection

b = getVectorInput()
xcomp, ycomp= ['' for i in range(len(b))], ['' for i in range(len(b))]

for i in range(len(b)):
	if len(b[i]) == 2:
		xcomp[i], ycomp[i] = vectorToComponents(b[i][0], b[i][1], 0, '')
	else:
		xcomp[i], ycomp[i] = vectorToComponents(b[i][0], b[i][1], b[i][2], b[i][3])
		
d, theta, fx, fy = componentToVector(xcomp, ycomp)
	
comps = ['Vectors', 'X Components', 'Y Components']
table = zip(b, xcomp, ycomp)
print "\n {:>15}{:>15}{:>15}".format(*comps)
for a,b,c in table:
	a = ' '.join(map(str, a))
	print "{:>15}{:>15.2f}{:>15.2f}".format(a,b,c)
print "{:>15}{:>15}{:>15}".format('', '--------', '--------')
print "{:>15}{:>15.2f}{:>15.2f}".format('', fx, fy)
dir1, dir2 = componentToDirection(fx, fy)
print "\n{:<26} {:.2f} [{} {:.2f} {}]".format("The resulting vector is: ", float(d), dir1, float(theta), dir2)
print "{:<26} {:.2f} [{} {:.2f} {}]".format("You can also write it as: ", float(d), dir2, (90-float(theta)), dir1)

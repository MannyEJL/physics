import math

def timeY(viy):
	return (2*viy)/9.81

def distanceX(vix, t):
	return vix*t

while True:
	try:
		magnitude = float(raw_input("Enter the projectile speed: "))
		angle = math.radians(float(raw_input("Enter the projectile angle: ")))
		break
	except:
		pass

xcomp = math.cos(angle) * magnitude
ycomp = math.sin(angle) * magnitude
time = timeY(ycomp)
dx = distanceX(xcomp, time)
row_format = "{:<12}: {:<6.2f}"
print row_format.format('X Component', xcomp)
print row_format.format('Y Component', ycomp)
print row_format.format('Time', time)
print row_format.format('X Distance', dx)

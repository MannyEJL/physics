#!/usr/bin/env python
'''
Emanuel Raad
2014-18-02

Converts speeds for 2D physics. 
Todo list:
  -add acceleration
  -add 5 kinematic equations
  -add multiple questions. get all answers
  ex: input 1+2, 2+3, 3+4, 4+5
      output 3,5,7,9
      ^you can easily check the answers to multiple kinematic questions
      
Features:
  -convert speeds
'''
# steps = []
distanceUnits = ['ft', 'm', 'km']
timeUnits = ['s', 'min', 'h']

def validateInput(word):    
    while True:
        a = raw_input("Input your " + word + " unit [distance/time]: ").lower()
        d = a.split('/')[0]
        t = a.split('/')[1]
        if d in distanceUnits and t in timeUnits:
            return d,t
        else:
            print "You didn't enter a supported unit:"

def convertDistance(number, unit):
    if distanceSpot == 0:
        return number
    elif distanceSpot < 0:
        return number * (1/distanceUnitsN[int(distanceUnits.index(unit))])
    elif distanceSpot > 0:
        return number * distanceUnitsN[int(distanceUnits.index(unit))]

def convertTime(number, unit):
    if timeSpot == 0:
        return number
    elif timeSpot < 0:
        return number * (1/timeUnitsN[int(timeUnits.index(unit))])
    elif timeSpot > 0:
        return number * timeUnitsN[int(timeUnits.index(unit))]

print "=====SPEED CONVERSION====="
print "  Distance: " + ', '.join(distanceUnits)
print "  Time    : " + ', '.join(timeUnits)
print "=========================="

startValue = float(raw_input("Input your starting number: "))
distanceStart, timeStart = validateInput('starting')
distanceEnd, timeEnd = validateInput('ending')

distanceUnitsN = [3.281, 1, 1000.0]
distanceSpot = int(distanceUnits.index(distanceStart)) - int(distanceUnits.index(distanceEnd)) 
timeUnitsN = [60.0, 1, 60.0]
timeSpot = int(timeUnits.index(timeStart)) - int(timeUnits.index(timeEnd))

currentDistance = convertDistance(convertDistance(startValue, distanceStart), distanceEnd)
currentTime = convertTime(convertTime(1, timeStart), timeEnd)
currentValue = currentDistance / currentTime
print "{0} {1}/{2} = {3} {4}/{5}".format(startValue, distanceStart, timeStart, currentValue, distanceEnd, timeEnd)

# showSteps = raw_input("Would you like to see the steps?").lower()
# yes = ['yes', 'y', 'ok', 'sure']
#  
# if showSteps in yes:
#     for i in steps:
#         print i
# else:
#     print "Okay :("


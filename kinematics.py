'''
Created on 2014-02-23

@author: Emanuel
'''
from sympy import *

data = [i for i in range(5)]
data[0], data[1], data[2], data[3], data[4] = symbols('vf vi a t d')
solveFor = []
known = ['vf', 'vi', 'a', 't', 'd']
toSort1 = ['vf', 'vi', 'a', 't', 'd']
toSort2 = ['vf', 'vi', 'a', 't', 'd']
checkList = ['a t vf vi', 'd t vf vi', 'a d t vi', 'a d t vf', 'a d vf vi']


def eq1():
    return Eq(data[0], data[1]+data[2]*data[3])
def eq2():
    return Eq(data[4], ((data[1]+data[0])/2)*data[3])
def eq3():
    return Eq(data[4], data[1]*data[3] + ((data[2]*data[3]**2)/2))
def eq4():
    return Eq(data[4], data[0]*data[3] - ((data[2]*data[3]**2)/2))
def eq5():
    return Eq(data[0]**2, data[1]**2 + 2*data[2]*data[4])

options = {0 : eq1,
           1 : eq2,
           2 : eq3,
           3 : eq4,
           4 : eq5,
}

prompt = ['Final Speed: ', 'Initial Speed: ', 'Acceleration: ', 'Time: ', 'Distance: ']
unknowns = 0

print "Press enter if the value is unknown."
for i in range(5):
    try:
        data[i] = int(raw_input(prompt[i]))
    except:
        unknowns = unknowns + 1

if unknowns > 2:
    print "I can't solve this, there are too many unknown variables :("
else:
    for i in data:
        if isinstance(i, int):
            pass
        else:
            known.remove(str(i))
            solveFor.append(str(i))
    
    toSort1.remove(solveFor[1])
    toSort1.sort()
    a = ' '.join(toSort1)
    
    toSort2.remove(solveFor[0])
    toSort2.sort()
    b = ' '.join(toSort2)
    

    for i in checkList:
        if i == a:
            steps1 = i
            ans1 = '{0} is {1}'.format(solveFor[0], solve(options[checkList.index(i)](), solveFor[0]))

    for i in checkList:
        if i == b:
            steps2 = i
            ans2 = '{0} is {1}'.format(solveFor[1], solve(options[checkList.index(i)](), solveFor[1]))
            
    data[0], data[1], data[2], data[3], data[4] = symbols('vf vi a t d')
    
    print
    print "Rewrote to solve for {0}".format(solveFor[0])
    print options[checkList.index(steps1)]()
    print "Into:"
    print solve(options[checkList.index(steps1)](), solveFor[0])
    print ans1
    print
    print "Rewrote to solve for {0}".format(solveFor[1])
    print options[checkList.index(steps2)]()
    print "Into:"
    print solve(options[checkList.index(steps2)](), solveFor[1])
    print ans2
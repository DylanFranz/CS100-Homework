"""
Dylan Franz
CS 100 2023F Section H09
HW 01, September 17, 2023
"""
import math
p = (math.pi)

#5B
year = 2023
month = 9
date = 17

#5C
ratingOne = 6.7
ratingTwo = 4.1
ratingThree = 9.1

#5D
name_first = "Dylan"
name_middle = "Michael"
name_last = "Franz"

#1.1
#1 You get a syntax error
#2 You get a syntax error
#3 It returns the number. 2++2 = 4
#4 leading zeros aren't allowed in python
#5 Incomplete input error

#1.2
#1
secondsTotal = (42*60) + 42
print(secondsTotal,'seconds in 42 minuites and 42 seconds')
#2
milesTotal = 10*0.621371
print(milesTotal,'miles in 10 kilometers')
#3
secondsPerMile = secondsTotal/milesTotal
print("pace is ", secondsPerMile//60,'minutes and',secondsPerMile % 60, 'seconds')
print("also known as ", (milesTotal/((secondsTotal/60)/60)), 'MPH')

#2.1
#1 You get an error, you can't assign backwards
#2 That works perfectly fine it assigns 1 to x and y
#3 Nothing, it doesn't effect the output
#4 Error, incomplete input
#5 Error, xy is not defined

#2.2
#1
r = 5
volume = (4/3)*(p)*(r**3)
print('The volume of a spere with radius 5 is', volume)
#2
msrpPrice = 24.95
bookstorePrice = 24.95*.6
numCopies = 60
print('the total wholesale cost for 60 copies is', round(bookstorePrice*numCopies + 3 + .75*(numCopies-1),2))
#3
easyPaceInSeconds = 8*60 + 15
tempoPaceInSeconds = 7*60 + 12
startingTimeInSeconds = 6*60*60 + 52*60
endingTimeInSeconds = startingTimeInSeconds + easyPaceInSeconds + 3*tempoPaceInSeconds + easyPaceInSeconds
print((endingTimeInSeconds//60)//60,':',(endingTimeInSeconds//60)%60,':',endingTimeInSeconds%60)

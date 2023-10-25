"""
Dylan Franz
CS 100 2023F Section H09
HW 06, October 10, 2023
"""

def hasFinalLetter (strList, letters):
    temp = []
    for string in strList:
        if (string[-1] in letters):
            temp.append(string)
    return temp

#testCase1
strList1 = ["red", "blue", "green"]
letters1 = "run"
print(hasFinalLetter(strList1, letters1))
#testCase2
strList2 = ["one", "Two", "three"]
letters2 = "numbers"
print(hasFinalLetter(strList2, letters2))
#testCase3
strList3 = ["Jacob Collier", "Snarky Puppy", "Lawrence"]
letters3 = "musical artists"
print(hasFinalLetter(strList3, letters3))

def isDevisible (maxInt, twoInts):
    temp = []
    for int in range(1,maxInt):
        if int % twoInts[0] and int % twoInts[1]:
            temp.append(int)
    return 

#testCase1
maxInt1 = 30
twoInts1 = [7, 4]
print(isDevisible(maxInt1, twoInts1))
#testCase2
maxInt2 = 45
twoInts2 = [2,3]
print(isDevisible(maxInt2, twoInts2))
#testCase3
maxInt3 = 49
twoInts3 = [7,3]
print(isDevisible(maxInt3, twoInts3))
"""
Dylan Franz
CS 100 2023F Section H09
HW 12, December 05, 2023
"""

# Problem 1
def safeOpen(filename):
    try:
        file = open(filename)
        return(file)
    except FileNotFoundError:
        return None

# Problem 2
def safeFloat(x):
    try:
        flt = float(x)
        return(flt)
    except ValueError:
        return 0.0

# Problem 3
def averageSpeed():
    filename = input("What is the name of the file to process?")
    file = safeOpen(filename)
    if file == None:
        filename = input("Please try again, what is the filename?")
        file = safeOpen(filename)
        if file == None:
            print("file not found, goodbye")
            return None
    content = file.read()
    uncheckedList = content.split('\n')
    speedList = []
    for item in uncheckedList:
        flt = safeFloat(item)
        if flt > 2:
            speedList.append(flt)
    total = 0
    for num in speedList:
        total += num
    print("Average speed is {} miles per hour.".format(total/len(speedList)))


averageSpeed()
     
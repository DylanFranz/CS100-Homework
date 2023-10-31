import os
import string
print(os.getcwd())
print(os.getlogin())
fileTest = open('testFileCS100.txt', 'w')
textArray = ['Line 1', 'LINE 2', 'LINE THREE', 'Line Four', 'Line 0123456789']
for line in textArray:
    fileTest.write(line + '\n')
fileTest.close()

fileTest = open('testFileCS100.txt', 'r')
for line in fileTest:
    if str(string.digits) in line:
        print(line, end= '')
fileTest.close()

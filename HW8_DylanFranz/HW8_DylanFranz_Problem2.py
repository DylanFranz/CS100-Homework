"""
Dylan Franz
CS 100 2023F Section H09
HW 08, November 1, 2023
"""

import string

def twoWords(length, firstLetter):
    rightLengthWord = input("Enter a " + str(length) + "-letter word please:")
    while int(len(rightLengthWord)) != int(length):
        rightLengthWord = input("Enter a " + str(length) + "-letter word please:")
    rightStartWord = input("Enter a word beginning with " + firstLetter + " please:")
    while rightStartWord[0].lower() != firstLetter.lower():
        rightStartWord = input("Enter a word beginning with " + firstLetter + " please:")
    return[rightLengthWord, rightStartWord]

print(twoWords(4,'B'))
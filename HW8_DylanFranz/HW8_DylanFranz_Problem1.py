"""
Dylan Franz
CS 100 2023F Section H09
HW 08, November 1, 2023
"""

import string

def twoWords(length, firstLetter):
    while True:
        rightLengthWord = input("Enter a " + str(length) + "-letter word please:")
        if int(len(rightLengthWord)) == int(length):
            break
    while True:
        rightStartWord = input("Enter a word beginning with " + firstLetter + " please:")
        if rightStartWord[0].lower() == firstLetter.lower():
            break
    return[rightLengthWord, rightStartWord]
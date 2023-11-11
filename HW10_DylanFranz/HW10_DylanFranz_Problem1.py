"""
Dylan Franz
CS 100 2023F Section H09
HW 10, November 11, 2023
"""

def initialLetterCount(wordList):
    d = {}
    for word in wordList:
        count = 0
        for word2 in wordList:
            if word[0] == word2[0]:
                count += 1
        d[word[0]] = count
    return d

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetterCount(horton))
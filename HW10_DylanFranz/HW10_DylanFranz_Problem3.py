"""
Dylan Franz
CS 100 2023F Section H09
HW 10, November 11, 2023
"""

def shareOneLetter(wordList):
    d = {}
    for word in wordList:
        l = []
        for letter in word:
            for word2 in wordList:
                if letter in word2 and word2 not in l:
                    l.append(word2)
        if word not in d.keys():
            d[word] = l
    return d

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(shareOneLetter(horton))
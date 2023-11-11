"""
Dylan Franz
CS 100 2023F Section H09
HW 10, November 11, 2023
"""

def initialLetters(wordList):
    d = {}
    for word in wordList:
        if word[0] not in d.keys():
            l = []
            for word2 in wordList:
                if word[0] == word2[0] and word2 not in l:
                    l.append(word2)
            d[word[0]] = l
    return d

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetters(horton))  
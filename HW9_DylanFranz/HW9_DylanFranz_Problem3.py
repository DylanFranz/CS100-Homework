"""
Dylan Franz
CS 100 2023F Section H09
HW 09, November 6, 2023
"""
import string

def repeat_words(in_file, out_file):
    inp = open(in_file, 'r')
    out = open(out_file, 'x')
    lines = inp.readlines()
    
    for line in lines:
        repeatedWords = []
        line = line.lower().strip(string.punctuation)

        words = line.split()
        words = [word.strip(string.punctuation) for word in words]

        for word in words:
            if words.count(word) > 1 and word not in repeatedWords:
                out.write(word + ' ')
                repeatedWords.append(word)
        out.write('\n')
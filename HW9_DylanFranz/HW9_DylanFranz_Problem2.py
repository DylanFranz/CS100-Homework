"""
Dylan Franz
CS 100 2023F Section H09
HW 09, November 6, 2023
"""

def file_stats(in_file):
    file = open(in_file, 'r')
    data = file.read()
    lines = len(data.split('\n'))
    words = len(re.split(' |\n', data))
    chars = data.__len__()
    print("lines", lines)
    print("words", words)
    print("characters", chars)
"""
Dylan Franz
CS 100 2023F Section H09
HW 09, November 6, 2023
"""

def file_copy(in_file, out_file):
    x = open(in_file)
    y = open(out_file, 'x')
    y.write(x.read())
    x.close()
    y.close()
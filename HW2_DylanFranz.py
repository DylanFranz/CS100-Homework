"""
Dylan Franz
CS 100 2023F Section H09
HW 02, September 24, 2023
"""

# 1
grades = ['A', 'F', 'C', 'F', 'A', 'B', 'A', 'C', 'A', 'B']
frequency = [grades.count('A'), grades.count('B'), grades.count('C'), grades.count('D'),grades.count('F')]
print(frequency)

#2
dog_breeds = ['collie', 'sheepdog', 'Chow', 'Chihuahua']
hearding_dogs = dog_breeds[:2]
print(hearding_dogs)
tiny_dogs = dog_breeds[3]
print(tiny_dogs)
print(dog_breeds.__contains__('Persian'))
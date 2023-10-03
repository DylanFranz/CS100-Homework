"""
Dylan Franz
CS 100 2023F Section H09
HW 05, October 3, 2023
"""
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for i in range(len(months)):
    if months[i][0] == "J":
        print(months[i])

for i in range(0, 100):
    if i%2 == 0 and i%5 == 0:
            print(i)

horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"
for char in horton:
     for char2 in vowels:
          if char == char2:
               print(char)

"""
Dylan Franz
CS 100 2023F Section H09
HW 08, November 1, 2023
"""

def enterNewPassword():
    while True:
        password = input("Please Enter a Password: ")
        if 7 < len(password) < 16:
            if any(c.isdigit() for c in password):
                break
        print("please try again!")
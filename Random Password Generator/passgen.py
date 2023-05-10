#Importing Functions
import random
import string

#Function Definition
def pass_gen(min_len, num, sp_char):
    numbers = string.digits
    letters = string.ascii_letters
    special = string.punctuation
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False
    characters = letters
    if num:
        characters += numbers
    if sp_char:
        characters += special
    
    while len(pwd) < min_len:
        new_char = random.choice(characters)
        pwd += new_char

        if pwd in numbers:
            has_number = True
        if pwd in special:
            has_special = True
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special:
            meets_criteria = has_number and meets_criteria

    print(pwd)


#Asking user requirement for the password
min_length = int(input("Enter the min_digits for the password: "))
num = input("Do you want to include numbers in the password(y/n)").lower()

if (num == 'y'):
    num_d = True
else:
    num_d = False

sp_char = input("Do you want to include special characters in the password(y/n): ").lower()

if (sp_char == "y"):
    spd = True
else:
    spd = False
#Function Call

pass_gen(min_length, num_d, spd)
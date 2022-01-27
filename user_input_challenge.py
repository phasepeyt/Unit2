'''
##############################
User Input Challenge
##############################

Create a program that asks the user to enter their name and their age. Print out a message 
addressed to them that tells them the year that they will turn 100 years old.

Add on to the previous program by asking the user for another number and printing out that 
many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n" is the same as pressing the ENTER button)
'''

### code here ###

user_name = input("What is your name? ")
print(user_name)
user_age = int(input("What is your age? "))
print(user_age)
final = ( f"{user_name} Your year is {2022 + 100 - user_age}")
print(final)

user_num = int(input("What number would you like? "))
print(user_num)
fin2 = (final * user_num)
print(fin2)
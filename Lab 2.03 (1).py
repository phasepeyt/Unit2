'''
##########################################
Lab 2.03 - Game Show
##########################################
In your Notebook
Follow the flow of execution in the following programs and predict what will happen for each
one
---------------------------------------
Example 1
---------------------------------------
a = input("What... is your quest")
b = "to seek the holy grail"
if a != b:
    print("Go On. Off you go")
else:
    b = input("What...is the air-speed velocity of an unladen swallow?")
    if b == "What do you mean? An African or European swallow?":
        print("I don't know that...AHHH [Bridgekeeper was thrown over bridge]")
    els e:
        print("[you were thrown over bridge]")

Prediction: what... is your quest?
go on. off you go
what... is the airspeed velocity of an unladen swallow?
i dont know that... AHHHH( bridgekeeper was thrown over bridge)
(u were thrown over bridge)
Actual:
pred
---------------------------------------
Example 2
---------------------------------------
user_input = input("What is your favorite color")
if user_input == 'blue':
    print("Blueskadoo")
elif user_input == "red":
    print("Roses are red!")
elif user_input == "yellow":
    print("Mellow Yellow")
elif user_input == "green":
    print("Green Machine")
elif user_input == "orange":
    print("Orange you glad I didn't say banana.")
elif user_input == "black":
    print("I see a red door and I want it painted black")
elif user_input == "purple":
    print("And we'll never be royalllssss")
elif user_input == "pink":
    print("Pinky- and the Brain")
else:
    print("I don't recognize that color. Is it even...??")

Prediction:whats ur fav color?
blueskadoo
roses r red
mellow yellow
green machine
orange u glad i didnt say banana
i see a red door and i want it painted black
and we'll never be royyalllllsssss
pinky and the brain
idk that color. it it even..??

Actual:
pred
---------------------------------------
In your Notebook
---------------------------------------
Translate this Snap! program into a Python program
***Refer to the image provided on Moodle located below the Lab 2.03 link***
Write program below:

---------------------------------------
Create a game show program
---------------------------------------
Declare 10 prizes (prize1, prize2, prize 3 at the top of your file)
User picks a number
The prize corresponding with that door is printed for the user.
Write code below the multiline comment
'''
##triangle
xin = input("what is x? ")
yin = input("what is y? ")
zin = input("what is z? ")

if ((xin + yin)> zin) and ((xin + zin) > yin) and ((yin + zin))
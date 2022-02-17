## game start


##textmonstergame

#map of dungeon


from re import T


dungeon = [
    ['grand prize','boss monster','sword','sword','stairs down'],
    ['magic stones','monster','stairs down','empty','stairs up'],
    ['empty','sword','stairs up','monster','empty']
        ]

#player info
inventory = []
current_room = 0
current_floor = 2
location = dungeon[current_floor][current_room]
dead = False

# game loop
game_over = False
while game_over == False:

    #update location
    location = dungeon[current_floor][current_room]

    #describe where we are
    if location == 'empty':
        print("you've found an empty room")
    elif location == 'sword':
        print("you have found a sword")
    elif location == 'stairs up':
        print("you see a staircase heading up")
    elif location == 'monster':
        print("you see a scary monster!")
    elif location == 'stairs down':
         print("you see a staircase heading down")
    elif location == 'magic stones':
        print("you find some magic stones")
    elif location == 'boss monster':
        print("there is a boss monster here!")
    elif location == 'grand prize':
        print("you've found the grand prize!!")
    elif location == 'cold and alone':
        print("the room is cold and alone")

    #player choices
    player_choices = input("what would you like to do? (left, right, up, down, grab, fight ")
    print(player_choices)

    if player_choices == 'right':
        current_room += 1
        if current_room == 5:
            print("you've hit a wall")
            current_room = 4

    elif player_choices == 'left':
        current_room -= 1
        if current_room == -1:
            print("you've hit a wall")

    elif player_choices == 'up':
        if location == 'stairs up':
            current_floor -= 1
        else:
            print("there are no stairs in this room")

    elif player_choices == 'down':
        if location == 'stairs down':
            current_floor += 1
        else:
            print("there are no stairs in this room")

    elif player_choices == 'grab':
        if location == 'sword' or location == 'magic stones':
            inventory.append(location)
            dungeon[current_floor][current_room] = 'empty'
        elif location == 'monster' or location == 'boss monster':
            print("are you serious?")
            dead = True
            break
        else:
            print("nothing to grab")

    elif location == 'grand prize':
        game_over = True
        break

    elif player_choices == 'inventory':
        print("you have: ")
        print(' '.join(inventory))  #joins every item from list with a space

    elif player_choices == 'fight':
        if location == 'monster':
            if 'sword' in inventory:
                print("you killed the monster, though he didnt put up much of a fight")
                dungeon[current_floor][current_room] = 'cold and alone'
                inventory.remove('sword')
            else:
                print("you dont have the required weapons")
                dead =  True
                break
        if location == 'boss monster':
            if 'sword' and 'magic stones' in inventory:
                print("you killed the boss monster, congrats..")
                inventory.remove('sword')
                inventory.remove('magic stones')
                dungeon[current_floor][current_room] = 'cold and alone'

            else:
                print("you dont have the required weapons")
                dead = True
                break
        
#determine win or loss
if dead == True:
    print("you've been eaten")
    game_over = True
else:
    print("congrats, you got the prize")
    game_over = True

#plau again
user_input = input("would you like to play again? (y/n)")
if user_input == 'y':
    dead = False
    game_over = False
            

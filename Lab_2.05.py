'''
############################
Lab 2.05 - Tic-Tac-Toe
############################
In your Notebook
1. Predict what will be printed. Then run the program and confirm
Example 1
---------
a = ['a', 'b', 'c', 'd', 'e']
print(a[0:3])
print(a[1:4])

Prediction: [a:d] [b:e]
Actual:['a','b','c'] ['b','c','d']

Example 2
---------
a = ['a', 'b', 'c', 'd', 'e']
print(a[1:len(a) - 3])

Prediction: e
Actual: ['b']

Example 3
---------
a = ['a', 'b', 'c', 'd', 'e']
b = a.remove('b')
print(a)
print(b)

Prediction: ['a','b','c','d','e'] , ['a','c','d','e']
Actual: same

Example 4
---------
a = ['a', 'b', 'c', 'd', 'e']
a[0] = 'haha'
b = a.pop()
print(a) 
print(b)

Prediction: ['haha','b','c','d','e'] , ['haha','b','c','d']
Actual: same 

Example 5
---------
a = ['a', 'b', 'c', 'd', 'e']
b = a + ['abc']
print(a)
print(b)

Prediction: ['a','b','c','d','e','abc']
Actual:same

Example 6
---------
a = ['a', 'b', 'c', 'd', 'e']
b = a.append('f')
print(a)
print(b)

Prediction:['a','b','c','d','e','f']
Actual:same
2. In script mode (Type your program below the multi-line comment)
We are going to start implementing Tic-Tac-Toe using a single list.
1. The user picks a location on the board according to the number:
    1 | 2 | 3
    ---------
    4 | 5 | 6
    ---------
    7 | 8 | 9
2. Depending on the position that the user inputs, update the position of the board to an "X" to reflect
that.
    Example:
        1 | 2 | 3
        ---------
        4 | 5 | X
        ---------
        7 | 8 | 9
3. Print the updated board out, but don't worry about making it look pretty.
4. Only need to implement one turn of the game
'''

# print starting board
board = [[1,2,3], [4,5,6], [7,8,9]]

print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
print(" - - - - ")
print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
print(" - - - - ")
print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")

#playerturn
turn = int(input("pick a number to place ur x: "))
if turn == 1:
    board[0][0] = 'x'
elif turn == 2:
    board[0][1] = 'x'
elif turn == 3:
    board[0][2] = 'x'
elif turn == 4:
    board[1][0] = 'x'
elif turn == 5:
    board[1][1] = 'x'
elif turn == 6:
    board[1][2] = 'x'
elif turn == 7:
    board[2][0] = 'x'
elif turn == 8:
    board[2][1] = 'x'
elif turn == 9:
    board[2][2] = 'x'
else:
    print("invalid number")

#update board
print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
print(" - - - - ")
print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
print(" - - - - ")
print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
'''
In this program, I use the list to form the square.
The player can also customize the key for move direction.
The square is messed up by randomly moving from init state.
So it's no need to discover whether the square is workable.
It's always solvable！！！
Some comments are provided to explain the functions.

Have fun to play it!!!
2021-03-21
'''


# function "print_square" is to print the square.
# the parameter "playnumber" is the demension of the square.
# the parameter "number_list_of_square_in_dimension" is to reprensent the square now.
def print_square(playnumber, number_list_of_square_in_dimension):
    for i in range(0, playnumber):
        for j in range(0, playnumber):
            print("%s\t" % (number_list_of_square_in_dimension[i * playnumber + j]), end="")
        print("")


# function "move_hint" is to give the hint about how to move the blank space at each step.
# the parameter "playnumber" is the demension of the square.
# the parameter "number_list_of_square_in_dimension" is to help to judge which direction can go to.
def move_hint(playnumber, number_list_of_square_in_dimension):
    if (number_list_of_square_in_dimension.index(""))//playnumber != playnumber-1:
        print("Enter %s for up" % (goingup))
    if (number_list_of_square_in_dimension.index(""))//playnumber != 0:
        print("Enter %s for down" % (goingdown))
    if (number_list_of_square_in_dimension.index("")) % playnumber != playnumber - 1:
        print("Enter %s for left" % (goingleft))
    if (number_list_of_square_in_dimension.index("")) % playnumber != 0:
        print("Enter %s for right" % (goingright))


# functon "move_control" is to move the balnk space in square.
# this function control the blank space by change the order of the numbers in the list.
# the parameter "playnumber" shows the demension of the square.
# the parameter "move_to_which_direction" shows which direction the number should move to.
# the parameter "moving_times" is to show how mang steps have done.
def move_control(playnumber, number_list_of_square_in_dimension, move_to_which_direction, moving_times):
    while True:
        ini_white_pos = number_list_of_square_in_dimension.index("")
        if move_to_which_direction == goingup:
            if (number_list_of_square_in_dimension.index(""))//playnumber != playnumber-1:
                mid_pos = ini_white_pos + playnumber
                number_to_up = number_list_of_square_in_dimension[mid_pos]
                number_list_of_square_in_dimension[mid_pos] = ""
                number_list_of_square_in_dimension[ini_white_pos] = number_to_up
                moving_times += 1
            break
        if move_to_which_direction == goingdown:
            if (number_list_of_square_in_dimension.index(""))//playnumber != 0:
                mid_pos = ini_white_pos - playnumber
                number_to_down = number_list_of_square_in_dimension[mid_pos]
                number_list_of_square_in_dimension[mid_pos] = ""
                number_list_of_square_in_dimension[ini_white_pos] = number_to_down
                moving_times += 1
            break
        if move_to_which_direction == goingleft:
            if (number_list_of_square_in_dimension.index("")) % playnumber != playnumber - 1:
                mid_pos = ini_white_pos + 1
                number_to_left = number_list_of_square_in_dimension[mid_pos]
                number_list_of_square_in_dimension[mid_pos] = ""
                number_list_of_square_in_dimension[ini_white_pos] = number_to_left
                moving_times += 1
            break
        if move_to_which_direction == goingright:
            if (number_list_of_square_in_dimension.index("")) % playnumber != 0:
                mid_pos = ini_white_pos - 1
                number_to_right = number_list_of_square_in_dimension[mid_pos]
                number_list_of_square_in_dimension[mid_pos] = ""
                number_list_of_square_in_dimension[ini_white_pos] = number_to_right
                moving_times += 1
            break
        break
    return moving_times, number_list_of_square_in_dimension


# functon "mess_the_order" is to mess up the square.
# this function mess up the square by moving the blank space randomly.
# the "moving_times" will count the numbers of moving step.
# the “mess_times” shows how many times random move have been done.
def mess_the_order(playnumber, number_list_of_square_in_dimension, move_to_which_direction, moving_times):
    mess_times = 0
    while mess_times < 2000:
        import random
        m = random.randint(1, 5)
        if m == 1:
            move_to_which_direction = goingup
        elif m == 2:
            move_to_which_direction = goingdown
        elif m == 3:
            move_to_which_direction = goingleft
        elif m == 4:
            move_to_which_direction = goingright
        moving_times, number_list_of_square_in_dimension = move_control(playnumber, number_list_of_square_in_dimension, move_to_which_direction, moving_times)
        mess_times = mess_times+1
    return number_list_of_square_in_dimension


# functon "Run_Game" is to start the game and end the game.
# this function start the game from choose the square with 3*3, 4*4 or more demension.
# this part will also initialize the correct order of the number_list of square.
# then the funtion will mess up the square.
# the function will compare the current list with the right list.
# when the order of the numbers in list is right, game will stop.
# the variable "move_to_which_direction" will represent the direction with numbers.
def Run_Game():
    number_list_of_square_in_dimension = []
    right_order_list = []
    moving_times = 0
    move_to_which_direction = 0
    playnumber = int(input("which do you want to play(enter 3 for 3*3、enter 4 for 4*4、or more):"))
    demension_have_achieve = 0
    while playnumber > demension_have_achieve:
        for i in range(1, playnumber+1):
            number_list_of_square_in_dimension.append(str(demension_have_achieve * playnumber + i))
            right_order_list.append(str(demension_have_achieve * playnumber + i))
        demension_have_achieve = demension_have_achieve + 1
    number_list_of_square_in_dimension.pop()
    number_list_of_square_in_dimension.append("")
    right_order_list.pop()
    right_order_list.append("")
    # "right_order_list" is the correct order of numbers in the list.
    # "number_list_of_square_in_dimension" is the real-time order of numbers in the list.

    number_list_of_square_in_dimension = mess_the_order(playnumber, number_list_of_square_in_dimension, move_to_which_direction, moving_times)
    moving_times = 0
    while number_list_of_square_in_dimension != right_order_list:
        print_square(playnumber, number_list_of_square_in_dimension)
        move_hint(playnumber, number_list_of_square_in_dimension)
        move_to_which_direction = input("Enter the direction:")
        moving_times, number_list_of_square_in_dimension = move_control(playnumber, number_list_of_square_in_dimension, move_to_which_direction, moving_times)
    print_square(playnumber, number_list_of_square_in_dimension)
    print("Congratuations, you use %s steps to finish it" % (moving_times))


# this part will initialize the start interface for this game.
print("Welcome to Sliding Puzzle!")
print("In this game, you can choose 3*3, 4*4 or enven more demension puzzle.")
print("move your number and make 3*3 puzzle to be:")
print_square(3, ["1", "2", "3", "4", "5", "6", "7", "8", ""])
print("or make more demension puzzle to be in order.")


# this part will let the player input the customized key for move direction.
# I use these parameters to store the keys that represent how the number move.
goingup = input("enter the key for up:")
goingdown = input("enter the key for down:")
goingleft = input("enter the key for left:")
goingright = input("enter the key for right:")


# this part will start the game by function "Run_Game()"
# it will also give player a chance to choose.
# the player can choose whether play it again.
while True:
    a = input("Do you want to start a new game?(enter yes/no)")
    if a == "yes":
        Run_Game()
        continue
    else:
        print("Thank you for playing!")
        break

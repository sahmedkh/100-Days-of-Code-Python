# This program was written to solve the maze challenge on Reeborg's World (reeborg.ca)
# The algorithm used to solve this is called right-hand on the wall rule
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal(): 
    if wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
            if front_is_clear():
                move()
    elif right_is_clear():
        turn_right()
        if front_is_clear():
            move()
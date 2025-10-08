from reeborg import move            # type: ignore
from reeborg import turn_left       # type: ignore
from reeborg import at_goal         # type: ignore
from reeborg import front_is_clear  # type: ignore
from reeborg import right_is_clear  # type: ignore

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_far(dist):
    if dist == 0:
        dist = 1
    for step in range(dist):
        move()
    
def hurdle_go(iter: int):
    if iter == 0:
        iter = 1

    for count in range(iter):
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()

def jump_wall():
    while not at_goal():
        if front_is_clear():
            if right_is_clear():
                turn_right()
                move()
            else:
                move()
        else:
            if right_is_clear():
                turn_right()
                move()
            else:
                turn_left()
        
jump_wall()
            

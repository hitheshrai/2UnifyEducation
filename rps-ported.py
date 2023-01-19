import xarm
import random
from time import sleep

arm = xarm.Controller('USB')

def shake_hand(times, waitTime = 500):
    for _ in range(times):
        arm.setPosition(4, 700, 300)
        sleep(waitTime / 1000)
        arm.setPosition(4, 535, 300)
        sleep(waitTime / 1000)

def pick_and_place(rockpaperscissors):
    match rockpaperscissors:
        case 1:
            shake_hand(3)
            # rock pose
            # TODO: improve this syntax somehow to be less tedious, at least omit "\"
            arm.setPosition(\
                servos = [[1, 695], [3, 110], [4, 815], [5, 675]],\
                duration = 300,\
            )
            sleep(3)
            print("ROCK")
        case 2:
            shake_hand(3)
            # paper pose
            arm.setPosition(\
                servos = [[1, 0], [3, 360], [4, 580], [5, 415]],\
                duration = 300,\
            )
            sleep(3)
            print("PAPER")
        case 3:
            shake_hand(3)
            sleep(1)
            arm.setPosition(\
                servos = [[1, 260], [2, 140], [3, 360], [4, 745], [5, 610]],\
                duration = 300,\
            )
            sleep(1)
            print("SCISSORS")
            arm.setPosition(1, 705, 300)
            sleep(1)
            arm.setPosition(\
                servos = [[1, 260], [2, 140], [3, 360], [4, 745], [5, 610]],\
                duration = 300,\
            )
            sleep(1)
            arm.setPosition(1, 705, 300)
            sleep(1)
            arm.setPosition(\
                servos = [[1, 260], [2, 140], [3, 360], [4, 745], [5, 610]],\
                duration = 300,\
            )
            sleep(1)
            arm.setPosition(1, 705, 300)
            sleep(1)
    # reset
    arm.setPosition([[1, 500], [3, 500], [4, 500], [5, 535]], 2000, wait=True)

def initial_position():
    arm.setPosition([[1, 500], [2, 500], [3, 500], [4, 500], [5, 535], [6, 500]], 2000, wait=True)

while (input("Ready to play? (Y/N): ").capitalize() == "Y"):
    initial_position()
    pick_and_place(random.randint(1,3))
    # pick_and_place(3)

# pick_and_place(2)
# pick_and_place(1)
# initial_position()
import xarm
import random
from time import sleep
from pynput import keyboard

arm = xarm.Controller('USB')
pos = 0
speed = 10
response = 25
# mode = True

# move a specific servo for a certain number of seconds
def move_with_time(servo, direc, time, speed):
    displacement = int(speed * time)
    if direc == 'down': displacement *= -1
    arm.setPosition(servo, arm.getPosition(servo) + displacement, int(time * 1000), response)

arm.setPosition(2, 500)
sleep(1)
# move wrist down for half a second, at speed 500
move_with_time(2, 'down', .5, 500)

# monitor for up/down key presses
with keyboard.Events() as events:
    for event in events:
        if event.key == keyboard.Key.up:
            if pos + speed > 1000: continue
            pos += speed
            arm.setPosition(2, pos, response)
            print('set up pos ' + str(pos))
        if event.key == keyboard.Key.down:
            if pos - speed < 0: continue
            pos -= speed
            arm.setPosition(2, pos, response)
            print('set down pos ' + str(pos))
        else:
            print('Received event {}'.format(event))
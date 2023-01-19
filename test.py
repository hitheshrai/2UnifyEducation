import xarm
import time

arm = xarm.Controller('USB')

arm.setPosition([[1, 1000]], duration = 500)
time.sleep(5)